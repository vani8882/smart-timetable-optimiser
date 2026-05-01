pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker build -t timetable .'
                sh 'docker run -d -p 5000:5000 timetable'
            }
        }

        stage('Monitoring') {
            steps {
                sh 'curl http://localhost:5000/health'
            }
        }
    }
}