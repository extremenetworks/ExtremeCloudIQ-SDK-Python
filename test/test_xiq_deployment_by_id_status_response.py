# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_deployment_by_id_status_response import XiqDeploymentByIdStatusResponse  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqDeploymentByIdStatusResponse(unittest.TestCase):
    """XiqDeploymentByIdStatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqDeploymentByIdStatusResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_deployment_by_id_status_response.XiqDeploymentByIdStatusResponse()  # noqa: E501
        if include_optional :
            return XiqDeploymentByIdStatusResponse(
                schedule_status = 'SCHEDULED', 
                schedule_time = 56, 
                created_time = 56, 
                updated_time = 56, 
                site_info = [
                    extremecloudiq.models.xiq_site_info.XiqSiteInfo(
                        site_id = 56, 
                        device_ids = [
                            56
                            ], 
                        overview = extremecloudiq.models.xiq_deployment_overview_details.XiqDeploymentOverviewDetails(
                            total_devices = 56, 
                            in_progress_devices = 56, 
                            total_progress = 56, ), )
                    ], 
                deployment_status = {
                    'key' : extremecloudiq.models.xiq_deployment_status.XiqDeploymentStatus(
                        is_finished = True, 
                        current_progress = 56, 
                        current_step_code = '0', 
                        current_step_message = '0', 
                        is_finished_successful = True, 
                        last_deploy_time = 56, 
                        status_message = '0', )
                    }, 
                overview = extremecloudiq.models.xiq_deployment_overview_details.XiqDeploymentOverviewDetails(
                    total_devices = 56, 
                    in_progress_devices = 56, 
                    total_progress = 56, )
            )
        else :
            return XiqDeploymentByIdStatusResponse(
        )

    def testXiqDeploymentByIdStatusResponse(self):
        """Test XiqDeploymentByIdStatusResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
