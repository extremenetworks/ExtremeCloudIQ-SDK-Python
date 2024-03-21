# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceStatsEntity(object):
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
        'avg_interference_utilization': 'int',
        'avg_tx_utilization': 'int',
        'avg_rx_utilization': 'int',
        'avg_total_channel_utilization': 'int',
        'avg_num_clients': 'int',
        'normal_interference': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'avg_interference_utilization': 'avg_interference_utilization',
        'avg_tx_utilization': 'avg_tx_utilization',
        'avg_rx_utilization': 'avg_rx_utilization',
        'avg_total_channel_utilization': 'avg_total_channel_utilization',
        'avg_num_clients': 'avg_num_clients',
        'normal_interference': 'normal_interference'
    }

    def __init__(self, timestamp=None, avg_interference_utilization=None, avg_tx_utilization=None, avg_rx_utilization=None, avg_total_channel_utilization=None, avg_num_clients=None, normal_interference=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceStatsEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._avg_interference_utilization = None
        self._avg_tx_utilization = None
        self._avg_rx_utilization = None
        self._avg_total_channel_utilization = None
        self._avg_num_clients = None
        self._normal_interference = None
        self.discriminator = None

        self.timestamp = timestamp
        if avg_interference_utilization is not None:
            self.avg_interference_utilization = avg_interference_utilization
        if avg_tx_utilization is not None:
            self.avg_tx_utilization = avg_tx_utilization
        if avg_rx_utilization is not None:
            self.avg_rx_utilization = avg_rx_utilization
        if avg_total_channel_utilization is not None:
            self.avg_total_channel_utilization = avg_total_channel_utilization
        if avg_num_clients is not None:
            self.avg_num_clients = avg_num_clients
        if normal_interference is not None:
            self.normal_interference = normal_interference

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqDeviceStatsEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqDeviceStatsEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def avg_interference_utilization(self):
        """Gets the avg_interference_utilization of this XiqDeviceStatsEntity.  # noqa: E501

        The average interference utilization   # noqa: E501

        :return: The avg_interference_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_interference_utilization

    @avg_interference_utilization.setter
    def avg_interference_utilization(self, avg_interference_utilization):
        """Sets the avg_interference_utilization of this XiqDeviceStatsEntity.

        The average interference utilization   # noqa: E501

        :param avg_interference_utilization: The avg_interference_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_interference_utilization = avg_interference_utilization

    @property
    def avg_tx_utilization(self):
        """Gets the avg_tx_utilization of this XiqDeviceStatsEntity.  # noqa: E501

        The Average Tx Utilization  # noqa: E501

        :return: The avg_tx_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_tx_utilization

    @avg_tx_utilization.setter
    def avg_tx_utilization(self, avg_tx_utilization):
        """Sets the avg_tx_utilization of this XiqDeviceStatsEntity.

        The Average Tx Utilization  # noqa: E501

        :param avg_tx_utilization: The avg_tx_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_tx_utilization = avg_tx_utilization

    @property
    def avg_rx_utilization(self):
        """Gets the avg_rx_utilization of this XiqDeviceStatsEntity.  # noqa: E501

        The Average Rx Utilization  # noqa: E501

        :return: The avg_rx_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_rx_utilization

    @avg_rx_utilization.setter
    def avg_rx_utilization(self, avg_rx_utilization):
        """Sets the avg_rx_utilization of this XiqDeviceStatsEntity.

        The Average Rx Utilization  # noqa: E501

        :param avg_rx_utilization: The avg_rx_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_rx_utilization = avg_rx_utilization

    @property
    def avg_total_channel_utilization(self):
        """Gets the avg_total_channel_utilization of this XiqDeviceStatsEntity.  # noqa: E501

        The Average Total Channel Utilization   # noqa: E501

        :return: The avg_total_channel_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_total_channel_utilization

    @avg_total_channel_utilization.setter
    def avg_total_channel_utilization(self, avg_total_channel_utilization):
        """Sets the avg_total_channel_utilization of this XiqDeviceStatsEntity.

        The Average Total Channel Utilization   # noqa: E501

        :param avg_total_channel_utilization: The avg_total_channel_utilization of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_total_channel_utilization = avg_total_channel_utilization

    @property
    def avg_num_clients(self):
        """Gets the avg_num_clients of this XiqDeviceStatsEntity.  # noqa: E501

        The Average Number of Clients  # noqa: E501

        :return: The avg_num_clients of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_num_clients

    @avg_num_clients.setter
    def avg_num_clients(self, avg_num_clients):
        """Sets the avg_num_clients of this XiqDeviceStatsEntity.

        The Average Number of Clients  # noqa: E501

        :param avg_num_clients: The avg_num_clients of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_num_clients = avg_num_clients

    @property
    def normal_interference(self):
        """Gets the normal_interference of this XiqDeviceStatsEntity.  # noqa: E501

        The normal interference   # noqa: E501

        :return: The normal_interference of this XiqDeviceStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._normal_interference

    @normal_interference.setter
    def normal_interference(self, normal_interference):
        """Sets the normal_interference of this XiqDeviceStatsEntity.

        The normal interference   # noqa: E501

        :param normal_interference: The normal_interference of this XiqDeviceStatsEntity.  # noqa: E501
        :type: int
        """

        self._normal_interference = normal_interference

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
        if not isinstance(other, XiqDeviceStatsEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceStatsEntity):
            return True

        return self.to_dict() != other.to_dict()
