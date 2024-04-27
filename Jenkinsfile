pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Add2Numbers') {
      steps {
        sh 'python3 Add2Numbers.py'
      }
    }
  }

