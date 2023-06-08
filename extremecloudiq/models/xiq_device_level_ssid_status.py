# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceLevelSsidStatus(object):
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
        'wifi0_enabled': 'bool',
        'wifi1_enabled': 'bool'
    }

    attribute_map = {
        'wifi0_enabled': 'wifi0_enabled',
        'wifi1_enabled': 'wifi1_enabled'
    }

    def __init__(self, wifi0_enabled=None, wifi1_enabled=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceLevelSsidStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wifi0_enabled = None
        self._wifi1_enabled = None
        self.discriminator = None

        self.wifi0_enabled = wifi0_enabled
        self.wifi1_enabled = wifi1_enabled

    @property
    def wifi0_enabled(self):
        """Gets the wifi0_enabled of this XiqDeviceLevelSsidStatus.  # noqa: E501

        The SSID is enabled or not on wifi0 interface  # noqa: E501

        :return: The wifi0_enabled of this XiqDeviceLevelSsidStatus.  # noqa: E501
        :rtype: bool
        """
        return self._wifi0_enabled

    @wifi0_enabled.setter
    def wifi0_enabled(self, wifi0_enabled):
        """Sets the wifi0_enabled of this XiqDeviceLevelSsidStatus.

        The SSID is enabled or not on wifi0 interface  # noqa: E501

        :param wifi0_enabled: The wifi0_enabled of this XiqDeviceLevelSsidStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and wifi0_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `wifi0_enabled`, must not be `None`")  # noqa: E501

        self._wifi0_enabled = wifi0_enabled

    @property
    def wifi1_enabled(self):
        """Gets the wifi1_enabled of this XiqDeviceLevelSsidStatus.  # noqa: E501

        The SSID is enabled or not on wifi1 interface  # noqa: E501

        :return: The wifi1_enabled of this XiqDeviceLevelSsidStatus.  # noqa: E501
        :rtype: bool
        """
        return self._wifi1_enabled

    @wifi1_enabled.setter
    def wifi1_enabled(self, wifi1_enabled):
        """Sets the wifi1_enabled of this XiqDeviceLevelSsidStatus.

        The SSID is enabled or not on wifi1 interface  # noqa: E501

        :param wifi1_enabled: The wifi1_enabled of this XiqDeviceLevelSsidStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and wifi1_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `wifi1_enabled`, must not be `None`")  # noqa: E501

        self._wifi1_enabled = wifi1_enabled

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
        if not isinstance(other, XiqDeviceLevelSsidStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceLevelSsidStatus):
            return True

        return self.to_dict() != other.to_dict()
