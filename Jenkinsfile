pipeline {
    agent any

    environment {
        APP_URL = 'http://127.0.0.1:5010'
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
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Start Flask Application') {
            steps {
                bat '''
                start "FlaskApp" /B python app.py
                '''

                bat 'timeout /t 10'
            }
        }

        stage('Execute API Test') {
            steps {
                bat 'python -m robot test_2.robot'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'

            archiveArtifacts artifacts: '*.html,*.xml,*.log', allowEmptyArchive: true
        }

        success {
            echo 'Build Successful'
        }

        failure {
            echo 'Build Failed'
        }
    }
}
