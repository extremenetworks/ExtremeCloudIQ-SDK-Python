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


class XiqInitKeyBasedPcgNetworkPolicyRequest(object):
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
        'policy_name': 'str',
        'ssid_name': 'str',
        'users': 'list[XiqKeyBasedPcgUserBaseInfo]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'ssid_name': 'ssid_name',
        'users': 'users'
    }

    def __init__(self, policy_name=None, ssid_name=None, users=None, local_vars_configuration=None):  # noqa: E501
        """XiqInitKeyBasedPcgNetworkPolicyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policy_name = None
        self._ssid_name = None
        self._users = None
        self.discriminator = None

        self.policy_name = policy_name
        self.ssid_name = ssid_name
        self.users = users

    @property
    def policy_name(self):
        """Gets the policy_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501

        The network policy name  # noqa: E501

        :return: The policy_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.

        The network policy name  # noqa: E501

        :param policy_name: The policy_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and policy_name is None:  # noqa: E501
            raise ValueError("Invalid value for `policy_name`, must not be `None`")  # noqa: E501

        self._policy_name = policy_name

    @property
    def ssid_name(self):
        """Gets the ssid_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501

        The SSID name  # noqa: E501

        :return: The ssid_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501
        :rtype: str
        """
        return self._ssid_name

    @ssid_name.setter
    def ssid_name(self, ssid_name):
        """Sets the ssid_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.

        The SSID name  # noqa: E501

        :param ssid_name: The ssid_name of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ssid_name is None:  # noqa: E501
            raise ValueError("Invalid value for `ssid_name`, must not be `None`")  # noqa: E501

        self._ssid_name = ssid_name

    @property
    def users(self):
        """Gets the users of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501

        The Key-based PCG users  # noqa: E501

        :return: The users of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501
        :rtype: list[XiqKeyBasedPcgUserBaseInfo]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this XiqInitKeyBasedPcgNetworkPolicyRequest.

        The Key-based PCG users  # noqa: E501

        :param users: The users of this XiqInitKeyBasedPcgNetworkPolicyRequest.  # noqa: E501
        :type: list[XiqKeyBasedPcgUserBaseInfo]
        """
        if self.local_vars_configuration.client_side_validation and users is None:  # noqa: E501
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

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
        if not isinstance(other, XiqInitKeyBasedPcgNetworkPolicyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqInitKeyBasedPcgNetworkPolicyRequest):
            return True

        return self.to_dict() != other.to_dict()
