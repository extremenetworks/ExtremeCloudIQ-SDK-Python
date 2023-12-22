# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqApiTokenInfo(object):
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
        'user_name': 'str',
        'user_id': 'int',
        'role': 'str',
        'owner_id': 'int',
        'data_center': 'str',
        'scopes': 'list[str]',
        'issued_at': 'datetime',
        'expiration_time': 'datetime',
        'expires_in': 'int'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_id': 'user_id',
        'role': 'role',
        'owner_id': 'owner_id',
        'data_center': 'data_center',
        'scopes': 'scopes',
        'issued_at': 'issued_at',
        'expiration_time': 'expiration_time',
        'expires_in': 'expires_in'
    }

    def __init__(self, user_name=None, user_id=None, role=None, owner_id=None, data_center=None, scopes=None, issued_at=None, expiration_time=None, expires_in=None, local_vars_configuration=None):  # noqa: E501
        """XiqApiTokenInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_name = None
        self._user_id = None
        self._role = None
        self._owner_id = None
        self._data_center = None
        self._scopes = None
        self._issued_at = None
        self._expiration_time = None
        self._expires_in = None
        self.discriminator = None

        self.user_name = user_name
        self.user_id = user_id
        self.role = role
        self.owner_id = owner_id
        self.data_center = data_center
        self.scopes = scopes
        self.issued_at = issued_at
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if expires_in is not None:
            self.expires_in = expires_in

    @property
    def user_name(self):
        """Gets the user_name of this XiqApiTokenInfo.  # noqa: E501

        The login username  # noqa: E501

        :return: The user_name of this XiqApiTokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this XiqApiTokenInfo.

        The login username  # noqa: E501

        :param user_name: The user_name of this XiqApiTokenInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def user_id(self):
        """Gets the user_id of this XiqApiTokenInfo.  # noqa: E501

        The login user ID  # noqa: E501

        :return: The user_id of this XiqApiTokenInfo.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this XiqApiTokenInfo.

        The login user ID  # noqa: E501

        :param user_id: The user_id of this XiqApiTokenInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def role(self):
        """Gets the role of this XiqApiTokenInfo.  # noqa: E501

        The role of login user  # noqa: E501

        :return: The role of this XiqApiTokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this XiqApiTokenInfo.

        The role of login user  # noqa: E501

        :param role: The role of this XiqApiTokenInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def owner_id(self):
        """Gets the owner_id of this XiqApiTokenInfo.  # noqa: E501

        The home ownerId of login user  # noqa: E501

        :return: The owner_id of this XiqApiTokenInfo.  # noqa: E501
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this XiqApiTokenInfo.

        The home ownerId of login user  # noqa: E501

        :param owner_id: The owner_id of this XiqApiTokenInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and owner_id is None:  # noqa: E501
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def data_center(self):
        """Gets the data_center of this XiqApiTokenInfo.  # noqa: E501

        The home data center of login user  # noqa: E501

        :return: The data_center of this XiqApiTokenInfo.  # noqa: E501
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this XiqApiTokenInfo.

        The home data center of login user  # noqa: E501

        :param data_center: The data_center of this XiqApiTokenInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_center is None:  # noqa: E501
            raise ValueError("Invalid value for `data_center`, must not be `None`")  # noqa: E501

        self._data_center = data_center

    @property
    def scopes(self):
        """Gets the scopes of this XiqApiTokenInfo.  # noqa: E501

        The login user permissions  # noqa: E501

        :return: The scopes of this XiqApiTokenInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this XiqApiTokenInfo.

        The login user permissions  # noqa: E501

        :param scopes: The scopes of this XiqApiTokenInfo.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and scopes is None:  # noqa: E501
            raise ValueError("Invalid value for `scopes`, must not be `None`")  # noqa: E501

        self._scopes = scopes

    @property
    def issued_at(self):
        """Gets the issued_at of this XiqApiTokenInfo.  # noqa: E501

        The time at which the JWT was issued  # noqa: E501

        :return: The issued_at of this XiqApiTokenInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this XiqApiTokenInfo.

        The time at which the JWT was issued  # noqa: E501

        :param issued_at: The issued_at of this XiqApiTokenInfo.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and issued_at is None:  # noqa: E501
            raise ValueError("Invalid value for `issued_at`, must not be `None`")  # noqa: E501

        self._issued_at = issued_at

    @property
    def expiration_time(self):
        """Gets the expiration_time of this XiqApiTokenInfo.  # noqa: E501

        The expiration time on or after which the JWT MUST NOT be accepted for processing  # noqa: E501

        :return: The expiration_time of this XiqApiTokenInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this XiqApiTokenInfo.

        The expiration time on or after which the JWT MUST NOT be accepted for processing  # noqa: E501

        :param expiration_time: The expiration_time of this XiqApiTokenInfo.  # noqa: E501
        :type: datetime
        """

        self._expiration_time = expiration_time

    @property
    def expires_in(self):
        """Gets the expires_in of this XiqApiTokenInfo.  # noqa: E501

        The expires in seconds  # noqa: E501

        :return: The expires_in of this XiqApiTokenInfo.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this XiqApiTokenInfo.

        The expires in seconds  # noqa: E501

        :param expires_in: The expires_in of this XiqApiTokenInfo.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

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
        if not isinstance(other, XiqApiTokenInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqApiTokenInfo):
            return True

        return self.to_dict() != other.to_dict()
