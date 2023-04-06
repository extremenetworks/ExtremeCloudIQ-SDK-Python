# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqInternalRadiusServer(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'org_id': 'int',
        'name': 'str',
        'description': 'str',
        'authentication_method_group': 'XiqInternalRadiusServerAuthenticationMethodGroup',
        'default_authentication_method': 'XiqInternalRadiusServerAuthenticationMethod',
        'enable_verify_server_cert': 'bool',
        'server_key_password': 'str',
        'enable_check_cert_common_name': 'bool',
        'enable_check_user_for_tls_auth': 'bool',
        'enable_check_user_for_peap_auth': 'bool',
        'enable_check_user_for_ttls_auth': 'bool',
        'enable_authentication_server': 'bool',
        'enable_radius_accounting_settings': 'bool',
        'authentication_server_port': 'int',
        'active_session_limit': 'int',
        'active_session_age_timeout': 'int',
        'external_user_directory': 'XiqExternalUserDirectory',
        'ca_certificate_id': 'int',
        'server_certificate_id': 'int',
        'server_key_id': 'int',
        'device_ids': 'list[int]',
        'clients': 'list[XiqRadiusClient]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'authentication_method_group': 'authentication_method_group',
        'default_authentication_method': 'default_authentication_method',
        'enable_verify_server_cert': 'enable_verify_server_cert',
        'server_key_password': 'server_key_password',
        'enable_check_cert_common_name': 'enable_check_cert_common_name',
        'enable_check_user_for_tls_auth': 'enable_check_user_for_tls_auth',
        'enable_check_user_for_peap_auth': 'enable_check_user_for_peap_auth',
        'enable_check_user_for_ttls_auth': 'enable_check_user_for_ttls_auth',
        'enable_authentication_server': 'enable_authentication_server',
        'enable_radius_accounting_settings': 'enable_radius_accounting_settings',
        'authentication_server_port': 'authentication_server_port',
        'active_session_limit': 'active_session_limit',
        'active_session_age_timeout': 'active_session_age_timeout',
        'external_user_directory': 'external_user_directory',
        'ca_certificate_id': 'ca_certificate_id',
        'server_certificate_id': 'server_certificate_id',
        'server_key_id': 'server_key_id',
        'device_ids': 'device_ids',
        'clients': 'clients'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, authentication_method_group=None, default_authentication_method=None, enable_verify_server_cert=None, server_key_password=None, enable_check_cert_common_name=None, enable_check_user_for_tls_auth=None, enable_check_user_for_peap_auth=None, enable_check_user_for_ttls_auth=None, enable_authentication_server=None, enable_radius_accounting_settings=None, authentication_server_port=1812, active_session_limit=0, active_session_age_timeout=30, external_user_directory=None, ca_certificate_id=None, server_certificate_id=None, server_key_id=None, device_ids=None, clients=None, local_vars_configuration=None):  # noqa: E501
        """XiqInternalRadiusServer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._authentication_method_group = None
        self._default_authentication_method = None
        self._enable_verify_server_cert = None
        self._server_key_password = None
        self._enable_check_cert_common_name = None
        self._enable_check_user_for_tls_auth = None
        self._enable_check_user_for_peap_auth = None
        self._enable_check_user_for_ttls_auth = None
        self._enable_authentication_server = None
        self._enable_radius_accounting_settings = None
        self._authentication_server_port = None
        self._active_session_limit = None
        self._active_session_age_timeout = None
        self._external_user_directory = None
        self._ca_certificate_id = None
        self._server_certificate_id = None
        self._server_key_id = None
        self._device_ids = None
        self._clients = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.name = name
        if description is not None:
            self.description = description
        self.authentication_method_group = authentication_method_group
        self.default_authentication_method = default_authentication_method
        self.enable_verify_server_cert = enable_verify_server_cert
        if server_key_password is not None:
            self.server_key_password = server_key_password
        self.enable_check_cert_common_name = enable_check_cert_common_name
        self.enable_check_user_for_tls_auth = enable_check_user_for_tls_auth
        if enable_check_user_for_peap_auth is not None:
            self.enable_check_user_for_peap_auth = enable_check_user_for_peap_auth
        if enable_check_user_for_ttls_auth is not None:
            self.enable_check_user_for_ttls_auth = enable_check_user_for_ttls_auth
        self.enable_authentication_server = enable_authentication_server
        self.enable_radius_accounting_settings = enable_radius_accounting_settings
        self.authentication_server_port = authentication_server_port
        if active_session_limit is not None:
            self.active_session_limit = active_session_limit
        if active_session_age_timeout is not None:
            self.active_session_age_timeout = active_session_age_timeout
        self.external_user_directory = external_user_directory
        self.ca_certificate_id = ca_certificate_id
        self.server_certificate_id = server_certificate_id
        self.server_key_id = server_key_id
        self.device_ids = device_ids
        if clients is not None:
            self.clients = clients

    @property
    def id(self):
        """Gets the id of this XiqInternalRadiusServer.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqInternalRadiusServer.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqInternalRadiusServer.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqInternalRadiusServer.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqInternalRadiusServer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqInternalRadiusServer.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqInternalRadiusServer.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqInternalRadiusServer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqInternalRadiusServer.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqInternalRadiusServer.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqInternalRadiusServer.  # noqa: E501

        The internal RADIUS server name  # noqa: E501

        :return: The name of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqInternalRadiusServer.

        The internal RADIUS server name  # noqa: E501

        :param name: The name of this XiqInternalRadiusServer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqInternalRadiusServer.  # noqa: E501

        The internal RADIUS server description  # noqa: E501

        :return: The description of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqInternalRadiusServer.

        The internal RADIUS server description  # noqa: E501

        :param description: The description of this XiqInternalRadiusServer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def authentication_method_group(self):
        """Gets the authentication_method_group of this XiqInternalRadiusServer.  # noqa: E501


        :return: The authentication_method_group of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: XiqInternalRadiusServerAuthenticationMethodGroup
        """
        return self._authentication_method_group

    @authentication_method_group.setter
    def authentication_method_group(self, authentication_method_group):
        """Sets the authentication_method_group of this XiqInternalRadiusServer.


        :param authentication_method_group: The authentication_method_group of this XiqInternalRadiusServer.  # noqa: E501
        :type: XiqInternalRadiusServerAuthenticationMethodGroup
        """
        if self.local_vars_configuration.client_side_validation and authentication_method_group is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_method_group`, must not be `None`")  # noqa: E501

        self._authentication_method_group = authentication_method_group

    @property
    def default_authentication_method(self):
        """Gets the default_authentication_method of this XiqInternalRadiusServer.  # noqa: E501


        :return: The default_authentication_method of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: XiqInternalRadiusServerAuthenticationMethod
        """
        return self._default_authentication_method

    @default_authentication_method.setter
    def default_authentication_method(self, default_authentication_method):
        """Sets the default_authentication_method of this XiqInternalRadiusServer.


        :param default_authentication_method: The default_authentication_method of this XiqInternalRadiusServer.  # noqa: E501
        :type: XiqInternalRadiusServerAuthenticationMethod
        """
        if self.local_vars_configuration.client_side_validation and default_authentication_method is None:  # noqa: E501
            raise ValueError("Invalid value for `default_authentication_method`, must not be `None`")  # noqa: E501

        self._default_authentication_method = default_authentication_method

    @property
    def enable_verify_server_cert(self):
        """Gets the enable_verify_server_cert of this XiqInternalRadiusServer.  # noqa: E501

        Enable verify server cert or not  # noqa: E501

        :return: The enable_verify_server_cert of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_verify_server_cert

    @enable_verify_server_cert.setter
    def enable_verify_server_cert(self, enable_verify_server_cert):
        """Sets the enable_verify_server_cert of this XiqInternalRadiusServer.

        Enable verify server cert or not  # noqa: E501

        :param enable_verify_server_cert: The enable_verify_server_cert of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_verify_server_cert is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_verify_server_cert`, must not be `None`")  # noqa: E501

        self._enable_verify_server_cert = enable_verify_server_cert

    @property
    def server_key_password(self):
        """Gets the server_key_password of this XiqInternalRadiusServer.  # noqa: E501

        password for server key  # noqa: E501

        :return: The server_key_password of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: str
        """
        return self._server_key_password

    @server_key_password.setter
    def server_key_password(self, server_key_password):
        """Sets the server_key_password of this XiqInternalRadiusServer.

        password for server key  # noqa: E501

        :param server_key_password: The server_key_password of this XiqInternalRadiusServer.  # noqa: E501
        :type: str
        """

        self._server_key_password = server_key_password

    @property
    def enable_check_cert_common_name(self):
        """Gets the enable_check_cert_common_name of this XiqInternalRadiusServer.  # noqa: E501

        Enable check cert common name or not  # noqa: E501

        :return: The enable_check_cert_common_name of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_check_cert_common_name

    @enable_check_cert_common_name.setter
    def enable_check_cert_common_name(self, enable_check_cert_common_name):
        """Sets the enable_check_cert_common_name of this XiqInternalRadiusServer.

        Enable check cert common name or not  # noqa: E501

        :param enable_check_cert_common_name: The enable_check_cert_common_name of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_check_cert_common_name is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_check_cert_common_name`, must not be `None`")  # noqa: E501

        self._enable_check_cert_common_name = enable_check_cert_common_name

    @property
    def enable_check_user_for_tls_auth(self):
        """Gets the enable_check_user_for_tls_auth of this XiqInternalRadiusServer.  # noqa: E501

        Enable check user for TLS auth or not  # noqa: E501

        :return: The enable_check_user_for_tls_auth of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_check_user_for_tls_auth

    @enable_check_user_for_tls_auth.setter
    def enable_check_user_for_tls_auth(self, enable_check_user_for_tls_auth):
        """Sets the enable_check_user_for_tls_auth of this XiqInternalRadiusServer.

        Enable check user for TLS auth or not  # noqa: E501

        :param enable_check_user_for_tls_auth: The enable_check_user_for_tls_auth of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_check_user_for_tls_auth is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_check_user_for_tls_auth`, must not be `None`")  # noqa: E501

        self._enable_check_user_for_tls_auth = enable_check_user_for_tls_auth

    @property
    def enable_check_user_for_peap_auth(self):
        """Gets the enable_check_user_for_peap_auth of this XiqInternalRadiusServer.  # noqa: E501

        Enable check user for PEAP auth or not, for Active Directory as the external user directory only  # noqa: E501

        :return: The enable_check_user_for_peap_auth of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_check_user_for_peap_auth

    @enable_check_user_for_peap_auth.setter
    def enable_check_user_for_peap_auth(self, enable_check_user_for_peap_auth):
        """Sets the enable_check_user_for_peap_auth of this XiqInternalRadiusServer.

        Enable check user for PEAP auth or not, for Active Directory as the external user directory only  # noqa: E501

        :param enable_check_user_for_peap_auth: The enable_check_user_for_peap_auth of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """

        self._enable_check_user_for_peap_auth = enable_check_user_for_peap_auth

    @property
    def enable_check_user_for_ttls_auth(self):
        """Gets the enable_check_user_for_ttls_auth of this XiqInternalRadiusServer.  # noqa: E501

        Enable check user for TTLS auth or not, for Active Directory as the external user directory only  # noqa: E501

        :return: The enable_check_user_for_ttls_auth of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_check_user_for_ttls_auth

    @enable_check_user_for_ttls_auth.setter
    def enable_check_user_for_ttls_auth(self, enable_check_user_for_ttls_auth):
        """Sets the enable_check_user_for_ttls_auth of this XiqInternalRadiusServer.

        Enable check user for TTLS auth or not, for Active Directory as the external user directory only  # noqa: E501

        :param enable_check_user_for_ttls_auth: The enable_check_user_for_ttls_auth of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """

        self._enable_check_user_for_ttls_auth = enable_check_user_for_ttls_auth

    @property
    def enable_authentication_server(self):
        """Gets the enable_authentication_server of this XiqInternalRadiusServer.  # noqa: E501

        Enable the RADIUS server as authentication or not  # noqa: E501

        :return: The enable_authentication_server of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_authentication_server

    @enable_authentication_server.setter
    def enable_authentication_server(self, enable_authentication_server):
        """Sets the enable_authentication_server of this XiqInternalRadiusServer.

        Enable the RADIUS server as authentication or not  # noqa: E501

        :param enable_authentication_server: The enable_authentication_server of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_authentication_server is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_authentication_server`, must not be `None`")  # noqa: E501

        self._enable_authentication_server = enable_authentication_server

    @property
    def enable_radius_accounting_settings(self):
        """Gets the enable_radius_accounting_settings of this XiqInternalRadiusServer.  # noqa: E501

        Enable the RADIUS server as accounting or not, must enable authentication server if want to enable accounting settings  # noqa: E501

        :return: The enable_radius_accounting_settings of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_radius_accounting_settings

    @enable_radius_accounting_settings.setter
    def enable_radius_accounting_settings(self, enable_radius_accounting_settings):
        """Sets the enable_radius_accounting_settings of this XiqInternalRadiusServer.

        Enable the RADIUS server as accounting or not, must enable authentication server if want to enable accounting settings  # noqa: E501

        :param enable_radius_accounting_settings: The enable_radius_accounting_settings of this XiqInternalRadiusServer.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_radius_accounting_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_radius_accounting_settings`, must not be `None`")  # noqa: E501

        self._enable_radius_accounting_settings = enable_radius_accounting_settings

    @property
    def authentication_server_port(self):
        """Gets the authentication_server_port of this XiqInternalRadiusServer.  # noqa: E501

        Port for the authentication, must enable authentication. Max:65535, Min:1  # noqa: E501

        :return: The authentication_server_port of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._authentication_server_port

    @authentication_server_port.setter
    def authentication_server_port(self, authentication_server_port):
        """Sets the authentication_server_port of this XiqInternalRadiusServer.

        Port for the authentication, must enable authentication. Max:65535, Min:1  # noqa: E501

        :param authentication_server_port: The authentication_server_port of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and authentication_server_port is None:  # noqa: E501
            raise ValueError("Invalid value for `authentication_server_port`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                authentication_server_port is not None and authentication_server_port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `authentication_server_port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                authentication_server_port is not None and authentication_server_port < 1):  # noqa: E501
            raise ValueError("Invalid value for `authentication_server_port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._authentication_server_port = authentication_server_port

    @property
    def active_session_limit(self):
        """Gets the active_session_limit of this XiqInternalRadiusServer.  # noqa: E501

        Active session limit, must enable accounting setting. Max:15, Min:0  # noqa: E501

        :return: The active_session_limit of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._active_session_limit

    @active_session_limit.setter
    def active_session_limit(self, active_session_limit):
        """Sets the active_session_limit of this XiqInternalRadiusServer.

        Active session limit, must enable accounting setting. Max:15, Min:0  # noqa: E501

        :param active_session_limit: The active_session_limit of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                active_session_limit is not None and active_session_limit > 15):  # noqa: E501
            raise ValueError("Invalid value for `active_session_limit`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                active_session_limit is not None and active_session_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `active_session_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._active_session_limit = active_session_limit

    @property
    def active_session_age_timeout(self):
        """Gets the active_session_age_timeout of this XiqInternalRadiusServer.  # noqa: E501

        Active session age timeout in seconds, must enable accounting setting. Max:300000000, Min:0  # noqa: E501

        :return: The active_session_age_timeout of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._active_session_age_timeout

    @active_session_age_timeout.setter
    def active_session_age_timeout(self, active_session_age_timeout):
        """Sets the active_session_age_timeout of this XiqInternalRadiusServer.

        Active session age timeout in seconds, must enable accounting setting. Max:300000000, Min:0  # noqa: E501

        :param active_session_age_timeout: The active_session_age_timeout of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                active_session_age_timeout is not None and active_session_age_timeout > 300000000):  # noqa: E501
            raise ValueError("Invalid value for `active_session_age_timeout`, must be a value less than or equal to `300000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                active_session_age_timeout is not None and active_session_age_timeout < 30):  # noqa: E501
            raise ValueError("Invalid value for `active_session_age_timeout`, must be a value greater than or equal to `30`")  # noqa: E501

        self._active_session_age_timeout = active_session_age_timeout

    @property
    def external_user_directory(self):
        """Gets the external_user_directory of this XiqInternalRadiusServer.  # noqa: E501


        :return: The external_user_directory of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: XiqExternalUserDirectory
        """
        return self._external_user_directory

    @external_user_directory.setter
    def external_user_directory(self, external_user_directory):
        """Sets the external_user_directory of this XiqInternalRadiusServer.


        :param external_user_directory: The external_user_directory of this XiqInternalRadiusServer.  # noqa: E501
        :type: XiqExternalUserDirectory
        """
        if self.local_vars_configuration.client_side_validation and external_user_directory is None:  # noqa: E501
            raise ValueError("Invalid value for `external_user_directory`, must not be `None`")  # noqa: E501

        self._external_user_directory = external_user_directory

    @property
    def ca_certificate_id(self):
        """Gets the ca_certificate_id of this XiqInternalRadiusServer.  # noqa: E501

        The CA certificate ID  # noqa: E501

        :return: The ca_certificate_id of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._ca_certificate_id

    @ca_certificate_id.setter
    def ca_certificate_id(self, ca_certificate_id):
        """Sets the ca_certificate_id of this XiqInternalRadiusServer.

        The CA certificate ID  # noqa: E501

        :param ca_certificate_id: The ca_certificate_id of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ca_certificate_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ca_certificate_id`, must not be `None`")  # noqa: E501

        self._ca_certificate_id = ca_certificate_id

    @property
    def server_certificate_id(self):
        """Gets the server_certificate_id of this XiqInternalRadiusServer.  # noqa: E501

        The Server certificate ID  # noqa: E501

        :return: The server_certificate_id of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._server_certificate_id

    @server_certificate_id.setter
    def server_certificate_id(self, server_certificate_id):
        """Sets the server_certificate_id of this XiqInternalRadiusServer.

        The Server certificate ID  # noqa: E501

        :param server_certificate_id: The server_certificate_id of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and server_certificate_id is None:  # noqa: E501
            raise ValueError("Invalid value for `server_certificate_id`, must not be `None`")  # noqa: E501

        self._server_certificate_id = server_certificate_id

    @property
    def server_key_id(self):
        """Gets the server_key_id of this XiqInternalRadiusServer.  # noqa: E501

        The Server key ID  # noqa: E501

        :return: The server_key_id of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: int
        """
        return self._server_key_id

    @server_key_id.setter
    def server_key_id(self, server_key_id):
        """Sets the server_key_id of this XiqInternalRadiusServer.

        The Server key ID  # noqa: E501

        :param server_key_id: The server_key_id of this XiqInternalRadiusServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and server_key_id is None:  # noqa: E501
            raise ValueError("Invalid value for `server_key_id`, must not be `None`")  # noqa: E501

        self._server_key_id = server_key_id

    @property
    def device_ids(self):
        """Gets the device_ids of this XiqInternalRadiusServer.  # noqa: E501

        The list of device ID associated with the internal RADIUS server  # noqa: E501

        :return: The device_ids of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this XiqInternalRadiusServer.

        The list of device ID associated with the internal RADIUS server  # noqa: E501

        :param device_ids: The device_ids of this XiqInternalRadiusServer.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and device_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `device_ids`, must not be `None`")  # noqa: E501

        self._device_ids = device_ids

    @property
    def clients(self):
        """Gets the clients of this XiqInternalRadiusServer.  # noqa: E501

        The RADIUS clients of RADIUS proxy  # noqa: E501

        :return: The clients of this XiqInternalRadiusServer.  # noqa: E501
        :rtype: list[XiqRadiusClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this XiqInternalRadiusServer.

        The RADIUS clients of RADIUS proxy  # noqa: E501

        :param clients: The clients of this XiqInternalRadiusServer.  # noqa: E501
        :type: list[XiqRadiusClient]
        """

        self._clients = clients

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, XiqInternalRadiusServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqInternalRadiusServer):
            return True

        return self.to_dict() != other.to_dict()
