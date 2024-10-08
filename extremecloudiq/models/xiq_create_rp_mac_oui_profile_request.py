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


class XiqCreateRpMacOuiProfileRequest(object):
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
        'value': 'str',
        'description': 'str',
        'mac_type': 'str',
        'defender_defined': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'description': 'description',
        'mac_type': 'mac_type',
        'defender_defined': 'defender_defined'
    }

    def __init__(self, name=None, value=None, description=None, mac_type=None, defender_defined=None, local_vars_configuration=None):  # noqa: E501
        """XiqCreateRpMacOuiProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self._description = None
        self._mac_type = None
        self._defender_defined = None
        self.discriminator = None

        self.name = name
        self.value = value
        if description is not None:
            self.description = description
        if mac_type is not None:
            self.mac_type = mac_type
        if defender_defined is not None:
            self.defender_defined = defender_defined

    @property
    def name(self):
        """Gets the name of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501

        The product name  # noqa: E501

        :return: The name of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqCreateRpMacOuiProfileRequest.

        The product name  # noqa: E501

        :param name: The name of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501

        The product MAC or OUI  # noqa: E501

        :return: The value of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this XiqCreateRpMacOuiProfileRequest.

        The product MAC or OUI  # noqa: E501

        :param value: The value of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def description(self):
        """Gets the description of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501

        The product description  # noqa: E501

        :return: The description of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqCreateRpMacOuiProfileRequest.

        The product description  # noqa: E501

        :param description: The description of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mac_type(self):
        """Gets the mac_type of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501

        The json type, eg, \"mac-oui-profile\"  or \"MAC_OUI\"  # noqa: E501

        :return: The mac_type of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._mac_type

    @mac_type.setter
    def mac_type(self, mac_type):
        """Sets the mac_type of this XiqCreateRpMacOuiProfileRequest.

        The json type, eg, \"mac-oui-profile\"  or \"MAC_OUI\"  # noqa: E501

        :param mac_type: The mac_type of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :type: str
        """

        self._mac_type = mac_type

    @property
    def defender_defined(self):
        """Gets the defender_defined of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501

        Whether defender is defined  # noqa: E501

        :return: The defender_defined of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._defender_defined

    @defender_defined.setter
    def defender_defined(self, defender_defined):
        """Sets the defender_defined of this XiqCreateRpMacOuiProfileRequest.

        Whether defender is defined  # noqa: E501

        :param defender_defined: The defender_defined of this XiqCreateRpMacOuiProfileRequest.  # noqa: E501
        :type: bool
        """

        self._defender_defined = defender_defined

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
        if not isinstance(other, XiqCreateRpMacOuiProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCreateRpMacOuiProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
