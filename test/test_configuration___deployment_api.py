# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.configuration___deployment_api import ConfigurationDeploymentApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationDeploymentApi(unittest.TestCase):
    """ConfigurationDeploymentApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___deployment_api.ConfigurationDeploymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deploy_config(self):
        """Test case for deploy_config

        Push configuration and upgrade firmware  # noqa: E501
        """
        pass

    def test_get_deploy_overview(self):
        """Test case for get_deploy_overview

        Get configuration deployment overview  # noqa: E501
        """
        pass

    def test_get_deploy_status(self):
        """Test case for get_deploy_status

        Get configuration deployment status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
