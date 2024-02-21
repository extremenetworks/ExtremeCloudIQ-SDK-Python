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


class XiqWirelessPerformanceEntity(object):
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
        'quality_index': 'int',
        'total_clients': 'int',
        'time_to_connect_score': 'int',
        'performance_score': 'int',
        'snr': 'int',
        'retries_data': 'XiqWirelessPerformanceRetriesEntity'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'quality_index': 'quality_index',
        'total_clients': 'total_clients',
        'time_to_connect_score': 'time_to_connect_score',
        'performance_score': 'performance_score',
        'snr': 'snr',
        'retries_data': 'retries_data'
    }

    def __init__(self, timestamp=None, quality_index=None, total_clients=None, time_to_connect_score=None, performance_score=None, snr=None, retries_data=None, local_vars_configuration=None):  # noqa: E501
        """XiqWirelessPerformanceEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._quality_index = None
        self._total_clients = None
        self._time_to_connect_score = None
        self._performance_score = None
        self._snr = None
        self._retries_data = None
        self.discriminator = None

        self.timestamp = timestamp
        if quality_index is not None:
            self.quality_index = quality_index
        if total_clients is not None:
            self.total_clients = total_clients
        if time_to_connect_score is not None:
            self.time_to_connect_score = time_to_connect_score
        if performance_score is not None:
            self.performance_score = performance_score
        if snr is not None:
            self.snr = snr
        if retries_data is not None:
            self.retries_data = retries_data

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqWirelessPerformanceEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqWirelessPerformanceEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def quality_index(self):
        """Gets the quality_index of this XiqWirelessPerformanceEntity.  # noqa: E501

        The quality index  # noqa: E501

        :return: The quality_index of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: int
        """
        return self._quality_index

    @quality_index.setter
    def quality_index(self, quality_index):
        """Sets the quality_index of this XiqWirelessPerformanceEntity.

        The quality index  # noqa: E501

        :param quality_index: The quality_index of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: int
        """

        self._quality_index = quality_index

    @property
    def total_clients(self):
        """Gets the total_clients of this XiqWirelessPerformanceEntity.  # noqa: E501

        The total clients  # noqa: E501

        :return: The total_clients of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: int
        """
        return self._total_clients

    @total_clients.setter
    def total_clients(self, total_clients):
        """Sets the total_clients of this XiqWirelessPerformanceEntity.

        The total clients  # noqa: E501

        :param total_clients: The total_clients of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: int
        """

        self._total_clients = total_clients

    @property
    def time_to_connect_score(self):
        """Gets the time_to_connect_score of this XiqWirelessPerformanceEntity.  # noqa: E501

        The time to connect score  # noqa: E501

        :return: The time_to_connect_score of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: int
        """
        return self._time_to_connect_score

    @time_to_connect_score.setter
    def time_to_connect_score(self, time_to_connect_score):
        """Sets the time_to_connect_score of this XiqWirelessPerformanceEntity.

        The time to connect score  # noqa: E501

        :param time_to_connect_score: The time_to_connect_score of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: int
        """

        self._time_to_connect_score = time_to_connect_score

    @property
    def performance_score(self):
        """Gets the performance_score of this XiqWirelessPerformanceEntity.  # noqa: E501

        The performance score  # noqa: E501

        :return: The performance_score of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: int
        """
        return self._performance_score

    @performance_score.setter
    def performance_score(self, performance_score):
        """Sets the performance_score of this XiqWirelessPerformanceEntity.

        The performance score  # noqa: E501

        :param performance_score: The performance_score of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: int
        """

        self._performance_score = performance_score

    @property
    def snr(self):
        """Gets the snr of this XiqWirelessPerformanceEntity.  # noqa: E501

        The average snr  # noqa: E501

        :return: The snr of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: int
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this XiqWirelessPerformanceEntity.

        The average snr  # noqa: E501

        :param snr: The snr of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: int
        """

        self._snr = snr

    @property
    def retries_data(self):
        """Gets the retries_data of this XiqWirelessPerformanceEntity.  # noqa: E501


        :return: The retries_data of this XiqWirelessPerformanceEntity.  # noqa: E501
        :rtype: XiqWirelessPerformanceRetriesEntity
        """
        return self._retries_data

    @retries_data.setter
    def retries_data(self, retries_data):
        """Sets the retries_data of this XiqWirelessPerformanceEntity.


        :param retries_data: The retries_data of this XiqWirelessPerformanceEntity.  # noqa: E501
        :type: XiqWirelessPerformanceRetriesEntity
        """

        self._retries_data = retries_data

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
        if not isinstance(other, XiqWirelessPerformanceEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWirelessPerformanceEntity):
            return True

        return self.to_dict() != other.to_dict()
