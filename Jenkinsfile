pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Build') {
      steps {
        sh 'python3 Add2Numbers.py'
      }
    }
  }
}
