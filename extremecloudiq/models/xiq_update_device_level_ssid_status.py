# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateDeviceLevelSsidStatus(object):
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
        'ssid_ids': 'list[int]',
        'if_names': 'list[XiqWirelessIfName]',
        'enabled': 'bool'
    }

    attribute_map = {
        'ssid_ids': 'ssid_ids',
        'if_names': 'if_names',
        'enabled': 'enabled'
    }

    def __init__(self, ssid_ids=None, if_names=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateDeviceLevelSsidStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ssid_ids = None
        self._if_names = None
        self._enabled = None
        self.discriminator = None

        self.ssid_ids = ssid_ids
        self.if_names = if_names
        self.enabled = enabled

    @property
    def ssid_ids(self):
        """Gets the ssid_ids of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501

        The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered.  # noqa: E501

        :return: The ssid_ids of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501
        :rtype: list[int]
        """
        return self._ssid_ids

    @ssid_ids.setter
    def ssid_ids(self, ssid_ids):
        """Sets the ssid_ids of this XiqUpdateDeviceLevelSsidStatus.

        The one or multiple SSID to be disabled/enabled, cannot be empty or no action will be triggered.  # noqa: E501

        :param ssid_ids: The ssid_ids of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and ssid_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `ssid_ids`, must not be `None`")  # noqa: E501

        self._ssid_ids = ssid_ids

    @property
    def if_names(self):
        """Gets the if_names of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501

        The one or multiple ssid on wifi interfaces (example:wifi0 or wifi1) to be disabled/enabled, cannot be empty or no SSID will be disabled or enabled.  # noqa: E501

        :return: The if_names of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501
        :rtype: list[XiqWirelessIfName]
        """
        return self._if_names

    @if_names.setter
    def if_names(self, if_names):
        """Sets the if_names of this XiqUpdateDeviceLevelSsidStatus.

        The one or multiple ssid on wifi interfaces (example:wifi0 or wifi1) to be disabled/enabled, cannot be empty or no SSID will be disabled or enabled.  # noqa: E501

        :param if_names: The if_names of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501
        :type: list[XiqWirelessIfName]
        """
        if self.local_vars_configuration.client_side_validation and if_names is None:  # noqa: E501
            raise ValueError("Invalid value for `if_names`, must not be `None`")  # noqa: E501

        self._if_names = if_names

    @property
    def enabled(self):
        """Gets the enabled of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501

        To disable or enable the given device level SSIDs on the wifi interfaces.  # noqa: E501

        :return: The enabled of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this XiqUpdateDeviceLevelSsidStatus.

        To disable or enable the given device level SSIDs on the wifi interfaces.  # noqa: E501

        :param enabled: The enabled of this XiqUpdateDeviceLevelSsidStatus.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if not isinstance(other, XiqUpdateDeviceLevelSsidStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateDeviceLevelSsidStatus):
            return True

        return self.to_dict() != other.to_dict()
