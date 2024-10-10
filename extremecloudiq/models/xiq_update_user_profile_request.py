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


class XiqUpdateUserProfileRequest(object):
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
        'vlan_profile_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'vlan_profile_id': 'vlan_profile_id'
    }

    def __init__(self, name=None, vlan_profile_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateUserProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._vlan_profile_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if vlan_profile_id is not None:
            self.vlan_profile_id = vlan_profile_id

    @property
    def name(self):
        """Gets the name of this XiqUpdateUserProfileRequest.  # noqa: E501

        The user profile name  # noqa: E501

        :return: The name of this XiqUpdateUserProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateUserProfileRequest.

        The user profile name  # noqa: E501

        :param name: The name of this XiqUpdateUserProfileRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def vlan_profile_id(self):
        """Gets the vlan_profile_id of this XiqUpdateUserProfileRequest.  # noqa: E501

        The VLAN profile id  # noqa: E501

        :return: The vlan_profile_id of this XiqUpdateUserProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._vlan_profile_id

    @vlan_profile_id.setter
    def vlan_profile_id(self, vlan_profile_id):
        """Sets the vlan_profile_id of this XiqUpdateUserProfileRequest.

        The VLAN profile id  # noqa: E501

        :param vlan_profile_id: The vlan_profile_id of this XiqUpdateUserProfileRequest.  # noqa: E501
        :type: int
        """

        self._vlan_profile_id = vlan_profile_id

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
        if not isinstance(other, XiqUpdateUserProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateUserProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
