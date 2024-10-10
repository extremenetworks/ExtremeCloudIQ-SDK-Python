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


class XiqGenerateApiTokenResponse(object):
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
        'access_token': 'str',
        'create_time': 'datetime',
        'expire_time': 'datetime',
        'creator_id': 'int',
        'customer_id': 'int',
        'description': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'access_token': 'access_token',
        'create_time': 'create_time',
        'expire_time': 'expire_time',
        'creator_id': 'creator_id',
        'customer_id': 'customer_id',
        'description': 'description',
        'permissions': 'permissions'
    }

    def __init__(self, access_token=None, create_time=None, expire_time=None, creator_id=None, customer_id=None, description=None, permissions=None, local_vars_configuration=None):  # noqa: E501
        """XiqGenerateApiTokenResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_token = None
        self._create_time = None
        self._expire_time = None
        self._creator_id = None
        self._customer_id = None
        self._description = None
        self._permissions = None
        self.discriminator = None

        self.access_token = access_token
        self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time
        self.creator_id = creator_id
        self.customer_id = customer_id
        if description is not None:
            self.description = description
        self.permissions = permissions

    @property
    def access_token(self):
        """Gets the access_token of this XiqGenerateApiTokenResponse.  # noqa: E501

        The API access token  # noqa: E501

        :return: The access_token of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this XiqGenerateApiTokenResponse.

        The API access token  # noqa: E501

        :param access_token: The access_token of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_token is None:  # noqa: E501
            raise ValueError("Invalid value for `access_token`, must not be `None`")  # noqa: E501

        self._access_token = access_token

    @property
    def create_time(self):
        """Gets the create_time of this XiqGenerateApiTokenResponse.  # noqa: E501

        The create timestamp  # noqa: E501

        :return: The create_time of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqGenerateApiTokenResponse.

        The create timestamp  # noqa: E501

        :param create_time: The create_time of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def expire_time(self):
        """Gets the expire_time of this XiqGenerateApiTokenResponse.  # noqa: E501

        The expire timestamp, if null means no expiration  # noqa: E501

        :return: The expire_time of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this XiqGenerateApiTokenResponse.

        The expire timestamp, if null means no expiration  # noqa: E501

        :param expire_time: The expire_time of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: datetime
        """

        self._expire_time = expire_time

    @property
    def creator_id(self):
        """Gets the creator_id of this XiqGenerateApiTokenResponse.  # noqa: E501

        The user ID who created the API token  # noqa: E501

        :return: The creator_id of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this XiqGenerateApiTokenResponse.

        The user ID who created the API token  # noqa: E501

        :param creator_id: The creator_id of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and creator_id is None:  # noqa: E501
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

    @property
    def customer_id(self):
        """Gets the customer_id of this XiqGenerateApiTokenResponse.  # noqa: E501

        The customer ID who owns the API token  # noqa: E501

        :return: The customer_id of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this XiqGenerateApiTokenResponse.

        The customer ID who owns the API token  # noqa: E501

        :param customer_id: The customer_id of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and customer_id is None:  # noqa: E501
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def description(self):
        """Gets the description of this XiqGenerateApiTokenResponse.  # noqa: E501

        The description for the API token  # noqa: E501

        :return: The description of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqGenerateApiTokenResponse.

        The description for the API token  # noqa: E501

        :param description: The description of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """Gets the permissions of this XiqGenerateApiTokenResponse.  # noqa: E501

        The permissions for the API token  # noqa: E501

        :return: The permissions of this XiqGenerateApiTokenResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this XiqGenerateApiTokenResponse.

        The permissions for the API token  # noqa: E501

        :param permissions: The permissions of this XiqGenerateApiTokenResponse.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and permissions is None:  # noqa: E501
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

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
        if not isinstance(other, XiqGenerateApiTokenResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqGenerateApiTokenResponse):
            return True

        return self.to_dict() != other.to_dict()
