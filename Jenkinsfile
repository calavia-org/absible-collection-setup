pipeline {

  agent {
    docker {
      label '*-molecule-agent'
      image 'robertdebock/github-action-molecule'
      args '-u 0 -v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  stages {

    stage ('Display versions') {
      steps {
        sh '''
          ansible --version
          molecule --version
        '''
      }
    }
//    stage ('Ansible test') {
//      steps {
//        sh '''
//          ansible-test sanity
//          ansible-test units
//          ansible-test integration -v ping
//        '''
//      }
//    }
    stage('Test roles'){
      matrix {
        axes {
          axis  {
            name 'SCENARIO'
            values 'rsyslog', 'logrotate'
          }
        }
        agent {
          label "${SCENARIO}-molecule-agent"
        }
        stages {
          stage('Molecule Test') {
            when { 
              beforeAgent true
              anyOf {
                changeset "roles/${SCENARIO}/*.yml"
                changeset "molecule/${SCENARIO}/*.yml"
              }
            }
            steps {
              sh '''
                pip install junit_xml 
                molecule lint -s ${SCENARIO}
                molecule destroy -s ${SCENARIO}
                molecule converge -s ${SCENARIO} 
                molecule idempotence -s ${SCENARIO}
                ANSIBLE_STDOUT_CALLBACK=junit JUNIT_OUTPUT_DIR="molecule/${SCENARIO}/reports/junit" JUNIT_FAIL_ON_CHANGE=true JUNIT_HIDE_TASK_ARGUMENTS=true JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT=no JUNIT_TEST_CASE_PREFIX=Test JUNIT_TASK_CLASS=true molecule verify -s ${SCENARIO}
                molecule destroy
              '''
              junit '**/reports/junit/*.xml'
            }
          }
        }
      }
    }
  } // close stages
}// close pipeline

