# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAdvancedOnboardDeviceResponse(object):
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
        'success_devices': 'list[XiqSuccessOnboardDevice]',
        'failure_devices': 'list[XiqFailureOnboardDevice]'
    }

    attribute_map = {
        'success_devices': 'success_devices',
        'failure_devices': 'failure_devices'
    }

    def __init__(self, success_devices=None, failure_devices=None, local_vars_configuration=None):  # noqa: E501
        """XiqAdvancedOnboardDeviceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._success_devices = None
        self._failure_devices = None
        self.discriminator = None

        if success_devices is not None:
            self.success_devices = success_devices
        if failure_devices is not None:
            self.failure_devices = failure_devices

    @property
    def success_devices(self):
        """Gets the success_devices of this XiqAdvancedOnboardDeviceResponse.  # noqa: E501

        The success devices  # noqa: E501

        :return: The success_devices of this XiqAdvancedOnboardDeviceResponse.  # noqa: E501
        :rtype: list[XiqSuccessOnboardDevice]
        """
        return self._success_devices

    @success_devices.setter
    def success_devices(self, success_devices):
        """Sets the success_devices of this XiqAdvancedOnboardDeviceResponse.

        The success devices  # noqa: E501

        :param success_devices: The success_devices of this XiqAdvancedOnboardDeviceResponse.  # noqa: E501
        :type: list[XiqSuccessOnboardDevice]
        """

        self._success_devices = success_devices

    @property
    def failure_devices(self):
        """Gets the failure_devices of this XiqAdvancedOnboardDeviceResponse.  # noqa: E501

        The failure devices  # noqa: E501

        :return: The failure_devices of this XiqAdvancedOnboardDeviceResponse.  # noqa: E501
        :rtype: list[XiqFailureOnboardDevice]
        """
        return self._failure_devices

    @failure_devices.setter
    def failure_devices(self, failure_devices):
        """Sets the failure_devices of this XiqAdvancedOnboardDeviceResponse.

        The failure devices  # noqa: E501

        :param failure_devices: The failure_devices of this XiqAdvancedOnboardDeviceResponse.  # noqa: E501
        :type: list[XiqFailureOnboardDevice]
        """

        self._failure_devices = failure_devices

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
        if not isinstance(other, XiqAdvancedOnboardDeviceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAdvancedOnboardDeviceResponse):
            return True

        return self.to_dict() != other.to_dict()
