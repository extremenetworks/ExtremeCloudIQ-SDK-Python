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
from extremecloudiq.models.paged_xiq_sms_log import PagedXiqSmsLog  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqSmsLog(unittest.TestCase):
    """PagedXiqSmsLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqSmsLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_sms_log.PagedXiqSmsLog()  # noqa: E501
        if include_optional :
            return PagedXiqSmsLog(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_sms_log.XiqSmsLog(
                        id = 56, 
                        user_id = 56, 
                        customer_id = '0', 
                        tel = '0', 
                        profile_name = '0', 
                        status = 'SEND_OUT', 
                        message_id = '0', 
                        status_from_provider = '0', 
                        provider_type = '0', 
                        org_id = 56, 
                        timestamp = 56, )
                    ]
            )
        else :
            return PagedXiqSmsLog(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqSmsLog(self):
        """Test PagedXiqSmsLog"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
