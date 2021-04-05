pipeline {

  agent {
    docker {
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
    stage ('Ansible test') {
      steps {
        sh '''
          ansible-test sanity
          ansible-test units
          ansible-test integration -v ping
        '''
      }
    }
    stage ('Molecule test') {
      parallel {
        stage('role rsyslog') {
          when { 
            beforeAgent true
            changeset pattern: "**/rsyslog/.yml", caseSensitive: true 
          }
          agent {
            label "rsyslog"
          }
          steps {
            sh '''
              molecule lint -s rsyslog
              molecule destroy -s rsyslog
              molecule converge -s rsyslog
              molecule idempotence -s rsyslog
              pip install junit_xml 
              ANSIBLE_STDOUT_CALLBACK=junit JUNIT_OUTPUT_DIR="molecule/rsyslog/reports/junit" JUNIT_FAIL_ON_CHANGE=true JUNIT_HIDE_TASK_ARGUMENTS=true JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT=no JUNIT_TEST_CASE_PREFIX=Test JUNIT_TASK_CLASS=true molecule verify -s rsyslog
              molecule destroy
            '''
            junit '**/reports/junit/*.xml'
          }
        }
        stage('role logrotate') {
          when { 
            beforeAgent true
            changeset pattern: "**/logrotate/.yml", caseSensitive: true 
          }
          agent {
            label "logrotate"
          }
          steps {
            sh '''
              molecule lint -s logrotate
              molecule destroy -s logrotate
              molecule converge -s logrotate
              molecule idempotence -s logrotate
              pip install junit_xml 
              ANSIBLE_STDOUT_CALLBACK=junit JUNIT_OUTPUT_DIR="molecule/logrotate/reports/junit" JUNIT_FAIL_ON_CHANGE=true JUNIT_HIDE_TASK_ARGUMENTS=true JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT=no JUNIT_TEST_CASE_PREFIX=Test JUNIT_TASK_CLASS=true molecule verify -s logrotate
              molecule destroy
            '''
            junit '**/reports/junit/*.xml'
          }
        }
      }
   }

  } // close stages
}// close pipeline

