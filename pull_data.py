import threading
import time
import os
import io
import json
import requests

exitFlag = 0


class CallApi(threading.Thread):
    def __init__(self, refresh_time, interval_time, symbol):
        threading.Thread.__init__(self)
        self.refresh_time = refresh_time
        self.interval_time = interval_time
        self.symbol = symbol
        self.run_time = True
        self.api_key = 'b97ec7bc8b5e0f368b7db0a58cdebf55'
        self.api_base_url = 'https://api.marketstack.com/v1/'
        self.session = requests.session()
        self.output = os.path.join('data', 'extract', 'prices.json')

    def run(self):

        while self.run_time:
            print("call every " + str(self.refresh_time) + "s")

            with io.open(self.output, 'w', encoding='utf8') as fd_out:
                self.extract(fd_out)

            time.sleep(self.refresh_time)

    def extract(self, fd_out):

        devices = self.get_file()

        json.dump(devices, fd_out, ensure_ascii=False, indent=4)

    def get_file(self):

        relative_url = "/intraday"
        params = dict()
        headers = dict()
        params['access_key'] = self.api_key
        params['interval'] = self.interval_time
        params['symbols'] = self.symbol

        url = self.api_base_url.strip("/") + relative_url
        print("http: Fetching:   {}".format(url))
        print("http: Parameters: {}".format(params))
        print("http: Headers:  {}".format(headers))

        response = self.session.get(url, params=params, headers=headers)

        print("http: Status ({}), {} bytes returned:".format(
            response.status_code, len(response.content)))
        content_str = ''
        if len(response.content) > 0:
            content_str = response.content.decode('utf-8')
            print(content_str)
            print()

        response.raise_for_status()

        if len(content_str) > 0:
            return json.loads(content_str)

        return None


def pull_data_from_api(time_refresh, interval, symbol):
    pull_data = CallApi(time_refresh, interval, symbol)
    pull_data.start()
# pull_data_from_api(10,"1min",["AAPL","AMD"])