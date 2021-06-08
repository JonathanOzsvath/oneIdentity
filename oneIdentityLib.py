import ipaddress
import json
import logging
import urllib.request
from urllib.error import URLError

"""
Test Library for One Identity
"""


BASE_URL = 'http://www.geoplugin.net/json.gp?ip='


def get_json(request_url):
    """
    Send request to the server and give back the data in json object.

    :param request_url: Full request url.
    :return: Return data in json object if the request get success response.
    """
    try:
        with urllib.request.urlopen(request_url) as url:
            if url.status == 200:
                logging.info(f'Request response: {url.msg}')

            data = json.loads(url.read().decode())

            return data
    except URLError as e:
        logging.error(e)
        return None


def get_base_information(ip_address=None):
    """
    Give back the basic information of the ip address.

    :param ip_address: Valid ip address or nothing.
    :return: Return the basic information in a dictionary. If something went wrong give back empty dictionary.
    """

    if ip_address is None:
        ip = 'xxx.xxx.xxx.xxx'
    else:
        try:
            ip = ipaddress.ip_address(ip_address)
        except ValueError as error:
            logging.error(error)
            return {}

    request_url = f'{BASE_URL}{ip_address}'

    response = get_json(request_url)

    if response:
        output = {
            'city': response['geoplugin_city'],
            'country': response['geoplugin_countryName'],
            'region': response['geoplugin_regionName'],
            'timezone': response['geoplugin_timezone'],
            'coordinates': {
                'latitude': response['geoplugin_latitude'],
                'longitude': response['geoplugin_longitude']
            },
        }
    else:
        output = {}

    return output
