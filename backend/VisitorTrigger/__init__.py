import logging
import uuid
import json

import azure.functions as func

def main(req: func.HttpRequest, messageJSON, message: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    counter = messageJSON[0]['usersCounter'] + 1
    messageJSON[0]['usersCounter'] = counter
    test = messageJSON[0].to_json()
    message.set(func.Document.from_json(messageJSON[0].to_json()))
    if counter:
        return func.HttpResponse(f"{counter}", status_code=200)
    else:
        return func.HttpResponse(
             "Error",
             status_code=500
        )
