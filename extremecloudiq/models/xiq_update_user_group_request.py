# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateUserGroupRequest(object):
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
        'password_db_location': 'XiqPasswordDbLocation',
        'ppsk_use_only': 'bool',
        'password_type': 'XiqPasswordType',
        'enable_max_clients_per_ppsk': 'bool',
        'max_clients_per_ppsk': 'int',
        'pcg_use_only': 'bool',
        'pcg_type': 'XiqPcgType',
        'enable_cwp_reg': 'bool',
        'password_settings': 'XiqPasswordSettings',
        'expiration_settings': 'XiqExpirationSettings',
        'delivery_settings': 'XiqDeliverySettings'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'password_db_location': 'password_db_location',
        'ppsk_use_only': 'ppsk_use_only',
        'password_type': 'password_type',
        'enable_max_clients_per_ppsk': 'enable_max_clients_per_ppsk',
        'max_clients_per_ppsk': 'max_clients_per_ppsk',
        'pcg_use_only': 'pcg_use_only',
        'pcg_type': 'pcg_type',
        'enable_cwp_reg': 'enable_cwp_reg',
        'password_settings': 'password_settings',
        'expiration_settings': 'expiration_settings',
        'delivery_settings': 'delivery_settings'
    }

    def __init__(self, name=None, description=None, password_db_location=None, ppsk_use_only=None, password_type=None, enable_max_clients_per_ppsk=None, max_clients_per_ppsk=None, pcg_use_only=None, pcg_type=None, enable_cwp_reg=None, password_settings=None, expiration_settings=None, delivery_settings=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateUserGroupRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._password_db_location = None
        self._ppsk_use_only = None
        self._password_type = None
        self._enable_max_clients_per_ppsk = None
        self._max_clients_per_ppsk = None
        self._pcg_use_only = None
        self._pcg_type = None
        self._enable_cwp_reg = None
        self._password_settings = None
        self._expiration_settings = None
        self._delivery_settings = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.password_db_location = password_db_location
        if ppsk_use_only is not None:
            self.ppsk_use_only = ppsk_use_only
        self.password_type = password_type
        if enable_max_clients_per_ppsk is not None:
            self.enable_max_clients_per_ppsk = enable_max_clients_per_ppsk
        if max_clients_per_ppsk is not None:
            self.max_clients_per_ppsk = max_clients_per_ppsk
        if pcg_use_only is not None:
            self.pcg_use_only = pcg_use_only
        if pcg_type is not None:
            self.pcg_type = pcg_type
        if enable_cwp_reg is not None:
            self.enable_cwp_reg = enable_cwp_reg
        self.password_settings = password_settings
        self.expiration_settings = expiration_settings
        self.delivery_settings = delivery_settings

    @property
    def name(self):
        """Gets the name of this XiqUpdateUserGroupRequest.  # noqa: E501

        The user group name  # noqa: E501

        :return: The name of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqUpdateUserGroupRequest.

        The user group name  # noqa: E501

        :param name: The name of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqUpdateUserGroupRequest.  # noqa: E501

        The user group description  # noqa: E501

        :return: The description of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqUpdateUserGroupRequest.

        The user group description  # noqa: E501

        :param description: The description of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def password_db_location(self):
        """Gets the password_db_location of this XiqUpdateUserGroupRequest.  # noqa: E501


        :return: The password_db_location of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: XiqPasswordDbLocation
        """
        return self._password_db_location

    @password_db_location.setter
    def password_db_location(self, password_db_location):
        """Sets the password_db_location of this XiqUpdateUserGroupRequest.


        :param password_db_location: The password_db_location of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: XiqPasswordDbLocation
        """
        if self.local_vars_configuration.client_side_validation and password_db_location is None:  # noqa: E501
            raise ValueError("Invalid value for `password_db_location`, must not be `None`")  # noqa: E501

        self._password_db_location = password_db_location

    @property
    def ppsk_use_only(self):
        """Gets the ppsk_use_only of this XiqUpdateUserGroupRequest.  # noqa: E501

        Whether it's for PPSK use only  # noqa: E501

        :return: The ppsk_use_only of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._ppsk_use_only

    @ppsk_use_only.setter
    def ppsk_use_only(self, ppsk_use_only):
        """Sets the ppsk_use_only of this XiqUpdateUserGroupRequest.

        Whether it's for PPSK use only  # noqa: E501

        :param ppsk_use_only: The ppsk_use_only of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: bool
        """

        self._ppsk_use_only = ppsk_use_only

    @property
    def password_type(self):
        """Gets the password_type of this XiqUpdateUserGroupRequest.  # noqa: E501


        :return: The password_type of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: XiqPasswordType
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this XiqUpdateUserGroupRequest.


        :param password_type: The password_type of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: XiqPasswordType
        """
        if self.local_vars_configuration.client_side_validation and password_type is None:  # noqa: E501
            raise ValueError("Invalid value for `password_type`, must not be `None`")  # noqa: E501

        self._password_type = password_type

    @property
    def enable_max_clients_per_ppsk(self):
        """Gets the enable_max_clients_per_ppsk of this XiqUpdateUserGroupRequest.  # noqa: E501

        The enablement for the maximum number of clients per private PSK  # noqa: E501

        :return: The enable_max_clients_per_ppsk of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_max_clients_per_ppsk

    @enable_max_clients_per_ppsk.setter
    def enable_max_clients_per_ppsk(self, enable_max_clients_per_ppsk):
        """Sets the enable_max_clients_per_ppsk of this XiqUpdateUserGroupRequest.

        The enablement for the maximum number of clients per private PSK  # noqa: E501

        :param enable_max_clients_per_ppsk: The enable_max_clients_per_ppsk of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: bool
        """

        self._enable_max_clients_per_ppsk = enable_max_clients_per_ppsk

    @property
    def max_clients_per_ppsk(self):
        """Gets the max_clients_per_ppsk of this XiqUpdateUserGroupRequest.  # noqa: E501

        The maximum number of clients per private PSK  # noqa: E501

        :return: The max_clients_per_ppsk of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_clients_per_ppsk

    @max_clients_per_ppsk.setter
    def max_clients_per_ppsk(self, max_clients_per_ppsk):
        """Sets the max_clients_per_ppsk of this XiqUpdateUserGroupRequest.

        The maximum number of clients per private PSK  # noqa: E501

        :param max_clients_per_ppsk: The max_clients_per_ppsk of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: int
        """

        self._max_clients_per_ppsk = max_clients_per_ppsk

    @property
    def pcg_use_only(self):
        """Gets the pcg_use_only of this XiqUpdateUserGroupRequest.  # noqa: E501

        Whether it's for PCG use only  # noqa: E501

        :return: The pcg_use_only of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._pcg_use_only

    @pcg_use_only.setter
    def pcg_use_only(self, pcg_use_only):
        """Sets the pcg_use_only of this XiqUpdateUserGroupRequest.

        Whether it's for PCG use only  # noqa: E501

        :param pcg_use_only: The pcg_use_only of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: bool
        """

        self._pcg_use_only = pcg_use_only

    @property
    def pcg_type(self):
        """Gets the pcg_type of this XiqUpdateUserGroupRequest.  # noqa: E501


        :return: The pcg_type of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: XiqPcgType
        """
        return self._pcg_type

    @pcg_type.setter
    def pcg_type(self, pcg_type):
        """Sets the pcg_type of this XiqUpdateUserGroupRequest.


        :param pcg_type: The pcg_type of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: XiqPcgType
        """

        self._pcg_type = pcg_type

    @property
    def enable_cwp_reg(self):
        """Gets the enable_cwp_reg of this XiqUpdateUserGroupRequest.  # noqa: E501

        Whether to enable CWP registration setting  # noqa: E501

        :return: The enable_cwp_reg of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cwp_reg

    @enable_cwp_reg.setter
    def enable_cwp_reg(self, enable_cwp_reg):
        """Sets the enable_cwp_reg of this XiqUpdateUserGroupRequest.

        Whether to enable CWP registration setting  # noqa: E501

        :param enable_cwp_reg: The enable_cwp_reg of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: bool
        """

        self._enable_cwp_reg = enable_cwp_reg

    @property
    def password_settings(self):
        """Gets the password_settings of this XiqUpdateUserGroupRequest.  # noqa: E501


        :return: The password_settings of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: XiqPasswordSettings
        """
        return self._password_settings

    @password_settings.setter
    def password_settings(self, password_settings):
        """Sets the password_settings of this XiqUpdateUserGroupRequest.


        :param password_settings: The password_settings of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: XiqPasswordSettings
        """
        if self.local_vars_configuration.client_side_validation and password_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `password_settings`, must not be `None`")  # noqa: E501

        self._password_settings = password_settings

    @property
    def expiration_settings(self):
        """Gets the expiration_settings of this XiqUpdateUserGroupRequest.  # noqa: E501


        :return: The expiration_settings of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: XiqExpirationSettings
        """
        return self._expiration_settings

    @expiration_settings.setter
    def expiration_settings(self, expiration_settings):
        """Sets the expiration_settings of this XiqUpdateUserGroupRequest.


        :param expiration_settings: The expiration_settings of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: XiqExpirationSettings
        """
        if self.local_vars_configuration.client_side_validation and expiration_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration_settings`, must not be `None`")  # noqa: E501

        self._expiration_settings = expiration_settings

    @property
    def delivery_settings(self):
        """Gets the delivery_settings of this XiqUpdateUserGroupRequest.  # noqa: E501


        :return: The delivery_settings of this XiqUpdateUserGroupRequest.  # noqa: E501
        :rtype: XiqDeliverySettings
        """
        return self._delivery_settings

    @delivery_settings.setter
    def delivery_settings(self, delivery_settings):
        """Sets the delivery_settings of this XiqUpdateUserGroupRequest.


        :param delivery_settings: The delivery_settings of this XiqUpdateUserGroupRequest.  # noqa: E501
        :type: XiqDeliverySettings
        """
        if self.local_vars_configuration.client_side_validation and delivery_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_settings`, must not be `None`")  # noqa: E501

        self._delivery_settings = delivery_settings

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
        if not isinstance(other, XiqUpdateUserGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateUserGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
