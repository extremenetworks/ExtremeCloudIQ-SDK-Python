# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_password_settings import XiqPasswordSettings  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqPasswordSettings(unittest.TestCase):
    """XiqPasswordSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqPasswordSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_password_settings.XiqPasswordSettings()  # noqa: E501
        if include_optional :
            return XiqPasswordSettings(
                enable_letters = True, 
                enable_numbers = True, 
                enable_special_characters = True, 
                password_concat_string = '0', 
                psk_generation_method = 'PASSWORD_ONLY', 
                password_character_types = 'INCLUDE_ALL_CHARACTER_TYPE_ENABLED', 
                password_length = 56
            )
        else :
            return XiqPasswordSettings(
                psk_generation_method = 'PASSWORD_ONLY',
                password_character_types = 'INCLUDE_ALL_CHARACTER_TYPE_ENABLED',
                password_length = 56,
        )

    def testXiqPasswordSettings(self):
        """Test XiqPasswordSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
