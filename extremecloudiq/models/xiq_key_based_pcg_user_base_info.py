# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqKeyBasedPcgUserBaseInfo(object):
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
        'email': 'str',
        'user_group_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'email': 'email',
        'user_group_name': 'user_group_name'
    }

    def __init__(self, name=None, email=None, user_group_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqKeyBasedPcgUserBaseInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._email = None
        self._user_group_name = None
        self.discriminator = None

        self.name = name
        self.email = email
        self.user_group_name = user_group_name

    @property
    def name(self):
        """Gets the name of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501

        The user name of key based PCG, which could not share with other exist key based PCG  # noqa: E501

        :return: The name of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqKeyBasedPcgUserBaseInfo.

        The user name of key based PCG, which could not share with other exist key based PCG  # noqa: E501

        :param name: The name of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def email(self):
        """Gets the email of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501

        The email for deliver key based PCG user password  # noqa: E501

        :return: The email of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this XiqKeyBasedPcgUserBaseInfo.

        The email for deliver key based PCG user password  # noqa: E501

        :param email: The email of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def user_group_name(self):
        """Gets the user_group_name of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501

        The user group name  # noqa: E501

        :return: The user_group_name of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this XiqKeyBasedPcgUserBaseInfo.

        The user group name  # noqa: E501

        :param user_group_name: The user_group_name of this XiqKeyBasedPcgUserBaseInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_group_name`, must not be `None`")  # noqa: E501

        self._user_group_name = user_group_name

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
        if not isinstance(other, XiqKeyBasedPcgUserBaseInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqKeyBasedPcgUserBaseInfo):
            return True

        return self.to_dict() != other.to_dict()
