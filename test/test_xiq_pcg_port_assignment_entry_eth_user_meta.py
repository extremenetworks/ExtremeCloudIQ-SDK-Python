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
from extremecloudiq.models.xiq_pcg_port_assignment_entry_eth_user_meta import XiqPcgPortAssignmentEntryEthUserMeta  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqPcgPortAssignmentEntryEthUserMeta(unittest.TestCase):
    """XiqPcgPortAssignmentEntryEthUserMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqPcgPortAssignmentEntryEthUserMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_pcg_port_assignment_entry_eth_user_meta.XiqPcgPortAssignmentEntryEthUserMeta()  # noqa: E501
        if include_optional :
            return XiqPcgPortAssignmentEntryEthUserMeta(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                org_id = 56, 
                name = '0', 
                password = '0', 
                user_type = '0', 
                user_group_name = '0', 
                ssids = [
                    '0'
                    ]
            )
        else :
            return XiqPcgPortAssignmentEntryEthUserMeta(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '0',
                password = '0',
                user_type = '0',
                user_group_name = '0',
                ssids = [
                    '0'
                    ],
        )

    def testXiqPcgPortAssignmentEntryEthUserMeta(self):
        """Test XiqPcgPortAssignmentEntryEthUserMeta"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
