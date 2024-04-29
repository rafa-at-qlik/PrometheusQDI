import time
import requests
import warnings
import json
import logging
import sys
warnings.filterwarnings("ignore")

###################################################
# Latency
threshold_latency_secs = 9000 # Task with latencies bigger than this parameter will get restarted, e.g. 9000s 2h30m
# Logging Config
logger = logging.getLogger(__name__)
time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename='PrometheusQDI.log',format='%(asctime)s - %(levelname)s - %(message)s', filemode='a', level=logging.INFO, datefmt=time_format)

def get_session_id(v_em_user, v_password, v_base_api_url):
    logger.info('Getting APISessionID')
    l_api_session_id = None
    try:
        session = requests.Session()
        session.auth = (v_em_user, v_password)
        auth = session.post(f"{v_base_api_url}/login", verify=False)
        response = session.get(f"{v_base_api_url}/login", verify=False)
        l_api_session_id = response.headers.get('EnterpriseManager.APISessionID')
        logger.info('Session token APISessionID successfully retrieved')
    except Exception as e:
        logger.error(f"Error while trying to get APISessionID in method get_session_id {logger.exception(e)}" )
    return l_api_session_id

def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def get_task_status(v_em_host, v_session_id, v_replicate_server, v_task_name):
    base_api_url = f"https://{v_em_host}/attunityenterprisemanager/api/v1"
    logger.info(f"Retrieving Task {v_task_name} Status for {v_replicate_server} - method get_task_status")
    task_status_url = f"{base_api_url}/servers/{v_replicate_server}/tasks/{v_task_name}"
    task_status_response = requests.get(task_status_url, headers={'EnterpriseManager.APISessionID': v_session_id},
                                      verify=False)
    try:
        task_status = json.loads(task_status_response.text)["state"]
        return task_status
    except Exception as e:
        logger.error(
            f"Error while trying to retrieve tasks status for server {v_replicate_server} and tasks {get_task_status} "
            f"{logger.exception(e)} - method get_task_status")
        return None

def get_replicate_servers(v_session_id, v_em_host):
    logger.info('Getting the List of Replicate Servers - method get_replicate_servers')
    get_server_list_url = f"https://{v_em_host}/attunityenterprisemanager/api/v1/servers"
    rep_server_list = list()
    try:
        task_response = requests.get(get_server_list_url, headers={'EnterpriseManager.APISessionID': v_session_id, "Content-Length": "0"}, verify=False)
        configjson = json.loads(task_response.text)
        logger.info('Replicate Server List Successfully retrieved')
        servers = configjson['serverList']
        for index in range(0, len(servers)):
            server = servers[index]
            if server['$type'] == 'ReplicateServerInfo':
                rep_server_list.append(server['name'])
                logger.info(f"Server {server['name']} is a Replicate Server")
    except Exception as e:
        logger.error(f"Error while trying to get Replicate Server {logger.exception(e)}")
    return rep_server_list

def get_task_list(v_em_host, v_session_id, v_server):
    logger.info(f"Retrieving Tasks for Server {v_server} - method get_task_list")
    get_task_list_url = f"https://{v_em_host}/attunityenterprisemanager/api/v1/servers/{v_server}/tasks"
    rep_server_tasks_lst = list()
    try:
        task_response = requests.get(get_task_list_url, headers={'EnterpriseManager.APISessionID': v_session_id, "Content-Length": "0"}, verify=False)
        configjson = json.loads(task_response.text)
        tasks = configjson['taskList']
        for index in range(0, len(tasks)):
            task = tasks[index]
            rep_server_tasks_lst.append(task['name'])
            logger.info(f"task {task['name']} added to list")
        logger.info(f"Tasks List Successfully retrieved for server {v_server}")
    except Exception as e:
        logger.error(f"Error while trying to retrieve tasks for server {v_server} {logger.exception(e)} - method get_task_list")
    return rep_server_tasks_lst

def get_task_details(v_em_host, v_session_id, v_server, v_task):
    logger.info(f"Retrieving Task Details for Server {v_server} and Task {v_task} - method get_task_details")
    get_task_details_url = (f"https://{v_em_host}/attunityenterprisemanager/api/v1/"
                            f"servers/{v_server}/tasks/{v_task}")
    try:
        task_response = requests.get(get_task_details_url, headers={'EnterpriseManager.APISessionID': v_session_id, "Content-Length": "0"}, verify=False)
        configjson = json.loads(task_response.text)
        return configjson
        logger.info(f"Tasks List Successfully retrieved for server {v_server}")
    except Exception as e:
        logger.error(f"Error while trying to retrieve tasks for server {v_server} {logger.exception(e)} - method get_task_list")
        return None
    return rep_server_tasks_lst
