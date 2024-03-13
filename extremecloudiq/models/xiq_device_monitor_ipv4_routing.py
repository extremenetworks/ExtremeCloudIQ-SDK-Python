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


class XiqDeviceMonitorIpv4Routing(object):
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
        'earliest_refresh_time': 'str',
        'latest_refresh_time': 'str',
        'latest_refresh_timestamp': 'int',
        'ipv4_routing_details': 'list[XiqDeviceMonitorIpv4RoutingDetail]'
    }

    attribute_map = {
        'earliest_refresh_time': 'earliest_refresh_time',
        'latest_refresh_time': 'latest_refresh_time',
        'latest_refresh_timestamp': 'latest_refresh_timestamp',
        'ipv4_routing_details': 'ipv4_routing_details'
    }

    def __init__(self, earliest_refresh_time=None, latest_refresh_time=None, latest_refresh_timestamp=None, ipv4_routing_details=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceMonitorIpv4Routing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._earliest_refresh_time = None
        self._latest_refresh_time = None
        self._latest_refresh_timestamp = None
        self._ipv4_routing_details = None
        self.discriminator = None

        self.earliest_refresh_time = earliest_refresh_time
        self.latest_refresh_time = latest_refresh_time
        self.latest_refresh_timestamp = latest_refresh_timestamp
        self.ipv4_routing_details = ipv4_routing_details

    @property
    def earliest_refresh_time(self):
        """Gets the earliest_refresh_time of this XiqDeviceMonitorIpv4Routing.  # noqa: E501

        the earliest time the refresh was successful  # noqa: E501

        :return: The earliest_refresh_time of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :rtype: str
        """
        return self._earliest_refresh_time

    @earliest_refresh_time.setter
    def earliest_refresh_time(self, earliest_refresh_time):
        """Sets the earliest_refresh_time of this XiqDeviceMonitorIpv4Routing.

        the earliest time the refresh was successful  # noqa: E501

        :param earliest_refresh_time: The earliest_refresh_time of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and earliest_refresh_time is None:  # noqa: E501
            raise ValueError("Invalid value for `earliest_refresh_time`, must not be `None`")  # noqa: E501

        self._earliest_refresh_time = earliest_refresh_time

    @property
    def latest_refresh_time(self):
        """Gets the latest_refresh_time of this XiqDeviceMonitorIpv4Routing.  # noqa: E501

        the latest time the refresh was successful  # noqa: E501

        :return: The latest_refresh_time of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :rtype: str
        """
        return self._latest_refresh_time

    @latest_refresh_time.setter
    def latest_refresh_time(self, latest_refresh_time):
        """Sets the latest_refresh_time of this XiqDeviceMonitorIpv4Routing.

        the latest time the refresh was successful  # noqa: E501

        :param latest_refresh_time: The latest_refresh_time of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and latest_refresh_time is None:  # noqa: E501
            raise ValueError("Invalid value for `latest_refresh_time`, must not be `None`")  # noqa: E501

        self._latest_refresh_time = latest_refresh_time

    @property
    def latest_refresh_timestamp(self):
        """Gets the latest_refresh_timestamp of this XiqDeviceMonitorIpv4Routing.  # noqa: E501

        The latest successful refresh timestamp  # noqa: E501

        :return: The latest_refresh_timestamp of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :rtype: int
        """
        return self._latest_refresh_timestamp

    @latest_refresh_timestamp.setter
    def latest_refresh_timestamp(self, latest_refresh_timestamp):
        """Sets the latest_refresh_timestamp of this XiqDeviceMonitorIpv4Routing.

        The latest successful refresh timestamp  # noqa: E501

        :param latest_refresh_timestamp: The latest_refresh_timestamp of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and latest_refresh_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `latest_refresh_timestamp`, must not be `None`")  # noqa: E501

        self._latest_refresh_timestamp = latest_refresh_timestamp

    @property
    def ipv4_routing_details(self):
        """Gets the ipv4_routing_details of this XiqDeviceMonitorIpv4Routing.  # noqa: E501

        The IPv4 Routing detail information that is monitored on the device  # noqa: E501

        :return: The ipv4_routing_details of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :rtype: list[XiqDeviceMonitorIpv4RoutingDetail]
        """
        return self._ipv4_routing_details

    @ipv4_routing_details.setter
    def ipv4_routing_details(self, ipv4_routing_details):
        """Sets the ipv4_routing_details of this XiqDeviceMonitorIpv4Routing.

        The IPv4 Routing detail information that is monitored on the device  # noqa: E501

        :param ipv4_routing_details: The ipv4_routing_details of this XiqDeviceMonitorIpv4Routing.  # noqa: E501
        :type: list[XiqDeviceMonitorIpv4RoutingDetail]
        """
        if self.local_vars_configuration.client_side_validation and ipv4_routing_details is None:  # noqa: E501
            raise ValueError("Invalid value for `ipv4_routing_details`, must not be `None`")  # noqa: E501

        self._ipv4_routing_details = ipv4_routing_details

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
        if not isinstance(other, XiqDeviceMonitorIpv4Routing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceMonitorIpv4Routing):
            return True

        return self.to_dict() != other.to_dict()
