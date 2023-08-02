# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAtpDeviceStatsEntity(object):
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
        'timestamp': 'int',
        'avg_cpu': 'float',
        'avg_memory': 'float',
        'avg_client_count': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'avg_cpu': 'avg_cpu',
        'avg_memory': 'avg_memory',
        'avg_client_count': 'avg_client_count'
    }

    def __init__(self, timestamp=None, avg_cpu=None, avg_memory=None, avg_client_count=None, local_vars_configuration=None):  # noqa: E501
        """XiqAtpDeviceStatsEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._avg_cpu = None
        self._avg_memory = None
        self._avg_client_count = None
        self.discriminator = None

        self.timestamp = timestamp
        if avg_cpu is not None:
            self.avg_cpu = avg_cpu
        if avg_memory is not None:
            self.avg_memory = avg_memory
        if avg_client_count is not None:
            self.avg_client_count = avg_client_count

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqAtpDeviceStatsEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqAtpDeviceStatsEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def avg_cpu(self):
        """Gets the avg_cpu of this XiqAtpDeviceStatsEntity.  # noqa: E501

        Avg Cpu  # noqa: E501

        :return: The avg_cpu of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :rtype: float
        """
        return self._avg_cpu

    @avg_cpu.setter
    def avg_cpu(self, avg_cpu):
        """Sets the avg_cpu of this XiqAtpDeviceStatsEntity.

        Avg Cpu  # noqa: E501

        :param avg_cpu: The avg_cpu of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :type: float
        """

        self._avg_cpu = avg_cpu

    @property
    def avg_memory(self):
        """Gets the avg_memory of this XiqAtpDeviceStatsEntity.  # noqa: E501

        Avg Memory  # noqa: E501

        :return: The avg_memory of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :rtype: float
        """
        return self._avg_memory

    @avg_memory.setter
    def avg_memory(self, avg_memory):
        """Sets the avg_memory of this XiqAtpDeviceStatsEntity.

        Avg Memory  # noqa: E501

        :param avg_memory: The avg_memory of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :type: float
        """

        self._avg_memory = avg_memory

    @property
    def avg_client_count(self):
        """Gets the avg_client_count of this XiqAtpDeviceStatsEntity.  # noqa: E501

        Avg Client Count  # noqa: E501

        :return: The avg_client_count of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_client_count

    @avg_client_count.setter
    def avg_client_count(self, avg_client_count):
        """Sets the avg_client_count of this XiqAtpDeviceStatsEntity.

        Avg Client Count  # noqa: E501

        :param avg_client_count: The avg_client_count of this XiqAtpDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_client_count = avg_client_count

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
        if not isinstance(other, XiqAtpDeviceStatsEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAtpDeviceStatsEntity):
            return True

        return self.to_dict() != other.to_dict()
