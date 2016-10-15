import urllib
import json


def process(city):
    if city is None:
        return None
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = make_yql_query(city)
    # "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='London')"
    if yql_query is None:
        return {}
    yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
    # 'https://query.yahooapis.com/v1/public/yql?q=select+%2A+from+weather.forecast+where+woeid+in+%28select+woeid+from+geo.places%281%29+where+text%3D%27London%27%29&format=json'
    result = urllib.urlopen(yql_url).read()
    data = json.loads(result)
    res = make_webhook_result(data)
    ''' {
            'displayText': u'Today in London: Showers, the temperature is 50 F',
            'source': 'wingjay-github-apiai-weather-webhook-sample',
            'speech': u'Today in London: Showers, the temperature is 50 F'
        }
    '''
    return res


def make_yql_query(city):
    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" \
           + city + "')"


def make_webhook_result(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return speech
