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


class XiqThreadNetworkData(object):
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
        'length': 'int',
        'max_length': 'int',
        'net_data_on_mesh_prefixes': 'list[XiqThreadNetDataPrefix]',
        'net_data_routes': 'list[XiqThreadNetDataRoute]',
        'net_data_services': 'list[XiqThreadNetDataService]'
    }

    attribute_map = {
        'length': 'length',
        'max_length': 'max_length',
        'net_data_on_mesh_prefixes': 'net_data_on_mesh_prefixes',
        'net_data_routes': 'net_data_routes',
        'net_data_services': 'net_data_services'
    }

    def __init__(self, length=None, max_length=None, net_data_on_mesh_prefixes=None, net_data_routes=None, net_data_services=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadNetworkData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._length = None
        self._max_length = None
        self._net_data_on_mesh_prefixes = None
        self._net_data_routes = None
        self._net_data_services = None
        self.discriminator = None

        if length is not None:
            self.length = length
        if max_length is not None:
            self.max_length = max_length
        if net_data_on_mesh_prefixes is not None:
            self.net_data_on_mesh_prefixes = net_data_on_mesh_prefixes
        if net_data_routes is not None:
            self.net_data_routes = net_data_routes
        if net_data_services is not None:
            self.net_data_services = net_data_services

    @property
    def length(self):
        """Gets the length of this XiqThreadNetworkData.  # noqa: E501


        :return: The length of this XiqThreadNetworkData.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this XiqThreadNetworkData.


        :param length: The length of this XiqThreadNetworkData.  # noqa: E501
        :type: int
        """

        self._length = length

    @property
    def max_length(self):
        """Gets the max_length of this XiqThreadNetworkData.  # noqa: E501


        :return: The max_length of this XiqThreadNetworkData.  # noqa: E501
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this XiqThreadNetworkData.


        :param max_length: The max_length of this XiqThreadNetworkData.  # noqa: E501
        :type: int
        """

        self._max_length = max_length

    @property
    def net_data_on_mesh_prefixes(self):
        """Gets the net_data_on_mesh_prefixes of this XiqThreadNetworkData.  # noqa: E501


        :return: The net_data_on_mesh_prefixes of this XiqThreadNetworkData.  # noqa: E501
        :rtype: list[XiqThreadNetDataPrefix]
        """
        return self._net_data_on_mesh_prefixes

    @net_data_on_mesh_prefixes.setter
    def net_data_on_mesh_prefixes(self, net_data_on_mesh_prefixes):
        """Sets the net_data_on_mesh_prefixes of this XiqThreadNetworkData.


        :param net_data_on_mesh_prefixes: The net_data_on_mesh_prefixes of this XiqThreadNetworkData.  # noqa: E501
        :type: list[XiqThreadNetDataPrefix]
        """

        self._net_data_on_mesh_prefixes = net_data_on_mesh_prefixes

    @property
    def net_data_routes(self):
        """Gets the net_data_routes of this XiqThreadNetworkData.  # noqa: E501


        :return: The net_data_routes of this XiqThreadNetworkData.  # noqa: E501
        :rtype: list[XiqThreadNetDataRoute]
        """
        return self._net_data_routes

    @net_data_routes.setter
    def net_data_routes(self, net_data_routes):
        """Sets the net_data_routes of this XiqThreadNetworkData.


        :param net_data_routes: The net_data_routes of this XiqThreadNetworkData.  # noqa: E501
        :type: list[XiqThreadNetDataRoute]
        """

        self._net_data_routes = net_data_routes

    @property
    def net_data_services(self):
        """Gets the net_data_services of this XiqThreadNetworkData.  # noqa: E501


        :return: The net_data_services of this XiqThreadNetworkData.  # noqa: E501
        :rtype: list[XiqThreadNetDataService]
        """
        return self._net_data_services

    @net_data_services.setter
    def net_data_services(self, net_data_services):
        """Sets the net_data_services of this XiqThreadNetworkData.


        :param net_data_services: The net_data_services of this XiqThreadNetworkData.  # noqa: E501
        :type: list[XiqThreadNetDataService]
        """

        self._net_data_services = net_data_services

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
        if not isinstance(other, XiqThreadNetworkData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadNetworkData):
            return True

        return self.to_dict() != other.to_dict()
