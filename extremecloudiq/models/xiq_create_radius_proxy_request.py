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


class XiqCreateRadiusProxyRequest(object):
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
        'name': 'str',
        'description': 'str',
        'format_type': 'XiqRadiusProxyFormatType',
        'retry_count': 'int',
        'retry_delay': 'int',
        'dead_time': 'int',
        'enable_inject_operator_name_attribute': 'bool',
        'clients': 'list[XiqCreateRadiusClient]',
        'realms': 'list[XiqCreateRadiusProxyRealm]',
        'device_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'format_type': 'format_type',
        'retry_count': 'retry_count',
        'retry_delay': 'retry_delay',
        'dead_time': 'dead_time',
        'enable_inject_operator_name_attribute': 'enable_inject_operator_name_attribute',
        'clients': 'clients',
        'realms': 'realms',
        'device_ids': 'device_ids'
    }

    def __init__(self, name=None, description=None, format_type=None, retry_count=None, retry_delay=None, dead_time=None, enable_inject_operator_name_attribute=None, clients=None, realms=None, device_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqCreateRadiusProxyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._format_type = None
        self._retry_count = None
        self._retry_delay = None
        self._dead_time = None
        self._enable_inject_operator_name_attribute = None
        self._clients = None
        self._realms = None
        self._device_ids = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.format_type = format_type
        self.retry_count = retry_count
        self.retry_delay = retry_delay
        self.dead_time = dead_time
        if enable_inject_operator_name_attribute is not None:
            self.enable_inject_operator_name_attribute = enable_inject_operator_name_attribute
        if clients is not None:
            self.clients = clients
        self.realms = realms
        self.device_ids = device_ids

    @property
    def name(self):
        """Gets the name of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The RADIUS proxy name  # noqa: E501

        :return: The name of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqCreateRadiusProxyRequest.

        The RADIUS proxy name  # noqa: E501

        :param name: The name of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The RADIUS proxy description  # noqa: E501

        :return: The description of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqCreateRadiusProxyRequest.

        The RADIUS proxy description  # noqa: E501

        :param description: The description of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format_type(self):
        """Gets the format_type of this XiqCreateRadiusProxyRequest.  # noqa: E501


        :return: The format_type of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: XiqRadiusProxyFormatType
        """
        return self._format_type

    @format_type.setter
    def format_type(self, format_type):
        """Sets the format_type of this XiqCreateRadiusProxyRequest.


        :param format_type: The format_type of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: XiqRadiusProxyFormatType
        """
        if self.local_vars_configuration.client_side_validation and format_type is None:  # noqa: E501
            raise ValueError("Invalid value for `format_type`, must not be `None`")  # noqa: E501

        self._format_type = format_type

    @property
    def retry_count(self):
        """Gets the retry_count of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The retry count of RADIUS proxy  # noqa: E501

        :return: The retry_count of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: int
        """
        return self._retry_count

    @retry_count.setter
    def retry_count(self, retry_count):
        """Sets the retry_count of this XiqCreateRadiusProxyRequest.

        The retry count of RADIUS proxy  # noqa: E501

        :param retry_count: The retry_count of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and retry_count is None:  # noqa: E501
            raise ValueError("Invalid value for `retry_count`, must not be `None`")  # noqa: E501

        self._retry_count = retry_count

    @property
    def retry_delay(self):
        """Gets the retry_delay of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The retry delay of RADIUS proxy  # noqa: E501

        :return: The retry_delay of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this XiqCreateRadiusProxyRequest.

        The retry delay of RADIUS proxy  # noqa: E501

        :param retry_delay: The retry_delay of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and retry_delay is None:  # noqa: E501
            raise ValueError("Invalid value for `retry_delay`, must not be `None`")  # noqa: E501

        self._retry_delay = retry_delay

    @property
    def dead_time(self):
        """Gets the dead_time of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The dead time of RADIUS proxy  # noqa: E501

        :return: The dead_time of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: int
        """
        return self._dead_time

    @dead_time.setter
    def dead_time(self, dead_time):
        """Sets the dead_time of this XiqCreateRadiusProxyRequest.

        The dead time of RADIUS proxy  # noqa: E501

        :param dead_time: The dead_time of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and dead_time is None:  # noqa: E501
            raise ValueError("Invalid value for `dead_time`, must not be `None`")  # noqa: E501

        self._dead_time = dead_time

    @property
    def enable_inject_operator_name_attribute(self):
        """Gets the enable_inject_operator_name_attribute of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The flag for enable inject operator name attribute  # noqa: E501

        :return: The enable_inject_operator_name_attribute of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_inject_operator_name_attribute

    @enable_inject_operator_name_attribute.setter
    def enable_inject_operator_name_attribute(self, enable_inject_operator_name_attribute):
        """Sets the enable_inject_operator_name_attribute of this XiqCreateRadiusProxyRequest.

        The flag for enable inject operator name attribute  # noqa: E501

        :param enable_inject_operator_name_attribute: The enable_inject_operator_name_attribute of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: bool
        """

        self._enable_inject_operator_name_attribute = enable_inject_operator_name_attribute

    @property
    def clients(self):
        """Gets the clients of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The RADIUS clients of RADIUS proxy  # noqa: E501

        :return: The clients of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: list[XiqCreateRadiusClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this XiqCreateRadiusProxyRequest.

        The RADIUS clients of RADIUS proxy  # noqa: E501

        :param clients: The clients of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: list[XiqCreateRadiusClient]
        """

        self._clients = clients

    @property
    def realms(self):
        """Gets the realms of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name 'DEFAULT' and 'NULL'  # noqa: E501

        :return: The realms of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: list[XiqCreateRadiusProxyRealm]
        """
        return self._realms

    @realms.setter
    def realms(self, realms):
        """Sets the realms of this XiqCreateRadiusProxyRequest.

        The RADIUS realms of RADIUS proxy, provide at least two default RADIUS realms with name 'DEFAULT' and 'NULL'  # noqa: E501

        :param realms: The realms of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: list[XiqCreateRadiusProxyRealm]
        """
        if self.local_vars_configuration.client_side_validation and realms is None:  # noqa: E501
            raise ValueError("Invalid value for `realms`, must not be `None`")  # noqa: E501

        self._realms = realms

    @property
    def device_ids(self):
        """Gets the device_ids of this XiqCreateRadiusProxyRequest.  # noqa: E501

        The device IDS to assign RADIUS proxy  # noqa: E501

        :return: The device_ids of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this XiqCreateRadiusProxyRequest.

        The device IDS to assign RADIUS proxy  # noqa: E501

        :param device_ids: The device_ids of this XiqCreateRadiusProxyRequest.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and device_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `device_ids`, must not be `None`")  # noqa: E501

        self._device_ids = device_ids

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
        if not isinstance(other, XiqCreateRadiusProxyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCreateRadiusProxyRequest):
            return True

        return self.to_dict() != other.to_dict()
