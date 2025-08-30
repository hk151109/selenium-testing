pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/hk151109/selenium-testing.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\gopal\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt pytest selenium'
            }
        }

        stage('Run App & Tests') {
            steps {
                bat 'start /B cmd /c "venv\\Scripts\\activate && flask run"'
                sleep 5
                bat 'venv\\Scripts\\activate && pytest -s -v tests/'
            }
        }
    }
}
