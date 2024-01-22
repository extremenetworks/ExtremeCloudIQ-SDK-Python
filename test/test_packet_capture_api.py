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

import extremecloudiq
from extremecloudiq.api.packet_capture_api import PacketCaptureApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestPacketCaptureApi(unittest.TestCase):
    """PacketCaptureApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.packet_capture_api.PacketCaptureApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_packet_capture(self):
        """Test case for create_packet_capture

        Create a new packet capture session  # noqa: E501
        """
        pass

    def test_delete_packet_capture(self):
        """Test case for delete_packet_capture

        Delete a packet capture session  # noqa: E501
        """
        pass

    def test_get_packet_capture(self):
        """Test case for get_packet_capture

        Get a packet capture session  # noqa: E501
        """
        pass

    def test_get_packet_capture_file(self):
        """Test case for get_packet_capture_file

        Get an AP packet capture file  # noqa: E501
        """
        pass

    def test_list_packet_captures(self):
        """Test case for list_packet_captures

        List packet capture sessions  # noqa: E501
        """
        pass

    def test_stop_packet_capture(self):
        """Test case for stop_packet_capture

        Stop a packet capture session  # noqa: E501
        """
        pass

    def test_upload_packet_capture_files(self):
        """Test case for upload_packet_capture_files

        Upload a packet capture session's capture files  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
