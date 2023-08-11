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
                sh "docker run --rm --network=${network} tests"
         }
         }
         }
     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'report']]
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
