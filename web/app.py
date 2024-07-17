from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data = {}

    # Fetch data from honeyphy
    try:
        honeyphy_response = requests.get('http://honeyphy-service:8080')
        data['honeyphy'] = honeyphy_response.json()
    except Exception as e:
        data['honeyphy'] = f"Error: {e}"

    # Fetch logs from honeyphy
    try:
        honeyphy_log_response = requests.get('http://honeyphy-service:9000/log')
        data['honeyphy_log'] = honeyphy_log_response.json()
    except Exception as e:
        data['honeyphy_log'] = f"Error: {e}"

    # Fetch data from crawler
    try:
        crawler_response = requests.get('http://crawler-service:5000/info')
        data['crawler'] = crawler_response.json()
    except Exception as e:
        data['crawler'] = f"Error: {e}"

    # Fetch certificates from cert
    try:
        cert_response = requests.get('http://cert-service:8500')
        data['cert'] = cert_response.json()
    except Exception as e:
        data['cert'] = f"Error: {e}"

    # Fetch data from virtot
    try:
        virtot_response = requests.post('http://virtot-service:8600')
        data['virtot'] = virtot_response.json()
    except Exception as e:
        data['virtot'] = f"Error: {e}"

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
