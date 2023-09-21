# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCopilotWirelessEvent(object):
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
        'average_value': 'float',
        'maximum_value': 'float',
        'mac': 'str',
        'os_type': 'str',
        'threshold': 'float',
        'hostname': 'str',
        'ssid': 'str',
        'client_id': 'str',
        'retries_data': 'XiqWirelessEventRetriesEntity'
    }

    attribute_map = {
        'average_value': 'average_value',
        'maximum_value': 'maximum_value',
        'mac': 'mac',
        'os_type': 'os_type',
        'threshold': 'threshold',
        'hostname': 'hostname',
        'ssid': 'ssid',
        'client_id': 'client_id',
        'retries_data': 'retries_data'
    }

    def __init__(self, average_value=None, maximum_value=None, mac=None, os_type=None, threshold=None, hostname=None, ssid=None, client_id=None, retries_data=None, local_vars_configuration=None):  # noqa: E501
        """XiqCopilotWirelessEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._average_value = None
        self._maximum_value = None
        self._mac = None
        self._os_type = None
        self._threshold = None
        self._hostname = None
        self._ssid = None
        self._client_id = None
        self._retries_data = None
        self.discriminator = None

        if average_value is not None:
            self.average_value = average_value
        if maximum_value is not None:
            self.maximum_value = maximum_value
        self.mac = mac
        if os_type is not None:
            self.os_type = os_type
        if threshold is not None:
            self.threshold = threshold
        if hostname is not None:
            self.hostname = hostname
        if ssid is not None:
            self.ssid = ssid
        self.client_id = client_id
        if retries_data is not None:
            self.retries_data = retries_data

    @property
    def average_value(self):
        """Gets the average_value of this XiqCopilotWirelessEvent.  # noqa: E501

        The average duration to associate/authenticate  # noqa: E501

        :return: The average_value of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: float
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value):
        """Sets the average_value of this XiqCopilotWirelessEvent.

        The average duration to associate/authenticate  # noqa: E501

        :param average_value: The average_value of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: float
        """

        self._average_value = average_value

    @property
    def maximum_value(self):
        """Gets the maximum_value of this XiqCopilotWirelessEvent.  # noqa: E501

        The maximum duration to associate/authenticate  # noqa: E501

        :return: The maximum_value of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: float
        """
        return self._maximum_value

    @maximum_value.setter
    def maximum_value(self, maximum_value):
        """Sets the maximum_value of this XiqCopilotWirelessEvent.

        The maximum duration to associate/authenticate  # noqa: E501

        :param maximum_value: The maximum_value of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: float
        """

        self._maximum_value = maximum_value

    @property
    def mac(self):
        """Gets the mac of this XiqCopilotWirelessEvent.  # noqa: E501

        The mac address  # noqa: E501

        :return: The mac of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this XiqCopilotWirelessEvent.

        The mac address  # noqa: E501

        :param mac: The mac of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mac is None:  # noqa: E501
            raise ValueError("Invalid value for `mac`, must not be `None`")  # noqa: E501

        self._mac = mac

    @property
    def os_type(self):
        """Gets the os_type of this XiqCopilotWirelessEvent.  # noqa: E501

        The os type  # noqa: E501

        :return: The os_type of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this XiqCopilotWirelessEvent.

        The os type  # noqa: E501

        :param os_type: The os_type of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def threshold(self):
        """Gets the threshold of this XiqCopilotWirelessEvent.  # noqa: E501

        The threshold for association/authentication  # noqa: E501

        :return: The threshold of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this XiqCopilotWirelessEvent.

        The threshold for association/authentication  # noqa: E501

        :param threshold: The threshold of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def hostname(self):
        """Gets the hostname of this XiqCopilotWirelessEvent.  # noqa: E501

        The hostname  # noqa: E501

        :return: The hostname of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this XiqCopilotWirelessEvent.

        The hostname  # noqa: E501

        :param hostname: The hostname of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ssid(self):
        """Gets the ssid of this XiqCopilotWirelessEvent.  # noqa: E501

        The SSID  # noqa: E501

        :return: The ssid of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this XiqCopilotWirelessEvent.

        The SSID  # noqa: E501

        :param ssid: The ssid of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def client_id(self):
        """Gets the client_id of this XiqCopilotWirelessEvent.  # noqa: E501

        The unique identifier for clients  # noqa: E501

        :return: The client_id of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this XiqCopilotWirelessEvent.

        The unique identifier for clients  # noqa: E501

        :param client_id: The client_id of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def retries_data(self):
        """Gets the retries_data of this XiqCopilotWirelessEvent.  # noqa: E501


        :return: The retries_data of this XiqCopilotWirelessEvent.  # noqa: E501
        :rtype: XiqWirelessEventRetriesEntity
        """
        return self._retries_data

    @retries_data.setter
    def retries_data(self, retries_data):
        """Sets the retries_data of this XiqCopilotWirelessEvent.


        :param retries_data: The retries_data of this XiqCopilotWirelessEvent.  # noqa: E501
        :type: XiqWirelessEventRetriesEntity
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
        if not isinstance(other, XiqCopilotWirelessEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCopilotWirelessEvent):
            return True

        return self.to_dict() != other.to_dict()
