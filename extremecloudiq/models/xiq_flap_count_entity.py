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


class XiqFlapCountEntity(object):
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
        'flap_count': 'float',
        'sub_optimal_count': 'int',
        'optimal_time_spent': 'float'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'flap_count': 'flap_count',
        'sub_optimal_count': 'sub_optimal_count',
        'optimal_time_spent': 'optimal_time_spent'
    }

    def __init__(self, timestamp=None, flap_count=None, sub_optimal_count=None, optimal_time_spent=None, local_vars_configuration=None):  # noqa: E501
        """XiqFlapCountEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._flap_count = None
        self._sub_optimal_count = None
        self._optimal_time_spent = None
        self.discriminator = None

        self.timestamp = timestamp
        if flap_count is not None:
            self.flap_count = flap_count
        if sub_optimal_count is not None:
            self.sub_optimal_count = sub_optimal_count
        if optimal_time_spent is not None:
            self.optimal_time_spent = optimal_time_spent

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqFlapCountEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqFlapCountEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqFlapCountEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqFlapCountEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def flap_count(self):
        """Gets the flap_count of this XiqFlapCountEntity.  # noqa: E501

        The flap count  # noqa: E501

        :return: The flap_count of this XiqFlapCountEntity.  # noqa: E501
        :rtype: float
        """
        return self._flap_count

    @flap_count.setter
    def flap_count(self, flap_count):
        """Sets the flap_count of this XiqFlapCountEntity.

        The flap count  # noqa: E501

        :param flap_count: The flap_count of this XiqFlapCountEntity.  # noqa: E501
        :type: float
        """

        self._flap_count = flap_count

    @property
    def sub_optimal_count(self):
        """Gets the sub_optimal_count of this XiqFlapCountEntity.  # noqa: E501

        The sub-optimal count  # noqa: E501

        :return: The sub_optimal_count of this XiqFlapCountEntity.  # noqa: E501
        :rtype: int
        """
        return self._sub_optimal_count

    @sub_optimal_count.setter
    def sub_optimal_count(self, sub_optimal_count):
        """Sets the sub_optimal_count of this XiqFlapCountEntity.

        The sub-optimal count  # noqa: E501

        :param sub_optimal_count: The sub_optimal_count of this XiqFlapCountEntity.  # noqa: E501
        :type: int
        """

        self._sub_optimal_count = sub_optimal_count

    @property
    def optimal_time_spent(self):
        """Gets the optimal_time_spent of this XiqFlapCountEntity.  # noqa: E501

        The time spent  # noqa: E501

        :return: The optimal_time_spent of this XiqFlapCountEntity.  # noqa: E501
        :rtype: float
        """
        return self._optimal_time_spent

    @optimal_time_spent.setter
    def optimal_time_spent(self, optimal_time_spent):
        """Sets the optimal_time_spent of this XiqFlapCountEntity.

        The time spent  # noqa: E501

        :param optimal_time_spent: The optimal_time_spent of this XiqFlapCountEntity.  # noqa: E501
        :type: float
        """

        self._optimal_time_spent = optimal_time_spent

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
        if not isinstance(other, XiqFlapCountEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqFlapCountEntity):
            return True

        return self.to_dict() != other.to_dict()
