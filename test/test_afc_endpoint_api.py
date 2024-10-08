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

import extremecloudiq
from extremecloudiq.api.afc_endpoint_api import AfcEndpointApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestAfcEndpointApi(unittest.TestCase):
    """AfcEndpointApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.afc_endpoint_api.AfcEndpointApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_site_afc_schedule(self):
        """Test case for create_site_afc_schedule

        """
        pass

    def test_get_afc_server(self):
        """Test case for get_afc_server

        Get Afc Server data  # noqa: E501
        """
        pass

    def test_get_afc_spectrum_per_ap(self):
        """Test case for get_afc_spectrum_per_ap

        """
        pass

    def test_get_afc_spectrum_per_site(self):
        """Test case for get_afc_spectrum_per_site

        """
        pass

    def test_get_aps_afc_diagnostics(self):
        """Test case for get_aps_afc_diagnostics

        """
        pass

    def test_get_aps_afc_info(self):
        """Test case for get_aps_afc_info

        Get Afc Summary Data  # noqa: E501
        """
        pass

    def test_get_aps_afc_summary_info(self):
        """Test case for get_aps_afc_summary_info

        """
        pass

    def test_get_site_afc_schedule(self):
        """Test case for get_site_afc_schedule

        """
        pass

    def test_list_afc_servers(self):
        """Test case for list_afc_servers

        Get Afc Server list and their status  # noqa: E501
        """
        pass

    def test_post_aps_manual_afc_spectrum(self):
        """Test case for post_aps_manual_afc_spectrum

        Manual Spectrum request for device(s)  # noqa: E501
        """
        pass

    def test_update_site_afc_schedule(self):
        """Test case for update_site_afc_schedule

        """
        pass


if __name__ == '__main__':
    unittest.main()
