# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.hiq_api import HIQApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestHIQApi(unittest.TestCase):
    """HIQApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.hiq_api.HIQApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_organization(self):
        """Test case for create_organization

        Create a new organization  # noqa: E501
        """
        pass

    def test_delete_organization(self):
        """Test case for delete_organization

        Delete an existing organization  # noqa: E501
        """
        pass

    def test_get_creating_org_id(self):
        """Test case for get_creating_org_id

        Get organization for creating new data  # noqa: E501
        """
        pass

    def test_get_hiq_context(self):
        """Test case for get_hiq_context

        Get HIQ context  # noqa: E501
        """
        pass

    def test_get_hiq_status(self):
        """Test case for get_hiq_status

        Get HIQ status  # noqa: E501
        """
        pass

    def test_get_reading_org_ids(self):
        """Test case for get_reading_org_ids

        Get organizations for reading data  # noqa: E501
        """
        pass

    def test_list_organizations(self):
        """Test case for list_organizations

        List all organizations  # noqa: E501
        """
        pass

    def test_rename_organization(self):
        """Test case for rename_organization

        Rename an existing organization  # noqa: E501
        """
        pass

    def test_set_creating_org_id(self):
        """Test case for set_creating_org_id

        Set organization for creating new data  # noqa: E501
        """
        pass

    def test_set_hiq_context(self):
        """Test case for set_hiq_context

        Set HIQ context  # noqa: E501
        """
        pass

    def test_set_reading_org_ids(self):
        """Test case for set_reading_org_ids

        Set organizations for reading data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
