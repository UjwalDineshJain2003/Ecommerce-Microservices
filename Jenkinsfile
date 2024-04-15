pipeline {
    agent any

    stages {
        // User Microservice
        stage('User: Build Docker Image') {
            steps {
                script {
                    docker.build("user-docker-image:latest", "-f User/Dockerfile User")
                }
            }
        }
        stage('User: Run Docker Compose') {
            steps {
                script {
                    sh 'docker-compose -f User/docker-compose.yml up -d'
                }
            }
        }
        stage('User: Run Tests') {
            steps {
                script {
                    sh 'docker-compose -f User/docker-compose.yml exec app python User/test_app.py'
                }
            }
        }
        stage('User: Deploy to Kubernetes') {
            steps {
                script {
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
        always {
            script {
                sh 'docker-compose -f User/docker-compose.yml down'
            }
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
