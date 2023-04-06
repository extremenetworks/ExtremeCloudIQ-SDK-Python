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

import extremecloudiq
from extremecloudiq.api.location_api import LocationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestLocationApi(unittest.TestCase):
    """LocationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.location_api.LocationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_building(self):
        """Test case for create_building

        Create building  # noqa: E501
        """
        pass

    def test_create_floor(self):
        """Test case for create_floor

        Create floor  # noqa: E501
        """
        pass

    def test_create_location(self):
        """Test case for create_location

        Create location  # noqa: E501
        """
        pass

    def test_delete_building(self):
        """Test case for delete_building

        Delete building by ID  # noqa: E501
        """
        pass

    def test_delete_floor(self):
        """Test case for delete_floor

        Delete floor by ID  # noqa: E501
        """
        pass

    def test_delete_location(self):
        """Test case for delete_location

        Delete location by ID  # noqa: E501
        """
        pass

    def test_get_location_tree(self):
        """Test case for get_location_tree

        Get location tree  # noqa: E501
        """
        pass

    def test_initialize_location(self):
        """Test case for initialize_location

        Initialize organization location  # noqa: E501
        """
        pass

    def test_update_building(self):
        """Test case for update_building

        Update building  # noqa: E501
        """
        pass

    def test_update_floor(self):
        """Test case for update_floor

        Update floor  # noqa: E501
        """
        pass

    def test_update_location(self):
        """Test case for update_location

        Update location  # noqa: E501
        """
        pass

    def test_upload_floorplan(self):
        """Test case for upload_floorplan

        Upload floorplan  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()