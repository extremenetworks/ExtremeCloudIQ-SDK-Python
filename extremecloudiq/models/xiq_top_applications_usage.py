# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqTopApplicationsUsage(object):
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
        'clients': 'int',
        'users': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'clients': 'clients',
        'users': 'users',
        'usage': 'usage'
    }

    def __init__(self, id=None, name=None, clients=None, users=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """XiqTopApplicationsUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._clients = None
        self._users = None
        self._usage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if clients is not None:
            self.clients = clients
        if users is not None:
            self.users = users
        if usage is not None:
            self.usage = usage

    @property
    def id(self):
        """Gets the id of this XiqTopApplicationsUsage.  # noqa: E501

        The application ID  # noqa: E501

        :return: The id of this XiqTopApplicationsUsage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqTopApplicationsUsage.

        The application ID  # noqa: E501

        :param id: The id of this XiqTopApplicationsUsage.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this XiqTopApplicationsUsage.  # noqa: E501

        The application name  # noqa: E501

        :return: The name of this XiqTopApplicationsUsage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqTopApplicationsUsage.

        The application name  # noqa: E501

        :param name: The name of this XiqTopApplicationsUsage.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def clients(self):
        """Gets the clients of this XiqTopApplicationsUsage.  # noqa: E501

        The associated unique client count  # noqa: E501

        :return: The clients of this XiqTopApplicationsUsage.  # noqa: E501
        :rtype: int
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this XiqTopApplicationsUsage.

        The associated unique client count  # noqa: E501

        :param clients: The clients of this XiqTopApplicationsUsage.  # noqa: E501
        :type: int
        """

        self._clients = clients

    @property
    def users(self):
        """Gets the users of this XiqTopApplicationsUsage.  # noqa: E501

        The associated unique user count  # noqa: E501

        :return: The users of this XiqTopApplicationsUsage.  # noqa: E501
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this XiqTopApplicationsUsage.

        The associated unique user count  # noqa: E501

        :param users: The users of this XiqTopApplicationsUsage.  # noqa: E501
        :type: int
        """

        self._users = users

    @property
    def usage(self):
        """Gets the usage of this XiqTopApplicationsUsage.  # noqa: E501

        The application usage  # noqa: E501

        :return: The usage of this XiqTopApplicationsUsage.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this XiqTopApplicationsUsage.

        The application usage  # noqa: E501

        :param usage: The usage of this XiqTopApplicationsUsage.  # noqa: E501
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
        if not isinstance(other, XiqTopApplicationsUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqTopApplicationsUsage):
            return True

        return self.to_dict() != other.to_dict()
