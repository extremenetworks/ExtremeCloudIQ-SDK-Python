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


class XiqCheckPermissionResponse(object):
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
        'permissions': 'list[XiqPermission]',
        'roles': 'list[str]'
    }

    attribute_map = {
        'permissions': 'permissions',
        'roles': 'roles'
    }

    def __init__(self, permissions=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """XiqCheckPermissionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._permissions = None
        self._roles = None
        self.discriminator = None

        self.permissions = permissions
        self.roles = roles

    @property
    def permissions(self):
        """Gets the permissions of this XiqCheckPermissionResponse.  # noqa: E501

        The permission list  # noqa: E501

        :return: The permissions of this XiqCheckPermissionResponse.  # noqa: E501
        :rtype: list[XiqPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this XiqCheckPermissionResponse.

        The permission list  # noqa: E501

        :param permissions: The permissions of this XiqCheckPermissionResponse.  # noqa: E501
        :type: list[XiqPermission]
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def roles(self):
        """Gets the roles of this XiqCheckPermissionResponse.  # noqa: E501

        The role list  # noqa: E501

        :return: The roles of this XiqCheckPermissionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this XiqCheckPermissionResponse.

        The role list  # noqa: E501

        :param roles: The roles of this XiqCheckPermissionResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and roles is None:  # noqa: E501
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

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
        if not isinstance(other, XiqCheckPermissionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCheckPermissionResponse):
            return True

        return self.to_dict() != other.to_dict()