import requests
import logging
import json
from simple_stripe_client.resources import Constants

try:
    # python 3
    import http.client as http_client
    from urllib.parse import urlparse, urlunparse, urlencode
except ImportError:
    # python 2
    import httplib as http_client
    # from urlparse import urlparse, urlunparse
    from urllib import urlencode

API_BASE_URL = 'https://api.stripe.com'
API_VERSION = 'v1'


class Api(object):
    def __init__(self, api_key, debug_http=False, timeout=None, base_url=None, api_version=None):
        self.api_key = api_key
        self._debug_http = debug_http
        self._timeout = timeout
        self.resources = Constants.resources
        self.url = ''

        if base_url:
            self.base_url = base_url
        else:
            self.base_url = API_BASE_URL

        if api_version:
            self.base_url = '/'.join([self.base_url, api_version])
        else:
            self.base_url = '/'.join([self.base_url, API_VERSION])

        if debug_http:
            http_client.HTTPConnection.debuglevel = 1
            logging.basicConfig()  # initialize logging
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True

        self._session = requests.Session()
        self._session.headers.update({'Authorization': 'Bearer ' + self.api_key})

    def __getattr__(self, attribute):
        """
        Intercepts every call to atrribute that does not exists
        :param attribute:
        :return:
        """
        if attribute in self.resources:
            self.url = '/'.join([self.url, attribute])
            return self
        else:
            raise AttributeError(attribute)

    def id(self,value):
        self.url = '/'.join([self.url,value])
        return self


    def get(self,**kwargs):
        print("url="+self.url)
        print(kwargs)
        return self._make_request('GET', self._get_and_reset_url(),data=kwargs)

    def post(self,**kwargs):
        print("url=" + self.url)
        return self._make_request('POST', self._get_and_reset_url(), data=kwargs)

    def put(self):
        pass

    def delete(self):
        pass

    def _get_and_reset_url(self):
        url = self.url
        self.url = None
        return url

    def _make_request(self, http_method, url, data=None, json=None):
        """
        :param http_method: http method i.e. GET, POST, PUT etc
        :param url: api endpoint url
        :param data: dictionary of key/value params
        :param json: json data
        :return:
        """
        if not data:
            data = {}

        data = self.__class__._parse_request_data(data)
        response = {}
        if http_method == 'GET':
            url = self._build_url(url, extra_params=data)
            response = self._session.get(url, timeout=self._timeout)
        elif http_method == 'POST':
            url = self._build_url(url)

            if json:
                response = self._session.post(url, json=json, timeout=self._timeout)
            else:
                response = self._session.post(url, data=data, timeout=self._timeout)

        try:
            response = self.__class__._parse_json_data(response.content.decode('utf-8'))
        except AttributeError as e:
            response = {"Error": "Unknown error while parsing response"}

        return response

    def _build_url(self, url, path_elements=None, extra_params=None):
        url = self.base_url + url
        (scheme, netloc, path, params, query, fragment) = urlparse(url)

        # Add extra_parameters to the query
        if extra_params and len(extra_params) > 0:
            extra_query = self.__class__._encode_parameters(extra_params)
            if query:
                query += '&' + extra_query
            else:
                query = extra_query
        print(url+'?'+query)
        return urlunparse((scheme, netloc, path, params, query, fragment))

    @staticmethod
    def _encode_parameters(parameters):
        """
        Return url encoded string in 'key=value&key=value' format
        """
        if not parameters or not isinstance(parameters, dict):
            return None
        return urlencode(parameters)

    @staticmethod
    def _parse_json_data(json_data):
        try:
            data = json.loads(json_data)
        except ValueError:
            data = json.loads('{"Error": "Unknown error while parsing response"}')
        return data

    @staticmethod
    def _parse_request_data(data):
        pd = {}
        for key,value in data.items():
            if isinstance(value,dict):
                npd = {}
                for k , v in value.items():
                    npd_key = "{key}[{k}]".format(key=key,k=k)
                    npd[npd_key] = v
                pd.update(__class__._parse_request_data(npd))
            else:
                pd.update({ key : value })
        return pd