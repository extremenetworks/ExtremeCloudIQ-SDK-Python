# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import extremecloudiq
from extremecloudiq.paths.dashboard_wired_device_health_memory_usage_issues import post  # noqa: E501
from extremecloudiq import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDashboardWiredDeviceHealthMemoryUsageIssues(ApiTestMixin, unittest.TestCase):
    """
    DashboardWiredDeviceHealthMemoryUsageIssues unit test stubs
        Wired Device Health Memory Usage Issues  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 401






if __name__ == '__main__':
    unittest.main()
