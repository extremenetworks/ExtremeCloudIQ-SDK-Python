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


class XiqUpdateMacObjectRequest(object):
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
        'name': 'str',
        'description': 'str',
        'value': 'str',
        'mac_address_end': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'value': 'value',
        'mac_address_end': 'mac_address_end'
    }

    def __init__(self, name=None, description=None, value=None, mac_address_end=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateMacObjectRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._value = None
        self._mac_address_end = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value
        if mac_address_end is not None:
            self.mac_address_end = mac_address_end

    @property
    def name(self):
        """Gets the name of this XiqUpdateMacObjectRequest.  # noqa: E501

        The product model  # noqa: E501

        :return: The name of this XiqUpdateMacObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateMacObjectRequest.

        The product model  # noqa: E501

        :param name: The name of this XiqUpdateMacObjectRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUpdateMacObjectRequest.  # noqa: E501

        The product description  # noqa: E501

        :return: The description of this XiqUpdateMacObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateMacObjectRequest.

        The product description  # noqa: E501

        :param description: The description of this XiqUpdateMacObjectRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this XiqUpdateMacObjectRequest.  # noqa: E501

        The MAC octets.  # noqa: E501

        :return: The value of this XiqUpdateMacObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this XiqUpdateMacObjectRequest.

        The MAC octets.  # noqa: E501

        :param value: The value of this XiqUpdateMacObjectRequest.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def mac_address_end(self):
        """Gets the mac_address_end of this XiqUpdateMacObjectRequest.  # noqa: E501

        The MAC address end, only available for \"MAC_RANGE\" type.  # noqa: E501

        :return: The mac_address_end of this XiqUpdateMacObjectRequest.  # noqa: E501
        :rtype: str
        """
        return self._mac_address_end

    @mac_address_end.setter
    def mac_address_end(self, mac_address_end):
        """Sets the mac_address_end of this XiqUpdateMacObjectRequest.

        The MAC address end, only available for \"MAC_RANGE\" type.  # noqa: E501

        :param mac_address_end: The mac_address_end of this XiqUpdateMacObjectRequest.  # noqa: E501
        :type: str
        """

        self._mac_address_end = mac_address_end

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
        if not isinstance(other, XiqUpdateMacObjectRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateMacObjectRequest):
            return True

        return self.to_dict() != other.to_dict()
