pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Install_packages') {
      steps {
        bat 'pip install -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        bat 'python manage.py test'
      }
    }
  }
}