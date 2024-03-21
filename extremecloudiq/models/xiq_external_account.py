# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqExternalAccount(object):
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
        'name': 'str',
        'alias': 'str',
        'active': 'bool',
        'data_center': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'alias': 'alias',
        'active': 'active',
        'data_center': 'data_center'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, alias=None, active=None, data_center=None, local_vars_configuration=None):  # noqa: E501
        """XiqExternalAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._alias = None
        self._active = None
        self._data_center = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.name = name
        self.alias = alias
        self.active = active
        self.data_center = data_center

    @property
    def id(self):
        """Gets the id of this XiqExternalAccount.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqExternalAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqExternalAccount.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqExternalAccount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqExternalAccount.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqExternalAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqExternalAccount.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqExternalAccount.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqExternalAccount.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqExternalAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqExternalAccount.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqExternalAccount.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqExternalAccount.  # noqa: E501

        The external account name  # noqa: E501

        :return: The name of this XiqExternalAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqExternalAccount.

        The external account name  # noqa: E501

        :param name: The name of this XiqExternalAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def alias(self):
        """Gets the alias of this XiqExternalAccount.  # noqa: E501

        The external account alias  # noqa: E501

        :return: The alias of this XiqExternalAccount.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this XiqExternalAccount.

        The external account alias  # noqa: E501

        :param alias: The alias of this XiqExternalAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and alias is None:  # noqa: E501
            raise ValueError("Invalid value for `alias`, must not be `None`")  # noqa: E501

        self._alias = alias

    @property
    def active(self):
        """Gets the active of this XiqExternalAccount.  # noqa: E501

        Enable or not  # noqa: E501

        :return: The active of this XiqExternalAccount.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this XiqExternalAccount.

        Enable or not  # noqa: E501

        :param active: The active of this XiqExternalAccount.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def data_center(self):
        """Gets the data_center of this XiqExternalAccount.  # noqa: E501

        The data center to store the VIQ data  # noqa: E501

        :return: The data_center of this XiqExternalAccount.  # noqa: E501
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this XiqExternalAccount.

        The data center to store the VIQ data  # noqa: E501

        :param data_center: The data_center of this XiqExternalAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_center is None:  # noqa: E501
            raise ValueError("Invalid value for `data_center`, must not be `None`")  # noqa: E501

        self._data_center = data_center

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
        if not isinstance(other, XiqExternalAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqExternalAccount):
            return True

        return self.to_dict() != other.to_dict()
