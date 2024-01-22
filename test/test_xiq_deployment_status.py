# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_deployment_status import XiqDeploymentStatus  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeploymentStatus(unittest.TestCase):
    """XiqDeploymentStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeploymentStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_deployment_status.XiqDeploymentStatus()  # noqa: E501
        if include_optional :
            return XiqDeploymentStatus(
                current_progress = 56, 
                current_step_code = '0', 
                current_step_message = '0', 
                is_finished_successful = True, 
                last_deploy_time = 56, 
                finished = True
            )
        else :
            return XiqDeploymentStatus(
        )

    def testXiqDeploymentStatus(self):
        """Test XiqDeploymentStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
