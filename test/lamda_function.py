import json
import ask_sdk_core

def get_trains_times(event, context):

    return ''

def lambda_handler(event , context):
    intent = event['request']['intent']['name']
    if intent == "GetTrainTimes":
        return get_trains_times(event,context)
