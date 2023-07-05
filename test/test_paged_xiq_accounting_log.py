# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_accounting_log import PagedXiqAccountingLog  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqAccountingLog(unittest.TestCase):
    """PagedXiqAccountingLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqAccountingLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_accounting_log.PagedXiqAccountingLog()  # noqa: E501
        if include_optional :
            return PagedXiqAccountingLog(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_accounting_log.XiqAccountingLog(
                        id = 56, 
                        username = '0', 
                        org_id = 56, 
                        timestamp = 56, 
                        vhm_id = '0', 
                        device_serial_number = '0', 
                        acct_session_id = '0', 
                        acct_multi_id = '0', 
                        group_name = '0', 
                        nas_ip_address = '0', 
                        nas_port = '0', 
                        nas_port_type = '0', 
                        acct_start_time = 56, 
                        acct_stop_time = 56, 
                        acct_session_time = 56, 
                        acct_authentic = '0', 
                        connect_info = '0', 
                        acct_input_octets = 56, 
                        acct_output_octets = 56, 
                        called_station_id = '0', 
                        calling_station_id = '0', 
                        acct_terminate_cause = '0', 
                        service_type = '0', 
                        framed_ip_address = '0', 
                        acct_start_delay = 56, 
                        acct_stop_delay = 56, 
                        ssid = '0', 
                        identity = '0', 
                        nas_identifier = '0', 
                        mgmt_mac_address = '0', 
                        attribute_num = 56, 
                        event_time = 56, 
                        usage = 56, )
                    ]
            )
        else :
            return PagedXiqAccountingLog(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqAccountingLog(self):
        """Test PagedXiqAccountingLog"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
