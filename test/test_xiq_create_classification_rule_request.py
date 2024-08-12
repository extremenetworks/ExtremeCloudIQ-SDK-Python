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
from extremecloudiq.models.xiq_create_classification_rule_request import XiqCreateClassificationRuleRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqCreateClassificationRuleRequest(unittest.TestCase):
    """XiqCreateClassificationRuleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqCreateClassificationRuleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_create_classification_rule_request.XiqCreateClassificationRuleRequest()  # noqa: E501
        if include_optional :
            return XiqCreateClassificationRuleRequest(
                name = '0', 
                description = '0', 
                classifications = [
                    extremecloudiq.models.xiq_create_classification_request.XiqCreateClassificationRequest(
                        classification_type = 'CLASSIFICATION_TYPE_UNSPECIFIED', 
                        match = True, 
                        classification_type_id = 56, )
                    ]
            )
        else :
            return XiqCreateClassificationRuleRequest(
                name = '0',
                classifications = [
                    extremecloudiq.models.xiq_create_classification_request.XiqCreateClassificationRequest(
                        classification_type = 'CLASSIFICATION_TYPE_UNSPECIFIED', 
                        match = True, 
                        classification_type_id = 56, )
                    ],
        )

    def testXiqCreateClassificationRuleRequest(self):
        """Test XiqCreateClassificationRuleRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
