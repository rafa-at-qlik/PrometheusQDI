import json
import logging
import time

from qem_util import *
from Task import *
import yaml
from prometheus_client import Gauge, start_http_server
from QEMGauge import *

# Logging Config
logger = logging.getLogger(__name__)
time_format = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename='PrometheusQDI.log', format='%(asctime)s - %(levelname)s - %(message)s', filemode='a', level=logging.INFO, datefmt=time_format)

###################################################
# EM Credentials
with open('access.yml') as f:
    access_cfg = yaml.safe_load(f)
em_host = access_cfg['QEM']['host']
em_user = access_cfg['QEM']['user']
em_password = access_cfg['QEM']['password']
base_api_url = f"https://{em_host}/attunityenterprisemanager/api/v1"
###################################################
# Retrieving Config
with open('config.yml') as f:
    config_cfg = yaml.safe_load(f)
###################################################

if __name__ == '__main__':
    start_http_server(config_cfg['Prometheus']['pull_port'])
    qem_gauge = QEMGauge()
    while True:
        session_id = get_session_id(em_user, em_password, base_api_url)
        rep_servers = get_replicate_servers(session_id, em_host)
        time.sleep(config_cfg['QEM']['collection_interval_s'])
        for rep_server in rep_servers:
            tasks = get_task_list(em_host, session_id, rep_server)
            for task in tasks:
                task_details = get_task_details(em_host, session_id, rep_server, task)
                task_dc = Task().from_dict(task_details)
                qem_gauge.set_gauges(task_dc, rep_server, task)
