# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.paged_xiq_audit_log import PagedXiqAuditLog  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqAuditLog(unittest.TestCase):
    """PagedXiqAuditLog unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqAuditLog
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_audit_log.PagedXiqAuditLog()  # noqa: E501
        if include_optional :
            return PagedXiqAuditLog(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_audit_log.XiqAuditLog(
                        id = 56, 
                        category = 'ADMIN', 
                        user_id = 56, 
                        code = 56, 
                        username = '0', 
                        vhm_name = '0', 
                        parameters = '0', 
                        org_id = 56, 
                        timestamp = 56, 
                        description = '0', )
                    ]
            )
        else :
            return PagedXiqAuditLog(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqAuditLog(self):
        """Test PagedXiqAuditLog"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
