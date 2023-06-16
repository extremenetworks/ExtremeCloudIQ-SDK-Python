# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqSetSsidModePpskRequest(object):
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
        'key_management': 'XiqSsidPpskKeyManagement',
        'encryption_method': 'XiqSsidPskEncryptionMethod',
        'user_group_ids': 'list[int]',
        'enable_max_clients_per_ppsk': 'bool',
        'max_clients_per_ppsk': 'int',
        'enable_mac_bind': 'bool',
        'max_macs_per_ppsk': 'int',
        'ppsk_server_id': 'int'
    }

    attribute_map = {
        'key_management': 'key_management',
        'encryption_method': 'encryption_method',
        'user_group_ids': 'user_group_ids',
        'enable_max_clients_per_ppsk': 'enable_max_clients_per_ppsk',
        'max_clients_per_ppsk': 'max_clients_per_ppsk',
        'enable_mac_bind': 'enable_mac_bind',
        'max_macs_per_ppsk': 'max_macs_per_ppsk',
        'ppsk_server_id': 'ppsk_server_id'
    }

    def __init__(self, key_management=None, encryption_method=None, user_group_ids=None, enable_max_clients_per_ppsk=None, max_clients_per_ppsk=None, enable_mac_bind=None, max_macs_per_ppsk=None, ppsk_server_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqSetSsidModePpskRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_management = None
        self._encryption_method = None
        self._user_group_ids = None
        self._enable_max_clients_per_ppsk = None
        self._max_clients_per_ppsk = None
        self._enable_mac_bind = None
        self._max_macs_per_ppsk = None
        self._ppsk_server_id = None
        self.discriminator = None

        self.key_management = key_management
        self.encryption_method = encryption_method
        self.user_group_ids = user_group_ids
        self.enable_max_clients_per_ppsk = enable_max_clients_per_ppsk
        if max_clients_per_ppsk is not None:
            self.max_clients_per_ppsk = max_clients_per_ppsk
        self.enable_mac_bind = enable_mac_bind
        if max_macs_per_ppsk is not None:
            self.max_macs_per_ppsk = max_macs_per_ppsk
        if ppsk_server_id is not None:
            self.ppsk_server_id = ppsk_server_id

    @property
    def key_management(self):
        """Gets the key_management of this XiqSetSsidModePpskRequest.  # noqa: E501


        :return: The key_management of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: XiqSsidPpskKeyManagement
        """
        return self._key_management

    @key_management.setter
    def key_management(self, key_management):
        """Sets the key_management of this XiqSetSsidModePpskRequest.


        :param key_management: The key_management of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: XiqSsidPpskKeyManagement
        """
        if self.local_vars_configuration.client_side_validation and key_management is None:  # noqa: E501
            raise ValueError("Invalid value for `key_management`, must not be `None`")  # noqa: E501

        self._key_management = key_management

    @property
    def encryption_method(self):
        """Gets the encryption_method of this XiqSetSsidModePpskRequest.  # noqa: E501


        :return: The encryption_method of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: XiqSsidPskEncryptionMethod
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        """Sets the encryption_method of this XiqSetSsidModePpskRequest.


        :param encryption_method: The encryption_method of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: XiqSsidPskEncryptionMethod
        """
        if self.local_vars_configuration.client_side_validation and encryption_method is None:  # noqa: E501
            raise ValueError("Invalid value for `encryption_method`, must not be `None`")  # noqa: E501

        self._encryption_method = encryption_method

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this XiqSetSsidModePpskRequest.  # noqa: E501

        The user group IDs to be attached to the SSID, cannot be empty  # noqa: E501

        :return: The user_group_ids of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this XiqSetSsidModePpskRequest.

        The user group IDs to be attached to the SSID, cannot be empty  # noqa: E501

        :param user_group_ids: The user_group_ids of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and user_group_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `user_group_ids`, must not be `None`")  # noqa: E501

        self._user_group_ids = user_group_ids

    @property
    def enable_max_clients_per_ppsk(self):
        """Gets the enable_max_clients_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501

        Flag for enabling the max clients per PPSK  # noqa: E501

        :return: The enable_max_clients_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_max_clients_per_ppsk

    @enable_max_clients_per_ppsk.setter
    def enable_max_clients_per_ppsk(self, enable_max_clients_per_ppsk):
        """Sets the enable_max_clients_per_ppsk of this XiqSetSsidModePpskRequest.

        Flag for enabling the max clients per PPSK  # noqa: E501

        :param enable_max_clients_per_ppsk: The enable_max_clients_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_max_clients_per_ppsk is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_max_clients_per_ppsk`, must not be `None`")  # noqa: E501

        self._enable_max_clients_per_ppsk = enable_max_clients_per_ppsk

    @property
    def max_clients_per_ppsk(self):
        """Gets the max_clients_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501

        The max clients (0-15) per PPSK if enabled enable_max_clients_per_ppsk flag, 0 means unlimited  # noqa: E501

        :return: The max_clients_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_clients_per_ppsk

    @max_clients_per_ppsk.setter
    def max_clients_per_ppsk(self, max_clients_per_ppsk):
        """Sets the max_clients_per_ppsk of this XiqSetSsidModePpskRequest.

        The max clients (0-15) per PPSK if enabled enable_max_clients_per_ppsk flag, 0 means unlimited  # noqa: E501

        :param max_clients_per_ppsk: The max_clients_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_clients_per_ppsk is not None and max_clients_per_ppsk > 15):  # noqa: E501
            raise ValueError("Invalid value for `max_clients_per_ppsk`, must be a value less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_clients_per_ppsk is not None and max_clients_per_ppsk < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_clients_per_ppsk`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_clients_per_ppsk = max_clients_per_ppsk

    @property
    def enable_mac_bind(self):
        """Gets the enable_mac_bind of this XiqSetSsidModePpskRequest.  # noqa: E501

        Flag for enabling mac binding or not. This setting is only supported with local PPSK.  # noqa: E501

        :return: The enable_mac_bind of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_mac_bind

    @enable_mac_bind.setter
    def enable_mac_bind(self, enable_mac_bind):
        """Sets the enable_mac_bind of this XiqSetSsidModePpskRequest.

        Flag for enabling mac binding or not. This setting is only supported with local PPSK.  # noqa: E501

        :param enable_mac_bind: The enable_mac_bind of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_mac_bind is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_mac_bind`, must not be `None`")  # noqa: E501

        self._enable_mac_bind = enable_mac_bind

    @property
    def max_macs_per_ppsk(self):
        """Gets the max_macs_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501

        Set the max MAC binding numbers per private PSK, Min:1, Max:5  # noqa: E501

        :return: The max_macs_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_macs_per_ppsk

    @max_macs_per_ppsk.setter
    def max_macs_per_ppsk(self, max_macs_per_ppsk):
        """Sets the max_macs_per_ppsk of this XiqSetSsidModePpskRequest.

        Set the max MAC binding numbers per private PSK, Min:1, Max:5  # noqa: E501

        :param max_macs_per_ppsk: The max_macs_per_ppsk of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_macs_per_ppsk is not None and max_macs_per_ppsk > 5):  # noqa: E501
            raise ValueError("Invalid value for `max_macs_per_ppsk`, must be a value less than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_macs_per_ppsk is not None and max_macs_per_ppsk < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_macs_per_ppsk`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_macs_per_ppsk = max_macs_per_ppsk

    @property
    def ppsk_server_id(self):
        """Gets the ppsk_server_id of this XiqSetSsidModePpskRequest.  # noqa: E501

        The PPSK server device ID  # noqa: E501

        :return: The ppsk_server_id of this XiqSetSsidModePpskRequest.  # noqa: E501
        :rtype: int
        """
        return self._ppsk_server_id

    @ppsk_server_id.setter
    def ppsk_server_id(self, ppsk_server_id):
        """Sets the ppsk_server_id of this XiqSetSsidModePpskRequest.

        The PPSK server device ID  # noqa: E501

        :param ppsk_server_id: The ppsk_server_id of this XiqSetSsidModePpskRequest.  # noqa: E501
        :type: int
        """

        self._ppsk_server_id = ppsk_server_id

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
        if not isinstance(other, XiqSetSsidModePpskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSetSsidModePpskRequest):
            return True

        return self.to_dict() != other.to_dict()
