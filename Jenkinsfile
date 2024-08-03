node {
    stage('Checkout') {
        git branch: 'main', url: 'https://github.com/Ravitnag/wog.git'
    }

        stage('Build') {
                // Run docker build
                bat 'docker build -t main_score:1.5 .'
        }

    stage('run') {
                // Run docker-compose up
                bat 'docker-compose up -d'          
        }

    stage('Test') {
       bat 'python e2e.py'
    }

     stage('Finalize') {
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            script {
                // Perform Docker login
                bat """
                echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                """
                // Tag and push the Docker image
                bat 'docker tag main_score:1.5 $DOCKER_USERNAME/main_score:1.5'
                bat 'docker push $DOCKER_USERNAME/main_score:1.5'
            }
        }
        // Stop and remove Docker containers
        bat 'docker-compose down'
    }
}
