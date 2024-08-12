# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqThreadIpv6Setting(object):
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
        'address': 'str',
        'scope': 'str',
        'cast': 'str',
        'type': 'str'
    }

    attribute_map = {
        'address': 'address',
        'scope': 'scope',
        'cast': 'cast',
        'type': 'type'
    }

    def __init__(self, address=None, scope=None, cast=None, type=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadIpv6Setting - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._scope = None
        self._cast = None
        self._type = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if scope is not None:
            self.scope = scope
        if cast is not None:
            self.cast = cast
        if type is not None:
            self.type = type

    @property
    def address(self):
        """Gets the address of this XiqThreadIpv6Setting.  # noqa: E501


        :return: The address of this XiqThreadIpv6Setting.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this XiqThreadIpv6Setting.


        :param address: The address of this XiqThreadIpv6Setting.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def scope(self):
        """Gets the scope of this XiqThreadIpv6Setting.  # noqa: E501


        :return: The scope of this XiqThreadIpv6Setting.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this XiqThreadIpv6Setting.


        :param scope: The scope of this XiqThreadIpv6Setting.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def cast(self):
        """Gets the cast of this XiqThreadIpv6Setting.  # noqa: E501


        :return: The cast of this XiqThreadIpv6Setting.  # noqa: E501
        :rtype: str
        """
        return self._cast

    @cast.setter
    def cast(self, cast):
        """Sets the cast of this XiqThreadIpv6Setting.


        :param cast: The cast of this XiqThreadIpv6Setting.  # noqa: E501
        :type: str
        """

        self._cast = cast

    @property
    def type(self):
        """Gets the type of this XiqThreadIpv6Setting.  # noqa: E501


        :return: The type of this XiqThreadIpv6Setting.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XiqThreadIpv6Setting.


        :param type: The type of this XiqThreadIpv6Setting.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, XiqThreadIpv6Setting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadIpv6Setting):
            return True

        return self.to_dict() != other.to_dict()
