#!/usr/bin/env groovy
pipeline {
    // agent { node { master } }
    agent any
    environment {

    }
    stages {
        state('Clone') {
            echo "hello, i m clone"
        }

        state('Build') {
            echo "hello, i m build"
        }

        state('Test') {
            echo "hello, i m test"
        }

        state('Deploy') {
            echo "Hello, i m deploy"
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