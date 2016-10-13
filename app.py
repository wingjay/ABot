import os
import json

from flask import Flask
from flask import request
from flask import make_response


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hi, Here is wingjay ABot'
    

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
	req = request.get_json(silent=True, force=True)

	print("Request:")
	print(json.dumps(req, indent=4))

	ai_action = req.get("result").get("action")
	if ai_action:
		result = process(ai_action)
	else:
		result = {'test':1, 'test2':2}

	response = make_response(result)
	response.headers['Content-Type'] = 'application/json'
	return response


def process(action):
	print "process action"
	print action
	return action


def _mock_request_from_apiai():
	return {
    "originalRequest": None, 
    "result": {
        "fulfillment": {
            "speech": ""
        }, 
        "speech": "", 
        "source": "agent", 
        "actionIncomplete": False, 
        "resolvedQuery": "weather in London", 
        "action": "yahooWeatherForecast", 
        "score": 1.0, 
        "metadata": {
            "webhookUsed": "true", 
            "intentId": "471fd4d3-d755-40ac-bcb7-85f01c404f57", 
            "intentName": "weather"
        }, 
        "parameters": {
            "geo-city": "London"
        }, 
         "contexts": []
     	}, 
	    "timestamp": "2016-10-13T07:49:21.419Z", 
	    "sessionId": "81e229ed-d013-4b19-9ef6-7b1cdd5827d9", 
	    "id": "f9c03e3b-97b3-4d38-b2ca-d83b0598d5d2", 
	    "status": {
	        "errorType": "success", 
	        "code": 200
	    }
	}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')