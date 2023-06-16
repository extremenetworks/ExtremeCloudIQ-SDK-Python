# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class InlineObject(object):
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
        'file': 'file'
    }

    attribute_map = {
        'file': 'file'
    }

    def __init__(self, file=None, local_vars_configuration=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file = None
        self.discriminator = None

        self.file = file

    @property
    def file(self):
        """Gets the file of this InlineObject.  # noqa: E501

        The floorplan image file to upload.   For better performance, Extreme Networks recommends that the image file (.png .jpeg) be less than 500 KB.  # noqa: E501

        :return: The file of this InlineObject.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InlineObject.

        The floorplan image file to upload.   For better performance, Extreme Networks recommends that the image file (.png .jpeg) be less than 500 KB.  # noqa: E501

        :param file: The file of this InlineObject.  # noqa: E501
        :type: file
        """
        if self.local_vars_configuration.client_side_validation and file is None:  # noqa: E501
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

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
        if not isinstance(other, InlineObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineObject):
            return True

        return self.to_dict() != other.to_dict()
