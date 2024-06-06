# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqApplicationTopClientsUsage(object):
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
        'application_id': 'int',
        'client_id': 'int',
        'client_mac_address': 'str',
        'client_host_name': 'str',
        'usage': 'int'
    }

    attribute_map = {
        'application_id': 'application_id',
        'client_id': 'client_id',
        'client_mac_address': 'client_mac_address',
        'client_host_name': 'client_host_name',
        'usage': 'usage'
    }

    def __init__(self, application_id=None, client_id=None, client_mac_address=None, client_host_name=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """XiqApplicationTopClientsUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_id = None
        self._client_id = None
        self._client_mac_address = None
        self._client_host_name = None
        self._usage = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if client_id is not None:
            self.client_id = client_id
        if client_mac_address is not None:
            self.client_mac_address = client_mac_address
        if client_host_name is not None:
            self.client_host_name = client_host_name
        if usage is not None:
            self.usage = usage

    @property
    def application_id(self):
        """Gets the application_id of this XiqApplicationTopClientsUsage.  # noqa: E501

        The application ID  # noqa: E501

        :return: The application_id of this XiqApplicationTopClientsUsage.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this XiqApplicationTopClientsUsage.

        The application ID  # noqa: E501

        :param application_id: The application_id of this XiqApplicationTopClientsUsage.  # noqa: E501
        :type: int
        """

        self._application_id = application_id

    @property
    def client_id(self):
        """Gets the client_id of this XiqApplicationTopClientsUsage.  # noqa: E501

        The TOP N client ID  # noqa: E501

        :return: The client_id of this XiqApplicationTopClientsUsage.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this XiqApplicationTopClientsUsage.

        The TOP N client ID  # noqa: E501

        :param client_id: The client_id of this XiqApplicationTopClientsUsage.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_mac_address(self):
        """Gets the client_mac_address of this XiqApplicationTopClientsUsage.  # noqa: E501

        The MAC address of TOP N client  # noqa: E501

        :return: The client_mac_address of this XiqApplicationTopClientsUsage.  # noqa: E501
        :rtype: str
        """
        return self._client_mac_address

    @client_mac_address.setter
    def client_mac_address(self, client_mac_address):
        """Sets the client_mac_address of this XiqApplicationTopClientsUsage.

        The MAC address of TOP N client  # noqa: E501

        :param client_mac_address: The client_mac_address of this XiqApplicationTopClientsUsage.  # noqa: E501
        :type: str
        """

        self._client_mac_address = client_mac_address

    @property
    def client_host_name(self):
        """Gets the client_host_name of this XiqApplicationTopClientsUsage.  # noqa: E501

        The host name of TOP N client  # noqa: E501

        :return: The client_host_name of this XiqApplicationTopClientsUsage.  # noqa: E501
        :rtype: str
        """
        return self._client_host_name

    @client_host_name.setter
    def client_host_name(self, client_host_name):
        """Sets the client_host_name of this XiqApplicationTopClientsUsage.

        The host name of TOP N client  # noqa: E501

        :param client_host_name: The client_host_name of this XiqApplicationTopClientsUsage.  # noqa: E501
        :type: str
        """

        self._client_host_name = client_host_name

    @property
    def usage(self):
        """Gets the usage of this XiqApplicationTopClientsUsage.  # noqa: E501

        The TOP N client usage  # noqa: E501

        :return: The usage of this XiqApplicationTopClientsUsage.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this XiqApplicationTopClientsUsage.

        The TOP N client usage  # noqa: E501

        :param usage: The usage of this XiqApplicationTopClientsUsage.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if not isinstance(other, XiqApplicationTopClientsUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqApplicationTopClientsUsage):
            return True

        return self.to_dict() != other.to_dict()
