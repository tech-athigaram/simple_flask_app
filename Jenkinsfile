pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }

    environment {
        FLASK_ENV = 'development'
    }

    stages {
        stage('Checkout') {
            steps {
                
                git url: 'https://github.com/tech-athigaram/simple_flask_app.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p test_reports
                    python -m unittest discover -s . -p "test_*.py" > test_reports/results.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                sh 'nohup python app.py > app.log 2>&1 &'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test_reports/results.txt', allowEmptyArchive: true
        }
        success {
            echo '✅ Flask app deployed inside Docker agent!'
        }
        failure {
            echo '❌ Build failed. Check logs and test results.'
        }
    }
}
