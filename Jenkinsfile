pipeline {
  agent { docker { image 'python:3.5.1' } }
  environment {
    COMPILER = 'Test Environemnt'
  }
  stages {
    stage('build') {
      steps {
        sh 'echo "Build"'
        sh 'python --version'
        sh 'python HelloWorld.py'
        sh 'printenv'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "Test"'
        sh './run_test.sh'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "Deploy"'
        sh './run_deploy.sh'
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
