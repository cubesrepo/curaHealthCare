// pipeline{
//     agent any
//
//     environment{
//         PYTHON_VERSION = "3.11.9"
//         VENV_DIR = "virtualenv"
//     }
//
//     stages{
//         stage("Check out"){
//             steps{
//                 git 'https://github.com/cubesrepo/curaHealthCare'
//
//             }
//         }
//         stage("Install dependencies and setup"){
//             steps{
//                 bat '''
//                 python -m venv ${VENV_DIR}
//                 call ${VENV_DIR}\\Scripts\\activate
//                 pip install -r utilities/requirements.txt
//                 '''
//             }
//         }
//         stage("Run tests"){
//             steps{
//                 bat '''
//                 ${VENV_DIR}\\Scripts\\activate
//                 pytest -m login
//                 --alluredir = reports/tstjenkins1234 --headless
//
//
//             }
//         }
//     }
//     post {
//         always {
//             allure([
//                 includeProperties: false,
//                 jdk: '',
//                 results: [[path: 'reports/testJenkins']]
//             ])
//         }
//     }
// }

pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'prod'], description: 'Select test environment')
        booleanParam(name: 'HEADLESS', defaultValue: true, description: 'Run tests in headless mode')
    }

    environment {
        PYTHON_VERSION = '3.9'
        VENV_DIR = 'venv'
        ALLURE_RESULTS = 'allure-results'
        ALLURE_REPORT = 'allure-report'
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
        timeout(time: 1, unit: 'HOURS')
    }

    stages {
        stage('Checkout') {
            steps {

                git 'https://github.com/cubesrepo/curaHealthCare.git'
            }
        }

        stage('Setup') {
            steps {
                script {
                    echo "Setting up Python environment..."
                    sh '''
                        python3 -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r utilities/requirements.txt
                    '''
                }
            }
        }


        stage('Run Tests') {
            steps {
                script {
                    echo "Running Selenium pytest tests..."
                    sh '''
                        . ${VENV_DIR}/bin/activate
                        pytest tests/ \
                            --alluredir=${ALLURE_RESULTS} \
                            --html=reports/report.html \
                            --self-contained-html \
                            -v \
                            --tb=short \
                            -m "not skip" \
                            --junit-xml=reports/junit.xml \
                            -n auto
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    echo "Generating Allure report..."
                    sh '''
                        . ${VENV_DIR}/bin/activate
                        allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean
                    '''
                }
            }
        }

        stage('Publish Reports') {
            steps {
                script {
                    // Archive test artifacts BEFORE cleanup
                    archiveArtifacts artifacts: 'reports/**,${ALLURE_REPORT}/**', allowEmptyArchive: true

                    // Publish JUnit results
                    junit 'reports/junit.xml'

                    // Publish Allure Report using HTML Publisher Plugin
                    publishHTML([
                        reportDir: "${ALLURE_REPORT}",
                        reportFiles: 'index.html',
                        reportName: 'Allure Report',
                        keepAll: true,
                        alwaysLinkToLastBuild: true
                    ])

                    // Alternative: Allure Jenkins Plugin integration
                    allure([
                        includeProperties: false,
                        jdk: '',
                        results: [[path: "${ALLURE_RESULTS}"]]
                    ])
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Cleaning up..."
                cleanWs(
                    deleteDirs: true,
                    patterns: [
                        [pattern: "${VENV_DIR}", type: 'INCLUDE'],
                        [pattern: "${ALLURE_RESULTS}", type: 'INCLUDE']
                    ]
                )
            }
        }
        success {
            echo "Tests passed successfully!"
            // Send success notification
        }
        failure {
            echo "Tests failed. Check Allure Report for details."
            // Send failure notification
        }
    }
}