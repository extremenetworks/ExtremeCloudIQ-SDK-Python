# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_viq import XiqViq  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqViq(unittest.TestCase):
    """XiqViq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqViq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_viq.XiqViq()  # noqa: E501
        if include_optional :
            return XiqViq(
                devices = 56, 
                standalone = True, 
                expired = True, 
                customer_id = '0', 
                vhm_id = '0', 
                owner_id = 56, 
                licenses = [
                    extremecloudiq.models.xiq_viq_license.XiqViqLicense(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = 'BUY', 
                        active_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expire_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        entitlement_key = '0', 
                        entitlement_type = 'EVALUATION', 
                        mode = 'BUY', 
                        devices = 56, 
                        activated = 56, 
                        available = 56, 
                        license_type = '0', )
                    ]
            )
        else :
            return XiqViq(
        )

    def testXiqViq(self):
        """Test XiqViq"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
