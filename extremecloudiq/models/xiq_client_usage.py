# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqClientUsage(object):
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
        'client_id': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'client_id': 'client_id',
        'usage': 'usage'
    }

    def __init__(self, client_id=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """XiqClientUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._usage = None
        self.discriminator = None

        if client_id is not None:
            self.client_id = client_id
        if usage is not None:
            self.usage = usage

    @property
    def client_id(self):
        """Gets the client_id of this XiqClientUsage.  # noqa: E501

        The client ID  # noqa: E501

        :return: The client_id of this XiqClientUsage.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this XiqClientUsage.

        The client ID  # noqa: E501

        :param client_id: The client_id of this XiqClientUsage.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def usage(self):
        """Gets the usage of this XiqClientUsage.  # noqa: E501

        The client total usage  # noqa: E501

        :return: The usage of this XiqClientUsage.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this XiqClientUsage.

        The client total usage  # noqa: E501

        :param usage: The usage of this XiqClientUsage.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if not isinstance(other, XiqClientUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClientUsage):
            return True

        return self.to_dict() != other.to_dict()
