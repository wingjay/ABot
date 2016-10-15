# get entities from API.AI
import urllib2
import json

token = "8c1583c6a19d4ca09247a38ddcc2f740"
author_entity_id = "ad1e6041-0979-41bc-aa6b-3ef308f9045c"
time_range_entity_id = "c6645f34-3fdf-4ee6-8670-27991cb2dba6"


def get_all_entities():
    return _handle_request("https://api.api.ai/v1/entities?v=20150910")


def get_author_entities():
    result = _handle_request("https://api.api.ai/v1/entities/%s?v=20150910" % author_entity_id)
    return _fetch_entry_list(result)


def get_time_range_entities():
    result = _handle_request("https://api.api.ai/v1/entities/%s?v=20150910" % time_range_entity_id)
    return _fetch_entry_list(result)


def _handle_request(url):
    request = urllib2.Request(url)
    request.add_header("Authorization", "Bearer %s" % token)
    result = urllib2.urlopen(request)
    result = json.load(result)
    return result


def _fetch_entry_list(result):
    if result is not None and 'entries' not in result and 'status' in result:
        print result['status']['errorDetails']
        return []
    entries = result['entries']
    return [entry['value'] for entry in entries]
