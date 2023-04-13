# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqRadiusClientObject(object):
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
        'enable_inject_operator_name_attribute': 'bool',
        'enable_message_authenticator_attribute': 'bool',
        'enable_permit_dynamic_authorization_message_change': 'bool',
        'retry_interval': 'int',
        'accounting_interim_update_interval': 'int',
        'entries': 'list[XiqRadiusClientObjectEntry]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'description': 'description',
        'enable_inject_operator_name_attribute': 'enable_inject_operator_name_attribute',
        'enable_message_authenticator_attribute': 'enable_message_authenticator_attribute',
        'enable_permit_dynamic_authorization_message_change': 'enable_permit_dynamic_authorization_message_change',
        'retry_interval': 'retry_interval',
        'accounting_interim_update_interval': 'accounting_interim_update_interval',
        'entries': 'entries'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, description=None, enable_inject_operator_name_attribute=None, enable_message_authenticator_attribute=None, enable_permit_dynamic_authorization_message_change=None, retry_interval=None, accounting_interim_update_interval=None, entries=None, local_vars_configuration=None):  # noqa: E501
        """XiqRadiusClientObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._description = None
        self._enable_inject_operator_name_attribute = None
        self._enable_message_authenticator_attribute = None
        self._enable_permit_dynamic_authorization_message_change = None
        self._retry_interval = None
        self._accounting_interim_update_interval = None
        self._entries = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.name = name
        if description is not None:
            self.description = description
        self.enable_inject_operator_name_attribute = enable_inject_operator_name_attribute
        self.enable_message_authenticator_attribute = enable_message_authenticator_attribute
        self.enable_permit_dynamic_authorization_message_change = enable_permit_dynamic_authorization_message_change
        self.retry_interval = retry_interval
        self.accounting_interim_update_interval = accounting_interim_update_interval
        self.entries = entries

    @property
    def id(self):
        """Gets the id of this XiqRadiusClientObject.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRadiusClientObject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRadiusClientObject.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRadiusClientObject.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRadiusClientObject.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRadiusClientObject.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRadiusClientObject.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRadiusClientObject.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRadiusClientObject.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRadiusClientObject.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRadiusClientObject.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRadiusClientObject.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqRadiusClientObject.  # noqa: E501

        The RADIUS client object name.  # noqa: E501

        :return: The name of this XiqRadiusClientObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqRadiusClientObject.

        The RADIUS client object name.  # noqa: E501

        :param name: The name of this XiqRadiusClientObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqRadiusClientObject.  # noqa: E501

        The RADIUS client object description.  # noqa: E501

        :return: The description of this XiqRadiusClientObject.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqRadiusClientObject.

        The RADIUS client object description.  # noqa: E501

        :param description: The description of this XiqRadiusClientObject.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_inject_operator_name_attribute(self):
        """Gets the enable_inject_operator_name_attribute of this XiqRadiusClientObject.  # noqa: E501

        The flag for enable inject operator name attribute.  # noqa: E501

        :return: The enable_inject_operator_name_attribute of this XiqRadiusClientObject.  # noqa: E501
        :rtype: bool
        """
        return self._enable_inject_operator_name_attribute

    @enable_inject_operator_name_attribute.setter
    def enable_inject_operator_name_attribute(self, enable_inject_operator_name_attribute):
        """Sets the enable_inject_operator_name_attribute of this XiqRadiusClientObject.

        The flag for enable inject operator name attribute.  # noqa: E501

        :param enable_inject_operator_name_attribute: The enable_inject_operator_name_attribute of this XiqRadiusClientObject.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_inject_operator_name_attribute is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_inject_operator_name_attribute`, must not be `None`")  # noqa: E501

        self._enable_inject_operator_name_attribute = enable_inject_operator_name_attribute

    @property
    def enable_message_authenticator_attribute(self):
        """Gets the enable_message_authenticator_attribute of this XiqRadiusClientObject.  # noqa: E501

        The flag for enable message authenticator attribute  # noqa: E501

        :return: The enable_message_authenticator_attribute of this XiqRadiusClientObject.  # noqa: E501
        :rtype: bool
        """
        return self._enable_message_authenticator_attribute

    @enable_message_authenticator_attribute.setter
    def enable_message_authenticator_attribute(self, enable_message_authenticator_attribute):
        """Sets the enable_message_authenticator_attribute of this XiqRadiusClientObject.

        The flag for enable message authenticator attribute  # noqa: E501

        :param enable_message_authenticator_attribute: The enable_message_authenticator_attribute of this XiqRadiusClientObject.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_message_authenticator_attribute is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_message_authenticator_attribute`, must not be `None`")  # noqa: E501

        self._enable_message_authenticator_attribute = enable_message_authenticator_attribute

    @property
    def enable_permit_dynamic_authorization_message_change(self):
        """Gets the enable_permit_dynamic_authorization_message_change of this XiqRadiusClientObject.  # noqa: E501

        The flag for enable permit dynamic authorization message change  # noqa: E501

        :return: The enable_permit_dynamic_authorization_message_change of this XiqRadiusClientObject.  # noqa: E501
        :rtype: bool
        """
        return self._enable_permit_dynamic_authorization_message_change

    @enable_permit_dynamic_authorization_message_change.setter
    def enable_permit_dynamic_authorization_message_change(self, enable_permit_dynamic_authorization_message_change):
        """Sets the enable_permit_dynamic_authorization_message_change of this XiqRadiusClientObject.

        The flag for enable permit dynamic authorization message change  # noqa: E501

        :param enable_permit_dynamic_authorization_message_change: The enable_permit_dynamic_authorization_message_change of this XiqRadiusClientObject.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_permit_dynamic_authorization_message_change is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_permit_dynamic_authorization_message_change`, must not be `None`")  # noqa: E501

        self._enable_permit_dynamic_authorization_message_change = enable_permit_dynamic_authorization_message_change

    @property
    def retry_interval(self):
        """Gets the retry_interval of this XiqRadiusClientObject.  # noqa: E501

        The retry interval, 60 - 100000000 seconds  # noqa: E501

        :return: The retry_interval of this XiqRadiusClientObject.  # noqa: E501
        :rtype: int
        """
        return self._retry_interval

    @retry_interval.setter
    def retry_interval(self, retry_interval):
        """Sets the retry_interval of this XiqRadiusClientObject.

        The retry interval, 60 - 100000000 seconds  # noqa: E501

        :param retry_interval: The retry_interval of this XiqRadiusClientObject.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and retry_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `retry_interval`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                retry_interval is not None and retry_interval > 100000000):  # noqa: E501
            raise ValueError("Invalid value for `retry_interval`, must be a value less than or equal to `100000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                retry_interval is not None and retry_interval < 60):  # noqa: E501
            raise ValueError("Invalid value for `retry_interval`, must be a value greater than or equal to `60`")  # noqa: E501

        self._retry_interval = retry_interval

    @property
    def accounting_interim_update_interval(self):
        """Gets the accounting_interim_update_interval of this XiqRadiusClientObject.  # noqa: E501

        The accounting interim update interval, 60 - 100000000 seconds  # noqa: E501

        :return: The accounting_interim_update_interval of this XiqRadiusClientObject.  # noqa: E501
        :rtype: int
        """
        return self._accounting_interim_update_interval

    @accounting_interim_update_interval.setter
    def accounting_interim_update_interval(self, accounting_interim_update_interval):
        """Sets the accounting_interim_update_interval of this XiqRadiusClientObject.

        The accounting interim update interval, 60 - 100000000 seconds  # noqa: E501

        :param accounting_interim_update_interval: The accounting_interim_update_interval of this XiqRadiusClientObject.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and accounting_interim_update_interval is None:  # noqa: E501
            raise ValueError("Invalid value for `accounting_interim_update_interval`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accounting_interim_update_interval is not None and accounting_interim_update_interval > 100000000):  # noqa: E501
            raise ValueError("Invalid value for `accounting_interim_update_interval`, must be a value less than or equal to `100000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accounting_interim_update_interval is not None and accounting_interim_update_interval < 60):  # noqa: E501
            raise ValueError("Invalid value for `accounting_interim_update_interval`, must be a value greater than or equal to `60`")  # noqa: E501

        self._accounting_interim_update_interval = accounting_interim_update_interval

    @property
    def entries(self):
        """Gets the entries of this XiqRadiusClientObject.  # noqa: E501

        The list of RADIUS client object entries  # noqa: E501

        :return: The entries of this XiqRadiusClientObject.  # noqa: E501
        :rtype: list[XiqRadiusClientObjectEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this XiqRadiusClientObject.

        The list of RADIUS client object entries  # noqa: E501

        :param entries: The entries of this XiqRadiusClientObject.  # noqa: E501
        :type: list[XiqRadiusClientObjectEntry]
        """
        if self.local_vars_configuration.client_side_validation and entries is None:  # noqa: E501
            raise ValueError("Invalid value for `entries`, must not be `None`")  # noqa: E501

        self._entries = entries

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
        if not isinstance(other, XiqRadiusClientObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRadiusClientObject):
            return True

        return self.to_dict() != other.to_dict()
