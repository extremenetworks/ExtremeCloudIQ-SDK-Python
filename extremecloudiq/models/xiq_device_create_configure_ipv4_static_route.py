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


class XiqDeviceCreateConfigureIpv4StaticRoute(object):
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
        'dest_subnetwork': 'str',
        'dest_subnetwork_to_int': 'int',
        'next_hop_ip': 'str',
        'next_hop_ip_to_int': 'int',
        'next_hop_ip_ping_protection': 'bool',
        'metric': 'int',
        'routing_instance': 'str',
        'predefined': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'dest_subnetwork': 'dest_subnetwork',
        'dest_subnetwork_to_int': 'dest_subnetwork_to_int',
        'next_hop_ip': 'next_hop_ip',
        'next_hop_ip_to_int': 'next_hop_ip_to_int',
        'next_hop_ip_ping_protection': 'next_hop_ip_ping_protection',
        'metric': 'metric',
        'routing_instance': 'routing_instance',
        'predefined': 'predefined'
    }

    def __init__(self, name=None, dest_subnetwork=None, dest_subnetwork_to_int=None, next_hop_ip=None, next_hop_ip_to_int=None, next_hop_ip_ping_protection=None, metric=None, routing_instance=None, predefined=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceCreateConfigureIpv4StaticRoute - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._dest_subnetwork = None
        self._dest_subnetwork_to_int = None
        self._next_hop_ip = None
        self._next_hop_ip_to_int = None
        self._next_hop_ip_ping_protection = None
        self._metric = None
        self._routing_instance = None
        self._predefined = None
        self.discriminator = None

        self.name = name
        self.dest_subnetwork = dest_subnetwork
        if dest_subnetwork_to_int is not None:
            self.dest_subnetwork_to_int = dest_subnetwork_to_int
        self.next_hop_ip = next_hop_ip
        if next_hop_ip_to_int is not None:
            self.next_hop_ip_to_int = next_hop_ip_to_int
        self.next_hop_ip_ping_protection = next_hop_ip_ping_protection
        self.metric = metric
        self.routing_instance = routing_instance
        self.predefined = predefined

    @property
    def name(self):
        """Gets the name of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Name of the static route  # noqa: E501

        :return: The name of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Name of the static route  # noqa: E501

        :param name: The name of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def dest_subnetwork(self):
        """Gets the dest_subnetwork of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Destination subnetwork IP and mask  # noqa: E501

        :return: The dest_subnetwork of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._dest_subnetwork

    @dest_subnetwork.setter
    def dest_subnetwork(self, dest_subnetwork):
        """Sets the dest_subnetwork of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Destination subnetwork IP and mask  # noqa: E501

        :param dest_subnetwork: The dest_subnetwork of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dest_subnetwork is None:  # noqa: E501
            raise ValueError("Invalid value for `dest_subnetwork`, must not be `None`")  # noqa: E501

        self._dest_subnetwork = dest_subnetwork

    @property
    def dest_subnetwork_to_int(self):
        """Gets the dest_subnetwork_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Destination subnetwork IP and mask to numeric format  # noqa: E501

        :return: The dest_subnetwork_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: int
        """
        return self._dest_subnetwork_to_int

    @dest_subnetwork_to_int.setter
    def dest_subnetwork_to_int(self, dest_subnetwork_to_int):
        """Sets the dest_subnetwork_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Destination subnetwork IP and mask to numeric format  # noqa: E501

        :param dest_subnetwork_to_int: The dest_subnetwork_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: int
        """

        self._dest_subnetwork_to_int = dest_subnetwork_to_int

    @property
    def next_hop_ip(self):
        """Gets the next_hop_ip of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Next hop IP  # noqa: E501

        :return: The next_hop_ip of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._next_hop_ip

    @next_hop_ip.setter
    def next_hop_ip(self, next_hop_ip):
        """Sets the next_hop_ip of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Next hop IP  # noqa: E501

        :param next_hop_ip: The next_hop_ip of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and next_hop_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `next_hop_ip`, must not be `None`")  # noqa: E501

        self._next_hop_ip = next_hop_ip

    @property
    def next_hop_ip_to_int(self):
        """Gets the next_hop_ip_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Next hop IP to numeric format  # noqa: E501

        :return: The next_hop_ip_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: int
        """
        return self._next_hop_ip_to_int

    @next_hop_ip_to_int.setter
    def next_hop_ip_to_int(self, next_hop_ip_to_int):
        """Sets the next_hop_ip_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Next hop IP to numeric format  # noqa: E501

        :param next_hop_ip_to_int: The next_hop_ip_to_int of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: int
        """

        self._next_hop_ip_to_int = next_hop_ip_to_int

    @property
    def next_hop_ip_ping_protection(self):
        """Gets the next_hop_ip_ping_protection of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Next hop IP ping protection  # noqa: E501

        :return: The next_hop_ip_ping_protection of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: bool
        """
        return self._next_hop_ip_ping_protection

    @next_hop_ip_ping_protection.setter
    def next_hop_ip_ping_protection(self, next_hop_ip_ping_protection):
        """Sets the next_hop_ip_ping_protection of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Next hop IP ping protection  # noqa: E501

        :param next_hop_ip_ping_protection: The next_hop_ip_ping_protection of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and next_hop_ip_ping_protection is None:  # noqa: E501
            raise ValueError("Invalid value for `next_hop_ip_ping_protection`, must not be `None`")  # noqa: E501

        self._next_hop_ip_ping_protection = next_hop_ip_ping_protection

    @property
    def metric(self):
        """Gets the metric of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        Metric set up on a static route  # noqa: E501

        :return: The metric of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this XiqDeviceCreateConfigureIpv4StaticRoute.

        Metric set up on a static route  # noqa: E501

        :param metric: The metric of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and metric is None:  # noqa: E501
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def routing_instance(self):
        """Gets the routing_instance of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        The Routing Instance  # noqa: E501

        :return: The routing_instance of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: str
        """
        return self._routing_instance

    @routing_instance.setter
    def routing_instance(self, routing_instance):
        """Sets the routing_instance of this XiqDeviceCreateConfigureIpv4StaticRoute.

        The Routing Instance  # noqa: E501

        :param routing_instance: The routing_instance of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and routing_instance is None:  # noqa: E501
            raise ValueError("Invalid value for `routing_instance`, must not be `None`")  # noqa: E501

        self._routing_instance = routing_instance

    @property
    def predefined(self):
        """Gets the predefined of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501

        The value is predefined and can not be change  # noqa: E501

        :return: The predefined of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqDeviceCreateConfigureIpv4StaticRoute.

        The value is predefined and can not be change  # noqa: E501

        :param predefined: The predefined of this XiqDeviceCreateConfigureIpv4StaticRoute.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and predefined is None:  # noqa: E501
            raise ValueError("Invalid value for `predefined`, must not be `None`")  # noqa: E501

        self._predefined = predefined

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
        if not isinstance(other, XiqDeviceCreateConfigureIpv4StaticRoute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceCreateConfigureIpv4StaticRoute):
            return True

        return self.to_dict() != other.to_dict()
