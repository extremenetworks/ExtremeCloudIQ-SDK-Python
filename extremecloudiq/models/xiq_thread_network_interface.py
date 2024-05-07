# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqThreadNetworkInterface(object):
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
        'interface_name': 'str',
        'is_active': 'bool',
        'is_broadcast': 'bool',
        'is_loopback': 'bool',
        'is_point_to_point': 'bool',
        'is_running': 'bool',
        'is_arp': 'bool',
        'is_promisc': 'bool',
        'is_all_multi': 'bool',
        'is_multicast': 'bool',
        'is_dynamic': 'bool',
        'mtu': 'int',
        'hw_mac_address': 'str',
        'ipv4': 'str',
        'ipv4_mask': 'str',
        'ipv4_broadcast': 'str',
        'ipv6_settings': 'list[XiqThreadIpv6Setting]'
    }

    attribute_map = {
        'interface_name': 'interface_name',
        'is_active': 'is_active',
        'is_broadcast': 'is_broadcast',
        'is_loopback': 'is_loopback',
        'is_point_to_point': 'is_point_to_point',
        'is_running': 'is_running',
        'is_arp': 'is_arp',
        'is_promisc': 'is_promisc',
        'is_all_multi': 'is_all_multi',
        'is_multicast': 'is_multicast',
        'is_dynamic': 'is_dynamic',
        'mtu': 'mtu',
        'hw_mac_address': 'hw_mac_address',
        'ipv4': 'ipv4',
        'ipv4_mask': 'ipv4_mask',
        'ipv4_broadcast': 'ipv4_broadcast',
        'ipv6_settings': 'ipv6_settings'
    }

    def __init__(self, interface_name=None, is_active=None, is_broadcast=None, is_loopback=None, is_point_to_point=None, is_running=None, is_arp=None, is_promisc=None, is_all_multi=None, is_multicast=None, is_dynamic=None, mtu=None, hw_mac_address=None, ipv4=None, ipv4_mask=None, ipv4_broadcast=None, ipv6_settings=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadNetworkInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._interface_name = None
        self._is_active = None
        self._is_broadcast = None
        self._is_loopback = None
        self._is_point_to_point = None
        self._is_running = None
        self._is_arp = None
        self._is_promisc = None
        self._is_all_multi = None
        self._is_multicast = None
        self._is_dynamic = None
        self._mtu = None
        self._hw_mac_address = None
        self._ipv4 = None
        self._ipv4_mask = None
        self._ipv4_broadcast = None
        self._ipv6_settings = None
        self.discriminator = None

        if interface_name is not None:
            self.interface_name = interface_name
        if is_active is not None:
            self.is_active = is_active
        if is_broadcast is not None:
            self.is_broadcast = is_broadcast
        if is_loopback is not None:
            self.is_loopback = is_loopback
        if is_point_to_point is not None:
            self.is_point_to_point = is_point_to_point
        if is_running is not None:
            self.is_running = is_running
        if is_arp is not None:
            self.is_arp = is_arp
        if is_promisc is not None:
            self.is_promisc = is_promisc
        if is_all_multi is not None:
            self.is_all_multi = is_all_multi
        if is_multicast is not None:
            self.is_multicast = is_multicast
        if is_dynamic is not None:
            self.is_dynamic = is_dynamic
        if mtu is not None:
            self.mtu = mtu
        if hw_mac_address is not None:
            self.hw_mac_address = hw_mac_address
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv4_mask is not None:
            self.ipv4_mask = ipv4_mask
        if ipv4_broadcast is not None:
            self.ipv4_broadcast = ipv4_broadcast
        if ipv6_settings is not None:
            self.ipv6_settings = ipv6_settings

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The interface_name of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqThreadNetworkInterface.


        :param interface_name: The interface_name of this XiqThreadNetworkInterface.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def is_active(self):
        """Gets the is_active of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_active of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this XiqThreadNetworkInterface.


        :param is_active: The is_active of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_broadcast(self):
        """Gets the is_broadcast of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_broadcast of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_broadcast

    @is_broadcast.setter
    def is_broadcast(self, is_broadcast):
        """Sets the is_broadcast of this XiqThreadNetworkInterface.


        :param is_broadcast: The is_broadcast of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_broadcast = is_broadcast

    @property
    def is_loopback(self):
        """Gets the is_loopback of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_loopback of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_loopback

    @is_loopback.setter
    def is_loopback(self, is_loopback):
        """Sets the is_loopback of this XiqThreadNetworkInterface.


        :param is_loopback: The is_loopback of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_loopback = is_loopback

    @property
    def is_point_to_point(self):
        """Gets the is_point_to_point of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_point_to_point of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_point_to_point

    @is_point_to_point.setter
    def is_point_to_point(self, is_point_to_point):
        """Sets the is_point_to_point of this XiqThreadNetworkInterface.


        :param is_point_to_point: The is_point_to_point of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_point_to_point = is_point_to_point

    @property
    def is_running(self):
        """Gets the is_running of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_running of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_running

    @is_running.setter
    def is_running(self, is_running):
        """Sets the is_running of this XiqThreadNetworkInterface.


        :param is_running: The is_running of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_running = is_running

    @property
    def is_arp(self):
        """Gets the is_arp of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_arp of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_arp

    @is_arp.setter
    def is_arp(self, is_arp):
        """Sets the is_arp of this XiqThreadNetworkInterface.


        :param is_arp: The is_arp of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_arp = is_arp

    @property
    def is_promisc(self):
        """Gets the is_promisc of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_promisc of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_promisc

    @is_promisc.setter
    def is_promisc(self, is_promisc):
        """Sets the is_promisc of this XiqThreadNetworkInterface.


        :param is_promisc: The is_promisc of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_promisc = is_promisc

    @property
    def is_all_multi(self):
        """Gets the is_all_multi of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_all_multi of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_all_multi

    @is_all_multi.setter
    def is_all_multi(self, is_all_multi):
        """Sets the is_all_multi of this XiqThreadNetworkInterface.


        :param is_all_multi: The is_all_multi of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_all_multi = is_all_multi

    @property
    def is_multicast(self):
        """Gets the is_multicast of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_multicast of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_multicast

    @is_multicast.setter
    def is_multicast(self, is_multicast):
        """Sets the is_multicast of this XiqThreadNetworkInterface.


        :param is_multicast: The is_multicast of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_multicast = is_multicast

    @property
    def is_dynamic(self):
        """Gets the is_dynamic of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The is_dynamic of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        """Sets the is_dynamic of this XiqThreadNetworkInterface.


        :param is_dynamic: The is_dynamic of this XiqThreadNetworkInterface.  # noqa: E501
        :type: bool
        """

        self._is_dynamic = is_dynamic

    @property
    def mtu(self):
        """Gets the mtu of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The mtu of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this XiqThreadNetworkInterface.


        :param mtu: The mtu of this XiqThreadNetworkInterface.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def hw_mac_address(self):
        """Gets the hw_mac_address of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The hw_mac_address of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._hw_mac_address

    @hw_mac_address.setter
    def hw_mac_address(self, hw_mac_address):
        """Sets the hw_mac_address of this XiqThreadNetworkInterface.


        :param hw_mac_address: The hw_mac_address of this XiqThreadNetworkInterface.  # noqa: E501
        :type: str
        """

        self._hw_mac_address = hw_mac_address

    @property
    def ipv4(self):
        """Gets the ipv4 of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The ipv4 of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this XiqThreadNetworkInterface.


        :param ipv4: The ipv4 of this XiqThreadNetworkInterface.  # noqa: E501
        :type: str
        """

        self._ipv4 = ipv4

    @property
    def ipv4_mask(self):
        """Gets the ipv4_mask of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The ipv4_mask of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_mask

    @ipv4_mask.setter
    def ipv4_mask(self, ipv4_mask):
        """Sets the ipv4_mask of this XiqThreadNetworkInterface.


        :param ipv4_mask: The ipv4_mask of this XiqThreadNetworkInterface.  # noqa: E501
        :type: str
        """

        self._ipv4_mask = ipv4_mask

    @property
    def ipv4_broadcast(self):
        """Gets the ipv4_broadcast of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The ipv4_broadcast of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_broadcast

    @ipv4_broadcast.setter
    def ipv4_broadcast(self, ipv4_broadcast):
        """Sets the ipv4_broadcast of this XiqThreadNetworkInterface.


        :param ipv4_broadcast: The ipv4_broadcast of this XiqThreadNetworkInterface.  # noqa: E501
        :type: str
        """

        self._ipv4_broadcast = ipv4_broadcast

    @property
    def ipv6_settings(self):
        """Gets the ipv6_settings of this XiqThreadNetworkInterface.  # noqa: E501


        :return: The ipv6_settings of this XiqThreadNetworkInterface.  # noqa: E501
        :rtype: list[XiqThreadIpv6Setting]
        """
        return self._ipv6_settings

    @ipv6_settings.setter
    def ipv6_settings(self, ipv6_settings):
        """Sets the ipv6_settings of this XiqThreadNetworkInterface.


        :param ipv6_settings: The ipv6_settings of this XiqThreadNetworkInterface.  # noqa: E501
        :type: list[XiqThreadIpv6Setting]
        """

        self._ipv6_settings = ipv6_settings

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
        if not isinstance(other, XiqThreadNetworkInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadNetworkInterface):
            return True

        return self.to_dict() != other.to_dict()
