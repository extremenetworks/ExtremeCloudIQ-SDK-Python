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


class XiqWirelessAppsResponse(object):
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
        'total_clients': 'int',
        'most_active_app': 'str',
        'most_active_user': 'str',
        'total_apps': 'int',
        'total_users': 'int'
    }

    attribute_map = {
        'total_clients': 'total_clients',
        'most_active_app': 'most_active_app',
        'most_active_user': 'most_active_user',
        'total_apps': 'total_apps',
        'total_users': 'total_users'
    }

    def __init__(self, total_clients=None, most_active_app=None, most_active_user=None, total_apps=None, total_users=None, local_vars_configuration=None):  # noqa: E501
        """XiqWirelessAppsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_clients = None
        self._most_active_app = None
        self._most_active_user = None
        self._total_apps = None
        self._total_users = None
        self.discriminator = None

        if total_clients is not None:
            self.total_clients = total_clients
        if most_active_app is not None:
            self.most_active_app = most_active_app
        if most_active_user is not None:
            self.most_active_user = most_active_user
        if total_apps is not None:
            self.total_apps = total_apps
        if total_users is not None:
            self.total_users = total_users

    @property
    def total_clients(self):
        """Gets the total_clients of this XiqWirelessAppsResponse.  # noqa: E501

        the total clients  # noqa: E501

        :return: The total_clients of this XiqWirelessAppsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_clients

    @total_clients.setter
    def total_clients(self, total_clients):
        """Sets the total_clients of this XiqWirelessAppsResponse.

        the total clients  # noqa: E501

        :param total_clients: The total_clients of this XiqWirelessAppsResponse.  # noqa: E501
        :type: int
        """

        self._total_clients = total_clients

    @property
    def most_active_app(self):
        """Gets the most_active_app of this XiqWirelessAppsResponse.  # noqa: E501

        the most active app  # noqa: E501

        :return: The most_active_app of this XiqWirelessAppsResponse.  # noqa: E501
        :rtype: str
        """
        return self._most_active_app

    @most_active_app.setter
    def most_active_app(self, most_active_app):
        """Sets the most_active_app of this XiqWirelessAppsResponse.

        the most active app  # noqa: E501

        :param most_active_app: The most_active_app of this XiqWirelessAppsResponse.  # noqa: E501
        :type: str
        """

        self._most_active_app = most_active_app

    @property
    def most_active_user(self):
        """Gets the most_active_user of this XiqWirelessAppsResponse.  # noqa: E501

        the most active user  # noqa: E501

        :return: The most_active_user of this XiqWirelessAppsResponse.  # noqa: E501
        :rtype: str
        """
        return self._most_active_user

    @most_active_user.setter
    def most_active_user(self, most_active_user):
        """Sets the most_active_user of this XiqWirelessAppsResponse.

        the most active user  # noqa: E501

        :param most_active_user: The most_active_user of this XiqWirelessAppsResponse.  # noqa: E501
        :type: str
        """

        self._most_active_user = most_active_user

    @property
    def total_apps(self):
        """Gets the total_apps of this XiqWirelessAppsResponse.  # noqa: E501

        the total apps  # noqa: E501

        :return: The total_apps of this XiqWirelessAppsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_apps

    @total_apps.setter
    def total_apps(self, total_apps):
        """Sets the total_apps of this XiqWirelessAppsResponse.

        the total apps  # noqa: E501

        :param total_apps: The total_apps of this XiqWirelessAppsResponse.  # noqa: E501
        :type: int
        """

        self._total_apps = total_apps

    @property
    def total_users(self):
        """Gets the total_users of this XiqWirelessAppsResponse.  # noqa: E501

        the total users  # noqa: E501

        :return: The total_users of this XiqWirelessAppsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_users

    @total_users.setter
    def total_users(self, total_users):
        """Sets the total_users of this XiqWirelessAppsResponse.

        the total users  # noqa: E501

        :param total_users: The total_users of this XiqWirelessAppsResponse.  # noqa: E501
        :type: int
        """

        self._total_users = total_users

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
        if not isinstance(other, XiqWirelessAppsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWirelessAppsResponse):
            return True

        return self.to_dict() != other.to_dict()
