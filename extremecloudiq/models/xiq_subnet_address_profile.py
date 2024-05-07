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


class XiqSubnetAddressProfile(object):
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
        'predefined': 'bool',
        'name': 'str',
        'description': 'str',
        'value': 'str',
        'enable_classification': 'bool',
        'address_type': 'XiqL3AddressType',
        'classified_entries': 'list[XiqAddressProfileClassifiedEntry]',
        'netmask': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'predefined': 'predefined',
        'name': 'name',
        'description': 'description',
        'value': 'value',
        'enable_classification': 'enable_classification',
        'address_type': 'address_type',
        'classified_entries': 'classified_entries',
        'netmask': 'netmask'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, predefined=None, name=None, description=None, value=None, enable_classification=None, address_type=None, classified_entries=None, netmask=None, local_vars_configuration=None):  # noqa: E501
        """XiqSubnetAddressProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._predefined = None
        self._name = None
        self._description = None
        self._value = None
        self._enable_classification = None
        self._address_type = None
        self._classified_entries = None
        self._netmask = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if predefined is not None:
            self.predefined = predefined
        self.name = name
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value
        if enable_classification is not None:
            self.enable_classification = enable_classification
        self.address_type = address_type
        if classified_entries is not None:
            self.classified_entries = classified_entries
        if netmask is not None:
            self.netmask = netmask

    @property
    def id(self):
        """Gets the id of this XiqSubnetAddressProfile.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqSubnetAddressProfile.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqSubnetAddressProfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqSubnetAddressProfile.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqSubnetAddressProfile.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqSubnetAddressProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqSubnetAddressProfile.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqSubnetAddressProfile.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqSubnetAddressProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqSubnetAddressProfile.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqSubnetAddressProfile.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqSubnetAddressProfile.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def predefined(self):
        """Gets the predefined of this XiqSubnetAddressProfile.  # noqa: E501

        Flag to describe whether the application is predefined or customised  # noqa: E501

        :return: The predefined of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqSubnetAddressProfile.

        Flag to describe whether the application is predefined or customised  # noqa: E501

        :param predefined: The predefined of this XiqSubnetAddressProfile.  # noqa: E501
        :type: bool
        """

        self._predefined = predefined

    @property
    def name(self):
        """Gets the name of this XiqSubnetAddressProfile.  # noqa: E501

        Address profile name  # noqa: E501

        :return: The name of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqSubnetAddressProfile.

        Address profile name  # noqa: E501

        :param name: The name of this XiqSubnetAddressProfile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqSubnetAddressProfile.  # noqa: E501

        Address profile description  # noqa: E501

        :return: The description of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqSubnetAddressProfile.

        Address profile description  # noqa: E501

        :param description: The description of this XiqSubnetAddressProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value(self):
        """Gets the value of this XiqSubnetAddressProfile.  # noqa: E501

        Address profile value  # noqa: E501

        :return: The value of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this XiqSubnetAddressProfile.

        Address profile value  # noqa: E501

        :param value: The value of this XiqSubnetAddressProfile.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def enable_classification(self):
        """Gets the enable_classification of this XiqSubnetAddressProfile.  # noqa: E501

        The flag to enable classification on L3 address profile  # noqa: E501

        :return: The enable_classification of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_classification

    @enable_classification.setter
    def enable_classification(self, enable_classification):
        """Sets the enable_classification of this XiqSubnetAddressProfile.

        The flag to enable classification on L3 address profile  # noqa: E501

        :param enable_classification: The enable_classification of this XiqSubnetAddressProfile.  # noqa: E501
        :type: bool
        """

        self._enable_classification = enable_classification

    @property
    def address_type(self):
        """Gets the address_type of this XiqSubnetAddressProfile.  # noqa: E501


        :return: The address_type of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: XiqL3AddressType
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this XiqSubnetAddressProfile.


        :param address_type: The address_type of this XiqSubnetAddressProfile.  # noqa: E501
        :type: XiqL3AddressType
        """
        if self.local_vars_configuration.client_side_validation and address_type is None:  # noqa: E501
            raise ValueError("Invalid value for `address_type`, must not be `None`")  # noqa: E501

        self._address_type = address_type

    @property
    def classified_entries(self):
        """Gets the classified_entries of this XiqSubnetAddressProfile.  # noqa: E501

        The address profile classified entries  # noqa: E501

        :return: The classified_entries of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: list[XiqAddressProfileClassifiedEntry]
        """
        return self._classified_entries

    @classified_entries.setter
    def classified_entries(self, classified_entries):
        """Sets the classified_entries of this XiqSubnetAddressProfile.

        The address profile classified entries  # noqa: E501

        :param classified_entries: The classified_entries of this XiqSubnetAddressProfile.  # noqa: E501
        :type: list[XiqAddressProfileClassifiedEntry]
        """

        self._classified_entries = classified_entries

    @property
    def netmask(self):
        """Gets the netmask of this XiqSubnetAddressProfile.  # noqa: E501

        The Subnet address netmask.  # noqa: E501

        :return: The netmask of this XiqSubnetAddressProfile.  # noqa: E501
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this XiqSubnetAddressProfile.

        The Subnet address netmask.  # noqa: E501

        :param netmask: The netmask of this XiqSubnetAddressProfile.  # noqa: E501
        :type: str
        """

        self._netmask = netmask

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
        if not isinstance(other, XiqSubnetAddressProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSubnetAddressProfile):
            return True

        return self.to_dict() != other.to_dict()