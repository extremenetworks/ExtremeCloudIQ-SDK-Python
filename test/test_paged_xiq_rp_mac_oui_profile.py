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
from extremecloudiq.models.paged_xiq_rp_mac_oui_profile import PagedXiqRpMacOuiProfile  # noqa: E501
from extremecloudiq.rest import ApiException

class TestPagedXiqRpMacOuiProfile(unittest.TestCase):
    """PagedXiqRpMacOuiProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedXiqRpMacOuiProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.paged_xiq_rp_mac_oui_profile.PagedXiqRpMacOuiProfile()  # noqa: E501
        if include_optional :
            return PagedXiqRpMacOuiProfile(
                page = 56, 
                count = 56, 
                total_pages = 56, 
                total_count = 56, 
                data = [
                    extremecloudiq.models.xiq_rp_mac_oui_profile.XiqRpMacOuiProfile(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        description = '0', 
                        predefined = True, 
                        value = '0', 
                        mac_type = '0', 
                        defender_defined = True, 
                        extreme_iot_defined = True, )
                    ]
            )
        else :
            return PagedXiqRpMacOuiProfile(
                page = 56,
                count = 56,
                total_pages = 56,
                total_count = 56,
        )

    def testPagedXiqRpMacOuiProfile(self):
        """Test PagedXiqRpMacOuiProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
