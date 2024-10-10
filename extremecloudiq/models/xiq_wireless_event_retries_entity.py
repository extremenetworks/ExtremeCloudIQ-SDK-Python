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


class XiqWirelessEventRetriesEntity(object):
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
        'avg_rx_retry': 'float',
        'max_rx_retry': 'float',
        'avg_tx_retry': 'float',
        'max_tx_retry': 'float',
        'rx_retry_threshold': 'float',
        'tx_retry_threshold': 'float'
    }

    attribute_map = {
        'avg_rx_retry': 'avg_rx_retry',
        'max_rx_retry': 'max_rx_retry',
        'avg_tx_retry': 'avg_tx_retry',
        'max_tx_retry': 'max_tx_retry',
        'rx_retry_threshold': 'rx_retry_threshold',
        'tx_retry_threshold': 'tx_retry_threshold'
    }

    def __init__(self, avg_rx_retry=None, max_rx_retry=None, avg_tx_retry=None, max_tx_retry=None, rx_retry_threshold=None, tx_retry_threshold=None, local_vars_configuration=None):  # noqa: E501
        """XiqWirelessEventRetriesEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._avg_rx_retry = None
        self._max_rx_retry = None
        self._avg_tx_retry = None
        self._max_tx_retry = None
        self._rx_retry_threshold = None
        self._tx_retry_threshold = None
        self.discriminator = None

        if avg_rx_retry is not None:
            self.avg_rx_retry = avg_rx_retry
        if max_rx_retry is not None:
            self.max_rx_retry = max_rx_retry
        if avg_tx_retry is not None:
            self.avg_tx_retry = avg_tx_retry
        if max_tx_retry is not None:
            self.max_tx_retry = max_tx_retry
        if rx_retry_threshold is not None:
            self.rx_retry_threshold = rx_retry_threshold
        if tx_retry_threshold is not None:
            self.tx_retry_threshold = tx_retry_threshold

    @property
    def avg_rx_retry(self):
        """Gets the avg_rx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501

        The average duration of rxRetry  # noqa: E501

        :return: The avg_rx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._avg_rx_retry

    @avg_rx_retry.setter
    def avg_rx_retry(self, avg_rx_retry):
        """Sets the avg_rx_retry of this XiqWirelessEventRetriesEntity.

        The average duration of rxRetry  # noqa: E501

        :param avg_rx_retry: The avg_rx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :type: float
        """

        self._avg_rx_retry = avg_rx_retry

    @property
    def max_rx_retry(self):
        """Gets the max_rx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501

        The maximum duration of rxRetry  # noqa: E501

        :return: The max_rx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._max_rx_retry

    @max_rx_retry.setter
    def max_rx_retry(self, max_rx_retry):
        """Sets the max_rx_retry of this XiqWirelessEventRetriesEntity.

        The maximum duration of rxRetry  # noqa: E501

        :param max_rx_retry: The max_rx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :type: float
        """

        self._max_rx_retry = max_rx_retry

    @property
    def avg_tx_retry(self):
        """Gets the avg_tx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501

        The average duration of txRetry  # noqa: E501

        :return: The avg_tx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._avg_tx_retry

    @avg_tx_retry.setter
    def avg_tx_retry(self, avg_tx_retry):
        """Sets the avg_tx_retry of this XiqWirelessEventRetriesEntity.

        The average duration of txRetry  # noqa: E501

        :param avg_tx_retry: The avg_tx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :type: float
        """

        self._avg_tx_retry = avg_tx_retry

    @property
    def max_tx_retry(self):
        """Gets the max_tx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501

        The maximum duration of txRetry  # noqa: E501

        :return: The max_tx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._max_tx_retry

    @max_tx_retry.setter
    def max_tx_retry(self, max_tx_retry):
        """Sets the max_tx_retry of this XiqWirelessEventRetriesEntity.

        The maximum duration of txRetry  # noqa: E501

        :param max_tx_retry: The max_tx_retry of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :type: float
        """

        self._max_tx_retry = max_tx_retry

    @property
    def rx_retry_threshold(self):
        """Gets the rx_retry_threshold of this XiqWirelessEventRetriesEntity.  # noqa: E501

        The threshold value of rxRetry  # noqa: E501

        :return: The rx_retry_threshold of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._rx_retry_threshold

    @rx_retry_threshold.setter
    def rx_retry_threshold(self, rx_retry_threshold):
        """Sets the rx_retry_threshold of this XiqWirelessEventRetriesEntity.

        The threshold value of rxRetry  # noqa: E501

        :param rx_retry_threshold: The rx_retry_threshold of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :type: float
        """

        self._rx_retry_threshold = rx_retry_threshold

    @property
    def tx_retry_threshold(self):
        """Gets the tx_retry_threshold of this XiqWirelessEventRetriesEntity.  # noqa: E501

        The threshold value of txRetry  # noqa: E501

        :return: The tx_retry_threshold of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :rtype: float
        """
        return self._tx_retry_threshold

    @tx_retry_threshold.setter
    def tx_retry_threshold(self, tx_retry_threshold):
        """Sets the tx_retry_threshold of this XiqWirelessEventRetriesEntity.

        The threshold value of txRetry  # noqa: E501

        :param tx_retry_threshold: The tx_retry_threshold of this XiqWirelessEventRetriesEntity.  # noqa: E501
        :type: float
        """

        self._tx_retry_threshold = tx_retry_threshold

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
        if not isinstance(other, XiqWirelessEventRetriesEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWirelessEventRetriesEntity):
            return True

        return self.to_dict() != other.to_dict()
