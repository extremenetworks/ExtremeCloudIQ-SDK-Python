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


class XiqUpdateCloudConfigGroupRequest(object):
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
        'description': 'str',
        'device_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'device_ids': 'device_ids'
    }

    def __init__(self, name=None, description=None, device_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateCloudConfigGroupRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._device_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if device_ids is not None:
            self.device_ids = device_ids

    @property
    def name(self):
        """Gets the name of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501

        The CCG name  # noqa: E501

        :return: The name of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateCloudConfigGroupRequest.

        The CCG name  # noqa: E501

        :param name: The name of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501

        The CCG description  # noqa: E501

        :return: The description of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateCloudConfigGroupRequest.

        The CCG description  # noqa: E501

        :param description: The description of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_ids(self):
        """Gets the device_ids of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501

        The device ID list.  # noqa: E501

        :return: The device_ids of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this XiqUpdateCloudConfigGroupRequest.

        The device ID list.  # noqa: E501

        :param device_ids: The device_ids of this XiqUpdateCloudConfigGroupRequest.  # noqa: E501
        :type: list[int]
        """

        self._device_ids = device_ids

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
        if not isinstance(other, XiqUpdateCloudConfigGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateCloudConfigGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
