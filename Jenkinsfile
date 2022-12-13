pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('Install_packages') {
      steps {
        bat 'pip -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        bat 'python manage.py test'
      }
    }
  }
}