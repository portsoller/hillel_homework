pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                //checkout scm
                git branch: 'homework31', url: 'https://github.com/portsoller/hillel_homework.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install --break-system-packages -r requirements.txt'
                sh 'python -m playwright install chromium'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m pytest tests/ --junitxml=result.xml'
            }
        }
        stage('Publish results') {
            steps {
                junit allowEmptyResults: true, testResults: '*.xml'
            }
        }
    }

    post {
        always {
            mail to: 'portsoller@gmail.com',
                 subject: "Jenkins Build ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                 body: "Результати виконання пайплайна ${env.JOB_NAME}: ${env.BUILD_URL}"
        }
    }
}