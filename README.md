# ABot
An AI Bot who can understand natural language, execute your commands. Based on API.AI from Google.


# How to query
- For Get request
```
GET https://api.api.ai/v1/query?v=20150910&query=weather&timezone=Europe/Paris&lang=en&contexts=weather&contexts=europe&latitude=37.459157&longitude=-122.17926&sessionId=1234567890

Headers:
Authorization: Bearer YOUR_ACCESS_TOKEN
```

- For Post request
```
POST https://api.api.ai/v1/query?v=20150910

Headers:
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json; charset=utf-8

POST body:
{
    "query": [
        "and for tomorrow"
    ],
    "contexts": [{
        "name": "weather",
        "lifespan": 4
    }],
    "location": {
        "latitude": 37.459157,
        "longitude": -122.17926
    },
    "timezone": "America/New_York",
    "lang": "en",
    "sessionId": "1234567890"
}
```

# What happens after you query as above?
1. Send a request like `https://api.api.ai/v1/query?xxx` with token in headers.
2. Request will taken your natural language and go to API.AI server and find your agent based on your token.
3. Your agent get user's raw request, it will recongnize user's background intent and transfer that into a json {'action': xxx, 'params': {} }
4. Your agent will use its webhook api `https://wingjay-abot.herokuapp.com/webhook`, make a request to this webhook api, Just wingjay/abot repo.
5. My ABot will process request from API.AI, handle its action and params, generate a result, return to agent
6. API.AI agent take this result and return to user.


# Deploy to:
Remember to use `deploy` branch.
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Other
More info about Api.ai webhooks could be found here:
[Api.ai Webhook](https://docs.api.ai/docs/webhook)

Procfile tells Heroku how to run your application.
Learn more: https://devcenter.heroku.com/articles/procfile