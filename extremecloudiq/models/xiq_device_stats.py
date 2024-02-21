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


class XiqDeviceStats(object):
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
        'total_device_count': 'int',
        'managed_device_count': 'int',
        'connected_device_count': 'int'
    }

    attribute_map = {
        'total_device_count': 'total_device_count',
        'managed_device_count': 'managed_device_count',
        'connected_device_count': 'connected_device_count'
    }

    def __init__(self, total_device_count=None, managed_device_count=None, connected_device_count=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_device_count = None
        self._managed_device_count = None
        self._connected_device_count = None
        self.discriminator = None

        if total_device_count is not None:
            self.total_device_count = total_device_count
        if managed_device_count is not None:
            self.managed_device_count = managed_device_count
        if connected_device_count is not None:
            self.connected_device_count = connected_device_count

    @property
    def total_device_count(self):
        """Gets the total_device_count of this XiqDeviceStats.  # noqa: E501


        :return: The total_device_count of this XiqDeviceStats.  # noqa: E501
        :rtype: int
        """
        return self._total_device_count

    @total_device_count.setter
    def total_device_count(self, total_device_count):
        """Sets the total_device_count of this XiqDeviceStats.


        :param total_device_count: The total_device_count of this XiqDeviceStats.  # noqa: E501
        :type: int
        """

        self._total_device_count = total_device_count

    @property
    def managed_device_count(self):
        """Gets the managed_device_count of this XiqDeviceStats.  # noqa: E501


        :return: The managed_device_count of this XiqDeviceStats.  # noqa: E501
        :rtype: int
        """
        return self._managed_device_count

    @managed_device_count.setter
    def managed_device_count(self, managed_device_count):
        """Sets the managed_device_count of this XiqDeviceStats.


        :param managed_device_count: The managed_device_count of this XiqDeviceStats.  # noqa: E501
        :type: int
        """

        self._managed_device_count = managed_device_count

    @property
    def connected_device_count(self):
        """Gets the connected_device_count of this XiqDeviceStats.  # noqa: E501


        :return: The connected_device_count of this XiqDeviceStats.  # noqa: E501
        :rtype: int
        """
        return self._connected_device_count

    @connected_device_count.setter
    def connected_device_count(self, connected_device_count):
        """Sets the connected_device_count of this XiqDeviceStats.


        :param connected_device_count: The connected_device_count of this XiqDeviceStats.  # noqa: E501
        :type: int
        """

        self._connected_device_count = connected_device_count

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
        if not isinstance(other, XiqDeviceStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceStats):
            return True

        return self.to_dict() != other.to_dict()
