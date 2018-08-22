pipeline {
  agent {
    docker {
      image 'python:3.5-alpine'
    }

  }
  stages {
    stage('Code pull') {
      steps {
        checkout scm
      }
    }
    stage('Build environment') {
      steps {
        echo "${BUILD_TAG}"
        sh 'python -m pip install --user --upgrade pip'
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