# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_iot_profile import XiqIotProfile  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqIotProfile(unittest.TestCase):
    """XiqIotProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqIotProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_iot_profile.XiqIotProfile()  # noqa: E501
        if include_optional :
            return XiqIotProfile(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '0', 
                app_id = 'THREAD_GATEWAY', 
                thread_gateway = extremecloudiq.models.xiq_iot_profile_thread_gateway.XiqIotProfileThreadGateway(
                    short_pan_id = 'a', 
                    ext_pan_id = 'a', 
                    master_key = 'a', 
                    network_name = '0', 
                    channel = 0, 
                    comm_credentials = 'a', 
                    comm_timeout = 1, 
                    enable_nat64 = True, 
                    white_list = [
                        extremecloudiq.models.xiq_iotp_tg_white_list_entry.XiqIotpTgWhiteListEntry(
                            long_eui = 'a', 
                            pskd = 'a', )
                        ], 
                    default_user_profile_id = 56, )
            )
        else :
            return XiqIotProfile(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '0',
                app_id = 'THREAD_GATEWAY',
        )

    def testXiqIotProfile(self):
        """Test XiqIotProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
