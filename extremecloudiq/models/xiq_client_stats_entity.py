# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqClientStatsEntity(object):
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
        'client_mac': 'str',
        'client_name': 'str',
        'client_host_os': 'str',
        'avg_snr': 'int',
        'avg_tx_rate': 'int',
        'avg_rx_rate': 'int',
        'client_id': 'int',
        'avg_rssi': 'int',
        'health_score': 'XiqAnomalyHealthType'
    }

    attribute_map = {
        'client_mac': 'client_mac',
        'client_name': 'client_name',
        'client_host_os': 'client_host_os',
        'avg_snr': 'avg_snr',
        'avg_tx_rate': 'avg_tx_rate',
        'avg_rx_rate': 'avg_rx_rate',
        'client_id': 'client_id',
        'avg_rssi': 'avg_rssi',
        'health_score': 'health_score'
    }

    def __init__(self, client_mac=None, client_name=None, client_host_os=None, avg_snr=None, avg_tx_rate=None, avg_rx_rate=None, client_id=None, avg_rssi=None, health_score=None, local_vars_configuration=None):  # noqa: E501
        """XiqClientStatsEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_mac = None
        self._client_name = None
        self._client_host_os = None
        self._avg_snr = None
        self._avg_tx_rate = None
        self._avg_rx_rate = None
        self._client_id = None
        self._avg_rssi = None
        self._health_score = None
        self.discriminator = None

        if client_mac is not None:
            self.client_mac = client_mac
        if client_name is not None:
            self.client_name = client_name
        if client_host_os is not None:
            self.client_host_os = client_host_os
        if avg_snr is not None:
            self.avg_snr = avg_snr
        if avg_tx_rate is not None:
            self.avg_tx_rate = avg_tx_rate
        if avg_rx_rate is not None:
            self.avg_rx_rate = avg_rx_rate
        if client_id is not None:
            self.client_id = client_id
        if avg_rssi is not None:
            self.avg_rssi = avg_rssi
        if health_score is not None:
            self.health_score = health_score

    @property
    def client_mac(self):
        """Gets the client_mac of this XiqClientStatsEntity.  # noqa: E501

        The client mac  # noqa: E501

        :return: The client_mac of this XiqClientStatsEntity.  # noqa: E501
        :rtype: str
        """
        return self._client_mac

    @client_mac.setter
    def client_mac(self, client_mac):
        """Sets the client_mac of this XiqClientStatsEntity.

        The client mac  # noqa: E501

        :param client_mac: The client_mac of this XiqClientStatsEntity.  # noqa: E501
        :type: str
        """

        self._client_mac = client_mac

    @property
    def client_name(self):
        """Gets the client_name of this XiqClientStatsEntity.  # noqa: E501

        The client name  # noqa: E501

        :return: The client_name of this XiqClientStatsEntity.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this XiqClientStatsEntity.

        The client name  # noqa: E501

        :param client_name: The client_name of this XiqClientStatsEntity.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def client_host_os(self):
        """Gets the client_host_os of this XiqClientStatsEntity.  # noqa: E501

        The client host os  # noqa: E501

        :return: The client_host_os of this XiqClientStatsEntity.  # noqa: E501
        :rtype: str
        """
        return self._client_host_os

    @client_host_os.setter
    def client_host_os(self, client_host_os):
        """Sets the client_host_os of this XiqClientStatsEntity.

        The client host os  # noqa: E501

        :param client_host_os: The client_host_os of this XiqClientStatsEntity.  # noqa: E501
        :type: str
        """

        self._client_host_os = client_host_os

    @property
    def avg_snr(self):
        """Gets the avg_snr of this XiqClientStatsEntity.  # noqa: E501

        The average SNR  # noqa: E501

        :return: The avg_snr of this XiqClientStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_snr

    @avg_snr.setter
    def avg_snr(self, avg_snr):
        """Sets the avg_snr of this XiqClientStatsEntity.

        The average SNR  # noqa: E501

        :param avg_snr: The avg_snr of this XiqClientStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_snr = avg_snr

    @property
    def avg_tx_rate(self):
        """Gets the avg_tx_rate of this XiqClientStatsEntity.  # noqa: E501

        The average TX rate  # noqa: E501

        :return: The avg_tx_rate of this XiqClientStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_tx_rate

    @avg_tx_rate.setter
    def avg_tx_rate(self, avg_tx_rate):
        """Sets the avg_tx_rate of this XiqClientStatsEntity.

        The average TX rate  # noqa: E501

        :param avg_tx_rate: The avg_tx_rate of this XiqClientStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_tx_rate = avg_tx_rate

    @property
    def avg_rx_rate(self):
        """Gets the avg_rx_rate of this XiqClientStatsEntity.  # noqa: E501

        The average RX rate  # noqa: E501

        :return: The avg_rx_rate of this XiqClientStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_rx_rate

    @avg_rx_rate.setter
    def avg_rx_rate(self, avg_rx_rate):
        """Sets the avg_rx_rate of this XiqClientStatsEntity.

        The average RX rate  # noqa: E501

        :param avg_rx_rate: The avg_rx_rate of this XiqClientStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_rx_rate = avg_rx_rate

    @property
    def client_id(self):
        """Gets the client_id of this XiqClientStatsEntity.  # noqa: E501

        The client id  # noqa: E501

        :return: The client_id of this XiqClientStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this XiqClientStatsEntity.

        The client id  # noqa: E501

        :param client_id: The client_id of this XiqClientStatsEntity.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def avg_rssi(self):
        """Gets the avg_rssi of this XiqClientStatsEntity.  # noqa: E501

         The average RSSI   # noqa: E501

        :return: The avg_rssi of this XiqClientStatsEntity.  # noqa: E501
        :rtype: int
        """
        return self._avg_rssi

    @avg_rssi.setter
    def avg_rssi(self, avg_rssi):
        """Sets the avg_rssi of this XiqClientStatsEntity.

         The average RSSI   # noqa: E501

        :param avg_rssi: The avg_rssi of this XiqClientStatsEntity.  # noqa: E501
        :type: int
        """

        self._avg_rssi = avg_rssi

    @property
    def health_score(self):
        """Gets the health_score of this XiqClientStatsEntity.  # noqa: E501


        :return: The health_score of this XiqClientStatsEntity.  # noqa: E501
        :rtype: XiqAnomalyHealthType
        """
        return self._health_score

    @health_score.setter
    def health_score(self, health_score):
        """Sets the health_score of this XiqClientStatsEntity.


        :param health_score: The health_score of this XiqClientStatsEntity.  # noqa: E501
        :type: XiqAnomalyHealthType
        """

        self._health_score = health_score

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
        if not isinstance(other, XiqClientStatsEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClientStatsEntity):
            return True

        return self.to_dict() != other.to_dict()
