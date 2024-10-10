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
from extremecloudiq.models.xiq_copilot_wireless_event import XiqCopilotWirelessEvent  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCopilotWirelessEvent(unittest.TestCase):
    """XiqCopilotWirelessEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCopilotWirelessEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_copilot_wireless_event.XiqCopilotWirelessEvent()  # noqa: E501
        if include_optional :
            return XiqCopilotWirelessEvent(
                average_value = 1.337, 
                maximum_value = 1.337, 
                mac = '0', 
                os_type = '0', 
                threshold = 1.337, 
                hostname = '0', 
                ssid = '0', 
                client_id = '0', 
                retries_data = extremecloudiq.models.xiq_wireless_event_retries_entity.XiqWirelessEventRetriesEntity(
                    avg_rx_retry = 1.337, 
                    max_rx_retry = 1.337, 
                    avg_tx_retry = 1.337, 
                    max_tx_retry = 1.337, 
                    rx_retry_threshold = 1.337, 
                    tx_retry_threshold = 1.337, )
            )
        else :
            return XiqCopilotWirelessEvent(
                mac = '0',
                client_id = '0',
        )

    def testXiqCopilotWirelessEvent(self):
        """Test XiqCopilotWirelessEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
