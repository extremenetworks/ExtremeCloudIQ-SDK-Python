# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqOnboardKeyBasedPcgRequest(object):
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
        'ssid_name': 'str',
        'enabled': 'bool',
        'user_ids': 'list[int]'
    }

    attribute_map = {
        'ssid_name': 'ssid_name',
        'enabled': 'enabled',
        'user_ids': 'user_ids'
    }

    def __init__(self, ssid_name=None, enabled=None, user_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqOnboardKeyBasedPcgRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ssid_name = None
        self._enabled = None
        self._user_ids = None
        self.discriminator = None

        self.ssid_name = ssid_name
        self.enabled = enabled
        self.user_ids = user_ids

    @property
    def ssid_name(self):
        """Gets the ssid_name of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501


        :return: The ssid_name of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501
        :rtype: str
        """
        return self._ssid_name

    @ssid_name.setter
    def ssid_name(self, ssid_name):
        """Sets the ssid_name of this XiqOnboardKeyBasedPcgRequest.


        :param ssid_name: The ssid_name of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ssid_name is None:  # noqa: E501
            raise ValueError("Invalid value for `ssid_name`, must not be `None`")  # noqa: E501

        self._ssid_name = ssid_name

    @property
    def enabled(self):
        """Gets the enabled of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501

        Enable the key based PCG  # noqa: E501

        :return: The enabled of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this XiqOnboardKeyBasedPcgRequest.

        Enable the key based PCG  # noqa: E501

        :param enabled: The enabled of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def user_ids(self):
        """Gets the user_ids of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501

        The request user IDs  # noqa: E501

        :return: The user_ids of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this XiqOnboardKeyBasedPcgRequest.

        The request user IDs  # noqa: E501

        :param user_ids: The user_ids of this XiqOnboardKeyBasedPcgRequest.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and user_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `user_ids`, must not be `None`")  # noqa: E501

        self._user_ids = user_ids

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
        if not isinstance(other, XiqOnboardKeyBasedPcgRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqOnboardKeyBasedPcgRequest):
            return True

        return self.to_dict() != other.to_dict()
