from flask import Flask, abort
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}) # -> get rid of cors

 

@app.route("/jobs/<int:id>", methods=['GET']) # value is int, if not -> 404
def jobs(id):
    if id not in range(14,16): abort(400) # value is not in range -> 400
    with open(f'./jsons/job_{id}.json', 'r') as f:
        data = json.load(f)
    return data