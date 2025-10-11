pipeline{
    agent any

    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/curaHealthCare'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv virtualenv'
                bat 'virtualenv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'virtualenv\\Scripts\\activate && pytest -v --alluredir=reports/testJenkins --headless'
            }
        }
    }
}