# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceLocation(object):
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
        'create_time': 'datetime',
        'update_time': 'datetime',
        'org_id': 'int',
        'parent_id': 'int',
        'location_name': 'str',
        'location_unique_name': 'str',
        'location_type': 'str',
        'location_address': 'str',
        'x': 'float',
        'y': 'float',
        'latitude': 'float',
        'longitude': 'float'
    }

    attribute_map = {
        'location_id': 'location_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'parent_id': 'parent_id',
        'location_name': 'location_name',
        'location_unique_name': 'location_unique_name',
        'location_type': 'location_type',
        'location_address': 'location_address',
        'x': 'x',
        'y': 'y',
        'latitude': 'latitude',
        'longitude': 'longitude'
    }

    def __init__(self, location_id=None, create_time=None, update_time=None, org_id=None, parent_id=None, location_name=None, location_unique_name=None, location_type=None, location_address=None, x=None, y=None, latitude=None, longitude=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location_id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._parent_id = None
        self._location_name = None
        self._location_unique_name = None
        self._location_type = None
        self._location_address = None
        self._x = None
        self._y = None
        self._latitude = None
        self._longitude = None
        self.discriminator = None

        if location_id is not None:
            self.location_id = location_id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if parent_id is not None:
            self.parent_id = parent_id
        self.location_name = location_name
        self.location_unique_name = location_unique_name
        self.location_type = location_type
        if location_address is not None:
            self.location_address = location_address
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
        """Gets the location_id of this XiqDeviceLocation.  # noqa: E501

        The assigned location ID, it must NOT be BUILDING type  # noqa: E501

        :return: The location_id of this XiqDeviceLocation.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqDeviceLocation.

        The assigned location ID, it must NOT be BUILDING type  # noqa: E501

        :param location_id: The location_id of this XiqDeviceLocation.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def create_time(self):
        """Gets the create_time of this XiqDeviceLocation.  # noqa: E501

        The timestamp when the device assigned to the location  # noqa: E501

        :return: The create_time of this XiqDeviceLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqDeviceLocation.

        The timestamp when the device assigned to the location  # noqa: E501

        :param create_time: The create_time of this XiqDeviceLocation.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqDeviceLocation.  # noqa: E501

        The timestamp when the location info was last updated  # noqa: E501

        :return: The update_time of this XiqDeviceLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqDeviceLocation.

        The timestamp when the location info was last updated  # noqa: E501

        :param update_time: The update_time of this XiqDeviceLocation.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqDeviceLocation.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqDeviceLocation.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqDeviceLocation.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqDeviceLocation.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def parent_id(self):
        """Gets the parent_id of this XiqDeviceLocation.  # noqa: E501

        The parent location ID  # noqa: E501

        :return: The parent_id of this XiqDeviceLocation.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this XiqDeviceLocation.

        The parent location ID  # noqa: E501

        :param parent_id: The parent_id of this XiqDeviceLocation.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def location_name(self):
        """Gets the location_name of this XiqDeviceLocation.  # noqa: E501

        The location name  # noqa: E501

        :return: The location_name of this XiqDeviceLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this XiqDeviceLocation.

        The location name  # noqa: E501

        :param location_name: The location_name of this XiqDeviceLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and location_name is None:  # noqa: E501
            raise ValueError("Invalid value for `location_name`, must not be `None`")  # noqa: E501

        self._location_name = location_name

    @property
    def location_unique_name(self):
        """Gets the location_unique_name of this XiqDeviceLocation.  # noqa: E501

        The unique location name  # noqa: E501

        :return: The location_unique_name of this XiqDeviceLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_unique_name

    @location_unique_name.setter
    def location_unique_name(self, location_unique_name):
        """Sets the location_unique_name of this XiqDeviceLocation.

        The unique location name  # noqa: E501

        :param location_unique_name: The location_unique_name of this XiqDeviceLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and location_unique_name is None:  # noqa: E501
            raise ValueError("Invalid value for `location_unique_name`, must not be `None`")  # noqa: E501

        self._location_unique_name = location_unique_name

    @property
    def location_type(self):
        """Gets the location_type of this XiqDeviceLocation.  # noqa: E501

        The location type  # noqa: E501

        :return: The location_type of this XiqDeviceLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this XiqDeviceLocation.

        The location type  # noqa: E501

        :param location_type: The location_type of this XiqDeviceLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and location_type is None:  # noqa: E501
            raise ValueError("Invalid value for `location_type`, must not be `None`")  # noqa: E501

        self._location_type = location_type

    @property
    def location_address(self):
        """Gets the location_address of this XiqDeviceLocation.  # noqa: E501

        The address for the location  # noqa: E501

        :return: The location_address of this XiqDeviceLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_address

    @location_address.setter
    def location_address(self, location_address):
        """Sets the location_address of this XiqDeviceLocation.

        The address for the location  # noqa: E501

        :param location_address: The location_address of this XiqDeviceLocation.  # noqa: E501
        :type: str
        """

        self._location_address = location_address

    @property
    def x(self):
        """Gets the x of this XiqDeviceLocation.  # noqa: E501

        The horizontal value in the floor map  # noqa: E501

        :return: The x of this XiqDeviceLocation.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this XiqDeviceLocation.

        The horizontal value in the floor map  # noqa: E501

        :param x: The x of this XiqDeviceLocation.  # noqa: E501
        :type: float
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this XiqDeviceLocation.  # noqa: E501

        The vertical value in the floor map  # noqa: E501

        :return: The y of this XiqDeviceLocation.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this XiqDeviceLocation.

        The vertical value in the floor map  # noqa: E501

        :param y: The y of this XiqDeviceLocation.  # noqa: E501
        :type: float
        """

        self._y = y

    @property
    def latitude(self):
        """Gets the latitude of this XiqDeviceLocation.  # noqa: E501

        The latitude in the geography  # noqa: E501

        :return: The latitude of this XiqDeviceLocation.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this XiqDeviceLocation.

        The latitude in the geography  # noqa: E501

        :param latitude: The latitude of this XiqDeviceLocation.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this XiqDeviceLocation.  # noqa: E501

        The longitude in the geography  # noqa: E501

        :return: The longitude of this XiqDeviceLocation.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this XiqDeviceLocation.

        The longitude in the geography  # noqa: E501

        :param longitude: The longitude of this XiqDeviceLocation.  # noqa: E501
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
        if not isinstance(other, XiqDeviceLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceLocation):
            return True

        return self.to_dict() != other.to_dict()
