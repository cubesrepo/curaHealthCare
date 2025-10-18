pipeline{
    agent any

    environment{
        PYTHON_VERSION = "3.11.9"
        VENV_DIR = "virtualenv"
        VENV_ACTIVATE = "${VENV_DIR}\\Scripts\\activate"
        ALLURE_REPORT = "reports/testJenkins"
    }

    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/curaHealthCare'

            }
        }
        stage("Install dependencies and setup"){
            steps{
                echo "Setting up python environment"
                bat """
                python -m venv ${VENV_DIR}
                call ${VENV_ACTIVATE}
                pip install -r utilities/requirements.txt
                """
            }
        }
        stage("Run tests"){
            steps{
                echo "Running selenium pytest tests..."
                bat """
                call ${VENV_ACTIVATE}
                pytest -m login --alluredir=${ALLURE_REPORT} --headless
                """
            }
        }
    }
    post {
        always {
            echo "Generating Allure report.."
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: '${ALLURE_REPORT}']]
            ])
        }
        success{
            echo "Test passed successfully!"
        }
        failure{
            echo "Test failed!"
        }
    }
}


