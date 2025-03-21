pipeline {
    agent any 
    environment {
        AWS_ACCOUNT_ID="769644977981"
        ECR_REPO_NAME="python/project"
        DOCKER_IMAGE="769644977981.dkr.ecr.us-east-1.amazonaws.com/${ECR_REPO_NAME}"
        AWS_REGION= "us-east-1"
        CREDENTIALS_ID= "aws-ecr-credentials"
    }
    stages {
        stage ('Git Checkout') {
            steps {
                git url:'https://github.com/praveenpeddapotula/python-project-2.git', branch:'main'
            }
        }
        
        stage ('Login to AWS ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: "${CREDENTIALS_ID}"]]) {
                sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 769644977981.dkr.ecr.us-east-1.amazonaws.com'
            }
            }
        }
        
        stage ('Docker Build') {
            steps {
                script {
                    sh """
                    docker build -t python/project:1.0 .
                    docker tag python/project:1.0 769644977981.dkr.ecr.us-east-1.amazonaws.com/python/project:1.0
                    """
                }
            }
        }
        
        stage ('Docker Push') {
            steps {
                script {
                    sh 'docker push 769644977981.dkr.ecr.us-east-1.amazonaws.com/python/project:1.0'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean workspace after the build
        }
    }
}
