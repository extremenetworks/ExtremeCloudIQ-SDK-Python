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
from extremecloudiq.models.xiq_update_site_request import XiqUpdateSiteRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqUpdateSiteRequest(unittest.TestCase):
    """XiqUpdateSiteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqUpdateSiteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_update_site_request.XiqUpdateSiteRequest()  # noqa: E501
        if include_optional :
            return XiqUpdateSiteRequest(
                parent_id = 56, 
                name = '0', 
                address = extremecloudiq.models.xiq_address.XiqAddress(
                    address = '0', 
                    address2 = '0', 
                    city = '0', 
                    state = '0', 
                    postal_code = '0', ), 
                country_code = 56, 
                latitude = 1.337, 
                longitude = 1.337
            )
        else :
            return XiqUpdateSiteRequest(
                name = '0',
                country_code = 56,
        )

    def testXiqUpdateSiteRequest(self):
        """Test XiqUpdateSiteRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
