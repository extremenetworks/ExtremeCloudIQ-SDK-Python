# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqError(object):
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
        'error_code': 'str',
        'error_id': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_id': 'error_id',
        'error_message': 'error_message'
    }

    def __init__(self, error_code=None, error_id=None, error_message=None, local_vars_configuration=None):  # noqa: E501
        """XiqError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._error_code = None
        self._error_id = None
        self._error_message = None
        self.discriminator = None

        self.error_code = error_code
        self.error_id = error_id
        self.error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this XiqError.  # noqa: E501

        The error code  # noqa: E501

        :return: The error_code of this XiqError.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this XiqError.

        The error code  # noqa: E501

        :param error_code: The error_code of this XiqError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error_code is None:  # noqa: E501
            raise ValueError("Invalid value for `error_code`, must not be `None`")  # noqa: E501

        self._error_code = error_code

    @property
    def error_id(self):
        """Gets the error_id of this XiqError.  # noqa: E501

        The error ID for internal troubleshooting  # noqa: E501

        :return: The error_id of this XiqError.  # noqa: E501
        :rtype: str
        """
        return self._error_id

    @error_id.setter
    def error_id(self, error_id):
        """Sets the error_id of this XiqError.

        The error ID for internal troubleshooting  # noqa: E501

        :param error_id: The error_id of this XiqError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error_id is None:  # noqa: E501
            raise ValueError("Invalid value for `error_id`, must not be `None`")  # noqa: E501

        self._error_id = error_id

    @property
    def error_message(self):
        """Gets the error_message of this XiqError.  # noqa: E501

        The error detail message  # noqa: E501

        :return: The error_message of this XiqError.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this XiqError.

        The error detail message  # noqa: E501

        :param error_message: The error_message of this XiqError.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and error_message is None:  # noqa: E501
            raise ValueError("Invalid value for `error_message`, must not be `None`")  # noqa: E501

        self._error_message = error_message

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
        if not isinstance(other, XiqError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqError):
            return True

        return self.to_dict() != other.to_dict()