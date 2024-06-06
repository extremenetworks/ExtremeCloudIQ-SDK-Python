# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceConfigureIpv4InterfaceResponse(object):
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
        'ip_address': 'str',
        'routing_instance': 'str',
        'enable_forwarding': 'bool',
        'enable_vlan_loopback': 'bool',
        'use_ip_addr_as_ospf_router_id': 'bool',
        'override_dhcp_relay': 'bool',
        'enable_dhcp': 'bool',
        'primary_dhcp_server': 'str',
        'secondary_dhcp_server': 'str',
        'predefined': 'bool',
        'subnetwork_id': 'int',
        'ipv4_interface_id': 'int',
        'vlan_attribute': 'XiqDeviceVlanAttributes'
    }

    attribute_map = {
        'ip_address': 'ip_address',
        'routing_instance': 'routing_instance',
        'enable_forwarding': 'enable_forwarding',
        'enable_vlan_loopback': 'enable_vlan_loopback',
        'use_ip_addr_as_ospf_router_id': 'use_ip_addr_as_ospf_router_id',
        'override_dhcp_relay': 'override_dhcp_relay',
        'enable_dhcp': 'enable_dhcp',
        'primary_dhcp_server': 'primary_dhcp_server',
        'secondary_dhcp_server': 'secondary_dhcp_server',
        'predefined': 'predefined',
        'subnetwork_id': 'subnetwork_id',
        'ipv4_interface_id': 'ipv4_interface_id',
        'vlan_attribute': 'vlan_attribute'
    }

    def __init__(self, ip_address=None, routing_instance=None, enable_forwarding=None, enable_vlan_loopback=None, use_ip_addr_as_ospf_router_id=None, override_dhcp_relay=None, enable_dhcp=None, primary_dhcp_server=None, secondary_dhcp_server=None, predefined=None, subnetwork_id=None, ipv4_interface_id=None, vlan_attribute=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceConfigureIpv4InterfaceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip_address = None
        self._routing_instance = None
        self._enable_forwarding = None
        self._enable_vlan_loopback = None
        self._use_ip_addr_as_ospf_router_id = None
        self._override_dhcp_relay = None
        self._enable_dhcp = None
        self._primary_dhcp_server = None
        self._secondary_dhcp_server = None
        self._predefined = None
        self._subnetwork_id = None
        self._ipv4_interface_id = None
        self._vlan_attribute = None
        self.discriminator = None

        self.ip_address = ip_address
        self.routing_instance = routing_instance
        self.enable_forwarding = enable_forwarding
        self.enable_vlan_loopback = enable_vlan_loopback
        self.use_ip_addr_as_ospf_router_id = use_ip_addr_as_ospf_router_id
        self.override_dhcp_relay = override_dhcp_relay
        self.enable_dhcp = enable_dhcp
        self.primary_dhcp_server = primary_dhcp_server
        self.secondary_dhcp_server = secondary_dhcp_server
        self.predefined = predefined
        if subnetwork_id is not None:
            self.subnetwork_id = subnetwork_id
        if ipv4_interface_id is not None:
            self.ipv4_interface_id = ipv4_interface_id
        if vlan_attribute is not None:
            self.vlan_attribute = vlan_attribute

    @property
    def ip_address(self):
        """Gets the ip_address of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        The IPv4 address set on the interface  # noqa: E501

        :return: The ip_address of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this XiqDeviceConfigureIpv4InterfaceResponse.

        The IPv4 address set on the interface  # noqa: E501

        :param ip_address: The ip_address of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ip_address is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def routing_instance(self):
        """Gets the routing_instance of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        The Routing Instance  # noqa: E501

        :return: The routing_instance of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._routing_instance

    @routing_instance.setter
    def routing_instance(self, routing_instance):
        """Sets the routing_instance of this XiqDeviceConfigureIpv4InterfaceResponse.

        The Routing Instance  # noqa: E501

        :param routing_instance: The routing_instance of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and routing_instance is None:  # noqa: E501
            raise ValueError("Invalid value for `routing_instance`, must not be `None`")  # noqa: E501

        self._routing_instance = routing_instance

    @property
    def enable_forwarding(self):
        """Gets the enable_forwarding of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Indicates whether or not IPv4 is forwarding on the VLAN  # noqa: E501

        :return: The enable_forwarding of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enable_forwarding

    @enable_forwarding.setter
    def enable_forwarding(self, enable_forwarding):
        """Sets the enable_forwarding of this XiqDeviceConfigureIpv4InterfaceResponse.

        Indicates whether or not IPv4 is forwarding on the VLAN  # noqa: E501

        :param enable_forwarding: The enable_forwarding of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_forwarding is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_forwarding`, must not be `None`")  # noqa: E501

        self._enable_forwarding = enable_forwarding

    @property
    def enable_vlan_loopback(self):
        """Gets the enable_vlan_loopback of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Indicates whether or not Vlan Loopback is enabled on the interface  # noqa: E501

        :return: The enable_vlan_loopback of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enable_vlan_loopback

    @enable_vlan_loopback.setter
    def enable_vlan_loopback(self, enable_vlan_loopback):
        """Sets the enable_vlan_loopback of this XiqDeviceConfigureIpv4InterfaceResponse.

        Indicates whether or not Vlan Loopback is enabled on the interface  # noqa: E501

        :param enable_vlan_loopback: The enable_vlan_loopback of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_vlan_loopback is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_vlan_loopback`, must not be `None`")  # noqa: E501

        self._enable_vlan_loopback = enable_vlan_loopback

    @property
    def use_ip_addr_as_ospf_router_id(self):
        """Gets the use_ip_addr_as_ospf_router_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Indicates whether or not to use ip address as ospf router id on the interface  # noqa: E501

        :return: The use_ip_addr_as_ospf_router_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._use_ip_addr_as_ospf_router_id

    @use_ip_addr_as_ospf_router_id.setter
    def use_ip_addr_as_ospf_router_id(self, use_ip_addr_as_ospf_router_id):
        """Sets the use_ip_addr_as_ospf_router_id of this XiqDeviceConfigureIpv4InterfaceResponse.

        Indicates whether or not to use ip address as ospf router id on the interface  # noqa: E501

        :param use_ip_addr_as_ospf_router_id: The use_ip_addr_as_ospf_router_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and use_ip_addr_as_ospf_router_id is None:  # noqa: E501
            raise ValueError("Invalid value for `use_ip_addr_as_ospf_router_id`, must not be `None`")  # noqa: E501

        self._use_ip_addr_as_ospf_router_id = use_ip_addr_as_ospf_router_id

    @property
    def override_dhcp_relay(self):
        """Gets the override_dhcp_relay of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Indicates whether or not to override DHCP relay on the interface  # noqa: E501

        :return: The override_dhcp_relay of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._override_dhcp_relay

    @override_dhcp_relay.setter
    def override_dhcp_relay(self, override_dhcp_relay):
        """Sets the override_dhcp_relay of this XiqDeviceConfigureIpv4InterfaceResponse.

        Indicates whether or not to override DHCP relay on the interface  # noqa: E501

        :param override_dhcp_relay: The override_dhcp_relay of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and override_dhcp_relay is None:  # noqa: E501
            raise ValueError("Invalid value for `override_dhcp_relay`, must not be `None`")  # noqa: E501

        self._override_dhcp_relay = override_dhcp_relay

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Indicates whether or not to enable DHCP relay on the interface if override DHCP relay is enabled  # noqa: E501

        :return: The enable_dhcp of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this XiqDeviceConfigureIpv4InterfaceResponse.

        Indicates whether or not to enable DHCP relay on the interface if override DHCP relay is enabled  # noqa: E501

        :param enable_dhcp: The enable_dhcp of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_dhcp is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_dhcp`, must not be `None`")  # noqa: E501

        self._enable_dhcp = enable_dhcp

    @property
    def primary_dhcp_server(self):
        """Gets the primary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Primary DHCP Server can be set if DHCP is enabled  # noqa: E501

        :return: The primary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._primary_dhcp_server

    @primary_dhcp_server.setter
    def primary_dhcp_server(self, primary_dhcp_server):
        """Sets the primary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.

        Primary DHCP Server can be set if DHCP is enabled  # noqa: E501

        :param primary_dhcp_server: The primary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and primary_dhcp_server is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_dhcp_server`, must not be `None`")  # noqa: E501

        self._primary_dhcp_server = primary_dhcp_server

    @property
    def secondary_dhcp_server(self):
        """Gets the secondary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        Secondary DHCP Server can be set if DHCP is enabled  # noqa: E501

        :return: The secondary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._secondary_dhcp_server

    @secondary_dhcp_server.setter
    def secondary_dhcp_server(self, secondary_dhcp_server):
        """Sets the secondary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.

        Secondary DHCP Server can be set if DHCP is enabled  # noqa: E501

        :param secondary_dhcp_server: The secondary_dhcp_server of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secondary_dhcp_server is None:  # noqa: E501
            raise ValueError("Invalid value for `secondary_dhcp_server`, must not be `None`")  # noqa: E501

        self._secondary_dhcp_server = secondary_dhcp_server

    @property
    def predefined(self):
        """Gets the predefined of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        The value is predefined and can not be change  # noqa: E501

        :return: The predefined of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqDeviceConfigureIpv4InterfaceResponse.

        The value is predefined and can not be change  # noqa: E501

        :param predefined: The predefined of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and predefined is None:  # noqa: E501
            raise ValueError("Invalid value for `predefined`, must not be `None`")  # noqa: E501

        self._predefined = predefined

    @property
    def subnetwork_id(self):
        """Gets the subnetwork_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        The Subnetwork ID  # noqa: E501

        :return: The subnetwork_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: int
        """
        return self._subnetwork_id

    @subnetwork_id.setter
    def subnetwork_id(self, subnetwork_id):
        """Sets the subnetwork_id of this XiqDeviceConfigureIpv4InterfaceResponse.

        The Subnetwork ID  # noqa: E501

        :param subnetwork_id: The subnetwork_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: int
        """

        self._subnetwork_id = subnetwork_id

    @property
    def ipv4_interface_id(self):
        """Gets the ipv4_interface_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501

        The IPv4 Interface ID  # noqa: E501

        :return: The ipv4_interface_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: int
        """
        return self._ipv4_interface_id

    @ipv4_interface_id.setter
    def ipv4_interface_id(self, ipv4_interface_id):
        """Sets the ipv4_interface_id of this XiqDeviceConfigureIpv4InterfaceResponse.

        The IPv4 Interface ID  # noqa: E501

        :param ipv4_interface_id: The ipv4_interface_id of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: int
        """

        self._ipv4_interface_id = ipv4_interface_id

    @property
    def vlan_attribute(self):
        """Gets the vlan_attribute of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501


        :return: The vlan_attribute of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :rtype: XiqDeviceVlanAttributes
        """
        return self._vlan_attribute

    @vlan_attribute.setter
    def vlan_attribute(self, vlan_attribute):
        """Sets the vlan_attribute of this XiqDeviceConfigureIpv4InterfaceResponse.


        :param vlan_attribute: The vlan_attribute of this XiqDeviceConfigureIpv4InterfaceResponse.  # noqa: E501
        :type: XiqDeviceVlanAttributes
        """

        self._vlan_attribute = vlan_attribute

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
        if not isinstance(other, XiqDeviceConfigureIpv4InterfaceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceConfigureIpv4InterfaceResponse):
            return True

        return self.to_dict() != other.to_dict()
