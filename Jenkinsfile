pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
    	catchError {
      	   script {
        	      sh"docker build -t try_again_tests ."
      	     }
          }
       }
    }
     stage('Pull browser') {
        script {
           docker.image('aerokube/selenoid:1.10.12').withRun('-p 4444:4444 -v /run/docker.sock:/var/run/docker.sock -v $PWD:/etc/selenoid/',
            	'-timeout 600s -limit 2')
        }
     }
     stage('Run tests') {
        steps {
           sh"""
           docker run -it try_again_tests --bversion ${bversion}
           --executor ${executor} --browser ${browser}
           --url_opencart ${url_opencart}
           """
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
     }
}
