pipeline {
    agent any
    stages{
        stage('Setup Python Virtual ENV'){
            steps{
                sh '''
                chmod +x envsetup.sh
                ./envsetup.sh
                '''
            }
        }
        stage('Run Django server'){
            steps{
                sh '''
                chmod +x run.sh
                ./run.sh
                '''
            }
        }
    }
}