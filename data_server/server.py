from flask import Flask
import json
import logging

# logging
logger = logging.getLogger('server_logger')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('/home/ubuntu/.dots/data/server.log')
# file_handler = logging.FileHandler('server.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

# APIs
@app.route('/service/latency_check', methods=['GET'])
def latency_check():
    # Read File
    latency = open("/home/ubuntu/.dots/data/latency_data.txt").read().strip()
    logger.log(logging.INFO, "Latency: " + latency + "ms")
    return json.dumps({'latency': latency})

@app.route('/service/cpu_idle', methods=['GET'])
def cpu_idle():
    # Read File
    cpu = open("/home/ubuntu/.dots/data/cpu_data.txt").read().strip()
    logger.log(logging.INFO, "Idle CPU: " + cpu + "%")
    return json.dumps({'idle_cpu': cpu})

if __name__ == '__main__':
    app.run(port=8080)