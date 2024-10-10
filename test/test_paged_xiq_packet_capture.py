# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_packet_capture import PagedXiqPacketCapture  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqPacketCapture(unittest.TestCase):
    """PagedXiqPacketCapture unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqPacketCapture
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_packet_capture.PagedXiqPacketCapture()  # noqa: E501
        if include_optional :
            return PagedXiqPacketCapture(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_packet_capture.XiqPacketCapture(
                        id = 56, 
                        start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        name = '0', 
                        duration = 0, 
                        capture_id_type = 'AP_SERIAL_NUMBER', 
                        ap_serial_number = '0', 
                        device_ids = [
                            56
                            ], 
                        location_id = 56, 
                        destination = 'CLOUD', 
                        filter = extremecloudiq.models.xiq_capture_filter.XiqCaptureFilter(
                            mac_addr = [
                                '0'
                                ], 
                            ip_addr = [
                                '0'
                                ], 
                            protocol = 'ANY', 
                            protocol_number = 0, 
                            port = 56, 
                            vlan = '0', 
                            wlan = '0', ), 
                        capture_if = extremecloudiq.models.xiq_capture_location.XiqCaptureLocation(
                            direction = 'BOTH', 
                            radio = 'ALL', 
                            wired_interface = 'ALL', 
                            wireless_band = 'ALL', 
                            wired_filters = [
                                'DHCP'
                                ], 
                            wireless_filters = [
                                'MANAGEMENT'
                                ], ), 
                        status = 'INITIAL', 
                        results = [
                            extremecloudiq.models.xiq_capture_result.XiqCaptureResult(
                                id = 56, 
                                org_id = 56, 
                                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                device_id = 56, 
                                hostname = '0', 
                                mac_address = '0', 
                                interface_name = '0', 
                                location_id = 56, 
                                locations = [
                                    extremecloudiq.models.xiq_location_legend.XiqLocationLegend(
                                        id = 56, 
                                        name = '0', )
                                    ], 
                                error_message = '0', 
                                storage = extremecloudiq.models.xiq_storage.XiqStorage(
                                    cloud_storage = '0', 
                                    cloud_shark_storage = extremecloudiq.models.xiq_cloud_shark_storage.XiqCloudSharkStorage(
                                        file_name = '0', 
                                        file_url = '0', ), ), )
                            ], 
                        cloud_storage = '0', )
                    ]
            )
        else :
            return PagedXiqPacketCapture(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqPacketCapture(self):
        """Test PagedXiqPacketCapture"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
