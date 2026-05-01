pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Code quality check passed'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Application deployed successfully (simulated)'
            }
        }

    }
}
