from flask import Flask
from flask_testing import TestCase
import subprocess
import json
import logging

# logging
logger = logging.getLogger('server_logger')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('server.log')
# file_handler = logging.FileHandler('server.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

# APIs
@app.route('/service/latency_check', methods=['GET'])
def latency_check():
    latency = subprocess.run(["systemctl", "--user", "status", "latency_check.service"], capture_output=True)
    latency = (latency.stdout.decode('utf-8').split("\n"))
    result = {}
    for i in latency:
        i = str(i).strip()
        if i.startswith("Loaded") or i.startswith("Active"):
            result[i.split(":")[0]] = i.split(":")[1].strip().split(" ")[0]
    logger.log(logging.INFO, "LATENCY_CHECK_SERVICE Status: " + str(result))
    if result["Active"] == "inactive":
        return json.dumps({'latency_service': "inactive", "status": result })
    else:
        return json.dumps({'latency_service': "active", "status": result })
@app.route('/service/latency_check/start', methods=['GET'])
def latency_check_start():
    start = subprocess.run(["systemctl", "--user", "start", "latency_check.service"], capture_output=True)
    print(str(start.returncode))
    start = (start.stdout.decode('utf-8').split("\n"))
    print(str(start))
    result = {}
    for i in start:
        i = str(i).strip()
        print(str(i))
        # if i.startswith("Loaded") or i.startswith("Active"):
        #     result[i.split(":")[0]] = i.split(":")[1].strip().split(" ")[0]
    logger.log(logging.INFO, "LATENCY_CHECK_SERVICE Status: " + str(result))
    # if result["Active"] == "inactive":
        # return json.dumps({'latency_service': "inactive", "status": result })
    # else:
    return json.dumps({'latency_service': "active", "status": result })

@app.route('/service/cpu_idle', methods=['GET'])
def cpu_idle():
    cpu = subprocess.run(["systemctl", "--user", "status", "cpu_check.service"], capture_output=True)
    cpu = (cpu.stdout.decode('utf-8').split("\n"))
    result = {}
    for i in cpu:
        i = str(i).strip()
        if i.startswith("Loaded") or i.startswith("Active"):
            result[i.split(":")[0]] = i.split(":")[1].strip().split(" ")[0]
    print(str(result))
    logger.log(logging.INFO, "CPU_SERVICE Status: " + str(result))
    if result["Active"] == "inactive":
        return json.dumps({'cpu_check_service': "inactive", "status": result })
    else:
        return json.dumps({'cpu_check_service': "active", "status": result})

if __name__ == '__main__':
    app.run(port=8080)