# -*- coding: UTF-8 -*-

import requests
import json

def get_reply(message):
  reply = "我不知道该说什么好了。"

  data = {
    "reqType":0,
      "perception": {
          "inputText": {
              "text": message
          }
      },
      "userInfo": {
          "apiKey": "c383a895748444df8f0c2b0dfb6e1794",
          "userId": "E132A4EE19475583632CD25F38BCB01E"
      }
  }
  response= requests.post('http://openapi.tuling123.com/openapi/api/v2', json.dumps(data))

  results = json.loads(response.text)['results']
  for result in results:
    if result['resultType'] == 'text':
      reply = result['values']['text']
  return reply
