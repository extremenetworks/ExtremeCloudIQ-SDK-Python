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


class XiqRadio(object):
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
        'name': 'str',
        'channel_number': 'int',
        'channel_width': 'str',
        'mode': 'str',
        'mac_address': 'str',
        'power': 'int',
        'clients': 'list[XiqWirelessClient]'
    }

    attribute_map = {
        'name': 'name',
        'channel_number': 'channel_number',
        'channel_width': 'channel_width',
        'mode': 'mode',
        'mac_address': 'mac_address',
        'power': 'power',
        'clients': 'clients'
    }

    def __init__(self, name=None, channel_number=None, channel_width=None, mode=None, mac_address=None, power=None, clients=None, local_vars_configuration=None):  # noqa: E501
        """XiqRadio - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._channel_number = None
        self._channel_width = None
        self._mode = None
        self._mac_address = None
        self._power = None
        self._clients = None
        self.discriminator = None

        self.name = name
        if channel_number is not None:
            self.channel_number = channel_number
        self.channel_width = channel_width
        self.mode = mode
        if mac_address is not None:
            self.mac_address = mac_address
        if power is not None:
            self.power = power
        if clients is not None:
            self.clients = clients

    @property
    def name(self):
        """Gets the name of this XiqRadio.  # noqa: E501

        the radio name  # noqa: E501

        :return: The name of this XiqRadio.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqRadio.

        the radio name  # noqa: E501

        :param name: The name of this XiqRadio.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def channel_number(self):
        """Gets the channel_number of this XiqRadio.  # noqa: E501

        the channel number  # noqa: E501

        :return: The channel_number of this XiqRadio.  # noqa: E501
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this XiqRadio.

        the channel number  # noqa: E501

        :param channel_number: The channel_number of this XiqRadio.  # noqa: E501
        :type: int
        """

        self._channel_number = channel_number

    @property
    def channel_width(self):
        """Gets the channel_width of this XiqRadio.  # noqa: E501

        the channel width  # noqa: E501

        :return: The channel_width of this XiqRadio.  # noqa: E501
        :rtype: str
        """
        return self._channel_width

    @channel_width.setter
    def channel_width(self, channel_width):
        """Sets the channel_width of this XiqRadio.

        the channel width  # noqa: E501

        :param channel_width: The channel_width of this XiqRadio.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and channel_width is None:  # noqa: E501
            raise ValueError("Invalid value for `channel_width`, must not be `None`")  # noqa: E501

        self._channel_width = channel_width

    @property
    def mode(self):
        """Gets the mode of this XiqRadio.  # noqa: E501

        the radio mode  # noqa: E501

        :return: The mode of this XiqRadio.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this XiqRadio.

        the radio mode  # noqa: E501

        :param mode: The mode of this XiqRadio.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mode is None:  # noqa: E501
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqRadio.  # noqa: E501

        the radio MAC address  # noqa: E501

        :return: The mac_address of this XiqRadio.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqRadio.

        the radio MAC address  # noqa: E501

        :param mac_address: The mac_address of this XiqRadio.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def power(self):
        """Gets the power of this XiqRadio.  # noqa: E501

        the radio power  # noqa: E501

        :return: The power of this XiqRadio.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this XiqRadio.

        the radio power  # noqa: E501

        :param power: The power of this XiqRadio.  # noqa: E501
        :type: int
        """

        self._power = power

    @property
    def clients(self):
        """Gets the clients of this XiqRadio.  # noqa: E501

        the clients and SSID details  # noqa: E501

        :return: The clients of this XiqRadio.  # noqa: E501
        :rtype: list[XiqWirelessClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this XiqRadio.

        the clients and SSID details  # noqa: E501

        :param clients: The clients of this XiqRadio.  # noqa: E501
        :type: list[XiqWirelessClient]
        """

        self._clients = clients

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
        if not isinstance(other, XiqRadio):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRadio):
            return True

        return self.to_dict() != other.to_dict()
