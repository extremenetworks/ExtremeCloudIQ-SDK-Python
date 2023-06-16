# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqExternalUserDirectoryEntry(object):
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
        'default_server_id': 'int',
        'server_role': 'XiqServerRole'
    }

    attribute_map = {
        'default_server_id': 'default_server_id',
        'server_role': 'server_role'
    }

    def __init__(self, default_server_id=None, server_role=None, local_vars_configuration=None):  # noqa: E501
        """XiqExternalUserDirectoryEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_server_id = None
        self._server_role = None
        self.discriminator = None

        self.default_server_id = default_server_id
        self.server_role = server_role

    @property
    def default_server_id(self):
        """Gets the default_server_id of this XiqExternalUserDirectoryEntry.  # noqa: E501

        The default external user directory server id, could be active directory server id(get the id list from endpoint: '/ad-servers') or LDAP server id(get the id list from endpoint: '/ldap-servers') depends on the 'external_user_directory_type'   # noqa: E501

        :return: The default_server_id of this XiqExternalUserDirectoryEntry.  # noqa: E501
        :rtype: int
        """
        return self._default_server_id

    @default_server_id.setter
    def default_server_id(self, default_server_id):
        """Sets the default_server_id of this XiqExternalUserDirectoryEntry.

        The default external user directory server id, could be active directory server id(get the id list from endpoint: '/ad-servers') or LDAP server id(get the id list from endpoint: '/ldap-servers') depends on the 'external_user_directory_type'   # noqa: E501

        :param default_server_id: The default_server_id of this XiqExternalUserDirectoryEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and default_server_id is None:  # noqa: E501
            raise ValueError("Invalid value for `default_server_id`, must not be `None`")  # noqa: E501

        self._default_server_id = default_server_id

    @property
    def server_role(self):
        """Gets the server_role of this XiqExternalUserDirectoryEntry.  # noqa: E501


        :return: The server_role of this XiqExternalUserDirectoryEntry.  # noqa: E501
        :rtype: XiqServerRole
        """
        return self._server_role

    @server_role.setter
    def server_role(self, server_role):
        """Sets the server_role of this XiqExternalUserDirectoryEntry.


        :param server_role: The server_role of this XiqExternalUserDirectoryEntry.  # noqa: E501
        :type: XiqServerRole
        """
        if self.local_vars_configuration.client_side_validation and server_role is None:  # noqa: E501
            raise ValueError("Invalid value for `server_role`, must not be `None`")  # noqa: E501

        self._server_role = server_role

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
        if not isinstance(other, XiqExternalUserDirectoryEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExternalUserDirectoryEntry):
            return True

        return self.to_dict() != other.to_dict()
