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


class XiqAttachIpFirewallPolicyToUserProfileRequest(object):
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
        'policy_id': 'int',
        'traffic': 'XiqTraffic'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'traffic': 'traffic'
    }

    def __init__(self, policy_id=None, traffic=None, local_vars_configuration=None):  # noqa: E501
        """XiqAttachIpFirewallPolicyToUserProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policy_id = None
        self._traffic = None
        self.discriminator = None

        self.policy_id = policy_id
        self.traffic = traffic

    @property
    def policy_id(self):
        """Gets the policy_id of this XiqAttachIpFirewallPolicyToUserProfileRequest.  # noqa: E501

        IP Firewall Policy ID  # noqa: E501

        :return: The policy_id of this XiqAttachIpFirewallPolicyToUserProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this XiqAttachIpFirewallPolicyToUserProfileRequest.

        IP Firewall Policy ID  # noqa: E501

        :param policy_id: The policy_id of this XiqAttachIpFirewallPolicyToUserProfileRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and policy_id is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_id`, must not be `None`")  # noqa: E501

        self._policy_id = policy_id

    @property
    def traffic(self):
        """Gets the traffic of this XiqAttachIpFirewallPolicyToUserProfileRequest.  # noqa: E501


        :return: The traffic of this XiqAttachIpFirewallPolicyToUserProfileRequest.  # noqa: E501
        :rtype: XiqTraffic
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """Sets the traffic of this XiqAttachIpFirewallPolicyToUserProfileRequest.


        :param traffic: The traffic of this XiqAttachIpFirewallPolicyToUserProfileRequest.  # noqa: E501
        :type: XiqTraffic
        """
        if self.local_vars_configuration.client_side_validation and traffic is None:  # noqa: E501
            raise ValueError("Invalid value for `traffic`, must not be `None`")  # noqa: E501

        self._traffic = traffic

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
        if not isinstance(other, XiqAttachIpFirewallPolicyToUserProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAttachIpFirewallPolicyToUserProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
