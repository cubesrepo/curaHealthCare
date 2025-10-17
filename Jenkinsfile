pipeline{
    agent any

    environment{
        PYTHON_VERSION = "3.11.9"
    }

    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/curaHealthCare'

            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv virtualenv'
                bat 'virtualenv\\Scripts\\activate && pip install -r utilities/requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'virtualenv\\Scripts\\activate && pytest -m login --alluredir=reports/testJenkins --headless'
            }
        }
    }
    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'reports/testJenkins']]
            ])
        }
    }
}