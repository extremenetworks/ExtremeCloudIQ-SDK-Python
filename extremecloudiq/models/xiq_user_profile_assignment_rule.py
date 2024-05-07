# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUserProfileAssignmentRule(object):
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
        'user_profile': 'XiqUserProfile',
        'user_profile_assignment': 'XiqUserProfileAssignment',
        'enable_by_cwp': 'bool'
    }

    attribute_map = {
        'user_profile': 'user_profile',
        'user_profile_assignment': 'user_profile_assignment',
        'enable_by_cwp': 'enable_by_cwp'
    }

    def __init__(self, user_profile=None, user_profile_assignment=None, enable_by_cwp=None, local_vars_configuration=None):  # noqa: E501
        """XiqUserProfileAssignmentRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_profile = None
        self._user_profile_assignment = None
        self._enable_by_cwp = None
        self.discriminator = None

        if user_profile is not None:
            self.user_profile = user_profile
        if user_profile_assignment is not None:
            self.user_profile_assignment = user_profile_assignment
        if enable_by_cwp is not None:
            self.enable_by_cwp = enable_by_cwp

    @property
    def user_profile(self):
        """Gets the user_profile of this XiqUserProfileAssignmentRule.  # noqa: E501


        :return: The user_profile of this XiqUserProfileAssignmentRule.  # noqa: E501
        :rtype: XiqUserProfile
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        """Sets the user_profile of this XiqUserProfileAssignmentRule.


        :param user_profile: The user_profile of this XiqUserProfileAssignmentRule.  # noqa: E501
        :type: XiqUserProfile
        """

        self._user_profile = user_profile

    @property
    def user_profile_assignment(self):
        """Gets the user_profile_assignment of this XiqUserProfileAssignmentRule.  # noqa: E501


        :return: The user_profile_assignment of this XiqUserProfileAssignmentRule.  # noqa: E501
        :rtype: XiqUserProfileAssignment
        """
        return self._user_profile_assignment

    @user_profile_assignment.setter
    def user_profile_assignment(self, user_profile_assignment):
        """Sets the user_profile_assignment of this XiqUserProfileAssignmentRule.


        :param user_profile_assignment: The user_profile_assignment of this XiqUserProfileAssignmentRule.  # noqa: E501
        :type: XiqUserProfileAssignment
        """

        self._user_profile_assignment = user_profile_assignment

    @property
    def enable_by_cwp(self):
        """Gets the enable_by_cwp of this XiqUserProfileAssignmentRule.  # noqa: E501

        The flag for enableBypassCwp.  # noqa: E501

        :return: The enable_by_cwp of this XiqUserProfileAssignmentRule.  # noqa: E501
        :rtype: bool
        """
        return self._enable_by_cwp

    @enable_by_cwp.setter
    def enable_by_cwp(self, enable_by_cwp):
        """Sets the enable_by_cwp of this XiqUserProfileAssignmentRule.

        The flag for enableBypassCwp.  # noqa: E501

        :param enable_by_cwp: The enable_by_cwp of this XiqUserProfileAssignmentRule.  # noqa: E501
        :type: bool
        """

        self._enable_by_cwp = enable_by_cwp

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
        if not isinstance(other, XiqUserProfileAssignmentRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUserProfileAssignmentRule):
            return True

        return self.to_dict() != other.to_dict()