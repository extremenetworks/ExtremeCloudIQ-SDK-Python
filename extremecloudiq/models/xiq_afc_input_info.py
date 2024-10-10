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


class XiqAfcInputInfo(object):
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
        'serial_number': 'str',
        'coordinates': 'XiqApCoordinates',
        'elevation': 'XiqElevation',
        'ellipse': 'XiqEllipse',
        'environment': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'coordinates': 'coordinates',
        'elevation': 'elevation',
        'ellipse': 'ellipse',
        'environment': 'environment'
    }

    def __init__(self, serial_number=None, coordinates=None, elevation=None, ellipse=None, environment=None, local_vars_configuration=None):  # noqa: E501
        """XiqAfcInputInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._serial_number = None
        self._coordinates = None
        self._elevation = None
        self._ellipse = None
        self._environment = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number
        if coordinates is not None:
            self.coordinates = coordinates
        if elevation is not None:
            self.elevation = elevation
        if ellipse is not None:
            self.ellipse = ellipse
        if environment is not None:
            self.environment = environment

    @property
    def serial_number(self):
        """Gets the serial_number of this XiqAfcInputInfo.  # noqa: E501


        :return: The serial_number of this XiqAfcInputInfo.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XiqAfcInputInfo.


        :param serial_number: The serial_number of this XiqAfcInputInfo.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def coordinates(self):
        """Gets the coordinates of this XiqAfcInputInfo.  # noqa: E501


        :return: The coordinates of this XiqAfcInputInfo.  # noqa: E501
        :rtype: XiqApCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this XiqAfcInputInfo.


        :param coordinates: The coordinates of this XiqAfcInputInfo.  # noqa: E501
        :type: XiqApCoordinates
        """

        self._coordinates = coordinates

    @property
    def elevation(self):
        """Gets the elevation of this XiqAfcInputInfo.  # noqa: E501


        :return: The elevation of this XiqAfcInputInfo.  # noqa: E501
        :rtype: XiqElevation
        """
        return self._elevation

    @elevation.setter
    def elevation(self, elevation):
        """Sets the elevation of this XiqAfcInputInfo.


        :param elevation: The elevation of this XiqAfcInputInfo.  # noqa: E501
        :type: XiqElevation
        """

        self._elevation = elevation

    @property
    def ellipse(self):
        """Gets the ellipse of this XiqAfcInputInfo.  # noqa: E501


        :return: The ellipse of this XiqAfcInputInfo.  # noqa: E501
        :rtype: XiqEllipse
        """
        return self._ellipse

    @ellipse.setter
    def ellipse(self, ellipse):
        """Sets the ellipse of this XiqAfcInputInfo.


        :param ellipse: The ellipse of this XiqAfcInputInfo.  # noqa: E501
        :type: XiqEllipse
        """

        self._ellipse = ellipse

    @property
    def environment(self):
        """Gets the environment of this XiqAfcInputInfo.  # noqa: E501


        :return: The environment of this XiqAfcInputInfo.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this XiqAfcInputInfo.


        :param environment: The environment of this XiqAfcInputInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["INDOOR", "OUTDOOR", "UNDERSEAT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and environment not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `environment` ({0}), must be one of {1}"  # noqa: E501
                .format(environment, allowed_values)
            )

        self._environment = environment

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
        if not isinstance(other, XiqAfcInputInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAfcInputInfo):
            return True

        return self.to_dict() != other.to_dict()
