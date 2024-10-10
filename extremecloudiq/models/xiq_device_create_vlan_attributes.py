# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceCreateVlanAttributes(object):
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
        'dhcp_snooping_enabled': 'bool',
        'dhcp_snooping_action': 'XiqDeviceVlanAttributesDhcpSnoopingAction',
        'igmp_snooping_enabled': 'bool',
        'immediate_leave': 'bool',
        'always_create': 'bool',
        'vlan_obj': 'XiqVlanObject',
        'vlan_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'dhcp_snooping_enabled': 'dhcp_snooping_enabled',
        'dhcp_snooping_action': 'dhcp_snooping_action',
        'igmp_snooping_enabled': 'igmp_snooping_enabled',
        'immediate_leave': 'immediate_leave',
        'always_create': 'always_create',
        'vlan_obj': 'vlan_obj',
        'vlan_id': 'vlan_id'
    }

    def __init__(self, name=None, dhcp_snooping_enabled=None, dhcp_snooping_action=None, igmp_snooping_enabled=None, immediate_leave=None, always_create=None, vlan_obj=None, vlan_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceCreateVlanAttributes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._dhcp_snooping_enabled = None
        self._dhcp_snooping_action = None
        self._igmp_snooping_enabled = None
        self._immediate_leave = None
        self._always_create = None
        self._vlan_obj = None
        self._vlan_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if dhcp_snooping_enabled is not None:
            self.dhcp_snooping_enabled = dhcp_snooping_enabled
        if dhcp_snooping_action is not None:
            self.dhcp_snooping_action = dhcp_snooping_action
        if igmp_snooping_enabled is not None:
            self.igmp_snooping_enabled = igmp_snooping_enabled
        if immediate_leave is not None:
            self.immediate_leave = immediate_leave
        if always_create is not None:
            self.always_create = always_create
        if vlan_obj is not None:
            self.vlan_obj = vlan_obj
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def name(self):
        """Gets the name of this XiqDeviceCreateVlanAttributes.  # noqa: E501

        Name of the vlan  # noqa: E501

        :return: The name of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqDeviceCreateVlanAttributes.

        Name of the vlan  # noqa: E501

        :param name: The name of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def dhcp_snooping_enabled(self):
        """Gets the dhcp_snooping_enabled of this XiqDeviceCreateVlanAttributes.  # noqa: E501

        Whether dhcp snooping is enabled on this vlan  # noqa: E501

        :return: The dhcp_snooping_enabled of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp_snooping_enabled

    @dhcp_snooping_enabled.setter
    def dhcp_snooping_enabled(self, dhcp_snooping_enabled):
        """Sets the dhcp_snooping_enabled of this XiqDeviceCreateVlanAttributes.

        Whether dhcp snooping is enabled on this vlan  # noqa: E501

        :param dhcp_snooping_enabled: The dhcp_snooping_enabled of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: bool
        """

        self._dhcp_snooping_enabled = dhcp_snooping_enabled

    @property
    def dhcp_snooping_action(self):
        """Gets the dhcp_snooping_action of this XiqDeviceCreateVlanAttributes.  # noqa: E501


        :return: The dhcp_snooping_action of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: XiqDeviceVlanAttributesDhcpSnoopingAction
        """
        return self._dhcp_snooping_action

    @dhcp_snooping_action.setter
    def dhcp_snooping_action(self, dhcp_snooping_action):
        """Sets the dhcp_snooping_action of this XiqDeviceCreateVlanAttributes.


        :param dhcp_snooping_action: The dhcp_snooping_action of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: XiqDeviceVlanAttributesDhcpSnoopingAction
        """

        self._dhcp_snooping_action = dhcp_snooping_action

    @property
    def igmp_snooping_enabled(self):
        """Gets the igmp_snooping_enabled of this XiqDeviceCreateVlanAttributes.  # noqa: E501

        Whether igmp snooping is enabled on this vlan  # noqa: E501

        :return: The igmp_snooping_enabled of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._igmp_snooping_enabled

    @igmp_snooping_enabled.setter
    def igmp_snooping_enabled(self, igmp_snooping_enabled):
        """Sets the igmp_snooping_enabled of this XiqDeviceCreateVlanAttributes.

        Whether igmp snooping is enabled on this vlan  # noqa: E501

        :param igmp_snooping_enabled: The igmp_snooping_enabled of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: bool
        """

        self._igmp_snooping_enabled = igmp_snooping_enabled

    @property
    def immediate_leave(self):
        """Gets the immediate_leave of this XiqDeviceCreateVlanAttributes.  # noqa: E501

        When enabled, the multicast host is removed immediately if it leaves the group  # noqa: E501

        :return: The immediate_leave of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._immediate_leave

    @immediate_leave.setter
    def immediate_leave(self, immediate_leave):
        """Sets the immediate_leave of this XiqDeviceCreateVlanAttributes.

        When enabled, the multicast host is removed immediately if it leaves the group  # noqa: E501

        :param immediate_leave: The immediate_leave of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: bool
        """

        self._immediate_leave = immediate_leave

    @property
    def always_create(self):
        """Gets the always_create of this XiqDeviceCreateVlanAttributes.  # noqa: E501

        Should the vlan be created irrespective of port bindings  # noqa: E501

        :return: The always_create of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._always_create

    @always_create.setter
    def always_create(self, always_create):
        """Sets the always_create of this XiqDeviceCreateVlanAttributes.

        Should the vlan be created irrespective of port bindings  # noqa: E501

        :param always_create: The always_create of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: bool
        """

        self._always_create = always_create

    @property
    def vlan_obj(self):
        """Gets the vlan_obj of this XiqDeviceCreateVlanAttributes.  # noqa: E501


        :return: The vlan_obj of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: XiqVlanObject
        """
        return self._vlan_obj

    @vlan_obj.setter
    def vlan_obj(self, vlan_obj):
        """Sets the vlan_obj of this XiqDeviceCreateVlanAttributes.


        :param vlan_obj: The vlan_obj of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: XiqVlanObject
        """

        self._vlan_obj = vlan_obj

    @property
    def vlan_id(self):
        """Gets the vlan_id of this XiqDeviceCreateVlanAttributes.  # noqa: E501

        Id of the vlan  # noqa: E501

        :return: The vlan_id of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this XiqDeviceCreateVlanAttributes.

        Id of the vlan  # noqa: E501

        :param vlan_id: The vlan_id of this XiqDeviceCreateVlanAttributes.  # noqa: E501
        :type: int
        """

        self._vlan_id = vlan_id

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
        if not isinstance(other, XiqDeviceCreateVlanAttributes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceCreateVlanAttributes):
            return True

        return self.to_dict() != other.to_dict()
