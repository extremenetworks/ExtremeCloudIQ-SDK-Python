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


class XiqLoginResponse(object):
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
        'access_token': 'str',
        'token_type': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'token_type': 'token_type',
        'expires_in': 'expires_in'
    }

    def __init__(self, access_token=None, token_type=None, expires_in=None, local_vars_configuration=None):  # noqa: E501
        """XiqLoginResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._token_type = None
        self._expires_in = None
        self.discriminator = None

        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in

    @property
    def access_token(self):
        """Gets the access_token of this XiqLoginResponse.  # noqa: E501

        The access token with JWT format issued by ExtremeCloud IQ  # noqa: E501

        :return: The access_token of this XiqLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this XiqLoginResponse.

        The access token with JWT format issued by ExtremeCloud IQ  # noqa: E501

        :param access_token: The access_token of this XiqLoginResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def token_type(self):
        """Gets the token_type of this XiqLoginResponse.  # noqa: E501

        The type of token, only supports \"Bearer\" currently  # noqa: E501

        :return: The token_type of this XiqLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this XiqLoginResponse.

        The type of token, only supports \"Bearer\" currently  # noqa: E501

        :param token_type: The token_type of this XiqLoginResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token_type is None:  # noqa: E501
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

    @property
    def expires_in(self):
        """Gets the expires_in of this XiqLoginResponse.  # noqa: E501

        The lifetime in seconds of the access token  # noqa: E501

        :return: The expires_in of this XiqLoginResponse.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this XiqLoginResponse.

        The lifetime in seconds of the access token  # noqa: E501

        :param expires_in: The expires_in of this XiqLoginResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

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
        if not isinstance(other, XiqLoginResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqLoginResponse):
            return True

        return self.to_dict() != other.to_dict()
