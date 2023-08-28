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


class XiqUpdateLocationRequest(object):
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
        'parent_id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'name': 'name'
    }

    def __init__(self, parent_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateLocationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parent_id = None
        self._name = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this XiqUpdateLocationRequest.  # noqa: E501

        The parent location ID  # noqa: E501

        :return: The parent_id of this XiqUpdateLocationRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this XiqUpdateLocationRequest.

        The parent location ID  # noqa: E501

        :param parent_id: The parent_id of this XiqUpdateLocationRequest.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this XiqUpdateLocationRequest.  # noqa: E501

        The location name  # noqa: E501

        :return: The name of this XiqUpdateLocationRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateLocationRequest.

        The location name  # noqa: E501

        :param name: The name of this XiqUpdateLocationRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, XiqUpdateLocationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateLocationRequest):
            return True

        return self.to_dict() != other.to_dict()
