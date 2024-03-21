# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_nac_entitlement_allocation import XiqNacEntitlementAllocation  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqNacEntitlementAllocation(unittest.TestCase):
    """XiqNacEntitlementAllocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqNacEntitlementAllocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_nac_entitlement_allocation.XiqNacEntitlementAllocation()  # noqa: E501
        if include_optional :
            return XiqNacEntitlementAllocation(
                allocation_list = [
                    extremecloudiq.models.xiq_nac_entitlement_allocation_detail.XiqNacEntitlementAllocationDetail(
                        owner_id = 56, 
                        serial_no = '0', 
                        display_name = '0', 
                        percentage = 1.337, 
                        allocated_devices = 56, )
                    ], 
                total_available_nac_licenses = 56, 
                available_nac_licenses = 56
            )
        else :
            return XiqNacEntitlementAllocation(
        )

    def testXiqNacEntitlementAllocation(self):
        """Test XiqNacEntitlementAllocation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()