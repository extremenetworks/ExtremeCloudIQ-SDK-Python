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
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_iotp_ma_ble_beacon import XiqIotpMaBleBeacon  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqIotpMaBleBeacon(unittest.TestCase):
    """XiqIotpMaBleBeacon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqIotpMaBleBeacon
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_iotp_ma_ble_beacon.XiqIotpMaBleBeacon()  # noqa: E501
        if include_optional :
            return XiqIotpMaBleBeacon(
                applications = [
                    extremecloudiq.models.xiq_iotp_ma_ble_beacon_application.XiqIotpMaBleBeaconApplication(
                        measured_rss = -120, 
                        advertise_interval = 100, 
                        tx_power = -16, 
                        major = 0, 
                        minor = 0, 
                        uuid = 'a', 
                        url = '0', 
                        app_type = 'IBEACON', )
                    ]
            )
        else :
            return XiqIotpMaBleBeacon(
        )

    def testXiqIotpMaBleBeacon(self):
        """Test XiqIotpMaBleBeacon"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
