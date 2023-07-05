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
from extremecloudiq.api.configuration___authentication_api import ConfigurationAuthenticationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestConfigurationAuthenticationApi(unittest.TestCase):
    """ConfigurationAuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.configuration___authentication_api.ConfigurationAuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_external_radius_server(self):
        """Test case for create_external_radius_server

        Create external RADIUS server configuration  # noqa: E501
        """
        pass

    def test_create_internal_radius_server(self):
        """Test case for create_internal_radius_server

        Create internal RADIUS server configuration  # noqa: E501
        """
        pass

    def test_create_ldap_server(self):
        """Test case for create_ldap_server

        Create LDAP server  # noqa: E501
        """
        pass

    def test_create_radius_client_object(self):
        """Test case for create_radius_client_object

        Create RADIUS client object configuration  # noqa: E501
        """
        pass

    def test_create_radius_proxy(self):
        """Test case for create_radius_proxy

        Create RADIUS proxy configuration  # noqa: E501
        """
        pass

    def test_delete_bulk_internal_radius_server(self):
        """Test case for delete_bulk_internal_radius_server

        [LRO] Delete internal RADIUS server configuration  # noqa: E501
        """
        pass

    def test_delete_external_radius_server(self):
        """Test case for delete_external_radius_server

        Delete external RADIUS server configuration  # noqa: E501
        """
        pass

    def test_delete_internal_radius_server(self):
        """Test case for delete_internal_radius_server

        Delete internal RADIUS server configuration  # noqa: E501
        """
        pass

    def test_delete_ldap_server(self):
        """Test case for delete_ldap_server

        Delete a LDAP server  # noqa: E501
        """
        pass

    def test_delete_radius_client_object(self):
        """Test case for delete_radius_client_object

        Delete a RADIUS client object configuration  # noqa: E501
        """
        pass

    def test_delete_radius_proxy(self):
        """Test case for delete_radius_proxy

        Delete the RADIUS proxy configuration  # noqa: E501
        """
        pass

    def test_get_external_radius_server(self):
        """Test case for get_external_radius_server

        Get external RADIUS server by ID  # noqa: E501
        """
        pass

    def test_get_internal_radius_server(self):
        """Test case for get_internal_radius_server

        Get internal RADIUS server by ID  # noqa: E501
        """
        pass

    def test_get_ldap_server(self):
        """Test case for get_ldap_server

        Get LDAP server by ID  # noqa: E501
        """
        pass

    def test_get_radius_client_object(self):
        """Test case for get_radius_client_object

        Get RADIUS client object by ID  # noqa: E501
        """
        pass

    def test_get_radius_proxy(self):
        """Test case for get_radius_proxy

        Get the RADIUS proxy configuration  # noqa: E501
        """
        pass

    def test_list_active_directory_servers(self):
        """Test case for list_active_directory_servers

        List active directory servers  # noqa: E501
        """
        pass

    def test_list_captive_web_portals(self):
        """Test case for list_captive_web_portals

        List captive web portals  # noqa: E501
        """
        pass

    def test_list_external_radius_servers(self):
        """Test case for list_external_radius_servers

        List external RADIUS servers  # noqa: E501
        """
        pass

    def test_list_internal_radius_devices(self):
        """Test case for list_internal_radius_devices

        List all internal RADIUS devices  # noqa: E501
        """
        pass

    def test_list_internal_radius_servers(self):
        """Test case for list_internal_radius_servers

        List all internal RADIUS servers  # noqa: E501
        """
        pass

    def test_list_ldap_servers(self):
        """Test case for list_ldap_servers

        List LDAP servers  # noqa: E501
        """
        pass

    def test_list_radius_client_objects(self):
        """Test case for list_radius_client_objects

        List RADIUS client objects  # noqa: E501
        """
        pass

    def test_list_radius_proxies(self):
        """Test case for list_radius_proxies

        List RADIUS proxies  # noqa: E501
        """
        pass

    def test_list_radius_proxy_devices(self):
        """Test case for list_radius_proxy_devices

        List Radius proxy devices  # noqa: E501
        """
        pass

    def test_update_external_radius_server(self):
        """Test case for update_external_radius_server

        Update external RADIUS server configuration  # noqa: E501
        """
        pass

    def test_update_internal_radius_server(self):
        """Test case for update_internal_radius_server

        Update internal RADIUS server configuration  # noqa: E501
        """
        pass

    def test_update_ldap_server(self):
        """Test case for update_ldap_server

        Update LDAP server configuration  # noqa: E501
        """
        pass

    def test_update_radius_client_object(self):
        """Test case for update_radius_client_object

        Update RADIUS client object configuration  # noqa: E501
        """
        pass

    def test_update_radius_proxy(self):
        """Test case for update_radius_proxy

        Update RADIUS proxy configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
