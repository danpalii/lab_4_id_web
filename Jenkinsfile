pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Install_packages') {
      steps {
        sh 'pip -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        sh 'python manage.py test'
      }
    }
  }
}