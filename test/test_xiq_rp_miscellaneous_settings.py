# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_rp_miscellaneous_settings import XiqRpMiscellaneousSettings  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqRpMiscellaneousSettings(unittest.TestCase):
    """XiqRpMiscellaneousSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqRpMiscellaneousSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_rp_miscellaneous_settings.XiqRpMiscellaneousSettings()  # noqa: E501
        if include_optional :
            return XiqRpMiscellaneousSettings(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                sla_throughput_level = '0', 
                radio_range = 56, 
                wmm_qos_settings = [
                    extremecloudiq.models.xiq_rp_wmm_qos_settings.XiqRpWmmQosSettings(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        access_category = '0', 
                        arbitration_interframe_space = 56, 
                        min_contention_window = 56, 
                        max_contention_window = 56, 
                        transmission_opportunity_limit = 56, 
                        enable_no_ack = True, )
                    ]
            )
        else :
            return XiqRpMiscellaneousSettings(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqRpMiscellaneousSettings(self):
        """Test XiqRpMiscellaneousSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
