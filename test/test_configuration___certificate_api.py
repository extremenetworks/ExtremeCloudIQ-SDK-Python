# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.configuration___certificate_api import ConfigurationCertificateApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationCertificateApi(unittest.TestCase):
    """ConfigurationCertificateApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___certificate_api.ConfigurationCertificateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_certificates(self):
        """Test case for list_certificates

        List certificates  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
