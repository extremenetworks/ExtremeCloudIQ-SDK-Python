# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_iot_profile_request import XiqIotProfileRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqIotProfileRequest(unittest.TestCase):
    """XiqIotProfileRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqIotProfileRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_iot_profile_request.XiqIotProfileRequest()  # noqa: E501
        if include_optional :
            return XiqIotProfileRequest(
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
                    default_user_profile_id = 56, ), 
                app_supported = 'SINGLE', 
                ble_beacon = extremecloudiq.models.xiq_iotp_ma_ble_beacon.XiqIotpMaBleBeacon(
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
                        ], ), 
                ble_scan = extremecloudiq.models.xiq_iotp_ma_ble_scan.XiqIotpMaBleScan(
                    destination = extremecloudiq.models.xiq_iotp_ma_ble_scan_destination.XiqIotpMaBleScanDestination(
                        interval = 1, 
                        http_server = extremecloudiq.models.xiq_http_server.XiqHttpServer(
                            url = '0', 
                            interval = 1, ), ), 
                    applications = [
                        extremecloudiq.models.xiq_iotp_ma_ble_scan_application.XiqIotpMaBleScanApplication(
                            min_rss = -120, 
                            uuid = 'a', 
                            vendors = [
                                extremecloudiq.models.xiq_iotp_ma_ble_scan_vendor.XiqIotpMaBleScanVendor(
                                    vendor_type = 'ANY', 
                                    vendor_name = '0', 
                                    company_id = -1, )
                                ], 
                            app_type = 'IBEACON', )
                        ], )
            )
        else :
            return XiqIotProfileRequest(
                name = '0',
                app_id = 'THREAD_GATEWAY',
                app_supported = 'SINGLE',
        )

    def testXiqIotProfileRequest(self):
        """Test XiqIotProfileRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
