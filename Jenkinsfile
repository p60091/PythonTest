pipeline {
  agent { docker { image 'python:3.5.1' } }
  environment {
    TEST_ENV = 'Test Environment Variable'
  }
  stages {
    stage('Prep') {
      steps{ git 'https://github.com/kyrus/python-junit-xml.git'
             sh 'pip install --user'
              }}
    stage('Build') {
      steps {
        sh 'ls'
        sh 'echo "Build Stage"'
        sh 'python --version'
        sh 'python HelloWorld.py'
        sh 'printenv'
        input "Test input:"
      }
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
    always { echo 'This will always run' }
    success { echo 'This will run if succsesful' 
              mail to: 'vinh.huynh@ironmountain.com',
                   subject: "Success Pipeline: ${currentBuild.fullDisplayName}",
                   body: "Build Successful ${env.BUILD_URL}" }
    failure { echo 'This will run if failed' }
    changed { echo 'This will run if pipeline changed' }
  }
}
