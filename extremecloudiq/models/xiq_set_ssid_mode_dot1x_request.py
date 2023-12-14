# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqSetSsidModeDot1xRequest(object):
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
        'key_management': 'XiqSsidDot1xKeyManagement',
        'encryption_method': 'XiqSsidDot1xEncryptionMethod',
        'enable_idm': 'bool',
        'transition_mode': 'bool',
        'radius_server_group_id': 'int',
        'user_group_ids': 'list[int]'
    }

    attribute_map = {
        'key_management': 'key_management',
        'encryption_method': 'encryption_method',
        'enable_idm': 'enable_idm',
        'transition_mode': 'transition_mode',
        'radius_server_group_id': 'radius_server_group_id',
        'user_group_ids': 'user_group_ids'
    }

    def __init__(self, key_management=None, encryption_method=None, enable_idm=None, transition_mode=None, radius_server_group_id=None, user_group_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqSetSsidModeDot1xRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_management = None
        self._encryption_method = None
        self._enable_idm = None
        self._transition_mode = None
        self._radius_server_group_id = None
        self._user_group_ids = None
        self.discriminator = None

        self.key_management = key_management
        self.encryption_method = encryption_method
        self.enable_idm = enable_idm
        if transition_mode is not None:
            self.transition_mode = transition_mode
        if radius_server_group_id is not None:
            self.radius_server_group_id = radius_server_group_id
        if user_group_ids is not None:
            self.user_group_ids = user_group_ids

    @property
    def key_management(self):
        """Gets the key_management of this XiqSetSsidModeDot1xRequest.  # noqa: E501


        :return: The key_management of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :rtype: XiqSsidDot1xKeyManagement
        """
        return self._key_management

    @key_management.setter
    def key_management(self, key_management):
        """Sets the key_management of this XiqSetSsidModeDot1xRequest.


        :param key_management: The key_management of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :type: XiqSsidDot1xKeyManagement
        """
        if self.local_vars_configuration.client_side_validation and key_management is None:  # noqa: E501
            raise ValueError("Invalid value for `key_management`, must not be `None`")  # noqa: E501

        self._key_management = key_management

    @property
    def encryption_method(self):
        """Gets the encryption_method of this XiqSetSsidModeDot1xRequest.  # noqa: E501


        :return: The encryption_method of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :rtype: XiqSsidDot1xEncryptionMethod
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        """Sets the encryption_method of this XiqSetSsidModeDot1xRequest.


        :param encryption_method: The encryption_method of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :type: XiqSsidDot1xEncryptionMethod
        """
        if self.local_vars_configuration.client_side_validation and encryption_method is None:  # noqa: E501
            raise ValueError("Invalid value for `encryption_method`, must not be `None`")  # noqa: E501

        self._encryption_method = encryption_method

    @property
    def enable_idm(self):
        """Gets the enable_idm of this XiqSetSsidModeDot1xRequest.  # noqa: E501

        Flag for using ExtremeCloud IQ Authentication Service or not  # noqa: E501

        :return: The enable_idm of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_idm

    @enable_idm.setter
    def enable_idm(self, enable_idm):
        """Sets the enable_idm of this XiqSetSsidModeDot1xRequest.

        Flag for using ExtremeCloud IQ Authentication Service or not  # noqa: E501

        :param enable_idm: The enable_idm of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_idm is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_idm`, must not be `None`")  # noqa: E501

        self._enable_idm = enable_idm

    @property
    def transition_mode(self):
        """Gets the transition_mode of this XiqSetSsidModeDot1xRequest.  # noqa: E501

        Flag for enabling transition mode if using WPA3 as the key management type  # noqa: E501

        :return: The transition_mode of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :rtype: bool
        """
        return self._transition_mode

    @transition_mode.setter
    def transition_mode(self, transition_mode):
        """Sets the transition_mode of this XiqSetSsidModeDot1xRequest.

        Flag for enabling transition mode if using WPA3 as the key management type  # noqa: E501

        :param transition_mode: The transition_mode of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :type: bool
        """

        self._transition_mode = transition_mode

    @property
    def radius_server_group_id(self):
        """Gets the radius_server_group_id of this XiqSetSsidModeDot1xRequest.  # noqa: E501

        The RADIUS server group ID if not using ExtremeCloud IQ Authentication Service  # noqa: E501

        :return: The radius_server_group_id of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :rtype: int
        """
        return self._radius_server_group_id

    @radius_server_group_id.setter
    def radius_server_group_id(self, radius_server_group_id):
        """Sets the radius_server_group_id of this XiqSetSsidModeDot1xRequest.

        The RADIUS server group ID if not using ExtremeCloud IQ Authentication Service  # noqa: E501

        :param radius_server_group_id: The radius_server_group_id of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :type: int
        """

        self._radius_server_group_id = radius_server_group_id

    @property
    def user_group_ids(self):
        """Gets the user_group_ids of this XiqSetSsidModeDot1xRequest.  # noqa: E501

        The user group IDs if using ExtremeCloud IQ Authentication Service  # noqa: E501

        :return: The user_group_ids of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._user_group_ids

    @user_group_ids.setter
    def user_group_ids(self, user_group_ids):
        """Sets the user_group_ids of this XiqSetSsidModeDot1xRequest.

        The user group IDs if using ExtremeCloud IQ Authentication Service  # noqa: E501

        :param user_group_ids: The user_group_ids of this XiqSetSsidModeDot1xRequest.  # noqa: E501
        :type: list[int]
        """

        self._user_group_ids = user_group_ids

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
        if not isinstance(other, XiqSetSsidModeDot1xRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSetSsidModeDot1xRequest):
            return True

        return self.to_dict() != other.to_dict()
