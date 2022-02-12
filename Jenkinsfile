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
                      pip3 install -r requirements.txt
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
                /usr/local/bin/pm2 restart bot.py --interpreter ./venv/bin/python
              '''
        }
        failure {
            echo "Build failed"
        }
    }
}
