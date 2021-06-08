import socket
import unittest
import urllib.request

from oneIdentityLib import get_base_information


class TestOneIdentifyLib(unittest.TestCase):
    def test_none_ip(self):
        data = get_base_information()

        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        correct_data = get_base_information(external_ip)

        self.assertEqual(data, correct_data)

    def test_correct_ip(self):
        data = get_base_information('80.99.24.143')
        correct_data = {'city': 'Budapest',
                        'country': 'Hungary',
                        'region': 'Budapest',
                        'timezone': 'Europe/Budapest',
                        'coordinates': {'latitude': '47.5', 'longitude': '19.0412'}}
        self.assertEqual(data, correct_data)

    def test_wrong_ip(self):
        data = get_base_information('80.99.24.1432')
        correct_data = {}
        self.assertEqual(data, correct_data)


if __name__ == '__main__':
    unittest.main()
