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


class XiqThreadNetworkTopology(object):
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
        'neighbors': 'list[XiqThreadRouterNeighbor]',
        'routers': 'list[XiqThreadRouter]',
        'clients': 'list[XiqClient]'
    }

    attribute_map = {
        'neighbors': 'neighbors',
        'routers': 'routers',
        'clients': 'clients'
    }

    def __init__(self, neighbors=None, routers=None, clients=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadNetworkTopology - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._neighbors = None
        self._routers = None
        self._clients = None
        self.discriminator = None

        if neighbors is not None:
            self.neighbors = neighbors
        if routers is not None:
            self.routers = routers
        if clients is not None:
            self.clients = clients

    @property
    def neighbors(self):
        """Gets the neighbors of this XiqThreadNetworkTopology.  # noqa: E501


        :return: The neighbors of this XiqThreadNetworkTopology.  # noqa: E501
        :rtype: list[XiqThreadRouterNeighbor]
        """
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors):
        """Sets the neighbors of this XiqThreadNetworkTopology.


        :param neighbors: The neighbors of this XiqThreadNetworkTopology.  # noqa: E501
        :type: list[XiqThreadRouterNeighbor]
        """

        self._neighbors = neighbors

    @property
    def routers(self):
        """Gets the routers of this XiqThreadNetworkTopology.  # noqa: E501


        :return: The routers of this XiqThreadNetworkTopology.  # noqa: E501
        :rtype: list[XiqThreadRouter]
        """
        return self._routers

    @routers.setter
    def routers(self, routers):
        """Sets the routers of this XiqThreadNetworkTopology.


        :param routers: The routers of this XiqThreadNetworkTopology.  # noqa: E501
        :type: list[XiqThreadRouter]
        """

        self._routers = routers

    @property
    def clients(self):
        """Gets the clients of this XiqThreadNetworkTopology.  # noqa: E501


        :return: The clients of this XiqThreadNetworkTopology.  # noqa: E501
        :rtype: list[XiqClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this XiqThreadNetworkTopology.


        :param clients: The clients of this XiqThreadNetworkTopology.  # noqa: E501
        :type: list[XiqClient]
        """

        self._clients = clients

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
        if not isinstance(other, XiqThreadNetworkTopology):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadNetworkTopology):
            return True

        return self.to_dict() != other.to_dict()
