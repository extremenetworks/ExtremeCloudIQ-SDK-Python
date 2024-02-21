# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqWiredEventEntity(object):
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
        'device_id': 'str',
        'hostname': 'str',
        'interface_errors': 'float',
        'maximum_errors': 'float',
        'mgmt_ip': 'str',
        'port': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'hostname': 'hostname',
        'interface_errors': 'interface_errors',
        'maximum_errors': 'maximum_errors',
        'mgmt_ip': 'mgmt_ip',
        'port': 'port',
        'serial_number': 'serial_number'
    }

    def __init__(self, device_id=None, hostname=None, interface_errors=None, maximum_errors=None, mgmt_ip=None, port=None, serial_number=None, local_vars_configuration=None):  # noqa: E501
        """XiqWiredEventEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._hostname = None
        self._interface_errors = None
        self._maximum_errors = None
        self._mgmt_ip = None
        self._port = None
        self._serial_number = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if hostname is not None:
            self.hostname = hostname
        if interface_errors is not None:
            self.interface_errors = interface_errors
        if maximum_errors is not None:
            self.maximum_errors = maximum_errors
        if mgmt_ip is not None:
            self.mgmt_ip = mgmt_ip
        if port is not None:
            self.port = port
        if serial_number is not None:
            self.serial_number = serial_number

    @property
    def device_id(self):
        """Gets the device_id of this XiqWiredEventEntity.  # noqa: E501

        the device id  # noqa: E501

        :return: The device_id of this XiqWiredEventEntity.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqWiredEventEntity.

        the device id  # noqa: E501

        :param device_id: The device_id of this XiqWiredEventEntity.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def hostname(self):
        """Gets the hostname of this XiqWiredEventEntity.  # noqa: E501

        the host name  # noqa: E501

        :return: The hostname of this XiqWiredEventEntity.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this XiqWiredEventEntity.

        the host name  # noqa: E501

        :param hostname: The hostname of this XiqWiredEventEntity.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def interface_errors(self):
        """Gets the interface_errors of this XiqWiredEventEntity.  # noqa: E501

        the interface errors ratio  # noqa: E501

        :return: The interface_errors of this XiqWiredEventEntity.  # noqa: E501
        :rtype: float
        """
        return self._interface_errors

    @interface_errors.setter
    def interface_errors(self, interface_errors):
        """Sets the interface_errors of this XiqWiredEventEntity.

        the interface errors ratio  # noqa: E501

        :param interface_errors: The interface_errors of this XiqWiredEventEntity.  # noqa: E501
        :type: float
        """

        self._interface_errors = interface_errors

    @property
    def maximum_errors(self):
        """Gets the maximum_errors of this XiqWiredEventEntity.  # noqa: E501

        the maximum errors ratio  # noqa: E501

        :return: The maximum_errors of this XiqWiredEventEntity.  # noqa: E501
        :rtype: float
        """
        return self._maximum_errors

    @maximum_errors.setter
    def maximum_errors(self, maximum_errors):
        """Sets the maximum_errors of this XiqWiredEventEntity.

        the maximum errors ratio  # noqa: E501

        :param maximum_errors: The maximum_errors of this XiqWiredEventEntity.  # noqa: E501
        :type: float
        """

        self._maximum_errors = maximum_errors

    @property
    def mgmt_ip(self):
        """Gets the mgmt_ip of this XiqWiredEventEntity.  # noqa: E501

        the management ip  # noqa: E501

        :return: The mgmt_ip of this XiqWiredEventEntity.  # noqa: E501
        :rtype: str
        """
        return self._mgmt_ip

    @mgmt_ip.setter
    def mgmt_ip(self, mgmt_ip):
        """Sets the mgmt_ip of this XiqWiredEventEntity.

        the management ip  # noqa: E501

        :param mgmt_ip: The mgmt_ip of this XiqWiredEventEntity.  # noqa: E501
        :type: str
        """

        self._mgmt_ip = mgmt_ip

    @property
    def port(self):
        """Gets the port of this XiqWiredEventEntity.  # noqa: E501

        the port  # noqa: E501

        :return: The port of this XiqWiredEventEntity.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this XiqWiredEventEntity.

        the port  # noqa: E501

        :param port: The port of this XiqWiredEventEntity.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def serial_number(self):
        """Gets the serial_number of this XiqWiredEventEntity.  # noqa: E501

        the device serial number  # noqa: E501

        :return: The serial_number of this XiqWiredEventEntity.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XiqWiredEventEntity.

        the device serial number  # noqa: E501

        :param serial_number: The serial_number of this XiqWiredEventEntity.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

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
        if not isinstance(other, XiqWiredEventEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWiredEventEntity):
            return True

        return self.to_dict() != other.to_dict()
