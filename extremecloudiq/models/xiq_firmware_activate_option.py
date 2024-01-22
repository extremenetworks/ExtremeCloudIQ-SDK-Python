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


class XiqFirmwareActivateOption(object):
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
        'enable_activate_at_next_reboot': 'bool',
        'activation_delay_seconds': 'int',
        'activation_time': 'int'
    }

    attribute_map = {
        'enable_activate_at_next_reboot': 'enable_activate_at_next_reboot',
        'activation_delay_seconds': 'activation_delay_seconds',
        'activation_time': 'activation_time'
    }

    def __init__(self, enable_activate_at_next_reboot=None, activation_delay_seconds=None, activation_time=None, local_vars_configuration=None):  # noqa: E501
        """XiqFirmwareActivateOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_activate_at_next_reboot = None
        self._activation_delay_seconds = None
        self._activation_time = None
        self.discriminator = None

        if enable_activate_at_next_reboot is not None:
            self.enable_activate_at_next_reboot = enable_activate_at_next_reboot
        if activation_delay_seconds is not None:
            self.activation_delay_seconds = activation_delay_seconds
        if activation_time is not None:
            self.activation_time = activation_time

    @property
    def enable_activate_at_next_reboot(self):
        """Gets the enable_activate_at_next_reboot of this XiqFirmwareActivateOption.  # noqa: E501

        Activate at next reboot (requires rebooting manually)  # noqa: E501

        :return: The enable_activate_at_next_reboot of this XiqFirmwareActivateOption.  # noqa: E501
        :rtype: bool
        """
        return self._enable_activate_at_next_reboot

    @enable_activate_at_next_reboot.setter
    def enable_activate_at_next_reboot(self, enable_activate_at_next_reboot):
        """Sets the enable_activate_at_next_reboot of this XiqFirmwareActivateOption.

        Activate at next reboot (requires rebooting manually)  # noqa: E501

        :param enable_activate_at_next_reboot: The enable_activate_at_next_reboot of this XiqFirmwareActivateOption.  # noqa: E501
        :type: bool
        """

        self._enable_activate_at_next_reboot = enable_activate_at_next_reboot

    @property
    def activation_delay_seconds(self):
        """Gets the activation_delay_seconds of this XiqFirmwareActivateOption.  # noqa: E501

        Activate after the given seconds  # noqa: E501

        :return: The activation_delay_seconds of this XiqFirmwareActivateOption.  # noqa: E501
        :rtype: int
        """
        return self._activation_delay_seconds

    @activation_delay_seconds.setter
    def activation_delay_seconds(self, activation_delay_seconds):
        """Sets the activation_delay_seconds of this XiqFirmwareActivateOption.

        Activate after the given seconds  # noqa: E501

        :param activation_delay_seconds: The activation_delay_seconds of this XiqFirmwareActivateOption.  # noqa: E501
        :type: int
        """

        self._activation_delay_seconds = activation_delay_seconds

    @property
    def activation_time(self):
        """Gets the activation_time of this XiqFirmwareActivateOption.  # noqa: E501

        Activate at the following time according to the system clock on the updated device  # noqa: E501

        :return: The activation_time of this XiqFirmwareActivateOption.  # noqa: E501
        :rtype: int
        """
        return self._activation_time

    @activation_time.setter
    def activation_time(self, activation_time):
        """Sets the activation_time of this XiqFirmwareActivateOption.

        Activate at the following time according to the system clock on the updated device  # noqa: E501

        :param activation_time: The activation_time of this XiqFirmwareActivateOption.  # noqa: E501
        :type: int
        """

        self._activation_time = activation_time

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
        if not isinstance(other, XiqFirmwareActivateOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqFirmwareActivateOption):
            return True

        return self.to_dict() != other.to_dict()
