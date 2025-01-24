# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import extremecloudiq
from extremecloudiq.paths.copilot_anomalies_wifi_capacity_stats import get  # noqa: E501
from extremecloudiq import configuration, schemas, api_client

from .. import ApiTestMixin


class TestCopilotAnomaliesWifiCapacityStats(ApiTestMixin, unittest.TestCase):
    """
    CopilotAnomaliesWifiCapacityStats unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 401




if __name__ == '__main__':
    unittest.main()
