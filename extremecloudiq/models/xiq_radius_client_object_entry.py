# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqRadiusClientObjectEntry(object):
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
        'server_role': 'XiqServerRole',
        'server_type': 'XiqRadiusClientObjectType',
        'radius_server_id': 'int'
    }

    attribute_map = {
        'server_role': 'server_role',
        'server_type': 'server_type',
        'radius_server_id': 'radius_server_id'
    }

    def __init__(self, server_role=None, server_type=None, radius_server_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqRadiusClientObjectEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._server_role = None
        self._server_type = None
        self._radius_server_id = None
        self.discriminator = None

        self.server_role = server_role
        self.server_type = server_type
        self.radius_server_id = radius_server_id

    @property
    def server_role(self):
        """Gets the server_role of this XiqRadiusClientObjectEntry.  # noqa: E501


        :return: The server_role of this XiqRadiusClientObjectEntry.  # noqa: E501
        :rtype: XiqServerRole
        """
        return self._server_role

    @server_role.setter
    def server_role(self, server_role):
        """Sets the server_role of this XiqRadiusClientObjectEntry.


        :param server_role: The server_role of this XiqRadiusClientObjectEntry.  # noqa: E501
        :type: XiqServerRole
        """
        if self.local_vars_configuration.client_side_validation and server_role is None:  # noqa: E501
            raise ValueError("Invalid value for `server_role`, must not be `None`")  # noqa: E501

        self._server_role = server_role

    @property
    def server_type(self):
        """Gets the server_type of this XiqRadiusClientObjectEntry.  # noqa: E501


        :return: The server_type of this XiqRadiusClientObjectEntry.  # noqa: E501
        :rtype: XiqRadiusClientObjectType
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this XiqRadiusClientObjectEntry.


        :param server_type: The server_type of this XiqRadiusClientObjectEntry.  # noqa: E501
        :type: XiqRadiusClientObjectType
        """
        if self.local_vars_configuration.client_side_validation and server_type is None:  # noqa: E501
            raise ValueError("Invalid value for `server_type`, must not be `None`")  # noqa: E501

        self._server_type = server_type

    @property
    def radius_server_id(self):
        """Gets the radius_server_id of this XiqRadiusClientObjectEntry.  # noqa: E501

        The ID of the RADIUS server object, for EXTERNAL_RADIUS_SERVER please use the ID of external RADIUS server object. For INTERNAL_RADIUS_SERVER, please use the RADIUS device ID  # noqa: E501

        :return: The radius_server_id of this XiqRadiusClientObjectEntry.  # noqa: E501
        :rtype: int
        """
        return self._radius_server_id

    @radius_server_id.setter
    def radius_server_id(self, radius_server_id):
        """Sets the radius_server_id of this XiqRadiusClientObjectEntry.

        The ID of the RADIUS server object, for EXTERNAL_RADIUS_SERVER please use the ID of external RADIUS server object. For INTERNAL_RADIUS_SERVER, please use the RADIUS device ID  # noqa: E501

        :param radius_server_id: The radius_server_id of this XiqRadiusClientObjectEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and radius_server_id is None:  # noqa: E501
            raise ValueError("Invalid value for `radius_server_id`, must not be `None`")  # noqa: E501

        self._radius_server_id = radius_server_id

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
        if not isinstance(other, XiqRadiusClientObjectEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRadiusClientObjectEntry):
            return True

        return self.to_dict() != other.to_dict()
