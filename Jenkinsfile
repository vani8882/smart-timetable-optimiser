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
                echo 'Code quality stage (placeholder)'
            }
        }

        stage('Security') {
            steps {
                echo 'Security scan stage (placeholder)'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker build -t timetable .'
                sh 'docker run -d -p 5002:5000 timetable || true'
            }
        }

        stage('Release') {
            steps {
                echo 'Release v1.0'
            }
        }

        stage('Monitoring') {
            steps {
                sh 'sleep 5'
                sh 'curl http://localhost:5002/health'
            }
        }
    }
}
