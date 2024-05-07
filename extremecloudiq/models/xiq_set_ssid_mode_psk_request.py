# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqSetSsidModePskRequest(object):
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
        'key_management': 'XiqSsidPskKeyManagement',
        'encryption_method': 'XiqSsidPskEncryptionMethod',
        'anti_logging_threshold': 'int',
        'key_type': 'XiqSsidKeyType',
        'key_value': 'str',
        'sae_group': 'XiqSsidSaeGroup',
        'transition_mode': 'bool'
    }

    attribute_map = {
        'key_management': 'key_management',
        'encryption_method': 'encryption_method',
        'anti_logging_threshold': 'anti_logging_threshold',
        'key_type': 'key_type',
        'key_value': 'key_value',
        'sae_group': 'sae_group',
        'transition_mode': 'transition_mode'
    }

    def __init__(self, key_management=None, encryption_method=None, anti_logging_threshold=None, key_type=None, key_value=None, sae_group=None, transition_mode=None, local_vars_configuration=None):  # noqa: E501
        """XiqSetSsidModePskRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_management = None
        self._encryption_method = None
        self._anti_logging_threshold = None
        self._key_type = None
        self._key_value = None
        self._sae_group = None
        self._transition_mode = None
        self.discriminator = None

        self.key_management = key_management
        self.encryption_method = encryption_method
        if anti_logging_threshold is not None:
            self.anti_logging_threshold = anti_logging_threshold
        self.key_type = key_type
        self.key_value = key_value
        if sae_group is not None:
            self.sae_group = sae_group
        if transition_mode is not None:
            self.transition_mode = transition_mode

    @property
    def key_management(self):
        """Gets the key_management of this XiqSetSsidModePskRequest.  # noqa: E501


        :return: The key_management of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: XiqSsidPskKeyManagement
        """
        return self._key_management

    @key_management.setter
    def key_management(self, key_management):
        """Sets the key_management of this XiqSetSsidModePskRequest.


        :param key_management: The key_management of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: XiqSsidPskKeyManagement
        """
        if self.local_vars_configuration.client_side_validation and key_management is None:  # noqa: E501
            raise ValueError("Invalid value for `key_management`, must not be `None`")  # noqa: E501

        self._key_management = key_management

    @property
    def encryption_method(self):
        """Gets the encryption_method of this XiqSetSsidModePskRequest.  # noqa: E501


        :return: The encryption_method of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: XiqSsidPskEncryptionMethod
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        """Sets the encryption_method of this XiqSetSsidModePskRequest.


        :param encryption_method: The encryption_method of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: XiqSsidPskEncryptionMethod
        """
        if self.local_vars_configuration.client_side_validation and encryption_method is None:  # noqa: E501
            raise ValueError("Invalid value for `encryption_method`, must not be `None`")  # noqa: E501

        self._encryption_method = encryption_method

    @property
    def anti_logging_threshold(self):
        """Gets the anti_logging_threshold of this XiqSetSsidModePskRequest.  # noqa: E501

        The anti logging threshold  # noqa: E501

        :return: The anti_logging_threshold of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: int
        """
        return self._anti_logging_threshold

    @anti_logging_threshold.setter
    def anti_logging_threshold(self, anti_logging_threshold):
        """Sets the anti_logging_threshold of this XiqSetSsidModePskRequest.

        The anti logging threshold  # noqa: E501

        :param anti_logging_threshold: The anti_logging_threshold of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: int
        """

        self._anti_logging_threshold = anti_logging_threshold

    @property
    def key_type(self):
        """Gets the key_type of this XiqSetSsidModePskRequest.  # noqa: E501


        :return: The key_type of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: XiqSsidKeyType
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this XiqSetSsidModePskRequest.


        :param key_type: The key_type of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: XiqSsidKeyType
        """
        if self.local_vars_configuration.client_side_validation and key_type is None:  # noqa: E501
            raise ValueError("Invalid value for `key_type`, must not be `None`")  # noqa: E501

        self._key_type = key_type

    @property
    def key_value(self):
        """Gets the key_value of this XiqSetSsidModePskRequest.  # noqa: E501

        The PSK key value, minimum 8 characters long  # noqa: E501

        :return: The key_value of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_value

    @key_value.setter
    def key_value(self, key_value):
        """Sets the key_value of this XiqSetSsidModePskRequest.

        The PSK key value, minimum 8 characters long  # noqa: E501

        :param key_value: The key_value of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key_value is None:  # noqa: E501
            raise ValueError("Invalid value for `key_value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key_value is not None and len(key_value) > 2147483647):
            raise ValueError("Invalid value for `key_value`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key_value is not None and len(key_value) < 8):
            raise ValueError("Invalid value for `key_value`, length must be greater than or equal to `8`")  # noqa: E501

        self._key_value = key_value

    @property
    def sae_group(self):
        """Gets the sae_group of this XiqSetSsidModePskRequest.  # noqa: E501


        :return: The sae_group of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: XiqSsidSaeGroup
        """
        return self._sae_group

    @sae_group.setter
    def sae_group(self, sae_group):
        """Sets the sae_group of this XiqSetSsidModePskRequest.


        :param sae_group: The sae_group of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: XiqSsidSaeGroup
        """

        self._sae_group = sae_group

    @property
    def transition_mode(self):
        """Gets the transition_mode of this XiqSetSsidModePskRequest.  # noqa: E501

        Indicates the transition mode if key management is WPA3  # noqa: E501

        :return: The transition_mode of this XiqSetSsidModePskRequest.  # noqa: E501
        :rtype: bool
        """
        return self._transition_mode

    @transition_mode.setter
    def transition_mode(self, transition_mode):
        """Sets the transition_mode of this XiqSetSsidModePskRequest.

        Indicates the transition mode if key management is WPA3  # noqa: E501

        :param transition_mode: The transition_mode of this XiqSetSsidModePskRequest.  # noqa: E501
        :type: bool
        """

        self._transition_mode = transition_mode

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
        if not isinstance(other, XiqSetSsidModePskRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSetSsidModePskRequest):
            return True

        return self.to_dict() != other.to_dict()
