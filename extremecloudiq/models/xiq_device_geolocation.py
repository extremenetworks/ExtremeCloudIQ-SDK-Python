# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceGeolocation(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'height': 'float',
        'major_axis': 'float',
        'minor_axis': 'float',
        'orientation': 'float',
        'last_reported': 'int'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'height': 'height',
        'major_axis': 'major_axis',
        'minor_axis': 'minor_axis',
        'orientation': 'orientation',
        'last_reported': 'last_reported'
    }

    def __init__(self, latitude=None, longitude=None, height=None, major_axis=None, minor_axis=None, orientation=None, last_reported=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceGeolocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._latitude = None
        self._longitude = None
        self._height = None
        self._major_axis = None
        self._minor_axis = None
        self._orientation = None
        self._last_reported = None
        self.discriminator = None

        if latitude is not None:
            self.latitude = latitude
        self.longitude = longitude
        self.height = height
        if major_axis is not None:
            self.major_axis = major_axis
        if minor_axis is not None:
            self.minor_axis = minor_axis
        self.orientation = orientation
        self.last_reported = last_reported

    @property
    def latitude(self):
        """Gets the latitude of this XiqDeviceGeolocation.  # noqa: E501

        The latitude of the AP  # noqa: E501

        :return: The latitude of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this XiqDeviceGeolocation.

        The latitude of the AP  # noqa: E501

        :param latitude: The latitude of this XiqDeviceGeolocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this XiqDeviceGeolocation.  # noqa: E501

        The longitude of the AP  # noqa: E501

        :return: The longitude of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this XiqDeviceGeolocation.

        The longitude of the AP  # noqa: E501

        :param longitude: The longitude of this XiqDeviceGeolocation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and longitude is None:  # noqa: E501
            raise ValueError("Invalid value for `longitude`, must not be `None`")  # noqa: E501

        self._longitude = longitude

    @property
    def height(self):
        """Gets the height of this XiqDeviceGeolocation.  # noqa: E501

        The height above sea level of the AP  # noqa: E501

        :return: The height of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this XiqDeviceGeolocation.

        The height above sea level of the AP  # noqa: E501

        :param height: The height of this XiqDeviceGeolocation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def major_axis(self):
        """Gets the major_axis of this XiqDeviceGeolocation.  # noqa: E501

        The major axis of the AP  # noqa: E501

        :return: The major_axis of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: float
        """
        return self._major_axis

    @major_axis.setter
    def major_axis(self, major_axis):
        """Sets the major_axis of this XiqDeviceGeolocation.

        The major axis of the AP  # noqa: E501

        :param major_axis: The major_axis of this XiqDeviceGeolocation.  # noqa: E501
        :type: float
        """

        self._major_axis = major_axis

    @property
    def minor_axis(self):
        """Gets the minor_axis of this XiqDeviceGeolocation.  # noqa: E501

        The minor axis of the AP  # noqa: E501

        :return: The minor_axis of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: float
        """
        return self._minor_axis

    @minor_axis.setter
    def minor_axis(self, minor_axis):
        """Sets the minor_axis of this XiqDeviceGeolocation.

        The minor axis of the AP  # noqa: E501

        :param minor_axis: The minor_axis of this XiqDeviceGeolocation.  # noqa: E501
        :type: float
        """

        self._minor_axis = minor_axis

    @property
    def orientation(self):
        """Gets the orientation of this XiqDeviceGeolocation.  # noqa: E501

        The orientation of the AP  # noqa: E501

        :return: The orientation of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: float
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this XiqDeviceGeolocation.

        The orientation of the AP  # noqa: E501

        :param orientation: The orientation of this XiqDeviceGeolocation.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and orientation is None:  # noqa: E501
            raise ValueError("Invalid value for `orientation`, must not be `None`")  # noqa: E501

        self._orientation = orientation

    @property
    def last_reported(self):
        """Gets the last_reported of this XiqDeviceGeolocation.  # noqa: E501

        The last updated time of the geolocation  # noqa: E501

        :return: The last_reported of this XiqDeviceGeolocation.  # noqa: E501
        :rtype: int
        """
        return self._last_reported

    @last_reported.setter
    def last_reported(self, last_reported):
        """Sets the last_reported of this XiqDeviceGeolocation.

        The last updated time of the geolocation  # noqa: E501

        :param last_reported: The last_reported of this XiqDeviceGeolocation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and last_reported is None:  # noqa: E501
            raise ValueError("Invalid value for `last_reported`, must not be `None`")  # noqa: E501

        self._last_reported = last_reported

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
        if not isinstance(other, XiqDeviceGeolocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceGeolocation):
            return True

        return self.to_dict() != other.to_dict()
