# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_rp_neighborhood_analysis import XiqRpNeighborhoodAnalysis  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqRpNeighborhoodAnalysis(unittest.TestCase):
    """XiqRpNeighborhoodAnalysis unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqRpNeighborhoodAnalysis
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_rp_neighborhood_analysis.XiqRpNeighborhoodAnalysis()  # noqa: E501
        if include_optional :
            return XiqRpNeighborhoodAnalysis(
                id = 56, 
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                enable_background_scan = True, 
                background_scan_interval = 56, 
                enable_skip_scan_when_clients_connected = True, 
                enable_skip_scan_when_clients_in_power_save_mode = True, 
                enable_skip_scan_when_process_voice_traffic = True
            )
        else :
            return XiqRpNeighborhoodAnalysis(
                id = 56,
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testXiqRpNeighborhoodAnalysis(self):
        """Test XiqRpNeighborhoodAnalysis"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
