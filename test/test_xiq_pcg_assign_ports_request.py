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
from extremecloudiq.models.xiq_pcg_assign_ports_request import XiqPcgAssignPortsRequest  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqPcgAssignPortsRequest(unittest.TestCase):
    """XiqPcgAssignPortsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqPcgAssignPortsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_pcg_assign_ports_request.XiqPcgAssignPortsRequest()  # noqa: E501
        if include_optional :
            return XiqPcgAssignPortsRequest(
                port_assignments = [
                    extremecloudiq.models.xiq_pcg_port_assignment.XiqPcgPortAssignment(
                        device_id = 56, 
                        eth1_user_id = 56, 
                        eth2_user_id = 56, 
                        eth3_user_id = 56, )
                    ]
            )
        else :
            return XiqPcgAssignPortsRequest(
                port_assignments = [
                    extremecloudiq.models.xiq_pcg_port_assignment.XiqPcgPortAssignment(
                        device_id = 56, 
                        eth1_user_id = 56, 
                        eth2_user_id = 56, 
                        eth3_user_id = 56, )
                    ],
        )

    def testXiqPcgAssignPortsRequest(self):
        """Test XiqPcgAssignPortsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
