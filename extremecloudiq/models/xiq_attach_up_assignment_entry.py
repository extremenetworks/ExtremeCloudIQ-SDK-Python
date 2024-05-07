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


class XiqAttachUPAssignmentEntry(object):
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
        'user_profile_id': 'int',
        'user_profile_assignment_id': 'int'
    }

    attribute_map = {
        'user_profile_id': 'user_profile_id',
        'user_profile_assignment_id': 'user_profile_assignment_id'
    }

    def __init__(self, user_profile_id=None, user_profile_assignment_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqAttachUPAssignmentEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_profile_id = None
        self._user_profile_assignment_id = None
        self.discriminator = None

        if user_profile_id is not None:
            self.user_profile_id = user_profile_id
        if user_profile_assignment_id is not None:
            self.user_profile_assignment_id = user_profile_assignment_id

    @property
    def user_profile_id(self):
        """Gets the user_profile_id of this XiqAttachUPAssignmentEntry.  # noqa: E501

        The User Profile ID.  # noqa: E501

        :return: The user_profile_id of this XiqAttachUPAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._user_profile_id

    @user_profile_id.setter
    def user_profile_id(self, user_profile_id):
        """Sets the user_profile_id of this XiqAttachUPAssignmentEntry.

        The User Profile ID.  # noqa: E501

        :param user_profile_id: The user_profile_id of this XiqAttachUPAssignmentEntry.  # noqa: E501
        :type: int
        """

        self._user_profile_id = user_profile_id

    @property
    def user_profile_assignment_id(self):
        """Gets the user_profile_assignment_id of this XiqAttachUPAssignmentEntry.  # noqa: E501

        The User Profile Assignment ID.  # noqa: E501

        :return: The user_profile_assignment_id of this XiqAttachUPAssignmentEntry.  # noqa: E501
        :rtype: int
        """
        return self._user_profile_assignment_id

    @user_profile_assignment_id.setter
    def user_profile_assignment_id(self, user_profile_assignment_id):
        """Sets the user_profile_assignment_id of this XiqAttachUPAssignmentEntry.

        The User Profile Assignment ID.  # noqa: E501

        :param user_profile_assignment_id: The user_profile_assignment_id of this XiqAttachUPAssignmentEntry.  # noqa: E501
        :type: int
        """

        self._user_profile_assignment_id = user_profile_assignment_id

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
        if not isinstance(other, XiqAttachUPAssignmentEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAttachUPAssignmentEntry):
            return True

        return self.to_dict() != other.to_dict()
