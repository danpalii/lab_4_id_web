pipeline {
    agent any

    stages {
        stage('Installing packages') {
                steps {
                    sh 'pip -r requirements.txt'
                }
            }    
        
        
        stage('Running Unit tests') {
                steps {
                    sh 'python manage.py test'
                }
            }
        
    }
}
