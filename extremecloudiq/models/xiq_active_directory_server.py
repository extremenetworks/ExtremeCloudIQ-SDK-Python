# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqActiveDirectoryServer(object):
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
        'base_dn': 'str',
        'enable_tls': 'bool',
        'bind_dn': 'str',
        'bind_dn_password': 'str',
        'domain': 'str',
        'computer_ou': 'str',
        'domain_admin': 'str',
        'domain_admin_password': 'str',
        'enable_save_domain_admin_credentials': 'bool',
        'short_domain': 'str',
        'realm': 'str',
        'base_dn_fetch_mode': 'XiqActiveDirectoryServerBaseDnFetchMode',
        'connection_setup_device_id': 'int',
        'l3_address_profile_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'base_dn': 'base_dn',
        'enable_tls': 'enable_tls',
        'bind_dn': 'bind_dn',
        'bind_dn_password': 'bind_dn_password',
        'domain': 'domain',
        'computer_ou': 'computer_ou',
        'domain_admin': 'domain_admin',
        'domain_admin_password': 'domain_admin_password',
        'enable_save_domain_admin_credentials': 'enable_save_domain_admin_credentials',
        'short_domain': 'short_domain',
        'realm': 'realm',
        'base_dn_fetch_mode': 'base_dn_fetch_mode',
        'connection_setup_device_id': 'connection_setup_device_id',
        'l3_address_profile_id': 'l3_address_profile_id'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, base_dn=None, enable_tls=None, bind_dn=None, bind_dn_password=None, domain=None, computer_ou=None, domain_admin=None, domain_admin_password=None, enable_save_domain_admin_credentials=None, short_domain=None, realm=None, base_dn_fetch_mode=None, connection_setup_device_id=None, l3_address_profile_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqActiveDirectoryServer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._base_dn = None
        self._enable_tls = None
        self._bind_dn = None
        self._bind_dn_password = None
        self._domain = None
        self._computer_ou = None
        self._domain_admin = None
        self._domain_admin_password = None
        self._enable_save_domain_admin_credentials = None
        self._short_domain = None
        self._realm = None
        self._base_dn_fetch_mode = None
        self._connection_setup_device_id = None
        self._l3_address_profile_id = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if base_dn is not None:
            self.base_dn = base_dn
        if enable_tls is not None:
            self.enable_tls = enable_tls
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_dn_password is not None:
            self.bind_dn_password = bind_dn_password
        if domain is not None:
            self.domain = domain
        if computer_ou is not None:
            self.computer_ou = computer_ou
        if domain_admin is not None:
            self.domain_admin = domain_admin
        if domain_admin_password is not None:
            self.domain_admin_password = domain_admin_password
        if enable_save_domain_admin_credentials is not None:
            self.enable_save_domain_admin_credentials = enable_save_domain_admin_credentials
        if short_domain is not None:
            self.short_domain = short_domain
        if realm is not None:
            self.realm = realm
        if base_dn_fetch_mode is not None:
            self.base_dn_fetch_mode = base_dn_fetch_mode
        if connection_setup_device_id is not None:
            self.connection_setup_device_id = connection_setup_device_id
        if l3_address_profile_id is not None:
            self.l3_address_profile_id = l3_address_profile_id

    @property
    def id(self):
        """Gets the id of this XiqActiveDirectoryServer.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqActiveDirectoryServer.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqActiveDirectoryServer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqActiveDirectoryServer.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqActiveDirectoryServer.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqActiveDirectoryServer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqActiveDirectoryServer.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqActiveDirectoryServer.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqActiveDirectoryServer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqActiveDirectoryServer.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqActiveDirectoryServer.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqActiveDirectoryServer.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqActiveDirectoryServer.  # noqa: E501

        The active directory server name  # noqa: E501

        :return: The name of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqActiveDirectoryServer.

        The active directory server name  # noqa: E501

        :param name: The name of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqActiveDirectoryServer.  # noqa: E501

        The description for active directory server  # noqa: E501

        :return: The description of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqActiveDirectoryServer.

        The description for active directory server  # noqa: E501

        :param description: The description of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def base_dn(self):
        """Gets the base_dn of this XiqActiveDirectoryServer.  # noqa: E501

        The base DN of active directory server  # noqa: E501

        :return: The base_dn of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this XiqActiveDirectoryServer.

        The base DN of active directory server  # noqa: E501

        :param base_dn: The base_dn of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def enable_tls(self):
        """Gets the enable_tls of this XiqActiveDirectoryServer.  # noqa: E501

        Flag to enable TLS  # noqa: E501

        :return: The enable_tls of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_tls

    @enable_tls.setter
    def enable_tls(self, enable_tls):
        """Sets the enable_tls of this XiqActiveDirectoryServer.

        Flag to enable TLS  # noqa: E501

        :param enable_tls: The enable_tls of this XiqActiveDirectoryServer.  # noqa: E501
        :type: bool
        """

        self._enable_tls = enable_tls

    @property
    def bind_dn(self):
        """Gets the bind_dn of this XiqActiveDirectoryServer.  # noqa: E501

        The bind DN of active directory server  # noqa: E501

        :return: The bind_dn of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this XiqActiveDirectoryServer.

        The bind DN of active directory server  # noqa: E501

        :param bind_dn: The bind_dn of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_dn_password(self):
        """Gets the bind_dn_password of this XiqActiveDirectoryServer.  # noqa: E501

        The bind DN password of active directory server  # noqa: E501

        :return: The bind_dn_password of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn_password

    @bind_dn_password.setter
    def bind_dn_password(self, bind_dn_password):
        """Sets the bind_dn_password of this XiqActiveDirectoryServer.

        The bind DN password of active directory server  # noqa: E501

        :param bind_dn_password: The bind_dn_password of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._bind_dn_password = bind_dn_password

    @property
    def domain(self):
        """Gets the domain of this XiqActiveDirectoryServer.  # noqa: E501

        The domain of active directory server  # noqa: E501

        :return: The domain of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this XiqActiveDirectoryServer.

        The domain of active directory server  # noqa: E501

        :param domain: The domain of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def computer_ou(self):
        """Gets the computer_ou of this XiqActiveDirectoryServer.  # noqa: E501

        The compute OU of active directory server  # noqa: E501

        :return: The computer_ou of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._computer_ou

    @computer_ou.setter
    def computer_ou(self, computer_ou):
        """Sets the computer_ou of this XiqActiveDirectoryServer.

        The compute OU of active directory server  # noqa: E501

        :param computer_ou: The computer_ou of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._computer_ou = computer_ou

    @property
    def domain_admin(self):
        """Gets the domain_admin of this XiqActiveDirectoryServer.  # noqa: E501

        The domain admin of active directory server  # noqa: E501

        :return: The domain_admin of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._domain_admin

    @domain_admin.setter
    def domain_admin(self, domain_admin):
        """Sets the domain_admin of this XiqActiveDirectoryServer.

        The domain admin of active directory server  # noqa: E501

        :param domain_admin: The domain_admin of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._domain_admin = domain_admin

    @property
    def domain_admin_password(self):
        """Gets the domain_admin_password of this XiqActiveDirectoryServer.  # noqa: E501

        The domain admin password of active directory server  # noqa: E501

        :return: The domain_admin_password of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._domain_admin_password

    @domain_admin_password.setter
    def domain_admin_password(self, domain_admin_password):
        """Sets the domain_admin_password of this XiqActiveDirectoryServer.

        The domain admin password of active directory server  # noqa: E501

        :param domain_admin_password: The domain_admin_password of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._domain_admin_password = domain_admin_password

    @property
    def enable_save_domain_admin_credentials(self):
        """Gets the enable_save_domain_admin_credentials of this XiqActiveDirectoryServer.  # noqa: E501

        Flag to enable save domain admin credentials  # noqa: E501

        :return: The enable_save_domain_admin_credentials of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: bool
        """
        return self._enable_save_domain_admin_credentials

    @enable_save_domain_admin_credentials.setter
    def enable_save_domain_admin_credentials(self, enable_save_domain_admin_credentials):
        """Sets the enable_save_domain_admin_credentials of this XiqActiveDirectoryServer.

        Flag to enable save domain admin credentials  # noqa: E501

        :param enable_save_domain_admin_credentials: The enable_save_domain_admin_credentials of this XiqActiveDirectoryServer.  # noqa: E501
        :type: bool
        """

        self._enable_save_domain_admin_credentials = enable_save_domain_admin_credentials

    @property
    def short_domain(self):
        """Gets the short_domain of this XiqActiveDirectoryServer.  # noqa: E501

        The short domain of active directory server  # noqa: E501

        :return: The short_domain of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._short_domain

    @short_domain.setter
    def short_domain(self, short_domain):
        """Sets the short_domain of this XiqActiveDirectoryServer.

        The short domain of active directory server  # noqa: E501

        :param short_domain: The short_domain of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._short_domain = short_domain

    @property
    def realm(self):
        """Gets the realm of this XiqActiveDirectoryServer.  # noqa: E501

        The realm of active directory server  # noqa: E501

        :return: The realm of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this XiqActiveDirectoryServer.

        The realm of active directory server  # noqa: E501

        :param realm: The realm of this XiqActiveDirectoryServer.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def base_dn_fetch_mode(self):
        """Gets the base_dn_fetch_mode of this XiqActiveDirectoryServer.  # noqa: E501


        :return: The base_dn_fetch_mode of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: XiqActiveDirectoryServerBaseDnFetchMode
        """
        return self._base_dn_fetch_mode

    @base_dn_fetch_mode.setter
    def base_dn_fetch_mode(self, base_dn_fetch_mode):
        """Sets the base_dn_fetch_mode of this XiqActiveDirectoryServer.


        :param base_dn_fetch_mode: The base_dn_fetch_mode of this XiqActiveDirectoryServer.  # noqa: E501
        :type: XiqActiveDirectoryServerBaseDnFetchMode
        """

        self._base_dn_fetch_mode = base_dn_fetch_mode

    @property
    def connection_setup_device_id(self):
        """Gets the connection_setup_device_id of this XiqActiveDirectoryServer.  # noqa: E501

        The connection setup device ID for active directory server  # noqa: E501

        :return: The connection_setup_device_id of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: int
        """
        return self._connection_setup_device_id

    @connection_setup_device_id.setter
    def connection_setup_device_id(self, connection_setup_device_id):
        """Sets the connection_setup_device_id of this XiqActiveDirectoryServer.

        The connection setup device ID for active directory server  # noqa: E501

        :param connection_setup_device_id: The connection_setup_device_id of this XiqActiveDirectoryServer.  # noqa: E501
        :type: int
        """

        self._connection_setup_device_id = connection_setup_device_id

    @property
    def l3_address_profile_id(self):
        """Gets the l3_address_profile_id of this XiqActiveDirectoryServer.  # noqa: E501

        The associate L3 address profile ID for active directory server  # noqa: E501

        :return: The l3_address_profile_id of this XiqActiveDirectoryServer.  # noqa: E501
        :rtype: int
        """
        return self._l3_address_profile_id

    @l3_address_profile_id.setter
    def l3_address_profile_id(self, l3_address_profile_id):
        """Sets the l3_address_profile_id of this XiqActiveDirectoryServer.

        The associate L3 address profile ID for active directory server  # noqa: E501

        :param l3_address_profile_id: The l3_address_profile_id of this XiqActiveDirectoryServer.  # noqa: E501
        :type: int
        """

        self._l3_address_profile_id = l3_address_profile_id

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
        if not isinstance(other, XiqActiveDirectoryServer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqActiveDirectoryServer):
            return True

        return self.to_dict() != other.to_dict()
