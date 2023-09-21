# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqPasswordSettings(object):
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
        'enable_letters': 'bool',
        'enable_numbers': 'bool',
        'enable_special_characters': 'bool',
        'password_concat_string': 'str',
        'psk_generation_method': 'XiqPskGenerationMethod',
        'password_character_types': 'XiqPasswordCharacterType',
        'password_length': 'int'
    }

    attribute_map = {
        'enable_letters': 'enable_letters',
        'enable_numbers': 'enable_numbers',
        'enable_special_characters': 'enable_special_characters',
        'password_concat_string': 'password_concat_string',
        'psk_generation_method': 'psk_generation_method',
        'password_character_types': 'password_character_types',
        'password_length': 'password_length'
    }

    def __init__(self, enable_letters=None, enable_numbers=None, enable_special_characters=None, password_concat_string=None, psk_generation_method=None, password_character_types=None, password_length=None, local_vars_configuration=None):  # noqa: E501
        """XiqPasswordSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_letters = None
        self._enable_numbers = None
        self._enable_special_characters = None
        self._password_concat_string = None
        self._psk_generation_method = None
        self._password_character_types = None
        self._password_length = None
        self.discriminator = None

        if enable_letters is not None:
            self.enable_letters = enable_letters
        if enable_numbers is not None:
            self.enable_numbers = enable_numbers
        if enable_special_characters is not None:
            self.enable_special_characters = enable_special_characters
        if password_concat_string is not None:
            self.password_concat_string = password_concat_string
        self.psk_generation_method = psk_generation_method
        self.password_character_types = password_character_types
        self.password_length = password_length

    @property
    def enable_letters(self):
        """Gets the enable_letters of this XiqPasswordSettings.  # noqa: E501

        Enable use of letters  # noqa: E501

        :return: The enable_letters of this XiqPasswordSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_letters

    @enable_letters.setter
    def enable_letters(self, enable_letters):
        """Sets the enable_letters of this XiqPasswordSettings.

        Enable use of letters  # noqa: E501

        :param enable_letters: The enable_letters of this XiqPasswordSettings.  # noqa: E501
        :type: bool
        """

        self._enable_letters = enable_letters

    @property
    def enable_numbers(self):
        """Gets the enable_numbers of this XiqPasswordSettings.  # noqa: E501

        Enable use of numbers  # noqa: E501

        :return: The enable_numbers of this XiqPasswordSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_numbers

    @enable_numbers.setter
    def enable_numbers(self, enable_numbers):
        """Sets the enable_numbers of this XiqPasswordSettings.

        Enable use of numbers  # noqa: E501

        :param enable_numbers: The enable_numbers of this XiqPasswordSettings.  # noqa: E501
        :type: bool
        """

        self._enable_numbers = enable_numbers

    @property
    def enable_special_characters(self):
        """Gets the enable_special_characters of this XiqPasswordSettings.  # noqa: E501

        Enable use of special characters  # noqa: E501

        :return: The enable_special_characters of this XiqPasswordSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_special_characters

    @enable_special_characters.setter
    def enable_special_characters(self, enable_special_characters):
        """Sets the enable_special_characters of this XiqPasswordSettings.

        Enable use of special characters  # noqa: E501

        :param enable_special_characters: The enable_special_characters of this XiqPasswordSettings.  # noqa: E501
        :type: bool
        """

        self._enable_special_characters = enable_special_characters

    @property
    def password_concat_string(self):
        """Gets the password_concat_string of this XiqPasswordSettings.  # noqa: E501

        The password concatenated string  # noqa: E501

        :return: The password_concat_string of this XiqPasswordSettings.  # noqa: E501
        :rtype: str
        """
        return self._password_concat_string

    @password_concat_string.setter
    def password_concat_string(self, password_concat_string):
        """Sets the password_concat_string of this XiqPasswordSettings.

        The password concatenated string  # noqa: E501

        :param password_concat_string: The password_concat_string of this XiqPasswordSettings.  # noqa: E501
        :type: str
        """

        self._password_concat_string = password_concat_string

    @property
    def psk_generation_method(self):
        """Gets the psk_generation_method of this XiqPasswordSettings.  # noqa: E501


        :return: The psk_generation_method of this XiqPasswordSettings.  # noqa: E501
        :rtype: XiqPskGenerationMethod
        """
        return self._psk_generation_method

    @psk_generation_method.setter
    def psk_generation_method(self, psk_generation_method):
        """Sets the psk_generation_method of this XiqPasswordSettings.


        :param psk_generation_method: The psk_generation_method of this XiqPasswordSettings.  # noqa: E501
        :type: XiqPskGenerationMethod
        """
        if self.local_vars_configuration.client_side_validation and psk_generation_method is None:  # noqa: E501
            raise ValueError("Invalid value for `psk_generation_method`, must not be `None`")  # noqa: E501

        self._psk_generation_method = psk_generation_method

    @property
    def password_character_types(self):
        """Gets the password_character_types of this XiqPasswordSettings.  # noqa: E501


        :return: The password_character_types of this XiqPasswordSettings.  # noqa: E501
        :rtype: XiqPasswordCharacterType
        """
        return self._password_character_types

    @password_character_types.setter
    def password_character_types(self, password_character_types):
        """Sets the password_character_types of this XiqPasswordSettings.


        :param password_character_types: The password_character_types of this XiqPasswordSettings.  # noqa: E501
        :type: XiqPasswordCharacterType
        """
        if self.local_vars_configuration.client_side_validation and password_character_types is None:  # noqa: E501
            raise ValueError("Invalid value for `password_character_types`, must not be `None`")  # noqa: E501

        self._password_character_types = password_character_types

    @property
    def password_length(self):
        """Gets the password_length of this XiqPasswordSettings.  # noqa: E501

        The maximun password string length  # noqa: E501

        :return: The password_length of this XiqPasswordSettings.  # noqa: E501
        :rtype: int
        """
        return self._password_length

    @password_length.setter
    def password_length(self, password_length):
        """Sets the password_length of this XiqPasswordSettings.

        The maximun password string length  # noqa: E501

        :param password_length: The password_length of this XiqPasswordSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and password_length is None:  # noqa: E501
            raise ValueError("Invalid value for `password_length`, must not be `None`")  # noqa: E501

        self._password_length = password_length

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
        if not isinstance(other, XiqPasswordSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPasswordSettings):
            return True

        return self.to_dict() != other.to_dict()
