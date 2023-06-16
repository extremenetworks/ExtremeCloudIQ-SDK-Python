# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAnomaliesCountVoEntity(object):
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
        'total_anomalies_count': 'int',
        'wifi_efficiency_count': 'int',
        'wifi_capacity_count': 'int',
        'poe_count': 'int',
        'pe_count': 'int',
        'dfs_count': 'int',
        'mb_cast_count': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'total_anomalies_count': 'total_anomalies_count',
        'wifi_efficiency_count': 'wifi_efficiency_count',
        'wifi_capacity_count': 'wifi_capacity_count',
        'poe_count': 'poe_count',
        'pe_count': 'pe_count',
        'dfs_count': 'dfs_count',
        'mb_cast_count': 'mb_cast_count'
    }

    def __init__(self, timestamp=None, total_anomalies_count=None, wifi_efficiency_count=None, wifi_capacity_count=None, poe_count=None, pe_count=None, dfs_count=None, mb_cast_count=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomaliesCountVoEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._total_anomalies_count = None
        self._wifi_efficiency_count = None
        self._wifi_capacity_count = None
        self._poe_count = None
        self._pe_count = None
        self._dfs_count = None
        self._mb_cast_count = None
        self.discriminator = None

        self.timestamp = timestamp
        if total_anomalies_count is not None:
            self.total_anomalies_count = total_anomalies_count
        if wifi_efficiency_count is not None:
            self.wifi_efficiency_count = wifi_efficiency_count
        if wifi_capacity_count is not None:
            self.wifi_capacity_count = wifi_capacity_count
        if poe_count is not None:
            self.poe_count = poe_count
        if pe_count is not None:
            self.pe_count = pe_count
        if dfs_count is not None:
            self.dfs_count = dfs_count
        if mb_cast_count is not None:
            self.mb_cast_count = mb_cast_count

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqAnomaliesCountVoEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def total_anomalies_count(self):
        """Gets the total_anomalies_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The total anomalies count  # noqa: E501

        :return: The total_anomalies_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._total_anomalies_count

    @total_anomalies_count.setter
    def total_anomalies_count(self, total_anomalies_count):
        """Sets the total_anomalies_count of this XiqAnomaliesCountVoEntity.

        The total anomalies count  # noqa: E501

        :param total_anomalies_count: The total_anomalies_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._total_anomalies_count = total_anomalies_count

    @property
    def wifi_efficiency_count(self):
        """Gets the wifi_efficiency_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The wifi efficiency count  # noqa: E501

        :return: The wifi_efficiency_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._wifi_efficiency_count

    @wifi_efficiency_count.setter
    def wifi_efficiency_count(self, wifi_efficiency_count):
        """Sets the wifi_efficiency_count of this XiqAnomaliesCountVoEntity.

        The wifi efficiency count  # noqa: E501

        :param wifi_efficiency_count: The wifi_efficiency_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._wifi_efficiency_count = wifi_efficiency_count

    @property
    def wifi_capacity_count(self):
        """Gets the wifi_capacity_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The wifi capacity count  # noqa: E501

        :return: The wifi_capacity_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._wifi_capacity_count

    @wifi_capacity_count.setter
    def wifi_capacity_count(self, wifi_capacity_count):
        """Sets the wifi_capacity_count of this XiqAnomaliesCountVoEntity.

        The wifi capacity count  # noqa: E501

        :param wifi_capacity_count: The wifi_capacity_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._wifi_capacity_count = wifi_capacity_count

    @property
    def poe_count(self):
        """Gets the poe_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The poe flapping count  # noqa: E501

        :return: The poe_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._poe_count

    @poe_count.setter
    def poe_count(self, poe_count):
        """Sets the poe_count of this XiqAnomaliesCountVoEntity.

        The poe flapping count  # noqa: E501

        :param poe_count: The poe_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._poe_count = poe_count

    @property
    def pe_count(self):
        """Gets the pe_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The port efficiency count  # noqa: E501

        :return: The pe_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._pe_count

    @pe_count.setter
    def pe_count(self, pe_count):
        """Sets the pe_count of this XiqAnomaliesCountVoEntity.

        The port efficiency count  # noqa: E501

        :param pe_count: The pe_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._pe_count = pe_count

    @property
    def dfs_count(self):
        """Gets the dfs_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The dfs recurrece count  # noqa: E501

        :return: The dfs_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._dfs_count

    @dfs_count.setter
    def dfs_count(self, dfs_count):
        """Sets the dfs_count of this XiqAnomaliesCountVoEntity.

        The dfs recurrece count  # noqa: E501

        :param dfs_count: The dfs_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._dfs_count = dfs_count

    @property
    def mb_cast_count(self):
        """Gets the mb_cast_count of this XiqAnomaliesCountVoEntity.  # noqa: E501

        The multibroadcast count  # noqa: E501

        :return: The mb_cast_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :rtype: int
        """
        return self._mb_cast_count

    @mb_cast_count.setter
    def mb_cast_count(self, mb_cast_count):
        """Sets the mb_cast_count of this XiqAnomaliesCountVoEntity.

        The multibroadcast count  # noqa: E501

        :param mb_cast_count: The mb_cast_count of this XiqAnomaliesCountVoEntity.  # noqa: E501
        :type: int
        """

        self._mb_cast_count = mb_cast_count

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
        if not isinstance(other, XiqAnomaliesCountVoEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomaliesCountVoEntity):
            return True

        return self.to_dict() != other.to_dict()
