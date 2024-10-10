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


class XiqClientMacAddressAlias(object):
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
        'mac_address': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'mac_address': 'mac_address',
        'alias': 'alias'
    }

    def __init__(self, mac_address=None, alias=None, local_vars_configuration=None):  # noqa: E501
        """XiqClientMacAddressAlias - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mac_address = None
        self._alias = None
        self.discriminator = None

        self.mac_address = mac_address
        if alias is not None:
            self.alias = alias

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqClientMacAddressAlias.  # noqa: E501

        The MAC address of the client  # noqa: E501

        :return: The mac_address of this XiqClientMacAddressAlias.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqClientMacAddressAlias.

        The MAC address of the client  # noqa: E501

        :param mac_address: The mac_address of this XiqClientMacAddressAlias.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mac_address is None:  # noqa: E501
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mac_address is not None and len(mac_address) > 16):
            raise ValueError("Invalid value for `mac_address`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                mac_address is not None and len(mac_address) < 12):
            raise ValueError("Invalid value for `mac_address`, length must be greater than or equal to `12`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def alias(self):
        """Gets the alias of this XiqClientMacAddressAlias.  # noqa: E501

        The alias of the client  # noqa: E501

        :return: The alias of this XiqClientMacAddressAlias.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this XiqClientMacAddressAlias.

        The alias of the client  # noqa: E501

        :param alias: The alias of this XiqClientMacAddressAlias.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                alias is not None and len(alias) > 255):
            raise ValueError("Invalid value for `alias`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                alias is not None and len(alias) < 0):
            raise ValueError("Invalid value for `alias`, length must be greater than or equal to `0`")  # noqa: E501

        self._alias = alias

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
        if not isinstance(other, XiqClientMacAddressAlias):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClientMacAddressAlias):
            return True

        return self.to_dict() != other.to_dict()
