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


class XiqDeviceDhcpRelay(object):
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
        'name': 'str',
        'description': 'str',
        'service_type': 'XiqDhcpServiceType',
        'platform': 'XiqDhcpPlatform',
        'primary_server': 'str',
        'secondary_server': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'service_type': 'service_type',
        'platform': 'platform',
        'primary_server': 'primary_server',
        'secondary_server': 'secondary_server'
    }

    def __init__(self, id=None, name=None, description=None, service_type=None, platform=None, primary_server=None, secondary_server=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceDhcpRelay - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._service_type = None
        self._platform = None
        self._primary_server = None
        self._secondary_server = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.service_type = service_type
        self.platform = platform
        self.primary_server = primary_server
        if secondary_server is not None:
            self.secondary_server = secondary_server

    @property
    def id(self):
        """Gets the id of this XiqDeviceDhcpRelay.  # noqa: E501

        The DHCP relay agent and server ID  # noqa: E501

        :return: The id of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqDeviceDhcpRelay.

        The DHCP relay agent and server ID  # noqa: E501

        :param id: The id of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this XiqDeviceDhcpRelay.  # noqa: E501

        Name of DHCP relay agent or server  # noqa: E501

        :return: The name of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqDeviceDhcpRelay.

        Name of DHCP relay agent or server  # noqa: E501

        :param name: The name of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqDeviceDhcpRelay.  # noqa: E501

        Description of DHCP relay agent or server  # noqa: E501

        :return: The description of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqDeviceDhcpRelay.

        Description of DHCP relay agent or server  # noqa: E501

        :param description: The description of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_type(self):
        """Gets the service_type of this XiqDeviceDhcpRelay.  # noqa: E501


        :return: The service_type of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: XiqDhcpServiceType
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this XiqDeviceDhcpRelay.


        :param service_type: The service_type of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: XiqDhcpServiceType
        """
        if self.local_vars_configuration.client_side_validation and service_type is None:  # noqa: E501
            raise ValueError("Invalid value for `service_type`, must not be `None`")  # noqa: E501

        self._service_type = service_type

    @property
    def platform(self):
        """Gets the platform of this XiqDeviceDhcpRelay.  # noqa: E501


        :return: The platform of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: XiqDhcpPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this XiqDeviceDhcpRelay.


        :param platform: The platform of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: XiqDhcpPlatform
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501

        self._platform = platform

    @property
    def primary_server(self):
        """Gets the primary_server of this XiqDeviceDhcpRelay.  # noqa: E501

        Primary Ip server of DHCP agent  # noqa: E501

        :return: The primary_server of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: str
        """
        return self._primary_server

    @primary_server.setter
    def primary_server(self, primary_server):
        """Sets the primary_server of this XiqDeviceDhcpRelay.

        Primary Ip server of DHCP agent  # noqa: E501

        :param primary_server: The primary_server of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and primary_server is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_server`, must not be `None`")  # noqa: E501

        self._primary_server = primary_server

    @property
    def secondary_server(self):
        """Gets the secondary_server of this XiqDeviceDhcpRelay.  # noqa: E501

        Secondary Ip server of DHCP agent  # noqa: E501

        :return: The secondary_server of this XiqDeviceDhcpRelay.  # noqa: E501
        :rtype: str
        """
        return self._secondary_server

    @secondary_server.setter
    def secondary_server(self, secondary_server):
        """Sets the secondary_server of this XiqDeviceDhcpRelay.

        Secondary Ip server of DHCP agent  # noqa: E501

        :param secondary_server: The secondary_server of this XiqDeviceDhcpRelay.  # noqa: E501
        :type: str
        """

        self._secondary_server = secondary_server

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
        if not isinstance(other, XiqDeviceDhcpRelay):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceDhcpRelay):
            return True

        return self.to_dict() != other.to_dict()
