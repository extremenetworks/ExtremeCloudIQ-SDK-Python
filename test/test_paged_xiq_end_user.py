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
from extremecloudiq.models.paged_xiq_end_user import PagedXiqEndUser  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqEndUser(unittest.TestCase):
    """PagedXiqEndUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqEndUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_end_user.PagedXiqEndUser()  # noqa: E501
        if include_optional :
            return PagedXiqEndUser(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_end_user.XiqEndUser(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        name = '0', 
                        description = '0', 
                        email_address = '0', 
                        phone_number = '0', 
                        password = '0', 
                        user_name = '0', 
                        organization = '0', 
                        visit_purpose = '0', 
                        email_password_delivery = '0', 
                        sms_password_delivery = '0', 
                        user_group_id = 56, 
                        user_group_name = '0', 
                        approval_type = '0', 
                        expired_time = 56, )
                    ]
            )
        else :
            return PagedXiqEndUser(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqEndUser(self):
        """Test PagedXiqEndUser"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
