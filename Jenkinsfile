pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/KavyaRMaitri/Devops_Practice.git']])
            }
        }
        stage('Stage 1') {
            steps {
                script {
                    def num1 = input(message: 'Enter the first number:', parameters: [string(defaultValue: '', description: 'First number', name: 'num1')])
                    def num2 = input(message: 'Enter the second number:', parameters: [string(defaultValue: '', description: 'Second number', name: 'num2')])
                    sh "python3 Add2Numbers.py ${num1} ${num2}"
                }
            }
        }
    }
}
