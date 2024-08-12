# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.misc_api import MiscApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestMiscApi(unittest.TestCase):
    """MiscApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.misc_api.MiscApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_country_list(self):
        """Test case for get_country_list

        Get country list  # noqa: E501
        """
        pass

    def test_get_state_list_by_country_code(self):
        """Test case for get_state_list_by_country_code

        Get state list by country code  # noqa: E501
        """
        pass

    def test_validate_country_code(self):
        """Test case for validate_country_code

        Validate country code  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
