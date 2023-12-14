# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqListAlertPolicies(object):
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
        'global_policy': 'XiqAlertPolicy',
        'site_policies': 'list[XiqAlertPolicy]'
    }

    attribute_map = {
        'global_policy': 'global_policy',
        'site_policies': 'site_policies'
    }

    def __init__(self, global_policy=None, site_policies=None, local_vars_configuration=None):  # noqa: E501
        """XiqListAlertPolicies - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._global_policy = None
        self._site_policies = None
        self.discriminator = None

        if global_policy is not None:
            self.global_policy = global_policy
        if site_policies is not None:
            self.site_policies = site_policies

    @property
    def global_policy(self):
        """Gets the global_policy of this XiqListAlertPolicies.  # noqa: E501


        :return: The global_policy of this XiqListAlertPolicies.  # noqa: E501
        :rtype: XiqAlertPolicy
        """
        return self._global_policy

    @global_policy.setter
    def global_policy(self, global_policy):
        """Sets the global_policy of this XiqListAlertPolicies.


        :param global_policy: The global_policy of this XiqListAlertPolicies.  # noqa: E501
        :type: XiqAlertPolicy
        """

        self._global_policy = global_policy

    @property
    def site_policies(self):
        """Gets the site_policies of this XiqListAlertPolicies.  # noqa: E501

        The site alert policy List  # noqa: E501

        :return: The site_policies of this XiqListAlertPolicies.  # noqa: E501
        :rtype: list[XiqAlertPolicy]
        """
        return self._site_policies

    @site_policies.setter
    def site_policies(self, site_policies):
        """Sets the site_policies of this XiqListAlertPolicies.

        The site alert policy List  # noqa: E501

        :param site_policies: The site_policies of this XiqListAlertPolicies.  # noqa: E501
        :type: list[XiqAlertPolicy]
        """

        self._site_policies = site_policies

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
        if not isinstance(other, XiqListAlertPolicies):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqListAlertPolicies):
            return True

        return self.to_dict() != other.to_dict()
