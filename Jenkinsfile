pipeline {
  agent { docker { image 'python:3.5.1' } }
  environment {
    TEST_ENV = 'Test Environment Variable'
  }
  stages {
    stage('Build') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
        sh 'pip install --user junit-xml'
        sh 'export PATH=$PATH:$WORKSPACE/.local/bin'
        sh 'echo "Build Stage"'
        sh 'python --version'
        sh 'python HelloWorld.py'
        sh 'printenv'
        input "Test input:"
      } }
    }
    stage('Test') {
      steps {
        sh 'echo "Test Stage"'
        sh './run_test.sh' // echo "Test Successful"
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo "Deploy Stage"'
        sh './run_deploy.sh' // echo "Deploy Successful"
      }
    }
  }
  post {
    always { echo 'This will always run'
             junit 'output.xml'
             deleteDir() }
    success { echo 'This will run if succsesful' }
    failure { echo 'This will run if failed' }
    changed { echo 'This will run if pipeline changed' }
  }
}
