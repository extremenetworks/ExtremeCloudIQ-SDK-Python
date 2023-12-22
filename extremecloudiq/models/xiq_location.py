# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqLocation(object):
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
        'type': 'str',
        'address': 'str',
        'children': 'list[XiqLocation]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'parent_id': 'parent_id',
        'name': 'name',
        'unique_name': 'unique_name',
        'type': 'type',
        'address': 'address',
        'children': 'children'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, parent_id=None, name=None, unique_name=None, type=None, address=None, children=None, local_vars_configuration=None):  # noqa: E501
        """XiqLocation - a model defined in OpenAPI"""  # noqa: E501
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
        self._type = None
        self._address = None
        self._children = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if parent_id is not None:
            self.parent_id = parent_id
        self.name = name
        self.unique_name = unique_name
        self.type = type
        if address is not None:
            self.address = address
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this XiqLocation.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqLocation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqLocation.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqLocation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqLocation.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqLocation.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqLocation.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqLocation.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqLocation.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqLocation.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqLocation.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqLocation.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqLocation.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqLocation.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def parent_id(self):
        """Gets the parent_id of this XiqLocation.  # noqa: E501

        The parent location ID  # noqa: E501

        :return: The parent_id of this XiqLocation.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this XiqLocation.

        The parent location ID  # noqa: E501

        :param parent_id: The parent_id of this XiqLocation.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this XiqLocation.  # noqa: E501

        The location name  # noqa: E501

        :return: The name of this XiqLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqLocation.

        The location name  # noqa: E501

        :param name: The name of this XiqLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def unique_name(self):
        """Gets the unique_name of this XiqLocation.  # noqa: E501

        The unique location name  # noqa: E501

        :return: The unique_name of this XiqLocation.  # noqa: E501
        :rtype: str
        """
        return self._unique_name

    @unique_name.setter
    def unique_name(self, unique_name):
        """Sets the unique_name of this XiqLocation.

        The unique location name  # noqa: E501

        :param unique_name: The unique_name of this XiqLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and unique_name is None:  # noqa: E501
            raise ValueError("Invalid value for `unique_name`, must not be `None`")  # noqa: E501

        self._unique_name = unique_name

    @property
    def type(self):
        """Gets the type of this XiqLocation.  # noqa: E501

        The location type  # noqa: E501

        :return: The type of this XiqLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XiqLocation.

        The location type  # noqa: E501

        :param type: The type of this XiqLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def address(self):
        """Gets the address of this XiqLocation.  # noqa: E501

        The address for the location  # noqa: E501

        :return: The address of this XiqLocation.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this XiqLocation.

        The address for the location  # noqa: E501

        :param address: The address of this XiqLocation.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def children(self):
        """Gets the children of this XiqLocation.  # noqa: E501

        The child locations  # noqa: E501

        :return: The children of this XiqLocation.  # noqa: E501
        :rtype: list[XiqLocation]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this XiqLocation.

        The child locations  # noqa: E501

        :param children: The children of this XiqLocation.  # noqa: E501
        :type: list[XiqLocation]
        """

        self._children = children

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
        if not isinstance(other, XiqLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqLocation):
            return True

        return self.to_dict() != other.to_dict()
