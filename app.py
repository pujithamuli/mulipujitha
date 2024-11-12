from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    name = "Your Full Name"  # Replace with your actual name
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    
    # Get top command output
    top_output = subprocess.getoutput("top -bn1")

    # Format the output
    output = f"<h1>System Info</h1>"
    output += f"<p><strong>Name:</strong> {name}</p>"
    output += f"<p><strong>Username:</strong> {username}</p>"
    output += f"<p><strong>Server Time (IST):</strong> {server_time}</p>"
    output += "<pre><strong>Top Output:</strong><br>" + top_output + "</pre>"
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
