# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqGenerateApiTokenRequest(object):
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
        'expire_time': 'int',
        'description': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'expire_time': 'expire_time',
        'description': 'description',
        'permissions': 'permissions'
    }

    def __init__(self, expire_time=None, description=None, permissions=None, local_vars_configuration=None):  # noqa: E501
        """XiqGenerateApiTokenRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expire_time = None
        self._description = None
        self._permissions = None
        self.discriminator = None

        if expire_time is not None:
            self.expire_time = expire_time
        if description is not None:
            self.description = description
        self.permissions = permissions

    @property
    def expire_time(self):
        """Gets the expire_time of this XiqGenerateApiTokenRequest.  # noqa: E501

        The token expire time, format is the number of seconds from epoch of 1970-01-01T00:00:00Z. If null means no expiration, the minimum value is current time plus 300 seconds.  # noqa: E501

        :return: The expire_time of this XiqGenerateApiTokenRequest.  # noqa: E501
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this XiqGenerateApiTokenRequest.

        The token expire time, format is the number of seconds from epoch of 1970-01-01T00:00:00Z. If null means no expiration, the minimum value is current time plus 300 seconds.  # noqa: E501

        :param expire_time: The expire_time of this XiqGenerateApiTokenRequest.  # noqa: E501
        :type: int
        """

        self._expire_time = expire_time

    @property
    def description(self):
        """Gets the description of this XiqGenerateApiTokenRequest.  # noqa: E501

        The token description  # noqa: E501

        :return: The description of this XiqGenerateApiTokenRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqGenerateApiTokenRequest.

        The token description  # noqa: E501

        :param description: The description of this XiqGenerateApiTokenRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """Gets the permissions of this XiqGenerateApiTokenRequest.  # noqa: E501

        The token permissions  # noqa: E501

        :return: The permissions of this XiqGenerateApiTokenRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this XiqGenerateApiTokenRequest.

        The token permissions  # noqa: E501

        :param permissions: The permissions of this XiqGenerateApiTokenRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

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
        if not isinstance(other, XiqGenerateApiTokenRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqGenerateApiTokenRequest):
            return True

        return self.to_dict() != other.to_dict()
