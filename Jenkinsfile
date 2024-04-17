pipeline {
    agent any

    stages {
        // stage("Git Clone"){
        //     steps{
        //         git credentialsId: 'GIT_HUB_CREDENTIALS', url: 'https://github.com/UjwalDineshJain2003/Ecommerce-Microservices.git'
        //     }
        // }

        stage('Initialize'){
            steps{
                script{
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                }
            }
        }

        // stage('Docker Hub Login'){
        //     steps{
        //         withCredentials([string(credentialsId: 'DOCKER_HUB_CREDENTIALS', variable: 'PASSWORD')]) {
        //             sh 'docker login -u ujwaldineshjain2003 -p $PASSWORD'
        //         }
        //     }
        // }

        // User Microservice
        stage('User: Build Docker Image') {
            steps {
                script {
                    // docker.build("ujwaldineshjain2003/user-app:latest", "-f User/Dockerfile .")
                    sh "docker build -t ujwaldineshjain2003/user-app:latest -f User/Dockerfile ."
                }
            }
        }

        stage("User: Push Image to Docker Hub"){
            steps{
                script{
                    sh 'docker push  ujwaldineshjain2003/user-app:latest'
                }
            }
        }

        stage('User: Deploy to Kubernetes') {
            steps {
                script {
                    // Replace with Kubernetes deployment commands
                    sh 'kubectl apply -f User/mongo-pv.yaml'
                    sh 'kubectl apply -f User/mongo-pvc.yaml'
                    sh 'kubectl apply -f User/mongo-svc.yaml'
                    sh 'kubectl apply -f User/mongo.yaml'
                    sh 'kubectl apply -f User/userapp-svc.yaml'
                    sh 'kubectl apply -f User/userapp-deployment.yaml'
                }
            }
        }

        // Product Microservice
        // Add stages for Product Microservice here

        // Order Microservice
        // Add stages for Order Microservice here
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
