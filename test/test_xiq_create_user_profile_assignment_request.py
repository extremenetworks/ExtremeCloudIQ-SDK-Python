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
from extremecloudiq.models.xiq_create_user_profile_assignment_request import XiqCreateUserProfileAssignmentRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateUserProfileAssignmentRequest(unittest.TestCase):
    """XiqCreateUserProfileAssignmentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateUserProfileAssignmentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_user_profile_assignment_request.XiqCreateUserProfileAssignmentRequest()  # noqa: E501
        if include_optional :
            return XiqCreateUserProfileAssignmentRequest(
                name = '0', 
                description = '0', 
                folder_ids = [
                    56
                    ], 
                assignment_radius_attribute = extremecloudiq.models.xiq_user_profile_assignment_radius_attribute.XiqUserProfileAssignmentRadiusAttribute(
                    attribute_type = 'TUNNEL', 
                    attribute_values = '0', )
            )
        else :
            return XiqCreateUserProfileAssignmentRequest(
        )

    def testXiqCreateUserProfileAssignmentRequest(self):
        """Test XiqCreateUserProfileAssignmentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
