# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqSetSsidModeWepRequest(object):
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
        'key_management': 'XiqSsidWepKeyManagement',
        'encryption_method': 'XiqSsidWepEncryptionMethod',
        'authentication_method': 'XiqSsidWepAuthenticationMethod',
        'default_key': 'XiqSsidWepDefaultKey',
        'key_type': 'XiqSsidKeyType',
        'key_value': 'str',
        'key_value2': 'str',
        'key_value3': 'str',
        'key_value4': 'str',
        'radius_server_group_id': 'int'
    }

    attribute_map = {
        'key_management': 'key_management',
        'encryption_method': 'encryption_method',
        'authentication_method': 'authentication_method',
        'default_key': 'default_key',
        'key_type': 'key_type',
        'key_value': 'key_value',
        'key_value2': 'key_value2',
        'key_value3': 'key_value3',
        'key_value4': 'key_value4',
        'radius_server_group_id': 'radius_server_group_id'
    }

    def __init__(self, key_management=None, encryption_method=None, authentication_method=None, default_key=None, key_type=None, key_value=None, key_value2=None, key_value3=None, key_value4=None, radius_server_group_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqSetSsidModeWepRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key_management = None
        self._encryption_method = None
        self._authentication_method = None
        self._default_key = None
        self._key_type = None
        self._key_value = None
        self._key_value2 = None
        self._key_value3 = None
        self._key_value4 = None
        self._radius_server_group_id = None
        self.discriminator = None

        self.key_management = key_management
        self.encryption_method = encryption_method
        if authentication_method is not None:
            self.authentication_method = authentication_method
        if default_key is not None:
            self.default_key = default_key
        if key_type is not None:
            self.key_type = key_type
        if key_value is not None:
            self.key_value = key_value
        if key_value2 is not None:
            self.key_value2 = key_value2
        if key_value3 is not None:
            self.key_value3 = key_value3
        if key_value4 is not None:
            self.key_value4 = key_value4
        if radius_server_group_id is not None:
            self.radius_server_group_id = radius_server_group_id

    @property
    def key_management(self):
        """Gets the key_management of this XiqSetSsidModeWepRequest.  # noqa: E501


        :return: The key_management of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: XiqSsidWepKeyManagement
        """
        return self._key_management

    @key_management.setter
    def key_management(self, key_management):
        """Sets the key_management of this XiqSetSsidModeWepRequest.


        :param key_management: The key_management of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: XiqSsidWepKeyManagement
        """
        if self.local_vars_configuration.client_side_validation and key_management is None:  # noqa: E501
            raise ValueError("Invalid value for `key_management`, must not be `None`")  # noqa: E501

        self._key_management = key_management

    @property
    def encryption_method(self):
        """Gets the encryption_method of this XiqSetSsidModeWepRequest.  # noqa: E501


        :return: The encryption_method of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: XiqSsidWepEncryptionMethod
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        """Sets the encryption_method of this XiqSetSsidModeWepRequest.


        :param encryption_method: The encryption_method of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: XiqSsidWepEncryptionMethod
        """
        if self.local_vars_configuration.client_side_validation and encryption_method is None:  # noqa: E501
            raise ValueError("Invalid value for `encryption_method`, must not be `None`")  # noqa: E501

        self._encryption_method = encryption_method

    @property
    def authentication_method(self):
        """Gets the authentication_method of this XiqSetSsidModeWepRequest.  # noqa: E501


        :return: The authentication_method of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: XiqSsidWepAuthenticationMethod
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this XiqSetSsidModeWepRequest.


        :param authentication_method: The authentication_method of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: XiqSsidWepAuthenticationMethod
        """

        self._authentication_method = authentication_method

    @property
    def default_key(self):
        """Gets the default_key of this XiqSetSsidModeWepRequest.  # noqa: E501


        :return: The default_key of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: XiqSsidWepDefaultKey
        """
        return self._default_key

    @default_key.setter
    def default_key(self, default_key):
        """Sets the default_key of this XiqSetSsidModeWepRequest.


        :param default_key: The default_key of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: XiqSsidWepDefaultKey
        """

        self._default_key = default_key

    @property
    def key_type(self):
        """Gets the key_type of this XiqSetSsidModeWepRequest.  # noqa: E501


        :return: The key_type of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: XiqSsidKeyType
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this XiqSetSsidModeWepRequest.


        :param key_type: The key_type of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: XiqSsidKeyType
        """

        self._key_type = key_type

    @property
    def key_value(self):
        """Gets the key_value of this XiqSetSsidModeWepRequest.  # noqa: E501

        The first key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :return: The key_value of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_value

    @key_value.setter
    def key_value(self, key_value):
        """Sets the key_value of this XiqSetSsidModeWepRequest.

        The first key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :param key_value: The key_value of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                key_value is not None and len(key_value) > 13):
            raise ValueError("Invalid value for `key_value`, length must be less than or equal to `13`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key_value is not None and len(key_value) < 5):
            raise ValueError("Invalid value for `key_value`, length must be greater than or equal to `5`")  # noqa: E501

        self._key_value = key_value

    @property
    def key_value2(self):
        """Gets the key_value2 of this XiqSetSsidModeWepRequest.  # noqa: E501

        The second key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :return: The key_value2 of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_value2

    @key_value2.setter
    def key_value2(self, key_value2):
        """Sets the key_value2 of this XiqSetSsidModeWepRequest.

        The second key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :param key_value2: The key_value2 of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                key_value2 is not None and len(key_value2) > 13):
            raise ValueError("Invalid value for `key_value2`, length must be less than or equal to `13`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key_value2 is not None and len(key_value2) < 5):
            raise ValueError("Invalid value for `key_value2`, length must be greater than or equal to `5`")  # noqa: E501

        self._key_value2 = key_value2

    @property
    def key_value3(self):
        """Gets the key_value3 of this XiqSetSsidModeWepRequest.  # noqa: E501

        The third key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :return: The key_value3 of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_value3

    @key_value3.setter
    def key_value3(self, key_value3):
        """Sets the key_value3 of this XiqSetSsidModeWepRequest.

        The third key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :param key_value3: The key_value3 of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                key_value3 is not None and len(key_value3) > 13):
            raise ValueError("Invalid value for `key_value3`, length must be less than or equal to `13`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key_value3 is not None and len(key_value3) < 5):
            raise ValueError("Invalid value for `key_value3`, length must be greater than or equal to `5`")  # noqa: E501

        self._key_value3 = key_value3

    @property
    def key_value4(self):
        """Gets the key_value4 of this XiqSetSsidModeWepRequest.  # noqa: E501

        The fourth key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :return: The key_value4 of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_value4

    @key_value4.setter
    def key_value4(self, key_value4):
        """Sets the key_value4 of this XiqSetSsidModeWepRequest.

        The fourth key value, must be 13 characters long for WEP104, and 5 characters long for WEP40, cannot be null if it is the default key  # noqa: E501

        :param key_value4: The key_value4 of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                key_value4 is not None and len(key_value4) > 13):
            raise ValueError("Invalid value for `key_value4`, length must be less than or equal to `13`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key_value4 is not None and len(key_value4) < 5):
            raise ValueError("Invalid value for `key_value4`, length must be greater than or equal to `5`")  # noqa: E501

        self._key_value4 = key_value4

    @property
    def radius_server_group_id(self):
        """Gets the radius_server_group_id of this XiqSetSsidModeWepRequest.  # noqa: E501

        The RADIUS server group ID if using WEP_8021x as the key management  # noqa: E501

        :return: The radius_server_group_id of this XiqSetSsidModeWepRequest.  # noqa: E501
        :rtype: int
        """
        return self._radius_server_group_id

    @radius_server_group_id.setter
    def radius_server_group_id(self, radius_server_group_id):
        """Sets the radius_server_group_id of this XiqSetSsidModeWepRequest.

        The RADIUS server group ID if using WEP_8021x as the key management  # noqa: E501

        :param radius_server_group_id: The radius_server_group_id of this XiqSetSsidModeWepRequest.  # noqa: E501
        :type: int
        """

        self._radius_server_group_id = radius_server_group_id

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
        if not isinstance(other, XiqSetSsidModeWepRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSetSsidModeWepRequest):
            return True

        return self.to_dict() != other.to_dict()
