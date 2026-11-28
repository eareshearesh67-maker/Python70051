pipeline {
    agent any

    environment {
        APP_URL = 'http://127.0.0.1:5015'
    }

    stages {

        stage('Fetch Project from GitHub') {
            steps {
                echo 'Fetching Project from GitHub'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Dependencies'
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Start Flask Application') {
            steps {
                echo 'Starting Flask Application'

                bat '''
                start "FlaskApp" /B python app.py
                '''

                bat 'timeout /t 10'
            }
        }

        stage('Execute API Test') {
            steps {
                echo 'Running Robot Framework Tests'
                bat 'python -m robot test_2.robot'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '*.xml,*.html,*.log', allowEmptyArchive: true
        }

        success {
            echo 'Pipeline Executed Successfully'
        }

        failure {
            echo 'Pipeline Failed'
        }
    }
}

