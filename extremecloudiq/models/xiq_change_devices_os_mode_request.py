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


class XiqChangeDevicesOsModeRequest(object):
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
        'device_ids': 'list[int]',
        'target_os': 'str'
    }

    attribute_map = {
        'device_ids': 'device_ids',
        'target_os': 'target_os'
    }

    def __init__(self, device_ids=None, target_os=None, local_vars_configuration=None):  # noqa: E501
        """XiqChangeDevicesOsModeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_ids = None
        self._target_os = None
        self.discriminator = None

        self.device_ids = device_ids
        self.target_os = target_os

    @property
    def device_ids(self):
        """Gets the device_ids of this XiqChangeDevicesOsModeRequest.  # noqa: E501

        The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \"AP_410C\", \"AP_460C\", \"AP_305C\", \"AP_305CX\", \"AP_460S6C\", \"AP_460S12C\", \"AP_302W\" are allowed change to WiNG OS. For Switch: only \"5520\", \"5420F\", \"5420M\" are allowed to change its OS type.  # noqa: E501

        :return: The device_ids of this XiqChangeDevicesOsModeRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this XiqChangeDevicesOsModeRequest.

        The one or multiple device IDs to change the OS mode. Must be all AP or Switches in the same list. For AP only \"AP_410C\", \"AP_460C\", \"AP_305C\", \"AP_305CX\", \"AP_460S6C\", \"AP_460S12C\", \"AP_302W\" are allowed change to WiNG OS. For Switch: only \"5520\", \"5420F\", \"5420M\" are allowed to change its OS type.  # noqa: E501

        :param device_ids: The device_ids of this XiqChangeDevicesOsModeRequest.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and device_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `device_ids`, must not be `None`")  # noqa: E501

        self._device_ids = device_ids

    @property
    def target_os(self):
        """Gets the target_os of this XiqChangeDevicesOsModeRequest.  # noqa: E501

        The target OS mode to change to, for AP: only WiNG is supported, for Switch: EXOS or VOSS  # noqa: E501

        :return: The target_os of this XiqChangeDevicesOsModeRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_os

    @target_os.setter
    def target_os(self, target_os):
        """Sets the target_os of this XiqChangeDevicesOsModeRequest.

        The target OS mode to change to, for AP: only WiNG is supported, for Switch: EXOS or VOSS  # noqa: E501

        :param target_os: The target_os of this XiqChangeDevicesOsModeRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_os is None:  # noqa: E501
            raise ValueError("Invalid value for `target_os`, must not be `None`")  # noqa: E501

        self._target_os = target_os

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
        if not isinstance(other, XiqChangeDevicesOsModeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqChangeDevicesOsModeRequest):
            return True

        return self.to_dict() != other.to_dict()
