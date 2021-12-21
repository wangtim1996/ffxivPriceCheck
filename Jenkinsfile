pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }
    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Build environment') {
            steps {
                sh '''python3 -m venv venv
                      source activate venv
                      pip install -r requirements.txt
                    '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''source activate ${BUILD_TAG}
                      pip list
                      which pip
                      which python
                    '''
            }
        }
    }
    post {
        always {
            echo "done"
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
