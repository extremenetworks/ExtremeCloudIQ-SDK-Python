# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceMonitorIpv4RouteNexthop(object):
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
        'nexthop_ipv4_address': 'str',
        'nexthop_device_id': 'int',
        'nexthop_host_name': 'str',
        'ping_protection_enabled': 'bool',
        'ping_protection_state': 'str',
        'ping_protection_last_uptime': 'str',
        'ping_protection_last_downtime': 'str',
        'routing_instance': 'str'
    }

    attribute_map = {
        'nexthop_ipv4_address': 'nexthop_ipv4_address',
        'nexthop_device_id': 'nexthop_device_id',
        'nexthop_host_name': 'nexthop_host_name',
        'ping_protection_enabled': 'ping_protection_enabled',
        'ping_protection_state': 'ping_protection_state',
        'ping_protection_last_uptime': 'ping_protection_last_uptime',
        'ping_protection_last_downtime': 'ping_protection_last_downtime',
        'routing_instance': 'routing_instance'
    }

    def __init__(self, nexthop_ipv4_address=None, nexthop_device_id=None, nexthop_host_name=None, ping_protection_enabled=None, ping_protection_state=None, ping_protection_last_uptime=None, ping_protection_last_downtime=None, routing_instance=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceMonitorIpv4RouteNexthop - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nexthop_ipv4_address = None
        self._nexthop_device_id = None
        self._nexthop_host_name = None
        self._ping_protection_enabled = None
        self._ping_protection_state = None
        self._ping_protection_last_uptime = None
        self._ping_protection_last_downtime = None
        self._routing_instance = None
        self.discriminator = None

        if nexthop_ipv4_address is not None:
            self.nexthop_ipv4_address = nexthop_ipv4_address
        if nexthop_device_id is not None:
            self.nexthop_device_id = nexthop_device_id
        if nexthop_host_name is not None:
            self.nexthop_host_name = nexthop_host_name
        if ping_protection_enabled is not None:
            self.ping_protection_enabled = ping_protection_enabled
        if ping_protection_state is not None:
            self.ping_protection_state = ping_protection_state
        if ping_protection_last_uptime is not None:
            self.ping_protection_last_uptime = ping_protection_last_uptime
        if ping_protection_last_downtime is not None:
            self.ping_protection_last_downtime = ping_protection_last_downtime
        if routing_instance is not None:
            self.routing_instance = routing_instance

    @property
    def nexthop_ipv4_address(self):
        """Gets the nexthop_ipv4_address of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The IPv4 Address of the Nexthop  # noqa: E501

        :return: The nexthop_ipv4_address of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: str
        """
        return self._nexthop_ipv4_address

    @nexthop_ipv4_address.setter
    def nexthop_ipv4_address(self, nexthop_ipv4_address):
        """Sets the nexthop_ipv4_address of this XiqDeviceMonitorIpv4RouteNexthop.

        The IPv4 Address of the Nexthop  # noqa: E501

        :param nexthop_ipv4_address: The nexthop_ipv4_address of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: str
        """

        self._nexthop_ipv4_address = nexthop_ipv4_address

    @property
    def nexthop_device_id(self):
        """Gets the nexthop_device_id of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The Device ID of the Nexthop  # noqa: E501

        :return: The nexthop_device_id of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: int
        """
        return self._nexthop_device_id

    @nexthop_device_id.setter
    def nexthop_device_id(self, nexthop_device_id):
        """Sets the nexthop_device_id of this XiqDeviceMonitorIpv4RouteNexthop.

        The Device ID of the Nexthop  # noqa: E501

        :param nexthop_device_id: The nexthop_device_id of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: int
        """

        self._nexthop_device_id = nexthop_device_id

    @property
    def nexthop_host_name(self):
        """Gets the nexthop_host_name of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The host name of the Nexthop  # noqa: E501

        :return: The nexthop_host_name of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: str
        """
        return self._nexthop_host_name

    @nexthop_host_name.setter
    def nexthop_host_name(self, nexthop_host_name):
        """Sets the nexthop_host_name of this XiqDeviceMonitorIpv4RouteNexthop.

        The host name of the Nexthop  # noqa: E501

        :param nexthop_host_name: The nexthop_host_name of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: str
        """

        self._nexthop_host_name = nexthop_host_name

    @property
    def ping_protection_enabled(self):
        """Gets the ping_protection_enabled of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        Indicates whether or not ping route protection is enabled for Static Routes  # noqa: E501

        :return: The ping_protection_enabled of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: bool
        """
        return self._ping_protection_enabled

    @ping_protection_enabled.setter
    def ping_protection_enabled(self, ping_protection_enabled):
        """Sets the ping_protection_enabled of this XiqDeviceMonitorIpv4RouteNexthop.

        Indicates whether or not ping route protection is enabled for Static Routes  # noqa: E501

        :param ping_protection_enabled: The ping_protection_enabled of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: bool
        """

        self._ping_protection_enabled = ping_protection_enabled

    @property
    def ping_protection_state(self):
        """Gets the ping_protection_state of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The state of the IPv4 ping protection gateway  # noqa: E501

        :return: The ping_protection_state of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: str
        """
        return self._ping_protection_state

    @ping_protection_state.setter
    def ping_protection_state(self, ping_protection_state):
        """Sets the ping_protection_state of this XiqDeviceMonitorIpv4RouteNexthop.

        The state of the IPv4 ping protection gateway  # noqa: E501

        :param ping_protection_state: The ping_protection_state of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: str
        """

        self._ping_protection_state = ping_protection_state

    @property
    def ping_protection_last_uptime(self):
        """Gets the ping_protection_last_uptime of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The last time the gateway transitioned to the UP state  # noqa: E501

        :return: The ping_protection_last_uptime of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: str
        """
        return self._ping_protection_last_uptime

    @ping_protection_last_uptime.setter
    def ping_protection_last_uptime(self, ping_protection_last_uptime):
        """Sets the ping_protection_last_uptime of this XiqDeviceMonitorIpv4RouteNexthop.

        The last time the gateway transitioned to the UP state  # noqa: E501

        :param ping_protection_last_uptime: The ping_protection_last_uptime of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: str
        """

        self._ping_protection_last_uptime = ping_protection_last_uptime

    @property
    def ping_protection_last_downtime(self):
        """Gets the ping_protection_last_downtime of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The last time the gateway transitioned to the DOWN state  # noqa: E501

        :return: The ping_protection_last_downtime of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: str
        """
        return self._ping_protection_last_downtime

    @ping_protection_last_downtime.setter
    def ping_protection_last_downtime(self, ping_protection_last_downtime):
        """Sets the ping_protection_last_downtime of this XiqDeviceMonitorIpv4RouteNexthop.

        The last time the gateway transitioned to the DOWN state  # noqa: E501

        :param ping_protection_last_downtime: The ping_protection_last_downtime of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: str
        """

        self._ping_protection_last_downtime = ping_protection_last_downtime

    @property
    def routing_instance(self):
        """Gets the routing_instance of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501

        The Routing Instance of the Nexthop  # noqa: E501

        :return: The routing_instance of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :rtype: str
        """
        return self._routing_instance

    @routing_instance.setter
    def routing_instance(self, routing_instance):
        """Sets the routing_instance of this XiqDeviceMonitorIpv4RouteNexthop.

        The Routing Instance of the Nexthop  # noqa: E501

        :param routing_instance: The routing_instance of this XiqDeviceMonitorIpv4RouteNexthop.  # noqa: E501
        :type: str
        """

        self._routing_instance = routing_instance

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
        if not isinstance(other, XiqDeviceMonitorIpv4RouteNexthop):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceMonitorIpv4RouteNexthop):
            return True

        return self.to_dict() != other.to_dict()
