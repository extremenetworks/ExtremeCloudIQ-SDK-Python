# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import extremecloudiq
from extremecloudiq.paths.radio_profiles_sensor_scan_id import put  # noqa: E501
from extremecloudiq import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRadioProfilesSensorScanId(ApiTestMixin, unittest.TestCase):
    """
    RadioProfilesSensorScanId unit test stubs
        Update sensor scan settings  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 401






if __name__ == '__main__':
    unittest.main()
