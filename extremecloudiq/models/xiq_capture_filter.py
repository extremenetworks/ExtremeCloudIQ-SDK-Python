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


class XiqCaptureFilter(object):
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
        'mac_addr': 'list[str]',
        'ip_addr': 'list[str]',
        'protocol': 'XiqPolicyRuleProtocolType',
        'protocol_number': 'int',
        'port': 'int',
        'vlan': 'str',
        'wlan': 'str'
    }

    attribute_map = {
        'mac_addr': 'mac_addr',
        'ip_addr': 'ip_addr',
        'protocol': 'protocol',
        'protocol_number': 'protocol_number',
        'port': 'port',
        'vlan': 'vlan',
        'wlan': 'wlan'
    }

    def __init__(self, mac_addr=None, ip_addr=None, protocol=None, protocol_number=None, port=None, vlan=None, wlan=None, local_vars_configuration=None):  # noqa: E501
        """XiqCaptureFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mac_addr = None
        self._ip_addr = None
        self._protocol = None
        self._protocol_number = None
        self._port = None
        self._vlan = None
        self._wlan = None
        self.discriminator = None

        if mac_addr is not None:
            self.mac_addr = mac_addr
        if ip_addr is not None:
            self.ip_addr = ip_addr
        if protocol is not None:
            self.protocol = protocol
        if protocol_number is not None:
            self.protocol_number = protocol_number
        if port is not None:
            self.port = port
        if vlan is not None:
            self.vlan = vlan
        if wlan is not None:
            self.wlan = wlan

    @property
    def mac_addr(self):
        """Gets the mac_addr of this XiqCaptureFilter.  # noqa: E501

        List of the client MAC addresses used for packet capturing  # noqa: E501

        :return: The mac_addr of this XiqCaptureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        """Sets the mac_addr of this XiqCaptureFilter.

        List of the client MAC addresses used for packet capturing  # noqa: E501

        :param mac_addr: The mac_addr of this XiqCaptureFilter.  # noqa: E501
        :type: list[str]
        """

        self._mac_addr = mac_addr

    @property
    def ip_addr(self):
        """Gets the ip_addr of this XiqCaptureFilter.  # noqa: E501

        List of  the client IP addresses used to filter the packets  # noqa: E501

        :return: The ip_addr of this XiqCaptureFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        """Sets the ip_addr of this XiqCaptureFilter.

        List of  the client IP addresses used to filter the packets  # noqa: E501

        :param ip_addr: The ip_addr of this XiqCaptureFilter.  # noqa: E501
        :type: list[str]
        """

        self._ip_addr = ip_addr

    @property
    def protocol(self):
        """Gets the protocol of this XiqCaptureFilter.  # noqa: E501


        :return: The protocol of this XiqCaptureFilter.  # noqa: E501
        :rtype: XiqPolicyRuleProtocolType
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this XiqCaptureFilter.


        :param protocol: The protocol of this XiqCaptureFilter.  # noqa: E501
        :type: XiqPolicyRuleProtocolType
        """

        self._protocol = protocol

    @property
    def protocol_number(self):
        """Gets the protocol_number of this XiqCaptureFilter.  # noqa: E501

        The protocol number if protocol is \"USER_DEFINED\"  # noqa: E501

        :return: The protocol_number of this XiqCaptureFilter.  # noqa: E501
        :rtype: int
        """
        return self._protocol_number

    @protocol_number.setter
    def protocol_number(self, protocol_number):
        """Sets the protocol_number of this XiqCaptureFilter.

        The protocol number if protocol is \"USER_DEFINED\"  # noqa: E501

        :param protocol_number: The protocol_number of this XiqCaptureFilter.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                protocol_number is not None and protocol_number > 255):  # noqa: E501
            raise ValueError("Invalid value for `protocol_number`, must be a value less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                protocol_number is not None and protocol_number < 0):  # noqa: E501
            raise ValueError("Invalid value for `protocol_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._protocol_number = protocol_number

    @property
    def port(self):
        """Gets the port of this XiqCaptureFilter.  # noqa: E501

        The port for packet capture  # noqa: E501

        :return: The port of this XiqCaptureFilter.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this XiqCaptureFilter.

        The port for packet capture  # noqa: E501

        :param port: The port of this XiqCaptureFilter.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def vlan(self):
        """Gets the vlan of this XiqCaptureFilter.  # noqa: E501

        Specific vlan ids in a string, e.g. range \"2-100\"; single \"3\"; list \"1,2,5,7,122\"; mixed \"2,4,5-10,19,29\". If not specified, default is all VLANs.  # noqa: E501

        :return: The vlan of this XiqCaptureFilter.  # noqa: E501
        :rtype: str
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this XiqCaptureFilter.

        Specific vlan ids in a string, e.g. range \"2-100\"; single \"3\"; list \"1,2,5,7,122\"; mixed \"2,4,5-10,19,29\". If not specified, default is all VLANs.  # noqa: E501

        :param vlan: The vlan of this XiqCaptureFilter.  # noqa: E501
        :type: str
        """

        self._vlan = vlan

    @property
    def wlan(self):
        """Gets the wlan of this XiqCaptureFilter.  # noqa: E501

        A WLAN SSID. If not specified, default is all WLANs.  # noqa: E501

        :return: The wlan of this XiqCaptureFilter.  # noqa: E501
        :rtype: str
        """
        return self._wlan

    @wlan.setter
    def wlan(self, wlan):
        """Sets the wlan of this XiqCaptureFilter.

        A WLAN SSID. If not specified, default is all WLANs.  # noqa: E501

        :param wlan: The wlan of this XiqCaptureFilter.  # noqa: E501
        :type: str
        """

        self._wlan = wlan

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
        if not isinstance(other, XiqCaptureFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCaptureFilter):
            return True

        return self.to_dict() != other.to_dict()
