pipeline{
    agent any

    environment{
        PYTHON_VERSION = "3.11.9"
        VENV_DIR = "virtualenv"
        VENV_ACTIVATE = "${VENV_DIR}\\Scripts\\activate"
        ALLURE_REPORT = "reports/T1"
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
                call ${VENV_ACTIVATE} && pip install -r utilities/requirements.txt
                """
            }
        }
        stage("Run tests"){
            steps{
                echo "Running selenium pytest tests..."
                bat """
                call ${VENV_ACTIVATE} && pytest -v --delay=1 --alluredir=${ALLURE_REPORT} --headless
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
                results: [[path: "${ALLURE_REPORT}"]]
            ])
            echo "Cleaning up worskpace.."
            cleanWs()
        }
        success {
            echo "✅ Tests passed successfully!"
        }
        failure {
            echo "❌ Tests failed!"
        }
    }
}


