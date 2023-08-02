# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCheckPermissionRequest(object):
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
        'uri': 'str',
        'method': 'str'
    }

    attribute_map = {
        'uri': 'uri',
        'method': 'method'
    }

    def __init__(self, uri=None, method=None, local_vars_configuration=None):  # noqa: E501
        """XiqCheckPermissionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uri = None
        self._method = None
        self.discriminator = None

        self.uri = uri
        self.method = method

    @property
    def uri(self):
        """Gets the uri of this XiqCheckPermissionRequest.  # noqa: E501

        The request HTTP URI  # noqa: E501

        :return: The uri of this XiqCheckPermissionRequest.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this XiqCheckPermissionRequest.

        The request HTTP URI  # noqa: E501

        :param uri: The uri of this XiqCheckPermissionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and uri is None:  # noqa: E501
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def method(self):
        """Gets the method of this XiqCheckPermissionRequest.  # noqa: E501

        The request HTTP method  # noqa: E501

        :return: The method of this XiqCheckPermissionRequest.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this XiqCheckPermissionRequest.

        The request HTTP method  # noqa: E501

        :param method: The method of this XiqCheckPermissionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and method is None:  # noqa: E501
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

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
        if not isinstance(other, XiqCheckPermissionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCheckPermissionRequest):
            return True

        return self.to_dict() != other.to_dict()
