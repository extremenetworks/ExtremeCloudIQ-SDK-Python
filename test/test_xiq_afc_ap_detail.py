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
from extremecloudiq.models.xiq_afc_ap_detail import XiqAfcApDetail  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqAfcApDetail(unittest.TestCase):
    """XiqAfcApDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqAfcApDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_afc_ap_detail.XiqAfcApDetail()  # noqa: E501
        if include_optional :
            return XiqAfcApDetail(
                status = 'PENDING', 
                expire = 56, 
                received = 56, 
                reason = '0', 
                spectrum = extremecloudiq.models.xiq_afc_available_spectrum.XiqAfcAvailableSpectrum(
                    request_id = '0', 
                    available_channel_info = [
                        extremecloudiq.models.xiq_available_channel_info.XiqAvailableChannelInfo(
                            global_operating_class = 56, 
                            channel_cfi = [
                                56
                                ], 
                            max_eirp = [
                                1.337
                                ], )
                        ], 
                    availability_expire_time = '0', )
            )
        else :
            return XiqAfcApDetail(
        )

    def testXiqAfcApDetail(self):
        """Test XiqAfcApDetail"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
