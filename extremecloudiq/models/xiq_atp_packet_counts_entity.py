# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAtpPacketCountsEntity(object):
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
        'unicast_tx': 'float',
        'unicast_rx': 'float',
        'multicast_tx': 'float',
        'multicast_rx': 'float',
        'broadcast_tx': 'float',
        'broadcast_rx': 'float'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'unicast_tx': 'unicast_tx',
        'unicast_rx': 'unicast_rx',
        'multicast_tx': 'multicast_tx',
        'multicast_rx': 'multicast_rx',
        'broadcast_tx': 'broadcast_tx',
        'broadcast_rx': 'broadcast_rx'
    }

    def __init__(self, timestamp=None, unicast_tx=None, unicast_rx=None, multicast_tx=None, multicast_rx=None, broadcast_tx=None, broadcast_rx=None, local_vars_configuration=None):  # noqa: E501
        """XiqAtpPacketCountsEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._unicast_tx = None
        self._unicast_rx = None
        self._multicast_tx = None
        self._multicast_rx = None
        self._broadcast_tx = None
        self._broadcast_rx = None
        self.discriminator = None

        self.timestamp = timestamp
        if unicast_tx is not None:
            self.unicast_tx = unicast_tx
        if unicast_rx is not None:
            self.unicast_rx = unicast_rx
        if multicast_tx is not None:
            self.multicast_tx = multicast_tx
        if multicast_rx is not None:
            self.multicast_rx = multicast_rx
        if broadcast_tx is not None:
            self.broadcast_tx = broadcast_tx
        if broadcast_rx is not None:
            self.broadcast_rx = broadcast_rx

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqAtpPacketCountsEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqAtpPacketCountsEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def unicast_tx(self):
        """Gets the unicast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501

        Unicast Tx  # noqa: E501

        :return: The unicast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: float
        """
        return self._unicast_tx

    @unicast_tx.setter
    def unicast_tx(self, unicast_tx):
        """Sets the unicast_tx of this XiqAtpPacketCountsEntity.

        Unicast Tx  # noqa: E501

        :param unicast_tx: The unicast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: float
        """

        self._unicast_tx = unicast_tx

    @property
    def unicast_rx(self):
        """Gets the unicast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501

        Unicast Rx  # noqa: E501

        :return: The unicast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: float
        """
        return self._unicast_rx

    @unicast_rx.setter
    def unicast_rx(self, unicast_rx):
        """Sets the unicast_rx of this XiqAtpPacketCountsEntity.

        Unicast Rx  # noqa: E501

        :param unicast_rx: The unicast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: float
        """

        self._unicast_rx = unicast_rx

    @property
    def multicast_tx(self):
        """Gets the multicast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501

        Multicast Tx  # noqa: E501

        :return: The multicast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: float
        """
        return self._multicast_tx

    @multicast_tx.setter
    def multicast_tx(self, multicast_tx):
        """Sets the multicast_tx of this XiqAtpPacketCountsEntity.

        Multicast Tx  # noqa: E501

        :param multicast_tx: The multicast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: float
        """

        self._multicast_tx = multicast_tx

    @property
    def multicast_rx(self):
        """Gets the multicast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501

        Multicast Rx  # noqa: E501

        :return: The multicast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: float
        """
        return self._multicast_rx

    @multicast_rx.setter
    def multicast_rx(self, multicast_rx):
        """Sets the multicast_rx of this XiqAtpPacketCountsEntity.

        Multicast Rx  # noqa: E501

        :param multicast_rx: The multicast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: float
        """

        self._multicast_rx = multicast_rx

    @property
    def broadcast_tx(self):
        """Gets the broadcast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501

        Broadcast Tx  # noqa: E501

        :return: The broadcast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: float
        """
        return self._broadcast_tx

    @broadcast_tx.setter
    def broadcast_tx(self, broadcast_tx):
        """Sets the broadcast_tx of this XiqAtpPacketCountsEntity.

        Broadcast Tx  # noqa: E501

        :param broadcast_tx: The broadcast_tx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: float
        """

        self._broadcast_tx = broadcast_tx

    @property
    def broadcast_rx(self):
        """Gets the broadcast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501

        Broadcast Rx  # noqa: E501

        :return: The broadcast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :rtype: float
        """
        return self._broadcast_rx

    @broadcast_rx.setter
    def broadcast_rx(self, broadcast_rx):
        """Sets the broadcast_rx of this XiqAtpPacketCountsEntity.

        Broadcast Rx  # noqa: E501

        :param broadcast_rx: The broadcast_rx of this XiqAtpPacketCountsEntity.  # noqa: E501
        :type: float
        """

        self._broadcast_rx = broadcast_rx

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
        if not isinstance(other, XiqAtpPacketCountsEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAtpPacketCountsEntity):
            return True

        return self.to_dict() != other.to_dict()
