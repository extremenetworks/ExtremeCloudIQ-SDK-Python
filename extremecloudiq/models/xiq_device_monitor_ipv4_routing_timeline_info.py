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


class XiqDeviceMonitorIpv4RoutingTimelineInfo(object):
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
        'static_routes_count': 'int',
        'direct_routes_count': 'int',
        'ospf_routes_count': 'int',
        'total_routes_count': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'static_routes_count': 'static_routes_count',
        'direct_routes_count': 'direct_routes_count',
        'ospf_routes_count': 'ospf_routes_count',
        'total_routes_count': 'total_routes_count',
        'timestamp': 'timestamp'
    }

    def __init__(self, static_routes_count=None, direct_routes_count=None, ospf_routes_count=None, total_routes_count=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceMonitorIpv4RoutingTimelineInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._static_routes_count = None
        self._direct_routes_count = None
        self._ospf_routes_count = None
        self._total_routes_count = None
        self._timestamp = None
        self.discriminator = None

        if static_routes_count is not None:
            self.static_routes_count = static_routes_count
        if direct_routes_count is not None:
            self.direct_routes_count = direct_routes_count
        if ospf_routes_count is not None:
            self.ospf_routes_count = ospf_routes_count
        if total_routes_count is not None:
            self.total_routes_count = total_routes_count
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def static_routes_count(self):
        """Gets the static_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501

        The number of Static routes  # noqa: E501

        :return: The static_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :rtype: int
        """
        return self._static_routes_count

    @static_routes_count.setter
    def static_routes_count(self, static_routes_count):
        """Sets the static_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.

        The number of Static routes  # noqa: E501

        :param static_routes_count: The static_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :type: int
        """

        self._static_routes_count = static_routes_count

    @property
    def direct_routes_count(self):
        """Gets the direct_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501

        The number of Direct routes  # noqa: E501

        :return: The direct_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :rtype: int
        """
        return self._direct_routes_count

    @direct_routes_count.setter
    def direct_routes_count(self, direct_routes_count):
        """Sets the direct_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.

        The number of Direct routes  # noqa: E501

        :param direct_routes_count: The direct_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :type: int
        """

        self._direct_routes_count = direct_routes_count

    @property
    def ospf_routes_count(self):
        """Gets the ospf_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501

        The number of OSPF routes  # noqa: E501

        :return: The ospf_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :rtype: int
        """
        return self._ospf_routes_count

    @ospf_routes_count.setter
    def ospf_routes_count(self, ospf_routes_count):
        """Sets the ospf_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.

        The number of OSPF routes  # noqa: E501

        :param ospf_routes_count: The ospf_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :type: int
        """

        self._ospf_routes_count = ospf_routes_count

    @property
    def total_routes_count(self):
        """Gets the total_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501

        The total number of routes  # noqa: E501

        :return: The total_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :rtype: int
        """
        return self._total_routes_count

    @total_routes_count.setter
    def total_routes_count(self, total_routes_count):
        """Sets the total_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.

        The total number of routes  # noqa: E501

        :param total_routes_count: The total_routes_count of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :type: int
        """

        self._total_routes_count = total_routes_count

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501

        The timestamp for when route information was stored  # noqa: E501

        :return: The timestamp of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqDeviceMonitorIpv4RoutingTimelineInfo.

        The timestamp for when route information was stored  # noqa: E501

        :param timestamp: The timestamp of this XiqDeviceMonitorIpv4RoutingTimelineInfo.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, XiqDeviceMonitorIpv4RoutingTimelineInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceMonitorIpv4RoutingTimelineInfo):
            return True

        return self.to_dict() != other.to_dict()
