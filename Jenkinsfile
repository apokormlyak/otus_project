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
      	    sh "docker network create ping-pong-network"
      	  }
           }
        }
     }
     stage('Run tests') {
        steps {
           catchError {
              script {
          	     docker.image('aerokube/selenoid:1.10.12').withRun('-p 4444:4444 --network ping-pong-network -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/',
            	'-timeout 600s -limit 2') { c ->

            	    sh "docker run --rm --network ping-pong-network tests"

            	}


        	     }
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
      	   results: [[path: 'allure-results']]
    	   ])
  	        }
         }
     }
}
