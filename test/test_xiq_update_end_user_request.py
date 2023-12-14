# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_update_end_user_request import XiqUpdateEndUserRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateEndUserRequest(unittest.TestCase):
    """XiqUpdateEndUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateEndUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_end_user_request.XiqUpdateEndUserRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateEndUserRequest(
                name = '0', 
                organization = '0', 
                visit_purpose = '0', 
                description = '0', 
                email_address = '0', 
                phone_number = '0', 
                password = '0', 
                email_password_delivery = '0', 
                sms_password_delivery = '0'
            )
        else :
            return XiqUpdateEndUserRequest(
        )

    def testXiqUpdateEndUserRequest(self):
        """Test XiqUpdateEndUserRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
