# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqExternalUserDirectory(object):
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
        'ldap_retry_interval': 'int',
        'local_check_interval': 'int',
        'remote_check_interval': 'int',
        'enable_radius_server_credential_caching': 'bool',
        'cache_lifetime': 'int',
        'user_group_attribute': 'str',
        'external_user_directory_type': 'XiqExternalUserDirectoryType',
        'entries': 'list[XiqExternalUserDirectoryEntry]'
    }

    attribute_map = {
        'ldap_retry_interval': 'ldap_retry_interval',
        'local_check_interval': 'local_check_interval',
        'remote_check_interval': 'remote_check_interval',
        'enable_radius_server_credential_caching': 'enable_radius_server_credential_caching',
        'cache_lifetime': 'cache_lifetime',
        'user_group_attribute': 'user_group_attribute',
        'external_user_directory_type': 'external_user_directory_type',
        'entries': 'entries'
    }

    def __init__(self, ldap_retry_interval=600, local_check_interval=300, remote_check_interval=30, enable_radius_server_credential_caching=None, cache_lifetime=86400, user_group_attribute='memberOf', external_user_directory_type=None, entries=None, local_vars_configuration=None):  # noqa: E501
        """XiqExternalUserDirectory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ldap_retry_interval = None
        self._local_check_interval = None
        self._remote_check_interval = None
        self._enable_radius_server_credential_caching = None
        self._cache_lifetime = None
        self._user_group_attribute = None
        self._external_user_directory_type = None
        self._entries = None
        self.discriminator = None

        self.ldap_retry_interval = ldap_retry_interval
        self.local_check_interval = local_check_interval
        self.remote_check_interval = remote_check_interval
        self.enable_radius_server_credential_caching = enable_radius_server_credential_caching
        self.cache_lifetime = cache_lifetime
        self.user_group_attribute = user_group_attribute
        self.external_user_directory_type = external_user_directory_type
        self.entries = entries

    @property
    def ldap_retry_interval(self):
        """Gets the ldap_retry_interval of this XiqExternalUserDirectory.  # noqa: E501

        Retry the previously unresponsive primary server after the specified seconds  # noqa: E501

        :return: The ldap_retry_interval of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: int
        """
        return self._ldap_retry_interval

    @ldap_retry_interval.setter
    def ldap_retry_interval(self, ldap_retry_interval):
        """Sets the ldap_retry_interval of this XiqExternalUserDirectory.

        Retry the previously unresponsive primary server after the specified seconds  # noqa: E501

        :param ldap_retry_interval: The ldap_retry_interval of this XiqExternalUserDirectory.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ldap_retry_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `ldap_retry_interval`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ldap_retry_interval is not None and ldap_retry_interval > 200000000):  # noqa: E501
            raise ValueError("Invalid value for `ldap_retry_interval`, must be a value less than or equal to `200000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ldap_retry_interval is not None and ldap_retry_interval < 60):  # noqa: E501
            raise ValueError("Invalid value for `ldap_retry_interval`, must be a value greater than or equal to `60`")  # noqa: E501

        self._ldap_retry_interval = ldap_retry_interval

    @property
    def local_check_interval(self):
        """Gets the local_check_interval of this XiqExternalUserDirectory.  # noqa: E501

        Time to user local cache if none of the external servers are reachable in seconds  # noqa: E501

        :return: The local_check_interval of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: int
        """
        return self._local_check_interval

    @local_check_interval.setter
    def local_check_interval(self, local_check_interval):
        """Sets the local_check_interval of this XiqExternalUserDirectory.

        Time to user local cache if none of the external servers are reachable in seconds  # noqa: E501

        :param local_check_interval: The local_check_interval of this XiqExternalUserDirectory.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and local_check_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `local_check_interval`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                local_check_interval is not None and local_check_interval > 3600):  # noqa: E501
            raise ValueError("Invalid value for `local_check_interval`, must be a value less than or equal to `3600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                local_check_interval is not None and local_check_interval < 30):  # noqa: E501
            raise ValueError("Invalid value for `local_check_interval`, must be a value greater than or equal to `30`")  # noqa: E501

        self._local_check_interval = local_check_interval

    @property
    def remote_check_interval(self):
        """Gets the remote_check_interval of this XiqExternalUserDirectory.  # noqa: E501

        Try the next backup server after specified seconds  # noqa: E501

        :return: The remote_check_interval of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: int
        """
        return self._remote_check_interval

    @remote_check_interval.setter
    def remote_check_interval(self, remote_check_interval):
        """Sets the remote_check_interval of this XiqExternalUserDirectory.

        Try the next backup server after specified seconds  # noqa: E501

        :param remote_check_interval: The remote_check_interval of this XiqExternalUserDirectory.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and remote_check_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `remote_check_interval`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                remote_check_interval is not None and remote_check_interval > 3600):  # noqa: E501
            raise ValueError("Invalid value for `remote_check_interval`, must be a value less than or equal to `3600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                remote_check_interval is not None and remote_check_interval < 10):  # noqa: E501
            raise ValueError("Invalid value for `remote_check_interval`, must be a value greater than or equal to `10`")  # noqa: E501

        self._remote_check_interval = remote_check_interval

    @property
    def enable_radius_server_credential_caching(self):
        """Gets the enable_radius_server_credential_caching of this XiqExternalUserDirectory.  # noqa: E501

        Caching credentials allows for better performance and higher availability by reducing the dependence on RADIUS servers across high-latency WAN links.  # noqa: E501

        :return: The enable_radius_server_credential_caching of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: bool
        """
        return self._enable_radius_server_credential_caching

    @enable_radius_server_credential_caching.setter
    def enable_radius_server_credential_caching(self, enable_radius_server_credential_caching):
        """Sets the enable_radius_server_credential_caching of this XiqExternalUserDirectory.

        Caching credentials allows for better performance and higher availability by reducing the dependence on RADIUS servers across high-latency WAN links.  # noqa: E501

        :param enable_radius_server_credential_caching: The enable_radius_server_credential_caching of this XiqExternalUserDirectory.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_radius_server_credential_caching is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_radius_server_credential_caching`, must not be `None`")  # noqa: E501

        self._enable_radius_server_credential_caching = enable_radius_server_credential_caching

    @property
    def cache_lifetime(self):
        """Gets the cache_lifetime of this XiqExternalUserDirectory.  # noqa: E501

        Retain Cache for  # noqa: E501

        :return: The cache_lifetime of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: int
        """
        return self._cache_lifetime

    @cache_lifetime.setter
    def cache_lifetime(self, cache_lifetime):
        """Sets the cache_lifetime of this XiqExternalUserDirectory.

        Retain Cache for  # noqa: E501

        :param cache_lifetime: The cache_lifetime of this XiqExternalUserDirectory.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cache_lifetime is None:  # noqa: E501
            raise ValueError("Invalid value for `cache_lifetime`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cache_lifetime is not None and cache_lifetime > 2592000):  # noqa: E501
            raise ValueError("Invalid value for `cache_lifetime`, must be a value less than or equal to `2592000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cache_lifetime is not None and cache_lifetime < 3600):  # noqa: E501
            raise ValueError("Invalid value for `cache_lifetime`, must be a value greater than or equal to `3600`")  # noqa: E501

        self._cache_lifetime = cache_lifetime

    @property
    def user_group_attribute(self):
        """Gets the user_group_attribute of this XiqExternalUserDirectory.  # noqa: E501

        The user group attribute, use string such as: 'memberOf'  # noqa: E501

        :return: The user_group_attribute of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: str
        """
        return self._user_group_attribute

    @user_group_attribute.setter
    def user_group_attribute(self, user_group_attribute):
        """Sets the user_group_attribute of this XiqExternalUserDirectory.

        The user group attribute, use string such as: 'memberOf'  # noqa: E501

        :param user_group_attribute: The user_group_attribute of this XiqExternalUserDirectory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_group_attribute is None:  # noqa: E501
            raise ValueError("Invalid value for `user_group_attribute`, must not be `None`")  # noqa: E501

        self._user_group_attribute = user_group_attribute

    @property
    def external_user_directory_type(self):
        """Gets the external_user_directory_type of this XiqExternalUserDirectory.  # noqa: E501


        :return: The external_user_directory_type of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: XiqExternalUserDirectoryType
        """
        return self._external_user_directory_type

    @external_user_directory_type.setter
    def external_user_directory_type(self, external_user_directory_type):
        """Sets the external_user_directory_type of this XiqExternalUserDirectory.


        :param external_user_directory_type: The external_user_directory_type of this XiqExternalUserDirectory.  # noqa: E501
        :type: XiqExternalUserDirectoryType
        """
        if self.local_vars_configuration.client_side_validation and external_user_directory_type is None:  # noqa: E501
            raise ValueError("Invalid value for `external_user_directory_type`, must not be `None`")  # noqa: E501

        self._external_user_directory_type = external_user_directory_type

    @property
    def entries(self):
        """Gets the entries of this XiqExternalUserDirectory.  # noqa: E501

        The external user directory server entries  # noqa: E501

        :return: The entries of this XiqExternalUserDirectory.  # noqa: E501
        :rtype: list[XiqExternalUserDirectoryEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this XiqExternalUserDirectory.

        The external user directory server entries  # noqa: E501

        :param entries: The entries of this XiqExternalUserDirectory.  # noqa: E501
        :type: list[XiqExternalUserDirectoryEntry]
        """
        if self.local_vars_configuration.client_side_validation and entries is None:  # noqa: E501
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

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
        if not isinstance(other, XiqExternalUserDirectory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExternalUserDirectory):
            return True

        return self.to_dict() != other.to_dict()
