# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqFloor(object):
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
        'id': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'org_id': 'int',
        'parent_id': 'int',
        'name': 'str',
        'unique_name': 'str',
        'environment': 'XiqRfEnvironmentType',
        'db_attenuation': 'float',
        'measurement_unit': 'XiqMeasurementUnit',
        'installation_height': 'float',
        'map_size_width': 'float',
        'map_size_height': 'float',
        'map_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'parent_id': 'parent_id',
        'name': 'name',
        'unique_name': 'unique_name',
        'environment': 'environment',
        'db_attenuation': 'db_attenuation',
        'measurement_unit': 'measurement_unit',
        'installation_height': 'installation_height',
        'map_size_width': 'map_size_width',
        'map_size_height': 'map_size_height',
        'map_name': 'map_name'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, parent_id=None, name=None, unique_name=None, environment=None, db_attenuation=None, measurement_unit=None, installation_height=None, map_size_width=None, map_size_height=None, map_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqFloor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._parent_id = None
        self._name = None
        self._unique_name = None
        self._environment = None
        self._db_attenuation = None
        self._measurement_unit = None
        self._installation_height = None
        self._map_size_width = None
        self._map_size_height = None
        self._map_name = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.parent_id = parent_id
        self.name = name
        self.unique_name = unique_name
        self.environment = environment
        self.db_attenuation = db_attenuation
        self.measurement_unit = measurement_unit
        self.installation_height = installation_height
        if map_size_width is not None:
            self.map_size_width = map_size_width
        if map_size_height is not None:
            self.map_size_height = map_size_height
        if map_name is not None:
            self.map_name = map_name

    @property
    def id(self):
        """Gets the id of this XiqFloor.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqFloor.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqFloor.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqFloor.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqFloor.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqFloor.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqFloor.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqFloor.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqFloor.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqFloor.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqFloor.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqFloor.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqFloor.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqFloor.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqFloor.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqFloor.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def parent_id(self):
        """Gets the parent_id of this XiqFloor.  # noqa: E501

        The parent building ID  # noqa: E501

        :return: The parent_id of this XiqFloor.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this XiqFloor.

        The parent building ID  # noqa: E501

        :param parent_id: The parent_id of this XiqFloor.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and parent_id is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_id`, must not be `None`")  # noqa: E501

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this XiqFloor.  # noqa: E501

        The floor name  # noqa: E501

        :return: The name of this XiqFloor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqFloor.

        The floor name  # noqa: E501

        :param name: The name of this XiqFloor.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unique_name(self):
        """Gets the unique_name of this XiqFloor.  # noqa: E501

        The floor unique name  # noqa: E501

        :return: The unique_name of this XiqFloor.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this XiqFloor.

        The floor unique name  # noqa: E501

        :param unique_name: The unique_name of this XiqFloor.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unique_name is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_name`, must not be `None`")  # noqa: E501

        self._unique_name = unique_name

    @property
    def environment(self):
        """Gets the environment of this XiqFloor.  # noqa: E501


        :return: The environment of this XiqFloor.  # noqa: E501
        :rtype: XiqRfEnvironmentType
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this XiqFloor.


        :param environment: The environment of this XiqFloor.  # noqa: E501
        :type: XiqRfEnvironmentType
        """
        if self.local_vars_configuration.client_side_validation and environment is None:  # noqa: E501
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def db_attenuation(self):
        """Gets the db_attenuation of this XiqFloor.  # noqa: E501

        The floor attenuation in dBs  # noqa: E501

        :return: The db_attenuation of this XiqFloor.  # noqa: E501
        :rtype: float
        """
        return self._db_attenuation

    @db_attenuation.setter
    def db_attenuation(self, db_attenuation):
        """Sets the db_attenuation of this XiqFloor.

        The floor attenuation in dBs  # noqa: E501

        :param db_attenuation: The db_attenuation of this XiqFloor.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and db_attenuation is None:  # noqa: E501
            raise ValueError("Invalid value for `db_attenuation`, must not be `None`")  # noqa: E501

        self._db_attenuation = db_attenuation

    @property
    def measurement_unit(self):
        """Gets the measurement_unit of this XiqFloor.  # noqa: E501


        :return: The measurement_unit of this XiqFloor.  # noqa: E501
        :rtype: XiqMeasurementUnit
        """
        return self._measurement_unit

    @measurement_unit.setter
    def measurement_unit(self, measurement_unit):
        """Sets the measurement_unit of this XiqFloor.


        :param measurement_unit: The measurement_unit of this XiqFloor.  # noqa: E501
        :type: XiqMeasurementUnit
        """
        if self.local_vars_configuration.client_side_validation and measurement_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `measurement_unit`, must not be `None`")  # noqa: E501

        self._measurement_unit = measurement_unit

    @property
    def installation_height(self):
        """Gets the installation_height of this XiqFloor.  # noqa: E501

        The installation height  # noqa: E501

        :return: The installation_height of this XiqFloor.  # noqa: E501
        :rtype: float
        """
        return self._installation_height

    @installation_height.setter
    def installation_height(self, installation_height):
        """Sets the installation_height of this XiqFloor.

        The installation height  # noqa: E501

        :param installation_height: The installation_height of this XiqFloor.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and installation_height is None:  # noqa: E501
            raise ValueError("Invalid value for `installation_height`, must not be `None`")  # noqa: E501

        self._installation_height = installation_height

    @property
    def map_size_width(self):
        """Gets the map_size_width of this XiqFloor.  # noqa: E501

        The floormap width  # noqa: E501

        :return: The map_size_width of this XiqFloor.  # noqa: E501
        :rtype: float
        """
        return self._map_size_width

    @map_size_width.setter
    def map_size_width(self, map_size_width):
        """Sets the map_size_width of this XiqFloor.

        The floormap width  # noqa: E501

        :param map_size_width: The map_size_width of this XiqFloor.  # noqa: E501
        :type: float
        """

        self._map_size_width = map_size_width

    @property
    def map_size_height(self):
        """Gets the map_size_height of this XiqFloor.  # noqa: E501

        The floormap height  # noqa: E501

        :return: The map_size_height of this XiqFloor.  # noqa: E501
        :rtype: float
        """
        return self._map_size_height

    @map_size_height.setter
    def map_size_height(self, map_size_height):
        """Sets the map_size_height of this XiqFloor.

        The floormap height  # noqa: E501

        :param map_size_height: The map_size_height of this XiqFloor.  # noqa: E501
        :type: float
        """

        self._map_size_height = map_size_height

    @property
    def map_name(self):
        """Gets the map_name of this XiqFloor.  # noqa: E501

        The floormap name  # noqa: E501

        :return: The map_name of this XiqFloor.  # noqa: E501
        :rtype: str
        """
        return self._map_name

    @map_name.setter
    def map_name(self, map_name):
        """Sets the map_name of this XiqFloor.

        The floormap name  # noqa: E501

        :param map_name: The map_name of this XiqFloor.  # noqa: E501
        :type: str
        """

        self._map_name = map_name

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
        if not isinstance(other, XiqFloor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqFloor):
            return True

        return self.to_dict() != other.to_dict()
