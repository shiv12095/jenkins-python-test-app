pipeline {
  agent {
    docker {
      image 'python:3.5.1'
    }

  }
  stages {
    stage('Code pull') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        withEnv(overrides: ["HOME=${env.WORKSPACE}"]) {
          sh '''
              python -m pip install --user virtualenv
              python -m virtualenv test_app
              source test_app/bin/activate
              python -m pip install -r requirements/dev.txt
             '''
        }
      }
    }
  }
  post {
    always {
      echo 'Completed'

    }
    failure {
      echo 'Send e-mail, when failed'
    }
  }
}
