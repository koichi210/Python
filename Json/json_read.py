import json

# 転送パラメータ
JENKINS_USER_KEY = 'USER_NAME'
JENKINS_PC_KEY = 'PC_NAME'

# 時間パラメータ
PROGRESS_BAR_TIME = 2
WAIT_QUEUEING_TIME = 0.5
WAIT_LOOP_TIME = 2

# Jenkinsのパラメータ
JenkinsToken = ''
JenkinsUser = ''
JenkinsAuth = ''

# JenkinsのURL
JenkinsBaseUrl = ''
JenkinsBuildableUrl = ''
JenkinsStatusUrl = ''
JenkinsQueueingUrl = ''
JenkinsBuildUrl = ''


if __name__ == '__main__':
    json_file_name = r'sample.json'

    json_file = open(json_file_name, 'r')
    json_object = json.load(json_file)
    json_file.close

    print(json_object)
    print(json_object['JENKINS_BASE_URL'])

    print(json_object['MAIN_SYSTEM']['MANAGE'])
    print(json_object['MAIN_SYSTEM']['MANAGE'][0])

    print(json_object['MAIN_SYSTEM']['WORKER'][0])
    print(json_object['MAIN_SYSTEM']['WORKER'][1])
    print(json_object['MAIN_SYSTEM']['WORKER'][2])

    for Chlid in json_object['MAIN_SYSTEM']['WORKER']:
        print(Chlid)
