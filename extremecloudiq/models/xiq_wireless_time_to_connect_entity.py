# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqWirelessTimeToConnectEntity(object):
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
        'above_assoc_threshold': 'int',
        'above_auth_threshold': 'int',
        'above_dhcp_threshold': 'int',
        'time_to_assoc': 'int',
        'time_to_auth': 'int',
        'time_to_dhcp': 'int',
        'performance_score': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'quality_index': 'quality_index',
        'total_clients': 'total_clients',
        'time_to_connect_score': 'time_to_connect_score',
        'above_assoc_threshold': 'above_assoc_threshold',
        'above_auth_threshold': 'above_auth_threshold',
        'above_dhcp_threshold': 'above_dhcp_threshold',
        'time_to_assoc': 'time_to_assoc',
        'time_to_auth': 'time_to_auth',
        'time_to_dhcp': 'time_to_dhcp',
        'performance_score': 'performance_score'
    }

    def __init__(self, timestamp=None, quality_index=None, total_clients=None, time_to_connect_score=None, above_assoc_threshold=None, above_auth_threshold=None, above_dhcp_threshold=None, time_to_assoc=None, time_to_auth=None, time_to_dhcp=None, performance_score=None, local_vars_configuration=None):  # noqa: E501
        """XiqWirelessTimeToConnectEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._quality_index = None
        self._total_clients = None
        self._time_to_connect_score = None
        self._above_assoc_threshold = None
        self._above_auth_threshold = None
        self._above_dhcp_threshold = None
        self._time_to_assoc = None
        self._time_to_auth = None
        self._time_to_dhcp = None
        self._performance_score = None
        self.discriminator = None

        self.timestamp = timestamp
        if quality_index is not None:
            self.quality_index = quality_index
        if total_clients is not None:
            self.total_clients = total_clients
        if time_to_connect_score is not None:
            self.time_to_connect_score = time_to_connect_score
        if above_assoc_threshold is not None:
            self.above_assoc_threshold = above_assoc_threshold
        if above_auth_threshold is not None:
            self.above_auth_threshold = above_auth_threshold
        if above_dhcp_threshold is not None:
            self.above_dhcp_threshold = above_dhcp_threshold
        if time_to_assoc is not None:
            self.time_to_assoc = time_to_assoc
        if time_to_auth is not None:
            self.time_to_auth = time_to_auth
        if time_to_dhcp is not None:
            self.time_to_dhcp = time_to_dhcp
        if performance_score is not None:
            self.performance_score = performance_score

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The timestamp  # noqa: E501

        :return: The timestamp of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqWirelessTimeToConnectEntity.

        The timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def quality_index(self):
        """Gets the quality_index of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The quality index  # noqa: E501

        :return: The quality_index of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._quality_index

    @quality_index.setter
    def quality_index(self, quality_index):
        """Sets the quality_index of this XiqWirelessTimeToConnectEntity.

        The quality index  # noqa: E501

        :param quality_index: The quality_index of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._quality_index = quality_index

    @property
    def total_clients(self):
        """Gets the total_clients of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The total clients  # noqa: E501

        :return: The total_clients of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._total_clients

    @total_clients.setter
    def total_clients(self, total_clients):
        """Sets the total_clients of this XiqWirelessTimeToConnectEntity.

        The total clients  # noqa: E501

        :param total_clients: The total_clients of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._total_clients = total_clients

    @property
    def time_to_connect_score(self):
        """Gets the time_to_connect_score of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The time to connect score  # noqa: E501

        :return: The time_to_connect_score of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._time_to_connect_score

    @time_to_connect_score.setter
    def time_to_connect_score(self, time_to_connect_score):
        """Sets the time_to_connect_score of this XiqWirelessTimeToConnectEntity.

        The time to connect score  # noqa: E501

        :param time_to_connect_score: The time_to_connect_score of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._time_to_connect_score = time_to_connect_score

    @property
    def above_assoc_threshold(self):
        """Gets the above_assoc_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The above association threshold  # noqa: E501

        :return: The above_assoc_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._above_assoc_threshold

    @above_assoc_threshold.setter
    def above_assoc_threshold(self, above_assoc_threshold):
        """Sets the above_assoc_threshold of this XiqWirelessTimeToConnectEntity.

        The above association threshold  # noqa: E501

        :param above_assoc_threshold: The above_assoc_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._above_assoc_threshold = above_assoc_threshold

    @property
    def above_auth_threshold(self):
        """Gets the above_auth_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The above authentication threshold  # noqa: E501

        :return: The above_auth_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._above_auth_threshold

    @above_auth_threshold.setter
    def above_auth_threshold(self, above_auth_threshold):
        """Sets the above_auth_threshold of this XiqWirelessTimeToConnectEntity.

        The above authentication threshold  # noqa: E501

        :param above_auth_threshold: The above_auth_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._above_auth_threshold = above_auth_threshold

    @property
    def above_dhcp_threshold(self):
        """Gets the above_dhcp_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The above dhcp threshold  # noqa: E501

        :return: The above_dhcp_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._above_dhcp_threshold

    @above_dhcp_threshold.setter
    def above_dhcp_threshold(self, above_dhcp_threshold):
        """Sets the above_dhcp_threshold of this XiqWirelessTimeToConnectEntity.

        The above dhcp threshold  # noqa: E501

        :param above_dhcp_threshold: The above_dhcp_threshold of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._above_dhcp_threshold = above_dhcp_threshold

    @property
    def time_to_assoc(self):
        """Gets the time_to_assoc of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The time to associate  # noqa: E501

        :return: The time_to_assoc of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._time_to_assoc

    @time_to_assoc.setter
    def time_to_assoc(self, time_to_assoc):
        """Sets the time_to_assoc of this XiqWirelessTimeToConnectEntity.

        The time to associate  # noqa: E501

        :param time_to_assoc: The time_to_assoc of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._time_to_assoc = time_to_assoc

    @property
    def time_to_auth(self):
        """Gets the time_to_auth of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The time to authenticate  # noqa: E501

        :return: The time_to_auth of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._time_to_auth

    @time_to_auth.setter
    def time_to_auth(self, time_to_auth):
        """Sets the time_to_auth of this XiqWirelessTimeToConnectEntity.

        The time to authenticate  # noqa: E501

        :param time_to_auth: The time_to_auth of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._time_to_auth = time_to_auth

    @property
    def time_to_dhcp(self):
        """Gets the time_to_dhcp of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The time to dhcp  # noqa: E501

        :return: The time_to_dhcp of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._time_to_dhcp

    @time_to_dhcp.setter
    def time_to_dhcp(self, time_to_dhcp):
        """Sets the time_to_dhcp of this XiqWirelessTimeToConnectEntity.

        The time to dhcp  # noqa: E501

        :param time_to_dhcp: The time_to_dhcp of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._time_to_dhcp = time_to_dhcp

    @property
    def performance_score(self):
        """Gets the performance_score of this XiqWirelessTimeToConnectEntity.  # noqa: E501

        The performance score  # noqa: E501

        :return: The performance_score of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :rtype: int
        """
        return self._performance_score

    @performance_score.setter
    def performance_score(self, performance_score):
        """Sets the performance_score of this XiqWirelessTimeToConnectEntity.

        The performance score  # noqa: E501

        :param performance_score: The performance_score of this XiqWirelessTimeToConnectEntity.  # noqa: E501
        :type: int
        """

        self._performance_score = performance_score

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
        if not isinstance(other, XiqWirelessTimeToConnectEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWirelessTimeToConnectEntity):
            return True

        return self.to_dict() != other.to_dict()
