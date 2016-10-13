## Request content To My server
 10.136.102.79 - - [13/Oct/2016 07:48:36] "POST /webhook HTTP/1.1" 200 -
 Request:
{
    "originalRequest": null, 
    "result": {
        "fulfillment": {
            "speech": ""
        }, 
        "speech": "", 
        "source": "agent", 
        "actionIncomplete": false, 
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
{'status': {'code': 200, 'errorType': 'success'}, 'timestamp': '2016-10-13T07:49:21.419Z', 'sessionId': '81e229ed-d013-4b19-9ef6-7b1cdd5827d9', 'result': {'source': 'agent', 'score': 1.0, 'speech': '', 'fulfillment': {'speech': ''}, 'actionIncomplete': False, 'action': 'yahooWeatherForecast', 'resolvedQuery': 'weather in London', 'parameters': {'geo-city': 'London'}, 'contexts': [], 'metadata': {'intentId': '471fd4d3-d755-40ac-bcb7-85f01c404f57', 'intentName': 'weather', 'webhookUsed': 'true'}}, 'id': 'f9c03e3b-97b3-4d38-b2ca-d83b0598d5d2', 'originalRequest': None}

## Response From My server To Api.AI
Today in London: Showers, the temperature is 50 F

## Request & Response From API.AI Agent
Raw console Request: https://console.api.ai/api/query?v=20150910
{
	"q":"weather in London",
	"timezone":"2016-10-13T16:01:27+0800",
	"lang":"en",
	"sessionId":"81e229ed-d013-4b19-9ef6-7b1cdd5827d9",
	"resetContexts":false
}

Raw Response:
{
  "id": "1ac10e65-f261-4129-94fe-9f705c84b5bb",
  "timestamp": "2016-10-13T08:01:28.985Z",
  "result": {
    "source": "agent",
    "resolvedQuery": "weather in London",
    "action": "yahooWeatherForecast",
    "actionIncomplete": false,
    "parameters": {
      "geo-city": "London"
    },
    "contexts": [],
    "metadata": {
      "intentId": "471fd4d3-d755-40ac-bcb7-85f01c404f57",
      "webhookUsed": "true",
      "intentName": "weather"
    },
    "fulfillment": {
      "speech": "Today in London: Showers, the temperature is 50 F",
      "source": "wingjay-github-apiai-weather-webhook-sample",
      "displayText": "Today in London: Showers, the temperature is 50 F"
    },
    "score": 1.0
  },
  "alternateResult": {
    "source": "domains",
    "resolvedQuery": "weather in London",
    "action": "weather.search",
    "actionIncomplete": false,
    "parameters": {
      "request_type": "explicit",
      "location": "London"
    },
    "metadata": {},
    "fulfillment": {
      "speech": ""
    },
    "score": 0.0
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "81e229ed-d013-4b19-9ef6-7b1cdd5827d9"
}

Final Response :
{
  "id": "f9c03e3b-97b3-4d38-b2ca-d83b0598d5d2",
  "timestamp": "2016-10-13T07:49:21.419Z",
  "result": {
    "source": "agent",
    "resolvedQuery": "weather in London",
    "action": "yahooWeatherForecast",
    "actionIncomplete": false,
    "parameters": {
      "geo-city": "London"
    },
    "contexts": [],
    "metadata": {
      "intentId": "471fd4d3-d755-40ac-bcb7-85f01c404f57",
      "webhookUsed": "true",
      "intentName": "weather"
    },
    "fulfillment": {
      "speech": "Today in London: Showers, the temperature is 50 F",
      "source": "wingjay-github-apiai-weather-webhook-sample",
      "displayText": "Today in London: Showers, the temperature is 50 F"
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "81e229ed-d013-4b19-9ef6-7b1cdd5827d9"
}