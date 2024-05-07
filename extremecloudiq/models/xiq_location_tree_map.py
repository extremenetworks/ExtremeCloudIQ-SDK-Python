# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqLocationTreeMap(object):
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
        'map_name': 'str',
        'width': 'float',
        'height': 'float',
        'data': 'str'
    }

    attribute_map = {
        'map_name': 'map_name',
        'width': 'width',
        'height': 'height',
        'data': 'data'
    }

    def __init__(self, map_name=None, width=None, height=None, data=None, local_vars_configuration=None):  # noqa: E501
        """XiqLocationTreeMap - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._map_name = None
        self._width = None
        self._height = None
        self._data = None
        self.discriminator = None

        self.map_name = map_name
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        self.data = data

    @property
    def map_name(self):
        """Gets the map_name of this XiqLocationTreeMap.  # noqa: E501

        The background map name.  # noqa: E501

        :return: The map_name of this XiqLocationTreeMap.  # noqa: E501
        :rtype: str
        """
        return self._map_name

    @map_name.setter
    def map_name(self, map_name):
        """Sets the map_name of this XiqLocationTreeMap.

        The background map name.  # noqa: E501

        :param map_name: The map_name of this XiqLocationTreeMap.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and map_name is None:  # noqa: E501
            raise ValueError("Invalid value for `map_name`, must not be `None`")  # noqa: E501

        self._map_name = map_name

    @property
    def width(self):
        """Gets the width of this XiqLocationTreeMap.  # noqa: E501

        The x-dimension of the map in pixels.  # noqa: E501

        :return: The width of this XiqLocationTreeMap.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this XiqLocationTreeMap.

        The x-dimension of the map in pixels.  # noqa: E501

        :param width: The width of this XiqLocationTreeMap.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this XiqLocationTreeMap.  # noqa: E501

        The y-dimension of the map in pixels.  # noqa: E501

        :return: The height of this XiqLocationTreeMap.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this XiqLocationTreeMap.

        The y-dimension of the map in pixels.  # noqa: E501

        :param height: The height of this XiqLocationTreeMap.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def data(self):
        """Gets the data of this XiqLocationTreeMap.  # noqa: E501

        The base-64 encoded string of the map.  # noqa: E501

        :return: The data of this XiqLocationTreeMap.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this XiqLocationTreeMap.

        The base-64 encoded string of the map.  # noqa: E501

        :param data: The data of this XiqLocationTreeMap.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data is None:  # noqa: E501
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if not isinstance(other, XiqLocationTreeMap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqLocationTreeMap):
            return True

        return self.to_dict() != other.to_dict()
