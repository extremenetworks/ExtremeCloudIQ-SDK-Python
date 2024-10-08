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


class XiqUpdateSsidAdvancedSettingsRequest(object):
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
        'enable802_dot11mc': 'bool'
    }

    attribute_map = {
        'enable802_dot11mc': 'enable802_dot11mc'
    }

    def __init__(self, enable802_dot11mc=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateSsidAdvancedSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable802_dot11mc = None
        self.discriminator = None

        if enable802_dot11mc is not None:
            self.enable802_dot11mc = enable802_dot11mc

    @property
    def enable802_dot11mc(self):
        """Gets the enable802_dot11mc of this XiqUpdateSsidAdvancedSettingsRequest.  # noqa: E501

        Whether to enable 802.11mc on SSID.  # noqa: E501

        :return: The enable802_dot11mc of this XiqUpdateSsidAdvancedSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable802_dot11mc

    @enable802_dot11mc.setter
    def enable802_dot11mc(self, enable802_dot11mc):
        """Sets the enable802_dot11mc of this XiqUpdateSsidAdvancedSettingsRequest.

        Whether to enable 802.11mc on SSID.  # noqa: E501

        :param enable802_dot11mc: The enable802_dot11mc of this XiqUpdateSsidAdvancedSettingsRequest.  # noqa: E501
        :type: bool
        """

        self._enable802_dot11mc = enable802_dot11mc

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
        if not isinstance(other, XiqUpdateSsidAdvancedSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateSsidAdvancedSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
