# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_key_based_pcg import XiqKeyBasedPcg  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqKeyBasedPcg(unittest.TestCase):
    """XiqKeyBasedPcg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqKeyBasedPcg
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_key_based_pcg.XiqKeyBasedPcg()  # noqa: E501
        if include_optional :
            return XiqKeyBasedPcg(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                policy_id = 56, 
                policy_name = '0', 
                ssid_name = '0', 
                enabled = True, 
                users = [
                    extremecloudiq.models.xiq_key_based_pcg_user.XiqKeyBasedPcgUser(
                        name = '0', 
                        email = '0', 
                        user_group_name = '0', 
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, )
                    ]
            )
        else :
            return XiqKeyBasedPcg(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                policy_id = 56,
                policy_name = '0',
                ssid_name = '0',
                enabled = True,
        )

    def testXiqKeyBasedPcg(self):
        """Test XiqKeyBasedPcg"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
