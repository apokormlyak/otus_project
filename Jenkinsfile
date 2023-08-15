pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      docker.build("tests", "-f Dockerfile .")
      	 }
          }
       }
    }
     stage('Pull browser') {
        steps {
           catchError {
              script {
      	    docker.image('selenoid/chrome:114.0')
      	  }
           }
        }
     }
     stage('Start selenoid') {
        steps {
            catchError {
                sh "/home/alisapokormlyak/Desktop/drivers/cm selenoid start"
        }
        }
     }
     stage('Run tests') {
        steps {
            catchError {
                sh "docker run --name test_run --network=${network} tests; docker cp test_run:app/allure-results ."
                sh "docker rm test_run"
         }
         }
         }
     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [[key: '--clean', value: '']],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: '/var/lib/jenkins/workspace/final_project/allure-results']]
    	   ])
  	        }
         }
     stage('Stop selenoid') {
        steps {
            catchError {
                sh "/home/alisapokormlyak/Desktop/drivers/cm selenoid stop"
        }
        }
     }
     }
}
