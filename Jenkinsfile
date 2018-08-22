pipeline {
    agent {
      docker {
        image '3.5-alpine'
      }
    }

    stages {
        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
    }
    post {
        always {
          echo "Completed"
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
