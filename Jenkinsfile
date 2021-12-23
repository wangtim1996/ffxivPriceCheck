pipeline {
    agent any

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Build environment') {
            steps {
                sh '''python3 -m venv venv
                      source venv/bin/activate
                      pip install -r requirements.txt
                    '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''source venv/bin/activate
                        pytest test_marketboard.py
                    '''
            }
        }
    }
    post {
        always {
            echo "done"
        }
        success {
          sh '''source venv/bin/activate
                cp ~/.env .
                pm2 restart bot.py --interpreter python3
              '''
        }
        failure {
            echo "Build failed"
        }
    }
}
