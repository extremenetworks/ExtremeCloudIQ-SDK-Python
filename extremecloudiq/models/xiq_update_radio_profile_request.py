# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateRadioProfileRequest(object):
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
        'description': 'str',
        'transmission_power': 'int',
        'max_transmit_power': 'int',
        'transmission_power_floor': 'int',
        'transmission_power_max_drop': 'int',
        'max_clients': 'int',
        'enable_client_transmission_power': 'bool',
        'client_transmission_power': 'int',
        'radio_mode': 'XiqRadioMode',
        'enable_ofdma': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'transmission_power': 'transmission_power',
        'max_transmit_power': 'max_transmit_power',
        'transmission_power_floor': 'transmission_power_floor',
        'transmission_power_max_drop': 'transmission_power_max_drop',
        'max_clients': 'max_clients',
        'enable_client_transmission_power': 'enable_client_transmission_power',
        'client_transmission_power': 'client_transmission_power',
        'radio_mode': 'radio_mode',
        'enable_ofdma': 'enable_ofdma'
    }

    def __init__(self, name=None, description=None, transmission_power=None, max_transmit_power=None, transmission_power_floor=None, transmission_power_max_drop=None, max_clients=None, enable_client_transmission_power=None, client_transmission_power=None, radio_mode=None, enable_ofdma=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateRadioProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._transmission_power = None
        self._max_transmit_power = None
        self._transmission_power_floor = None
        self._transmission_power_max_drop = None
        self._max_clients = None
        self._enable_client_transmission_power = None
        self._client_transmission_power = None
        self._radio_mode = None
        self._enable_ofdma = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if transmission_power is not None:
            self.transmission_power = transmission_power
        if max_transmit_power is not None:
            self.max_transmit_power = max_transmit_power
        if transmission_power_floor is not None:
            self.transmission_power_floor = transmission_power_floor
        if transmission_power_max_drop is not None:
            self.transmission_power_max_drop = transmission_power_max_drop
        if max_clients is not None:
            self.max_clients = max_clients
        if enable_client_transmission_power is not None:
            self.enable_client_transmission_power = enable_client_transmission_power
        if client_transmission_power is not None:
            self.client_transmission_power = client_transmission_power
        if radio_mode is not None:
            self.radio_mode = radio_mode
        if enable_ofdma is not None:
            self.enable_ofdma = enable_ofdma

    @property
    def name(self):
        """Gets the name of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The radio profile name  # noqa: E501

        :return: The name of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateRadioProfileRequest.

        The radio profile name  # noqa: E501

        :param name: The name of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The radio profile description.  # noqa: E501

        :return: The description of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateRadioProfileRequest.

        The radio profile description.  # noqa: E501

        :param description: The description of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def transmission_power(self):
        """Gets the transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The transmission power floor in the range of 1-20 dBm or null for Auto.  # noqa: E501

        :return: The transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._transmission_power

    @transmission_power.setter
    def transmission_power(self, transmission_power):
        """Sets the transmission_power of this XiqUpdateRadioProfileRequest.

        The transmission power floor in the range of 1-20 dBm or null for Auto.  # noqa: E501

        :param transmission_power: The transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                transmission_power is not None and transmission_power > 20):  # noqa: E501
            raise ValueError("Invalid value for `transmission_power`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmission_power is not None and transmission_power < 1):  # noqa: E501
            raise ValueError("Invalid value for `transmission_power`, must be a value greater than or equal to `1`")  # noqa: E501

        self._transmission_power = transmission_power

    @property
    def max_transmit_power(self):
        """Gets the max_transmit_power of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The maximum transmit power in the range of 10-20 dBm.  # noqa: E501

        :return: The max_transmit_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_transmit_power

    @max_transmit_power.setter
    def max_transmit_power(self, max_transmit_power):
        """Sets the max_transmit_power of this XiqUpdateRadioProfileRequest.

        The maximum transmit power in the range of 10-20 dBm.  # noqa: E501

        :param max_transmit_power: The max_transmit_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_transmit_power is not None and max_transmit_power > 20):  # noqa: E501
            raise ValueError("Invalid value for `max_transmit_power`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_transmit_power is not None and max_transmit_power < 10):  # noqa: E501
            raise ValueError("Invalid value for `max_transmit_power`, must be a value greater than or equal to `10`")  # noqa: E501

        self._max_transmit_power = max_transmit_power

    @property
    def transmission_power_floor(self):
        """Gets the transmission_power_floor of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The transmission power floor in the range of 2-20 dBm.  # noqa: E501

        :return: The transmission_power_floor of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._transmission_power_floor

    @transmission_power_floor.setter
    def transmission_power_floor(self, transmission_power_floor):
        """Sets the transmission_power_floor of this XiqUpdateRadioProfileRequest.

        The transmission power floor in the range of 2-20 dBm.  # noqa: E501

        :param transmission_power_floor: The transmission_power_floor of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                transmission_power_floor is not None and transmission_power_floor > 20):  # noqa: E501
            raise ValueError("Invalid value for `transmission_power_floor`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmission_power_floor is not None and transmission_power_floor < 2):  # noqa: E501
            raise ValueError("Invalid value for `transmission_power_floor`, must be a value greater than or equal to `2`")  # noqa: E501

        self._transmission_power_floor = transmission_power_floor

    @property
    def transmission_power_max_drop(self):
        """Gets the transmission_power_max_drop of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The transmission power max drop in the range of 0-18 dB.  # noqa: E501

        :return: The transmission_power_max_drop of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._transmission_power_max_drop

    @transmission_power_max_drop.setter
    def transmission_power_max_drop(self, transmission_power_max_drop):
        """Sets the transmission_power_max_drop of this XiqUpdateRadioProfileRequest.

        The transmission power max drop in the range of 0-18 dB.  # noqa: E501

        :param transmission_power_max_drop: The transmission_power_max_drop of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                transmission_power_max_drop is not None and transmission_power_max_drop > 18):  # noqa: E501
            raise ValueError("Invalid value for `transmission_power_max_drop`, must be a value less than or equal to `18`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transmission_power_max_drop is not None and transmission_power_max_drop < 0):  # noqa: E501
            raise ValueError("Invalid value for `transmission_power_max_drop`, must be a value greater than or equal to `0`")  # noqa: E501

        self._transmission_power_max_drop = transmission_power_max_drop

    @property
    def max_clients(self):
        """Gets the max_clients of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The maximum number of clients in the range of 1-255.  # noqa: E501

        :return: The max_clients of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_clients

    @max_clients.setter
    def max_clients(self, max_clients):
        """Sets the max_clients of this XiqUpdateRadioProfileRequest.

        The maximum number of clients in the range of 1-255.  # noqa: E501

        :param max_clients: The max_clients of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_clients is not None and max_clients > 255):  # noqa: E501
            raise ValueError("Invalid value for `max_clients`, must be a value less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_clients is not None and max_clients < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_clients`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_clients = max_clients

    @property
    def enable_client_transmission_power(self):
        """Gets the enable_client_transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501

        Whether or not client transmission power control (802.11h) is enabled.  # noqa: E501

        :return: The enable_client_transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_client_transmission_power

    @enable_client_transmission_power.setter
    def enable_client_transmission_power(self, enable_client_transmission_power):
        """Sets the enable_client_transmission_power of this XiqUpdateRadioProfileRequest.

        Whether or not client transmission power control (802.11h) is enabled.  # noqa: E501

        :param enable_client_transmission_power: The enable_client_transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: bool
        """

        self._enable_client_transmission_power = enable_client_transmission_power

    @property
    def client_transmission_power(self):
        """Gets the client_transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501

        The client transmission power (in the range of 1-20 dBm) if it is enabled.  # noqa: E501

        :return: The client_transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_transmission_power

    @client_transmission_power.setter
    def client_transmission_power(self, client_transmission_power):
        """Sets the client_transmission_power of this XiqUpdateRadioProfileRequest.

        The client transmission power (in the range of 1-20 dBm) if it is enabled.  # noqa: E501

        :param client_transmission_power: The client_transmission_power of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                client_transmission_power is not None and client_transmission_power > 20):  # noqa: E501
            raise ValueError("Invalid value for `client_transmission_power`, must be a value less than or equal to `20`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_transmission_power is not None and client_transmission_power < 1):  # noqa: E501
            raise ValueError("Invalid value for `client_transmission_power`, must be a value greater than or equal to `1`")  # noqa: E501

        self._client_transmission_power = client_transmission_power

    @property
    def radio_mode(self):
        """Gets the radio_mode of this XiqUpdateRadioProfileRequest.  # noqa: E501


        :return: The radio_mode of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: XiqRadioMode
        """
        return self._radio_mode

    @radio_mode.setter
    def radio_mode(self, radio_mode):
        """Sets the radio_mode of this XiqUpdateRadioProfileRequest.


        :param radio_mode: The radio_mode of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: XiqRadioMode
        """

        self._radio_mode = radio_mode

    @property
    def enable_ofdma(self):
        """Gets the enable_ofdma of this XiqUpdateRadioProfileRequest.  # noqa: E501

        Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel.  # noqa: E501

        :return: The enable_ofdma of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ofdma

    @enable_ofdma.setter
    def enable_ofdma(self, enable_ofdma):
        """Sets the enable_ofdma of this XiqUpdateRadioProfileRequest.

        Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel.  # noqa: E501

        :param enable_ofdma: The enable_ofdma of this XiqUpdateRadioProfileRequest.  # noqa: E501
        :type: bool
        """

        self._enable_ofdma = enable_ofdma

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
        if not isinstance(other, XiqUpdateRadioProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateRadioProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
