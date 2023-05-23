# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqSpeedDuplexEntity(object):
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
        'speed_value': 'int',
        'duplex_value': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'speed_value': 'speed_value',
        'duplex_value': 'duplex_value'
    }

    def __init__(self, timestamp=None, speed_value=None, duplex_value=None, local_vars_configuration=None):  # noqa: E501
        """XiqSpeedDuplexEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._speed_value = None
        self._duplex_value = None
        self.discriminator = None

        self.timestamp = timestamp
        if speed_value is not None:
            self.speed_value = speed_value
        if duplex_value is not None:
            self.duplex_value = duplex_value

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqSpeedDuplexEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqSpeedDuplexEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqSpeedDuplexEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqSpeedDuplexEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def speed_value(self):
        """Gets the speed_value of this XiqSpeedDuplexEntity.  # noqa: E501

        The speed value  # noqa: E501

        :return: The speed_value of this XiqSpeedDuplexEntity.  # noqa: E501
        :rtype: int
        """
        return self._speed_value

    @speed_value.setter
    def speed_value(self, speed_value):
        """Sets the speed_value of this XiqSpeedDuplexEntity.

        The speed value  # noqa: E501

        :param speed_value: The speed_value of this XiqSpeedDuplexEntity.  # noqa: E501
        :type: int
        """

        self._speed_value = speed_value

    @property
    def duplex_value(self):
        """Gets the duplex_value of this XiqSpeedDuplexEntity.  # noqa: E501

        The duplex value  # noqa: E501

        :return: The duplex_value of this XiqSpeedDuplexEntity.  # noqa: E501
        :rtype: int
        """
        return self._duplex_value

    @duplex_value.setter
    def duplex_value(self, duplex_value):
        """Sets the duplex_value of this XiqSpeedDuplexEntity.

        The duplex value  # noqa: E501

        :param duplex_value: The duplex_value of this XiqSpeedDuplexEntity.  # noqa: E501
        :type: int
        """

        self._duplex_value = duplex_value

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
        if not isinstance(other, XiqSpeedDuplexEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSpeedDuplexEntity):
            return True

        return self.to_dict() != other.to_dict()
