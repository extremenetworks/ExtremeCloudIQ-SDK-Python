# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_valid_for_time_period_settings import XiqValidForTimePeriodSettings  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqValidForTimePeriodSettings(unittest.TestCase):
    """XiqValidForTimePeriodSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqValidForTimePeriodSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_valid_for_time_period_settings.XiqValidForTimePeriodSettings()  # noqa: E501
        if include_optional :
            return XiqValidForTimePeriodSettings(
                valid_time_period_after = 'ID_CREATION', 
                after_id_creation_settings = extremecloudiq.models.xiq_valid_time_period_after_id_creation.XiqValidTimePeriodAfterIdCreation(
                    valid_time_period = 56, 
                    valid_time_period_unit = 'MINUTE', ), 
                after_first_login_settings = extremecloudiq.models.xiq_valid_time_period_after_first_login.XiqValidTimePeriodAfterFirstLogin(
                    valid_time_period = 56, 
                    valid_time_period_unit = 'MINUTE', 
                    first_login_within = 56, 
                    first_login_within_unit = 'MINUTE', )
            )
        else :
            return XiqValidForTimePeriodSettings(
                valid_time_period_after = 'ID_CREATION',
        )

    def testXiqValidForTimePeriodSettings(self):
        """Test XiqValidForTimePeriodSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
