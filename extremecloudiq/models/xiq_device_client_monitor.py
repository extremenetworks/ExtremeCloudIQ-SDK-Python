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


class XiqDeviceClientMonitor(object):
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
        'client_monitor_profile_id': 'int',
        'enable': 'bool'
    }

    attribute_map = {
        'client_monitor_profile_id': 'client_monitor_profile_id',
        'enable': 'enable'
    }

    def __init__(self, client_monitor_profile_id=None, enable=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceClientMonitor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_monitor_profile_id = None
        self._enable = None
        self.discriminator = None

        if client_monitor_profile_id is not None:
            self.client_monitor_profile_id = client_monitor_profile_id
        if enable is not None:
            self.enable = enable

    @property
    def client_monitor_profile_id(self):
        """Gets the client_monitor_profile_id of this XiqDeviceClientMonitor.  # noqa: E501

        The assigned client monitor profile ID  # noqa: E501

        :return: The client_monitor_profile_id of this XiqDeviceClientMonitor.  # noqa: E501
        :rtype: int
        """
        return self._client_monitor_profile_id

    @client_monitor_profile_id.setter
    def client_monitor_profile_id(self, client_monitor_profile_id):
        """Sets the client_monitor_profile_id of this XiqDeviceClientMonitor.

        The assigned client monitor profile ID  # noqa: E501

        :param client_monitor_profile_id: The client_monitor_profile_id of this XiqDeviceClientMonitor.  # noqa: E501
        :type: int
        """

        self._client_monitor_profile_id = client_monitor_profile_id

    @property
    def enable(self):
        """Gets the enable of this XiqDeviceClientMonitor.  # noqa: E501

        The timestamp when the device assigned to the location  # noqa: E501

        :return: The enable of this XiqDeviceClientMonitor.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this XiqDeviceClientMonitor.

        The timestamp when the device assigned to the location  # noqa: E501

        :param enable: The enable of this XiqDeviceClientMonitor.  # noqa: E501
        :type: bool
        """

        self._enable = enable

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
        if not isinstance(other, XiqDeviceClientMonitor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceClientMonitor):
            return True

        return self.to_dict() != other.to_dict()
