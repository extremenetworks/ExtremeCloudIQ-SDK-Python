# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_classification_rule import XiqClassificationRule  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqClassificationRule(unittest.TestCase):
    """XiqClassificationRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqClassificationRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_classification_rule.XiqClassificationRule()  # noqa: E501
        if include_optional :
            return XiqClassificationRule(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                name = '0', 
                description = '0', 
                classifications = [
                    extremecloudiq.models.xiq_classification.XiqClassification(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        classification_type = 'LOCATION', 
                        match = True, 
                        classification_id = 56, 
                        value = '0', )
                    ]
            )
        else :
            return XiqClassificationRule(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '0',
        )

    def testXiqClassificationRule(self):
        """Test XiqClassificationRule"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
