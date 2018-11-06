pipeline {
  agent { docker { image 'python:3.5.1' } }
  stages {
    stage('build') {
      steps {
        sh 'python --version'
        sh 'echo "Test"'
      }
    }
  }
  post {
    always { echo 'This will always run' }
    success { echo 'This will run if succsesful' }
    failure { echo 'This will run if failed' }
    changed { echo 'This will run if pipeline changed' }
  }
}
