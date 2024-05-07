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


class XiqRadiusProxy(object):
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
        'name': 'str',
        'description': 'str',
        'format_type': 'XiqRadiusProxyFormatType',
        'retry_count': 'int',
        'retry_delay': 'int',
        'dead_time': 'int',
        'enable_inject_operator_name_attribute': 'bool',
        'clients': 'list[XiqRadiusClient]',
        'realms': 'list[XiqRadiusProxyRealm]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'format_type': 'format_type',
        'retry_count': 'retry_count',
        'retry_delay': 'retry_delay',
        'dead_time': 'dead_time',
        'enable_inject_operator_name_attribute': 'enable_inject_operator_name_attribute',
        'clients': 'clients',
        'realms': 'realms'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, format_type=None, retry_count=None, retry_delay=None, dead_time=None, enable_inject_operator_name_attribute=None, clients=None, realms=None, local_vars_configuration=None):  # noqa: E501
        """XiqRadiusProxy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._format_type = None
        self._retry_count = None
        self._retry_delay = None
        self._dead_time = None
        self._enable_inject_operator_name_attribute = None
        self._clients = None
        self._realms = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if format_type is not None:
            self.format_type = format_type
        if retry_count is not None:
            self.retry_count = retry_count
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if dead_time is not None:
            self.dead_time = dead_time
        if enable_inject_operator_name_attribute is not None:
            self.enable_inject_operator_name_attribute = enable_inject_operator_name_attribute
        if clients is not None:
            self.clients = clients
        if realms is not None:
            self.realms = realms

    @property
    def id(self):
        """Gets the id of this XiqRadiusProxy.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRadiusProxy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRadiusProxy.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRadiusProxy.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRadiusProxy.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRadiusProxy.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRadiusProxy.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRadiusProxy.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRadiusProxy.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRadiusProxy.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRadiusProxy.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRadiusProxy.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqRadiusProxy.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqRadiusProxy.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqRadiusProxy.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqRadiusProxy.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqRadiusProxy.  # noqa: E501

        The RADIUS proxy name  # noqa: E501

        :return: The name of this XiqRadiusProxy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqRadiusProxy.

        The RADIUS proxy name  # noqa: E501

        :param name: The name of this XiqRadiusProxy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqRadiusProxy.  # noqa: E501

        The RADIUS proxy description  # noqa: E501

        :return: The description of this XiqRadiusProxy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqRadiusProxy.

        The RADIUS proxy description  # noqa: E501

        :param description: The description of this XiqRadiusProxy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format_type(self):
        """Gets the format_type of this XiqRadiusProxy.  # noqa: E501


        :return: The format_type of this XiqRadiusProxy.  # noqa: E501
        :rtype: XiqRadiusProxyFormatType
        """
        return self._format_type

    @format_type.setter
    def format_type(self, format_type):
        """Sets the format_type of this XiqRadiusProxy.


        :param format_type: The format_type of this XiqRadiusProxy.  # noqa: E501
        :type: XiqRadiusProxyFormatType
        """

        self._format_type = format_type

    @property
    def retry_count(self):
        """Gets the retry_count of this XiqRadiusProxy.  # noqa: E501

        The retry count of RADIUS proxy  # noqa: E501

        :return: The retry_count of this XiqRadiusProxy.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this XiqRadiusProxy.

        The retry count of RADIUS proxy  # noqa: E501

        :param retry_count: The retry_count of this XiqRadiusProxy.  # noqa: E501
        :type: int
        """

        self._retry_count = retry_count

    @property
    def retry_delay(self):
        """Gets the retry_delay of this XiqRadiusProxy.  # noqa: E501

        The retry delay of RADIUS proxy  # noqa: E501

        :return: The retry_delay of this XiqRadiusProxy.  # noqa: E501
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this XiqRadiusProxy.

        The retry delay of RADIUS proxy  # noqa: E501

        :param retry_delay: The retry_delay of this XiqRadiusProxy.  # noqa: E501
        :type: int
        """

        self._retry_delay = retry_delay

    @property
    def dead_time(self):
        """Gets the dead_time of this XiqRadiusProxy.  # noqa: E501

        The dead time of RADIUS proxy  # noqa: E501

        :return: The dead_time of this XiqRadiusProxy.  # noqa: E501
        :rtype: int
        """
        return self._dead_time

    @dead_time.setter
    def dead_time(self, dead_time):
        """Sets the dead_time of this XiqRadiusProxy.

        The dead time of RADIUS proxy  # noqa: E501

        :param dead_time: The dead_time of this XiqRadiusProxy.  # noqa: E501
        :type: int
        """

        self._dead_time = dead_time

    @property
    def enable_inject_operator_name_attribute(self):
        """Gets the enable_inject_operator_name_attribute of this XiqRadiusProxy.  # noqa: E501

        The flag for enable inject operator name attribute  # noqa: E501

        :return: The enable_inject_operator_name_attribute of this XiqRadiusProxy.  # noqa: E501
        :rtype: bool
        """
        return self._enable_inject_operator_name_attribute

    @enable_inject_operator_name_attribute.setter
    def enable_inject_operator_name_attribute(self, enable_inject_operator_name_attribute):
        """Sets the enable_inject_operator_name_attribute of this XiqRadiusProxy.

        The flag for enable inject operator name attribute  # noqa: E501

        :param enable_inject_operator_name_attribute: The enable_inject_operator_name_attribute of this XiqRadiusProxy.  # noqa: E501
        :type: bool
        """

        self._enable_inject_operator_name_attribute = enable_inject_operator_name_attribute

    @property
    def clients(self):
        """Gets the clients of this XiqRadiusProxy.  # noqa: E501

        The RADIUS clients of RADIUS proxy  # noqa: E501

        :return: The clients of this XiqRadiusProxy.  # noqa: E501
        :rtype: list[XiqRadiusClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this XiqRadiusProxy.

        The RADIUS clients of RADIUS proxy  # noqa: E501

        :param clients: The clients of this XiqRadiusProxy.  # noqa: E501
        :type: list[XiqRadiusClient]
        """

        self._clients = clients

    @property
    def realms(self):
        """Gets the realms of this XiqRadiusProxy.  # noqa: E501

        The RADIUS realms of RADIUS proxy  # noqa: E501

        :return: The realms of this XiqRadiusProxy.  # noqa: E501
        :rtype: list[XiqRadiusProxyRealm]
        """
        return self._realms

    @realms.setter
    def realms(self, realms):
        """Sets the realms of this XiqRadiusProxy.

        The RADIUS realms of RADIUS proxy  # noqa: E501

        :param realms: The realms of this XiqRadiusProxy.  # noqa: E501
        :type: list[XiqRadiusProxyRealm]
        """

        self._realms = realms

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
        if not isinstance(other, XiqRadiusProxy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRadiusProxy):
            return True

        return self.to_dict() != other.to_dict()
