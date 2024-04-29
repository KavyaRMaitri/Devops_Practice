pipeline {
    agent any
     
    stages {
        stage('Stage 1') {
            steps {
                script {
                    def num1 = input(message: 'Enter the first number:', parameters: [string(defaultValue: '', description: 'First number', name: 'num1')])
                    def num2 = input(message: 'Enter the second number:', parameters: [string(defaultValue: '', description: 'Second number', name: 'num2')])
                    sh "python3 Add2Numbers.py ${num1} ${num2}"
                }
            }
        }
            stage('Parallel Stages') {
                parallel {
                    stage('Stage 2') {
                         environment {
                                num1 = credentials('NUMBER1_SECRET')
                                num2 = credentials('NUMBER2_SECRET')
                      }
                        steps {
                            script {
                               sh ('python3 Secrete.py $num1 $num2')
                               }
                            }
                        }
                     stage('Stage 3') {
                        steps {
                            sh "python3 Text.py"
                        }
                    }
                }
            }
    }
}
