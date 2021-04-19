pipeline {
    // agent { node { master } }
    agent any
    // environment {

    // }
    stages {
        state('Clone') {
            steps {
                echo 'hello, i m clone'
            }
            
        }

        state('Build') {
            steps {
                echo 'hello, i m build'
            }
            
        }

        state('Test') {
            steps {
                echo 'hello, i m test'
            }
        }

        state('Deploy') {   
            steps {
                echo 'Hello, i m deploy'
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