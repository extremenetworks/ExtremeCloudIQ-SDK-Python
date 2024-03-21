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


class XiqWirelessPerformanceRetriesEntity(object):
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
        'rx_retry': 'float',
        'tx_retry': 'float',
        'above_retry_threshold': 'float'
    }

    attribute_map = {
        'rx_retry': 'rx_retry',
        'tx_retry': 'tx_retry',
        'above_retry_threshold': 'above_retry_threshold'
    }

    def __init__(self, rx_retry=None, tx_retry=None, above_retry_threshold=None, local_vars_configuration=None):  # noqa: E501
        """XiqWirelessPerformanceRetriesEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rx_retry = None
        self._tx_retry = None
        self._above_retry_threshold = None
        self.discriminator = None

        if rx_retry is not None:
            self.rx_retry = rx_retry
        if tx_retry is not None:
            self.tx_retry = tx_retry
        if above_retry_threshold is not None:
            self.above_retry_threshold = above_retry_threshold

    @property
    def rx_retry(self):
        """Gets the rx_retry of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501

        The rx retries  # noqa: E501

        :return: The rx_retry of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._rx_retry

    @rx_retry.setter
    def rx_retry(self, rx_retry):
        """Sets the rx_retry of this XiqWirelessPerformanceRetriesEntity.

        The rx retries  # noqa: E501

        :param rx_retry: The rx_retry of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501
        :type: float
        """

        self._rx_retry = rx_retry

    @property
    def tx_retry(self):
        """Gets the tx_retry of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501

        The tx retries  # noqa: E501

        :return: The tx_retry of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._tx_retry

    @tx_retry.setter
    def tx_retry(self, tx_retry):
        """Sets the tx_retry of this XiqWirelessPerformanceRetriesEntity.

        The tx retries  # noqa: E501

        :param tx_retry: The tx_retry of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501
        :type: float
        """

        self._tx_retry = tx_retry

    @property
    def above_retry_threshold(self):
        """Gets the above_retry_threshold of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501

        The above retry threshold  # noqa: E501

        :return: The above_retry_threshold of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._above_retry_threshold

    @above_retry_threshold.setter
    def above_retry_threshold(self, above_retry_threshold):
        """Sets the above_retry_threshold of this XiqWirelessPerformanceRetriesEntity.

        The above retry threshold  # noqa: E501

        :param above_retry_threshold: The above_retry_threshold of this XiqWirelessPerformanceRetriesEntity.  # noqa: E501
        :type: float
        """

        self._above_retry_threshold = above_retry_threshold

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
        if not isinstance(other, XiqWirelessPerformanceRetriesEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWirelessPerformanceRetriesEntity):
            return True

        return self.to_dict() != other.to_dict()
