pipeline{
  agent any
  environment{
     APP_URL='http://127.0.0.1:5010'
  }
  stages{
    stage{
      echo 'Fetching Project from Githup'
      checkout scm
    }
  }
  stage('Install Dependencies'){
     steps{
       bat 'python -m pip install -r requirements.txt'
     }
  }
  stage('Start Flask Application'){
    steps{
      bat '''start "FlaskApp" /B python app.py'''
    }
  }

  stage('Execute API Test'){
    steps{
      bat ''' python -m robot test_2.robot'''
    }
  }
}
    
