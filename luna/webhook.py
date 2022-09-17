from flask import request, abort
from flask import Blueprint
import json


data = Blueprint("data", __name__, static_folder="static")



@data.route('/test')
def api_root():
    return "Welcome guys"

@data.route("/webhook", methods=["POST"])
def webhook():
    if request.headers['Content-Type'] == 'application/json':
        my_info = json.dumps(request.json)
        print(my_info)
        return my_info
