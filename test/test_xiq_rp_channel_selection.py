# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_rp_channel_selection import XiqRpChannelSelection  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqRpChannelSelection(unittest.TestCase):
    """XiqRpChannelSelection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqRpChannelSelection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_rp_channel_selection.XiqRpChannelSelection()  # noqa: E501
        if include_optional :
            return XiqRpChannelSelection(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                enable_dynamic_channel_switching = True, 
                channel_width = '0', 
                enable_dynamic_frequency_selection = True, 
                enable_static_channel = True, 
                enable_zero_wait_dfs = True, 
                enable_use_last_selection = True, 
                exclude_channels = '0', 
                exclude_channels_width = '0', 
                channel = 56, 
                enable_limit_channel_selection = True, 
                channel_region = '0', 
                channel_model = 3, 
                channels = '0', 
                enable_channel_auto_selection = True, 
                channel_selection_start_time = '0', 
                channel_selection_end_time = '0', 
                enable_avoid_switch_channel_if_clients_connected = True, 
                channel_selection_max_clients = 56, 
                enable_switch_channel_if_exceed_threshold = True, 
                rf_interference_threshold = 56, 
                crc_error_threshold = 56
            )
        else :
            return XiqRpChannelSelection(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqRpChannelSelection(self):
        """Test XiqRpChannelSelection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
