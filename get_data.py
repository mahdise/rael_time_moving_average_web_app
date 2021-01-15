
import requests
from dotenv import load_dotenv
import os
import io
import json

class ExtractData:
  API_BASE_URL = 'https://api.marketstack.com/v1/'
  API_KEY = 'b97ec7bc8b5e0f368b7db0a58cdebf55'
  session = requests.session()
  def getData(self,symbol,interval,*, params={}, headers={}):
    '''
    Executes an HTTP GET against the given resource.
    The request is authorized using the given URL key.
    '''
    params['access_key'] = self.API_KEY
    params['interval'] = interval
    params['symbols'] = symbol
    relative_url = '/intraday'
    url = self.API_BASE_URL.strip("/") + relative_url

    # print("http: Fetching:   {}".format(url))
    # print("http: Parameters: {}".format(params))
    # print("http: Headers:  {}".format(headers))
    # print()
    #
    response = self.session.get(url, params=params, headers=headers)
    content_str = ''
    if len(response.content) > 0:
        content_str = response.content.decode('utf-8')

    content_json = json.loads(content_str)

    return content_json["data"]

    
    


# obj = ExtractData()
# print(obj.getData('AMD','1hour'))
