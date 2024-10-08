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


class XiqMacFirewallRuleRequest(object):
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
        'action': 'XiqMacFirewallAction',
        'source_mac': 'int',
        'destination_mac': 'int',
        'logging_type': 'XiqLoggingType'
    }

    attribute_map = {
        'action': 'action',
        'source_mac': 'source_mac',
        'destination_mac': 'destination_mac',
        'logging_type': 'logging_type'
    }

    def __init__(self, action=None, source_mac=None, destination_mac=None, logging_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqMacFirewallRuleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._source_mac = None
        self._destination_mac = None
        self._logging_type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if source_mac is not None:
            self.source_mac = source_mac
        if destination_mac is not None:
            self.destination_mac = destination_mac
        if logging_type is not None:
            self.logging_type = logging_type

    @property
    def action(self):
        """Gets the action of this XiqMacFirewallRuleRequest.  # noqa: E501


        :return: The action of this XiqMacFirewallRuleRequest.  # noqa: E501
        :rtype: XiqMacFirewallAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this XiqMacFirewallRuleRequest.


        :param action: The action of this XiqMacFirewallRuleRequest.  # noqa: E501
        :type: XiqMacFirewallAction
        """

        self._action = action

    @property
    def source_mac(self):
        """Gets the source_mac of this XiqMacFirewallRuleRequest.  # noqa: E501

        Source MAC address for MAC Firewall Rule.  # noqa: E501

        :return: The source_mac of this XiqMacFirewallRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._source_mac

    @source_mac.setter
    def source_mac(self, source_mac):
        """Sets the source_mac of this XiqMacFirewallRuleRequest.

        Source MAC address for MAC Firewall Rule.  # noqa: E501

        :param source_mac: The source_mac of this XiqMacFirewallRuleRequest.  # noqa: E501
        :type: int
        """

        self._source_mac = source_mac

    @property
    def destination_mac(self):
        """Gets the destination_mac of this XiqMacFirewallRuleRequest.  # noqa: E501

         Destination MAC address for MAC Firewall Rule.  # noqa: E501

        :return: The destination_mac of this XiqMacFirewallRuleRequest.  # noqa: E501
        :rtype: int
        """
        return self._destination_mac

    @destination_mac.setter
    def destination_mac(self, destination_mac):
        """Sets the destination_mac of this XiqMacFirewallRuleRequest.

         Destination MAC address for MAC Firewall Rule.  # noqa: E501

        :param destination_mac: The destination_mac of this XiqMacFirewallRuleRequest.  # noqa: E501
        :type: int
        """

        self._destination_mac = destination_mac

    @property
    def logging_type(self):
        """Gets the logging_type of this XiqMacFirewallRuleRequest.  # noqa: E501


        :return: The logging_type of this XiqMacFirewallRuleRequest.  # noqa: E501
        :rtype: XiqLoggingType
        """
        return self._logging_type

    @logging_type.setter
    def logging_type(self, logging_type):
        """Sets the logging_type of this XiqMacFirewallRuleRequest.


        :param logging_type: The logging_type of this XiqMacFirewallRuleRequest.  # noqa: E501
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
        if not isinstance(other, XiqMacFirewallRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqMacFirewallRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
