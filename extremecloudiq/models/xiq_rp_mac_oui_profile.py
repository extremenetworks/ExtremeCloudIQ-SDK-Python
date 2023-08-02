# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqRpMacOuiProfile(object):
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
        'description': 'str',
        'predefined': 'bool',
        'value': 'str',
        'mac_type': 'str',
        'defender_defined': 'bool',
        'extreme_iot_defined': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'description': 'description',
        'predefined': 'predefined',
        'value': 'value',
        'mac_type': 'mac_type',
        'defender_defined': 'defender_defined',
        'extreme_iot_defined': 'extreme_iot_defined'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, description=None, predefined=None, value=None, mac_type=None, defender_defined=None, extreme_iot_defined=None, local_vars_configuration=None):  # noqa: E501
        """XiqRpMacOuiProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._description = None
        self._predefined = None
        self._value = None
        self._mac_type = None
        self._defender_defined = None
        self._extreme_iot_defined = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if predefined is not None:
            self.predefined = predefined
        if value is not None:
            self.value = value
        if mac_type is not None:
            self.mac_type = mac_type
        if defender_defined is not None:
            self.defender_defined = defender_defined
        if extreme_iot_defined is not None:
            self.extreme_iot_defined = extreme_iot_defined

    @property
    def id(self):
        """Gets the id of this XiqRpMacOuiProfile.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRpMacOuiProfile.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRpMacOuiProfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRpMacOuiProfile.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRpMacOuiProfile.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRpMacOuiProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRpMacOuiProfile.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRpMacOuiProfile.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRpMacOuiProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqRpMacOuiProfile.  # noqa: E501

        The product model  # noqa: E501

        :return: The name of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqRpMacOuiProfile.

        The product model  # noqa: E501

        :param name: The name of this XiqRpMacOuiProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqRpMacOuiProfile.  # noqa: E501

        The product description  # noqa: E501

        :return: The description of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqRpMacOuiProfile.

        The product description  # noqa: E501

        :param description: The description of this XiqRpMacOuiProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def predefined(self):
        """Gets the predefined of this XiqRpMacOuiProfile.  # noqa: E501

        Whether the MAC Oui is predefined.  # noqa: E501

        :return: The predefined of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqRpMacOuiProfile.

        Whether the MAC Oui is predefined.  # noqa: E501

        :param predefined: The predefined of this XiqRpMacOuiProfile.  # noqa: E501
        :type: bool
        """

        self._predefined = predefined

    @property
    def value(self):
        """Gets the value of this XiqRpMacOuiProfile.  # noqa: E501

        The MAC octets  # noqa: E501

        :return: The value of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this XiqRpMacOuiProfile.

        The MAC octets  # noqa: E501

        :param value: The value of this XiqRpMacOuiProfile.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def mac_type(self):
        """Gets the mac_type of this XiqRpMacOuiProfile.  # noqa: E501

        The type or \"MAC_OUI\"  # noqa: E501

        :return: The mac_type of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: str
        """
        return self._mac_type

    @mac_type.setter
    def mac_type(self, mac_type):
        """Sets the mac_type of this XiqRpMacOuiProfile.

        The type or \"MAC_OUI\"  # noqa: E501

        :param mac_type: The mac_type of this XiqRpMacOuiProfile.  # noqa: E501
        :type: str
        """

        self._mac_type = mac_type

    @property
    def defender_defined(self):
        """Gets the defender_defined of this XiqRpMacOuiProfile.  # noqa: E501

        Whether defender is defined  # noqa: E501

        :return: The defender_defined of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: bool
        """
        return self._defender_defined

    @defender_defined.setter
    def defender_defined(self, defender_defined):
        """Sets the defender_defined of this XiqRpMacOuiProfile.

        Whether defender is defined  # noqa: E501

        :param defender_defined: The defender_defined of this XiqRpMacOuiProfile.  # noqa: E501
        :type: bool
        """

        self._defender_defined = defender_defined

    @property
    def extreme_iot_defined(self):
        """Gets the extreme_iot_defined of this XiqRpMacOuiProfile.  # noqa: E501

        Whether is the Extreme Iot Defined  # noqa: E501

        :return: The extreme_iot_defined of this XiqRpMacOuiProfile.  # noqa: E501
        :rtype: bool
        """
        return self._extreme_iot_defined

    @extreme_iot_defined.setter
    def extreme_iot_defined(self, extreme_iot_defined):
        """Sets the extreme_iot_defined of this XiqRpMacOuiProfile.

        Whether is the Extreme Iot Defined  # noqa: E501

        :param extreme_iot_defined: The extreme_iot_defined of this XiqRpMacOuiProfile.  # noqa: E501
        :type: bool
        """

        self._extreme_iot_defined = extreme_iot_defined

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
        if not isinstance(other, XiqRpMacOuiProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRpMacOuiProfile):
            return True

        return self.to_dict() != other.to_dict()
