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
from extremecloudiq.models.xiq_account import XiqAccount  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAccount(unittest.TestCase):
    """XiqAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_account.XiqAccount()  # noqa: E501
        if include_optional :
            return XiqAccount(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '0', 
                account_type = 'INTERNAL', 
                account_mode = 'COPILOT', 
                quota = '0', 
                data_center = '0', 
                industry = '0', 
                country = '0', 
                state = '0', 
                city = '0', 
                address = '0', 
                zipcode = '0'
            )
        else :
            return XiqAccount(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '0',
                account_type = 'INTERNAL',
                account_mode = 'COPILOT',
                quota = '0',
                data_center = '0',
        )

    def testXiqAccount(self):
        """Test XiqAccount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
