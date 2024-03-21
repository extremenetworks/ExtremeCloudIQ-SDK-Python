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


class XiqDeviceMonitorVlanAttributesInfo(object):
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
        'vlan_id': 'int',
        'vlan_name': 'str',
        'active_ports': 'list[str]',
        'stp_instance': 'str',
        'stp_enabled': 'bool',
        'igmp_snooping_enabled': 'bool',
        'dhcp_snooping_enabled': 'bool',
        'vrf_name': 'str',
        'dynamic_enabled': 'bool',
        'member_ports': 'list[str]',
        'tagged_ports': 'list[str]',
        'untagged_ports': 'list[str]',
        'dynamic_ports': 'list[str]',
        'non_forwarding_vlan_enabled': 'bool'
    }

    attribute_map = {
        'vlan_id': 'vlan_id',
        'vlan_name': 'vlan_name',
        'active_ports': 'active_ports',
        'stp_instance': 'stp_instance',
        'stp_enabled': 'stp_enabled',
        'igmp_snooping_enabled': 'igmp_snooping_enabled',
        'dhcp_snooping_enabled': 'dhcp_snooping_enabled',
        'vrf_name': 'vrf_name',
        'dynamic_enabled': 'dynamic_enabled',
        'member_ports': 'member_ports',
        'tagged_ports': 'tagged_ports',
        'untagged_ports': 'untagged_ports',
        'dynamic_ports': 'dynamic_ports',
        'non_forwarding_vlan_enabled': 'non_forwarding_vlan_enabled'
    }

    def __init__(self, vlan_id=None, vlan_name=None, active_ports=None, stp_instance=None, stp_enabled=None, igmp_snooping_enabled=None, dhcp_snooping_enabled=None, vrf_name=None, dynamic_enabled=None, member_ports=None, tagged_ports=None, untagged_ports=None, dynamic_ports=None, non_forwarding_vlan_enabled=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceMonitorVlanAttributesInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vlan_id = None
        self._vlan_name = None
        self._active_ports = None
        self._stp_instance = None
        self._stp_enabled = None
        self._igmp_snooping_enabled = None
        self._dhcp_snooping_enabled = None
        self._vrf_name = None
        self._dynamic_enabled = None
        self._member_ports = None
        self._tagged_ports = None
        self._untagged_ports = None
        self._dynamic_ports = None
        self._non_forwarding_vlan_enabled = None
        self.discriminator = None

        self.vlan_id = vlan_id
        if vlan_name is not None:
            self.vlan_name = vlan_name
        if active_ports is not None:
            self.active_ports = active_ports
        if stp_instance is not None:
            self.stp_instance = stp_instance
        if stp_enabled is not None:
            self.stp_enabled = stp_enabled
        if igmp_snooping_enabled is not None:
            self.igmp_snooping_enabled = igmp_snooping_enabled
        if dhcp_snooping_enabled is not None:
            self.dhcp_snooping_enabled = dhcp_snooping_enabled
        if vrf_name is not None:
            self.vrf_name = vrf_name
        if dynamic_enabled is not None:
            self.dynamic_enabled = dynamic_enabled
        if member_ports is not None:
            self.member_ports = member_ports
        if tagged_ports is not None:
            self.tagged_ports = tagged_ports
        if untagged_ports is not None:
            self.untagged_ports = untagged_ports
        if dynamic_ports is not None:
            self.dynamic_ports = dynamic_ports
        if non_forwarding_vlan_enabled is not None:
            self.non_forwarding_vlan_enabled = non_forwarding_vlan_enabled

    @property
    def vlan_id(self):
        """Gets the vlan_id of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The VLAN ID  # noqa: E501

        :return: The vlan_id of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this XiqDeviceMonitorVlanAttributesInfo.

        The VLAN ID  # noqa: E501

        :param vlan_id: The vlan_id of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and vlan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def vlan_name(self):
        """Gets the vlan_name of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The VLAN Name  # noqa: E501

        :return: The vlan_name of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: str
        """
        return self._vlan_name

    @vlan_name.setter
    def vlan_name(self, vlan_name):
        """Sets the vlan_name of this XiqDeviceMonitorVlanAttributesInfo.

        The VLAN Name  # noqa: E501

        :param vlan_name: The vlan_name of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: str
        """

        self._vlan_name = vlan_name

    @property
    def active_ports(self):
        """Gets the active_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The active ports in the VLAN  # noqa: E501

        :return: The active_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._active_ports

    @active_ports.setter
    def active_ports(self, active_ports):
        """Sets the active_ports of this XiqDeviceMonitorVlanAttributesInfo.

        The active ports in the VLAN  # noqa: E501

        :param active_ports: The active_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: list[str]
        """

        self._active_ports = active_ports

    @property
    def stp_instance(self):
        """Gets the stp_instance of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The STP instance name for the VLAN  # noqa: E501

        :return: The stp_instance of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: str
        """
        return self._stp_instance

    @stp_instance.setter
    def stp_instance(self, stp_instance):
        """Sets the stp_instance of this XiqDeviceMonitorVlanAttributesInfo.

        The STP instance name for the VLAN  # noqa: E501

        :param stp_instance: The stp_instance of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: str
        """

        self._stp_instance = stp_instance

    @property
    def stp_enabled(self):
        """Gets the stp_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        Indicates whether or not STP is enabled or disabled on the VLAN  # noqa: E501

        :return: The stp_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._stp_enabled

    @stp_enabled.setter
    def stp_enabled(self, stp_enabled):
        """Sets the stp_enabled of this XiqDeviceMonitorVlanAttributesInfo.

        Indicates whether or not STP is enabled or disabled on the VLAN  # noqa: E501

        :param stp_enabled: The stp_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: bool
        """

        self._stp_enabled = stp_enabled

    @property
    def igmp_snooping_enabled(self):
        """Gets the igmp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        Indicates whether or not IGMP Snooping is enabled or disabled on the VLAN  # noqa: E501

        :return: The igmp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._igmp_snooping_enabled

    @igmp_snooping_enabled.setter
    def igmp_snooping_enabled(self, igmp_snooping_enabled):
        """Sets the igmp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.

        Indicates whether or not IGMP Snooping is enabled or disabled on the VLAN  # noqa: E501

        :param igmp_snooping_enabled: The igmp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: bool
        """

        self._igmp_snooping_enabled = igmp_snooping_enabled

    @property
    def dhcp_snooping_enabled(self):
        """Gets the dhcp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        Indicates whether or not DCHP Snooping is enabled or disabled on the VLAN  # noqa: E501

        :return: The dhcp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp_snooping_enabled

    @dhcp_snooping_enabled.setter
    def dhcp_snooping_enabled(self, dhcp_snooping_enabled):
        """Sets the dhcp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.

        Indicates whether or not DCHP Snooping is enabled or disabled on the VLAN  # noqa: E501

        :param dhcp_snooping_enabled: The dhcp_snooping_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: bool
        """

        self._dhcp_snooping_enabled = dhcp_snooping_enabled

    @property
    def vrf_name(self):
        """Gets the vrf_name of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The name of the VRF for the VLAN  # noqa: E501

        :return: The vrf_name of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: str
        """
        return self._vrf_name

    @vrf_name.setter
    def vrf_name(self, vrf_name):
        """Sets the vrf_name of this XiqDeviceMonitorVlanAttributesInfo.

        The name of the VRF for the VLAN  # noqa: E501

        :param vrf_name: The vrf_name of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: str
        """

        self._vrf_name = vrf_name

    @property
    def dynamic_enabled(self):
        """Gets the dynamic_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        Indicates whether or not this is a Dynamic VLAN  # noqa: E501

        :return: The dynamic_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic_enabled

    @dynamic_enabled.setter
    def dynamic_enabled(self, dynamic_enabled):
        """Sets the dynamic_enabled of this XiqDeviceMonitorVlanAttributesInfo.

        Indicates whether or not this is a Dynamic VLAN  # noqa: E501

        :param dynamic_enabled: The dynamic_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: bool
        """

        self._dynamic_enabled = dynamic_enabled

    @property
    def member_ports(self):
        """Gets the member_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The member ports in the VLAN  # noqa: E501

        :return: The member_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._member_ports

    @member_ports.setter
    def member_ports(self, member_ports):
        """Sets the member_ports of this XiqDeviceMonitorVlanAttributesInfo.

        The member ports in the VLAN  # noqa: E501

        :param member_ports: The member_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: list[str]
        """

        self._member_ports = member_ports

    @property
    def tagged_ports(self):
        """Gets the tagged_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The tagged ports in the VLAN  # noqa: E501

        :return: The tagged_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._tagged_ports

    @tagged_ports.setter
    def tagged_ports(self, tagged_ports):
        """Sets the tagged_ports of this XiqDeviceMonitorVlanAttributesInfo.

        The tagged ports in the VLAN  # noqa: E501

        :param tagged_ports: The tagged_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: list[str]
        """

        self._tagged_ports = tagged_ports

    @property
    def untagged_ports(self):
        """Gets the untagged_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The untagged ports in the VLAN  # noqa: E501

        :return: The untagged_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._untagged_ports

    @untagged_ports.setter
    def untagged_ports(self, untagged_ports):
        """Sets the untagged_ports of this XiqDeviceMonitorVlanAttributesInfo.

        The untagged ports in the VLAN  # noqa: E501

        :param untagged_ports: The untagged_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: list[str]
        """

        self._untagged_ports = untagged_ports

    @property
    def dynamic_ports(self):
        """Gets the dynamic_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        The dynamic ports in the VLAN  # noqa: E501

        :return: The dynamic_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._dynamic_ports

    @dynamic_ports.setter
    def dynamic_ports(self, dynamic_ports):
        """Sets the dynamic_ports of this XiqDeviceMonitorVlanAttributesInfo.

        The dynamic ports in the VLAN  # noqa: E501

        :param dynamic_ports: The dynamic_ports of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: list[str]
        """

        self._dynamic_ports = dynamic_ports

    @property
    def non_forwarding_vlan_enabled(self):
        """Gets the non_forwarding_vlan_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501

        Indicates whether or not this is a Non Forwarding VLAN (learning VLAN)  # noqa: E501

        :return: The non_forwarding_vlan_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :rtype: bool
        """
        return self._non_forwarding_vlan_enabled

    @non_forwarding_vlan_enabled.setter
    def non_forwarding_vlan_enabled(self, non_forwarding_vlan_enabled):
        """Sets the non_forwarding_vlan_enabled of this XiqDeviceMonitorVlanAttributesInfo.

        Indicates whether or not this is a Non Forwarding VLAN (learning VLAN)  # noqa: E501

        :param non_forwarding_vlan_enabled: The non_forwarding_vlan_enabled of this XiqDeviceMonitorVlanAttributesInfo.  # noqa: E501
        :type: bool
        """

        self._non_forwarding_vlan_enabled = non_forwarding_vlan_enabled

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
        if not isinstance(other, XiqDeviceMonitorVlanAttributesInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceMonitorVlanAttributesInfo):
            return True

        return self.to_dict() != other.to_dict()