# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_pcg_assign_ports_response import XiqPcgAssignPortsResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqPcgAssignPortsResponse(unittest.TestCase):
    """XiqPcgAssignPortsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqPcgAssignPortsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_pcg_assign_ports_response.XiqPcgAssignPortsResponse()  # noqa: E501
        if include_optional :
            return XiqPcgAssignPortsResponse(
                policy_id = 56, 
                policy_name = '0', 
                pcg_port_assignment_entries = [
                    extremecloudiq.models.xiq_pcg_port_assignment_entry.XiqPcgPortAssignmentEntry(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        device_id = 56, 
                        eth1_user_id = 56, 
                        eth2_user_id = 56, 
                        eth3_user_id = 56, )
                    ]
            )
        else :
            return XiqPcgAssignPortsResponse(
                policy_id = 56,
                policy_name = '0',
                pcg_port_assignment_entries = [
                    extremecloudiq.models.xiq_pcg_port_assignment_entry.XiqPcgPortAssignmentEntry(
                        id = 56, 
                        create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        org_id = 56, 
                        device_id = 56, 
                        eth1_user_id = 56, 
                        eth2_user_id = 56, 
                        eth3_user_id = 56, )
                    ],
        )

    def testXiqPcgAssignPortsResponse(self):
        """Test XiqPcgAssignPortsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()