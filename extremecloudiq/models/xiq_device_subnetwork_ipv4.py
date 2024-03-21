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


class XiqDeviceSubnetworkIpv4(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'ip_addr_space': 'str',
        'gateway_ip_type': 'XiqGatewayIpType',
        'vlan_profile': 'str',
        'enable_dhcp': 'bool',
        'dhcp_relay': 'XiqDeviceDhcpRelay',
        'clients_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'ip_addr_space': 'ip_addr_space',
        'gateway_ip_type': 'gateway_ip_type',
        'vlan_profile': 'vlan_profile',
        'enable_dhcp': 'enable_dhcp',
        'dhcp_relay': 'dhcp_relay',
        'clients_number': 'clients_number'
    }

    def __init__(self, id=None, name=None, description=None, ip_addr_space=None, gateway_ip_type=None, vlan_profile=None, enable_dhcp=None, dhcp_relay=None, clients_number=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceSubnetworkIpv4 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._ip_addr_space = None
        self._gateway_ip_type = None
        self._vlan_profile = None
        self._enable_dhcp = None
        self._dhcp_relay = None
        self._clients_number = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.ip_addr_space = ip_addr_space
        self.gateway_ip_type = gateway_ip_type
        self.vlan_profile = vlan_profile
        self.enable_dhcp = enable_dhcp
        if dhcp_relay is not None:
            self.dhcp_relay = dhcp_relay
        self.clients_number = clients_number

    @property
    def id(self):
        """Gets the id of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        The IPv4 Subnetwork ID  # noqa: E501

        :return: The id of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqDeviceSubnetworkIpv4.

        The IPv4 Subnetwork ID  # noqa: E501

        :param id: The id of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        Subnetwork name  # noqa: E501

        :return: The name of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqDeviceSubnetworkIpv4.

        Subnetwork name  # noqa: E501

        :param name: The name of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        Subnetwork description  # noqa: E501

        :return: The description of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqDeviceSubnetworkIpv4.

        Subnetwork description  # noqa: E501

        :param description: The description of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ip_addr_space(self):
        """Gets the ip_addr_space of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        Subnetwork Ipv4 address  # noqa: E501

        :return: The ip_addr_space of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: str
        """
        return self._ip_addr_space

    @ip_addr_space.setter
    def ip_addr_space(self, ip_addr_space):
        """Sets the ip_addr_space of this XiqDeviceSubnetworkIpv4.

        Subnetwork Ipv4 address  # noqa: E501

        :param ip_addr_space: The ip_addr_space of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ip_addr_space is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_addr_space`, must not be `None`")  # noqa: E501

        self._ip_addr_space = ip_addr_space

    @property
    def gateway_ip_type(self):
        """Gets the gateway_ip_type of this XiqDeviceSubnetworkIpv4.  # noqa: E501


        :return: The gateway_ip_type of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: XiqGatewayIpType
        """
        return self._gateway_ip_type

    @gateway_ip_type.setter
    def gateway_ip_type(self, gateway_ip_type):
        """Sets the gateway_ip_type of this XiqDeviceSubnetworkIpv4.


        :param gateway_ip_type: The gateway_ip_type of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: XiqGatewayIpType
        """
        if self.local_vars_configuration.client_side_validation and gateway_ip_type is None:  # noqa: E501
            raise ValueError("Invalid value for `gateway_ip_type`, must not be `None`")  # noqa: E501

        self._gateway_ip_type = gateway_ip_type

    @property
    def vlan_profile(self):
        """Gets the vlan_profile of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        The VLAN ID  # noqa: E501

        :return: The vlan_profile of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: str
        """
        return self._vlan_profile

    @vlan_profile.setter
    def vlan_profile(self, vlan_profile):
        """Sets the vlan_profile of this XiqDeviceSubnetworkIpv4.

        The VLAN ID  # noqa: E501

        :param vlan_profile: The vlan_profile of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and vlan_profile is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan_profile`, must not be `None`")  # noqa: E501

        self._vlan_profile = vlan_profile

    @property
    def enable_dhcp(self):
        """Gets the enable_dhcp of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        Enable DHCP relay server  # noqa: E501

        :return: The enable_dhcp of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dhcp

    @enable_dhcp.setter
    def enable_dhcp(self, enable_dhcp):
        """Sets the enable_dhcp of this XiqDeviceSubnetworkIpv4.

        Enable DHCP relay server  # noqa: E501

        :param enable_dhcp: The enable_dhcp of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_dhcp is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_dhcp`, must not be `None`")  # noqa: E501

        self._enable_dhcp = enable_dhcp

    @property
    def dhcp_relay(self):
        """Gets the dhcp_relay of this XiqDeviceSubnetworkIpv4.  # noqa: E501


        :return: The dhcp_relay of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: XiqDeviceDhcpRelay
        """
        return self._dhcp_relay

    @dhcp_relay.setter
    def dhcp_relay(self, dhcp_relay):
        """Sets the dhcp_relay of this XiqDeviceSubnetworkIpv4.


        :param dhcp_relay: The dhcp_relay of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: XiqDeviceDhcpRelay
        """

        self._dhcp_relay = dhcp_relay

    @property
    def clients_number(self):
        """Gets the clients_number of this XiqDeviceSubnetworkIpv4.  # noqa: E501

        Number of clients available for subnetwork  # noqa: E501

        :return: The clients_number of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :rtype: int
        """
        return self._clients_number

    @clients_number.setter
    def clients_number(self, clients_number):
        """Sets the clients_number of this XiqDeviceSubnetworkIpv4.

        Number of clients available for subnetwork  # noqa: E501

        :param clients_number: The clients_number of this XiqDeviceSubnetworkIpv4.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and clients_number is None:  # noqa: E501
            raise ValueError("Invalid value for `clients_number`, must not be `None`")  # noqa: E501

        self._clients_number = clients_number

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
        if not isinstance(other, XiqDeviceSubnetworkIpv4):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceSubnetworkIpv4):
            return True

        return self.to_dict() != other.to_dict()
