# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_radio_profile import PagedXiqRadioProfile  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqRadioProfile(unittest.TestCase):
    """PagedXiqRadioProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqRadioProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_radio_profile.PagedXiqRadioProfile()  # noqa: E501
        if include_optional :
            return PagedXiqRadioProfile(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_radio_profile.XiqRadioProfile(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        predefined = True, 
                        description = '0', 
                        transmission_power = 56, 
                        max_transmit_power = 56, 
                        transmission_power_floor = 56, 
                        transmission_power_max_drop = 56, 
                        max_clients = 56, 
                        enable_client_transmission_power = True, 
                        client_transmission_power = 56, 
                        enable_ofdma = True, 
                        radio_mode = 'B_G', 
                        neighborhood_analysis_id = 56, 
                        channel_selection_id = 56, 
                        radio_usage_optimization_id = 56, 
                        miscellaneous_settings_id = 56, 
                        presence_server_settings_id = 56, 
                        sensor_scan_settings_id = 56, )
                    ]
            )
        else :
            return PagedXiqRadioProfile(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqRadioProfile(self):
        """Test PagedXiqRadioProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
