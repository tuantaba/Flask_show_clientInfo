pipeline {
    // agent { node { master } }
    agent any
    // environment {

    // }
    stages {
        stage('Clone') {
            steps {
                echo 'hello, i m clone'
            }
            
        }

        stage('Build') {
            steps {
                echo 'hello, i m build'
            }
            
        }

        stage('Test') {
            steps {
                echo 'hello, i m test'
            }
        }

        stage('Deploy') {   
            steps {
                echo 'Hello, i m deploy'
                echo "change something"
            }
        }

    }

    post {
        always {
            echo 'One way or another, I have finished'
            // deleteDir() /* clean up our workspace */
        }
        success {
            echo 'I succeeded!'
        }
        unstable {
            echo 'I am unstable :/'
        }
        failure {
            echo 'I failed :('
        }
        changed {
            echo 'Things were different before...'
        }
    }

}