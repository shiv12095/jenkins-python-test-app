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
          sh 'python -m pip install --user virtualenv'
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
