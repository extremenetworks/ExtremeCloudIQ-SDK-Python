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


class XiqDeviceLocationAssignment(object):
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
        'location_id': 'int',
        'x': 'float',
        'y': 'float',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'location_id': 'location_id',
        'x': 'x',
        'y': 'y',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, location_id=None, x=None, y=None, latitude=None, longitude=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceLocationAssignment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location_id = None
        self._x = None
        self._y = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        self.location_id = location_id
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude

    @property
    def location_id(self):
        """Gets the location_id of this XiqDeviceLocationAssignment.  # noqa: E501

        The assigned location ID, it must be FLOOR type  # noqa: E501

        :return: The location_id of this XiqDeviceLocationAssignment.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqDeviceLocationAssignment.

        The assigned location ID, it must be FLOOR type  # noqa: E501

        :param location_id: The location_id of this XiqDeviceLocationAssignment.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and location_id is None:  # noqa: E501
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def x(self):
        """Gets the x of this XiqDeviceLocationAssignment.  # noqa: E501

        The horizontal value in the floor map  # noqa: E501

        :return: The x of this XiqDeviceLocationAssignment.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this XiqDeviceLocationAssignment.

        The horizontal value in the floor map  # noqa: E501

        :param x: The x of this XiqDeviceLocationAssignment.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this XiqDeviceLocationAssignment.  # noqa: E501

        The vertical value in the floor map  # noqa: E501

        :return: The y of this XiqDeviceLocationAssignment.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this XiqDeviceLocationAssignment.

        The vertical value in the floor map  # noqa: E501

        :param y: The y of this XiqDeviceLocationAssignment.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def latitude(self):
        """Gets the latitude of this XiqDeviceLocationAssignment.  # noqa: E501

        The latitude in the geography  # noqa: E501

        :return: The latitude of this XiqDeviceLocationAssignment.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this XiqDeviceLocationAssignment.

        The latitude in the geography  # noqa: E501

        :param latitude: The latitude of this XiqDeviceLocationAssignment.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this XiqDeviceLocationAssignment.  # noqa: E501

        The longitude in the geography  # noqa: E501

        :return: The longitude of this XiqDeviceLocationAssignment.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this XiqDeviceLocationAssignment.

        The longitude in the geography  # noqa: E501

        :param longitude: The longitude of this XiqDeviceLocationAssignment.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

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
        if not isinstance(other, XiqDeviceLocationAssignment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceLocationAssignment):
            return True

        return self.to_dict() != other.to_dict()
