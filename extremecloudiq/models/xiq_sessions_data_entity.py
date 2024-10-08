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


class XiqSessionsDataEntity(object):
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
        'data_rate_failure_percent': 'float',
        'client_count': 'int',
        'normal_failure_percent': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'data_rate_failure_percent': 'data_rate_failure_percent',
        'client_count': 'client_count',
        'normal_failure_percent': 'normal_failure_percent'
    }

    def __init__(self, timestamp=None, data_rate_failure_percent=None, client_count=None, normal_failure_percent=None, local_vars_configuration=None):  # noqa: E501
        """XiqSessionsDataEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._data_rate_failure_percent = None
        self._client_count = None
        self._normal_failure_percent = None
        self.discriminator = None

        self.timestamp = timestamp
        if data_rate_failure_percent is not None:
            self.data_rate_failure_percent = data_rate_failure_percent
        if client_count is not None:
            self.client_count = client_count
        if normal_failure_percent is not None:
            self.normal_failure_percent = normal_failure_percent

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqSessionsDataEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqSessionsDataEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqSessionsDataEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqSessionsDataEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def data_rate_failure_percent(self):
        """Gets the data_rate_failure_percent of this XiqSessionsDataEntity.  # noqa: E501

        The data rate failure percent   # noqa: E501

        :return: The data_rate_failure_percent of this XiqSessionsDataEntity.  # noqa: E501
        :rtype: float
        """
        return self._data_rate_failure_percent

    @data_rate_failure_percent.setter
    def data_rate_failure_percent(self, data_rate_failure_percent):
        """Sets the data_rate_failure_percent of this XiqSessionsDataEntity.

        The data rate failure percent   # noqa: E501

        :param data_rate_failure_percent: The data_rate_failure_percent of this XiqSessionsDataEntity.  # noqa: E501
        :type: float
        """

        self._data_rate_failure_percent = data_rate_failure_percent

    @property
    def client_count(self):
        """Gets the client_count of this XiqSessionsDataEntity.  # noqa: E501

        The client count  # noqa: E501

        :return: The client_count of this XiqSessionsDataEntity.  # noqa: E501
        :rtype: int
        """
        return self._client_count

    @client_count.setter
    def client_count(self, client_count):
        """Sets the client_count of this XiqSessionsDataEntity.

        The client count  # noqa: E501

        :param client_count: The client_count of this XiqSessionsDataEntity.  # noqa: E501
        :type: int
        """

        self._client_count = client_count

    @property
    def normal_failure_percent(self):
        """Gets the normal_failure_percent of this XiqSessionsDataEntity.  # noqa: E501

        The normal failure percent  # noqa: E501

        :return: The normal_failure_percent of this XiqSessionsDataEntity.  # noqa: E501
        :rtype: int
        """
        return self._normal_failure_percent

    @normal_failure_percent.setter
    def normal_failure_percent(self, normal_failure_percent):
        """Sets the normal_failure_percent of this XiqSessionsDataEntity.

        The normal failure percent  # noqa: E501

        :param normal_failure_percent: The normal_failure_percent of this XiqSessionsDataEntity.  # noqa: E501
        :type: int
        """

        self._normal_failure_percent = normal_failure_percent

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
        if not isinstance(other, XiqSessionsDataEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSessionsDataEntity):
            return True

        return self.to_dict() != other.to_dict()
