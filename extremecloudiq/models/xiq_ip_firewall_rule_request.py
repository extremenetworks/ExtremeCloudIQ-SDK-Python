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


class XiqIpFirewallRuleRequest(object):
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
        'action': 'XiqIpFirewallAction',
        'service_id': 'int',
        'source_ip_id': 'int',
        'destination_ip_id': 'int',
        'logging_type': 'XiqLoggingType'
    }

    attribute_map = {
        'action': 'action',
        'service_id': 'service_id',
        'source_ip_id': 'source_ip_id',
        'destination_ip_id': 'destination_ip_id',
        'logging_type': 'logging_type'
    }

    def __init__(self, action=None, service_id=None, source_ip_id=None, destination_ip_id=None, logging_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqIpFirewallRuleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._service_id = None
        self._source_ip_id = None
        self._destination_ip_id = None
        self._logging_type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if service_id is not None:
            self.service_id = service_id
        if source_ip_id is not None:
            self.source_ip_id = source_ip_id
        if destination_ip_id is not None:
            self.destination_ip_id = destination_ip_id
        if logging_type is not None:
            self.logging_type = logging_type

    @property
    def action(self):
        """Gets the action of this XiqIpFirewallRuleRequest.  # noqa: E501


        :return: The action of this XiqIpFirewallRuleRequest.  # noqa: E501
        :rtype: XiqIpFirewallAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this XiqIpFirewallRuleRequest.


        :param action: The action of this XiqIpFirewallRuleRequest.  # noqa: E501
        :type: XiqIpFirewallAction
        """

        self._action = action

    @property
    def service_id(self):
        """Gets the service_id of this XiqIpFirewallRuleRequest.  # noqa: E501

        Application or Network Service ID for IP Firewall Rule.  # noqa: E501

        :return: The service_id of this XiqIpFirewallRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this XiqIpFirewallRuleRequest.

        Application or Network Service ID for IP Firewall Rule.  # noqa: E501

        :param service_id: The service_id of this XiqIpFirewallRuleRequest.  # noqa: E501
        :type: int
        """

        self._service_id = service_id

    @property
    def source_ip_id(self):
        """Gets the source_ip_id of this XiqIpFirewallRuleRequest.  # noqa: E501

        Source IP for IP Firewall Rule.  # noqa: E501

        :return: The source_ip_id of this XiqIpFirewallRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._source_ip_id

    @source_ip_id.setter
    def source_ip_id(self, source_ip_id):
        """Sets the source_ip_id of this XiqIpFirewallRuleRequest.

        Source IP for IP Firewall Rule.  # noqa: E501

        :param source_ip_id: The source_ip_id of this XiqIpFirewallRuleRequest.  # noqa: E501
        :type: int
        """

        self._source_ip_id = source_ip_id

    @property
    def destination_ip_id(self):
        """Gets the destination_ip_id of this XiqIpFirewallRuleRequest.  # noqa: E501

        Destination IP for IP Firewall Rule.  # noqa: E501

        :return: The destination_ip_id of this XiqIpFirewallRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._destination_ip_id

    @destination_ip_id.setter
    def destination_ip_id(self, destination_ip_id):
        """Sets the destination_ip_id of this XiqIpFirewallRuleRequest.

        Destination IP for IP Firewall Rule.  # noqa: E501

        :param destination_ip_id: The destination_ip_id of this XiqIpFirewallRuleRequest.  # noqa: E501
        :type: int
        """

        self._destination_ip_id = destination_ip_id

    @property
    def logging_type(self):
        """Gets the logging_type of this XiqIpFirewallRuleRequest.  # noqa: E501


        :return: The logging_type of this XiqIpFirewallRuleRequest.  # noqa: E501
        :rtype: XiqLoggingType
        """
        return self._logging_type

    @logging_type.setter
    def logging_type(self, logging_type):
        """Sets the logging_type of this XiqIpFirewallRuleRequest.


        :param logging_type: The logging_type of this XiqIpFirewallRuleRequest.  # noqa: E501
        :type: XiqLoggingType
        """

        self._logging_type = logging_type

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
        if not isinstance(other, XiqIpFirewallRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIpFirewallRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
