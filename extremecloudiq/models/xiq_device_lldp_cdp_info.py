# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceLldpCdpInfo(object):
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
        'port_id': 'str',
        'system_id': 'str',
        'system_name': 'str',
        'interface_name': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'system_id': 'system_id',
        'system_name': 'system_name',
        'interface_name': 'interface_name'
    }

    def __init__(self, port_id=None, system_id=None, system_name=None, interface_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceLldpCdpInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._port_id = None
        self._system_id = None
        self._system_name = None
        self._interface_name = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if system_id is not None:
            self.system_id = system_id
        if system_name is not None:
            self.system_name = system_name
        if interface_name is not None:
            self.interface_name = interface_name

    @property
    def port_id(self):
        """Gets the port_id of this XiqDeviceLldpCdpInfo.  # noqa: E501

        The port ID.  # noqa: E501

        :return: The port_id of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this XiqDeviceLldpCdpInfo.

        The port ID.  # noqa: E501

        :param port_id: The port_id of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :type: str
        """

        self._port_id = port_id

    @property
    def system_id(self):
        """Gets the system_id of this XiqDeviceLldpCdpInfo.  # noqa: E501

        The system ID.  # noqa: E501

        :return: The system_id of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this XiqDeviceLldpCdpInfo.

        The system ID.  # noqa: E501

        :param system_id: The system_id of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

    @property
    def system_name(self):
        """Gets the system_name of this XiqDeviceLldpCdpInfo.  # noqa: E501

        The system name.  # noqa: E501

        :return: The system_name of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this XiqDeviceLldpCdpInfo.

        The system name.  # noqa: E501

        :param system_name: The system_name of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqDeviceLldpCdpInfo.  # noqa: E501

        The interface name.  # noqa: E501

        :return: The interface_name of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqDeviceLldpCdpInfo.

        The interface name.  # noqa: E501

        :param interface_name: The interface_name of this XiqDeviceLldpCdpInfo.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

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
        if not isinstance(other, XiqDeviceLldpCdpInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceLldpCdpInfo):
            return True

        return self.to_dict() != other.to_dict()
