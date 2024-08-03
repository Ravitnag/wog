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


                bat 'docker-compose down'
                bat 'docker tag main_score:1.5 01022021/main_score:1.5'
                bat "docker push 01022021/main_score:1.5"
            
    }
}
