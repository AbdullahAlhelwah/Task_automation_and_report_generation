import os
import subprocess
from time import sleep
from flask import Flask, jsonify

import subprocess

app = Flask(__name__)

def get_system_info():
    cmd = 'wmic os get '
    targets = ['FreePhysicalMemory', 'NumberOfProcesses', 'TotalVirtualMemorySize', 'TotalVisibleMemorySize']
    
    system_info = {}
    for target in targets:
        new_cmd = cmd + target
        result = subprocess.run(new_cmd, capture_output=True, text=True, shell=False)
        x = result.stdout.strip().split("\n")
        system_info[target] = x[-1]
    
    return system_info

@app.route('/system_info', methods=['GET'])
def system_info():
    info = get_system_info()
    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)