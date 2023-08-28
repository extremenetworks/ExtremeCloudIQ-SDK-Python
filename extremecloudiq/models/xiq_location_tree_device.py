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


class XiqLocationTreeDevice(object):
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
        'device_name': 'str',
        'serial_number': 'str',
        'mac_address': 'str',
        'device_function': 'str',
        'product_type': 'str',
        'ip_address': 'str',
        'location_id': 'int',
        'map_name': 'str',
        'x': 'float',
        'y': 'float',
        'scale_x': 'float',
        'scale_y': 'float'
    }

    attribute_map = {
        'device_name': 'device_name',
        'serial_number': 'serial_number',
        'mac_address': 'mac_address',
        'device_function': 'device_function',
        'product_type': 'product_type',
        'ip_address': 'ip_address',
        'location_id': 'location_id',
        'map_name': 'map_name',
        'x': 'x',
        'y': 'y',
        'scale_x': 'scale_x',
        'scale_y': 'scale_y'
    }

    def __init__(self, device_name=None, serial_number=None, mac_address=None, device_function=None, product_type=None, ip_address=None, location_id=None, map_name=None, x=None, y=None, scale_x=None, scale_y=None, local_vars_configuration=None):  # noqa: E501
        """XiqLocationTreeDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_name = None
        self._serial_number = None
        self._mac_address = None
        self._device_function = None
        self._product_type = None
        self._ip_address = None
        self._location_id = None
        self._map_name = None
        self._x = None
        self._y = None
        self._scale_x = None
        self._scale_y = None
        self.discriminator = None

        self.device_name = device_name
        if serial_number is not None:
            self.serial_number = serial_number
        self.mac_address = mac_address
        if device_function is not None:
            self.device_function = device_function
        if product_type is not None:
            self.product_type = product_type
        if ip_address is not None:
            self.ip_address = ip_address
        if location_id is not None:
            self.location_id = location_id
        if map_name is not None:
            self.map_name = map_name
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if scale_x is not None:
            self.scale_x = scale_x
        if scale_y is not None:
            self.scale_y = scale_y

    @property
    def device_name(self):
        """Gets the device_name of this XiqLocationTreeDevice.  # noqa: E501

        The name of the device.  # noqa: E501

        :return: The device_name of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this XiqLocationTreeDevice.

        The name of the device.  # noqa: E501

        :param device_name: The device_name of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_name is None:  # noqa: E501
            raise ValueError("Invalid value for `device_name`, must not be `None`")  # noqa: E501

        self._device_name = device_name

    @property
    def serial_number(self):
        """Gets the serial_number of this XiqLocationTreeDevice.  # noqa: E501

        The device serial number.  # noqa: E501

        :return: The serial_number of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XiqLocationTreeDevice.

        The device serial number.  # noqa: E501

        :param serial_number: The serial_number of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqLocationTreeDevice.  # noqa: E501

        The device MAC address.  # noqa: E501

        :return: The mac_address of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqLocationTreeDevice.

        The device MAC address.  # noqa: E501

        :param mac_address: The mac_address of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mac_address is None:  # noqa: E501
            raise ValueError("Invalid value for `mac_address`, must not be `None`")  # noqa: E501

        self._mac_address = mac_address

    @property
    def device_function(self):
        """Gets the device_function of this XiqLocationTreeDevice.  # noqa: E501

        The device function, such as AP, Router, Switch, etc.  # noqa: E501

        :return: The device_function of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._device_function

    @device_function.setter
    def device_function(self, device_function):
        """Sets the device_function of this XiqLocationTreeDevice.

        The device function, such as AP, Router, Switch, etc.  # noqa: E501

        :param device_function: The device_function of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """

        self._device_function = device_function

    @property
    def product_type(self):
        """Gets the product_type of this XiqLocationTreeDevice.  # noqa: E501

        The product type, such as: AP_230, BR_100, NX9600, etc.  # noqa: E501

        :return: The product_type of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this XiqLocationTreeDevice.

        The product type, such as: AP_230, BR_100, NX9600, etc.  # noqa: E501

        :param product_type: The product_type of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def ip_address(self):
        """Gets the ip_address of this XiqLocationTreeDevice.  # noqa: E501

        The device IPv4 address.  # noqa: E501

        :return: The ip_address of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this XiqLocationTreeDevice.

        The device IPv4 address.  # noqa: E501

        :param ip_address: The ip_address of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def location_id(self):
        """Gets the location_id of this XiqLocationTreeDevice.  # noqa: E501

        The location ID of the device on the location hierarchy.  # noqa: E501

        :return: The location_id of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqLocationTreeDevice.

        The location ID of the device on the location hierarchy.  # noqa: E501

        :param location_id: The location_id of this XiqLocationTreeDevice.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def map_name(self):
        """Gets the map_name of this XiqLocationTreeDevice.  # noqa: E501

        The associated background map for the device.  # noqa: E501

        :return: The map_name of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: str
        """
        return self._map_name

    @map_name.setter
    def map_name(self, map_name):
        """Sets the map_name of this XiqLocationTreeDevice.

        The associated background map for the device.  # noqa: E501

        :param map_name: The map_name of this XiqLocationTreeDevice.  # noqa: E501
        :type: str
        """

        self._map_name = map_name

    @property
    def x(self):
        """Gets the x of this XiqLocationTreeDevice.  # noqa: E501

        The x-position of the device relative to the horizontal scale in meter.  # noqa: E501

        :return: The x of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this XiqLocationTreeDevice.

        The x-position of the device relative to the horizontal scale in meter.  # noqa: E501

        :param x: The x of this XiqLocationTreeDevice.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this XiqLocationTreeDevice.  # noqa: E501

        The y-position of the device relative to the vertical scale in meter.  # noqa: E501

        :return: The y of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this XiqLocationTreeDevice.

        The y-position of the device relative to the vertical scale in meter.  # noqa: E501

        :param y: The y of this XiqLocationTreeDevice.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def scale_x(self):
        """Gets the scale_x of this XiqLocationTreeDevice.  # noqa: E501

        The horizontal scale for the background map in meter.  # noqa: E501

        :return: The scale_x of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: float
        """
        return self._scale_x

    @scale_x.setter
    def scale_x(self, scale_x):
        """Sets the scale_x of this XiqLocationTreeDevice.

        The horizontal scale for the background map in meter.  # noqa: E501

        :param scale_x: The scale_x of this XiqLocationTreeDevice.  # noqa: E501
        :type: float
        """

        self._scale_x = scale_x

    @property
    def scale_y(self):
        """Gets the scale_y of this XiqLocationTreeDevice.  # noqa: E501

        The vertical scale for the background map in meter.  # noqa: E501

        :return: The scale_y of this XiqLocationTreeDevice.  # noqa: E501
        :rtype: float
        """
        return self._scale_y

    @scale_y.setter
    def scale_y(self, scale_y):
        """Sets the scale_y of this XiqLocationTreeDevice.

        The vertical scale for the background map in meter.  # noqa: E501

        :param scale_y: The scale_y of this XiqLocationTreeDevice.  # noqa: E501
        :type: float
        """

        self._scale_y = scale_y

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
        if not isinstance(other, XiqLocationTreeDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqLocationTreeDevice):
            return True

        return self.to_dict() != other.to_dict()