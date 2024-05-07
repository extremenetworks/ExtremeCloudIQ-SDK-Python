# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_update_vlan_object_classified_entry_request import XiqUpdateVlanObjectClassifiedEntryRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateVlanObjectClassifiedEntryRequest(unittest.TestCase):
    """XiqUpdateVlanObjectClassifiedEntryRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateVlanObjectClassifiedEntryRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_vlan_object_classified_entry_request.XiqUpdateVlanObjectClassifiedEntryRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateVlanObjectClassifiedEntryRequest(
                vlan_id = 56, 
                classification_rule_id = 56
            )
        else :
            return XiqUpdateVlanObjectClassifiedEntryRequest(
                vlan_id = 56,
                classification_rule_id = 56,
        )

    def testXiqUpdateVlanObjectClassifiedEntryRequest(self):
        """Test XiqUpdateVlanObjectClassifiedEntryRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
