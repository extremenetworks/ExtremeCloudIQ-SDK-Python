# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCreateEndUserRequest(object):
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
        'user_group_id': 'int',
        'name': 'str',
        'user_name': 'str',
        'organization': 'str',
        'visit_purpose': 'str',
        'description': 'str',
        'email_address': 'str',
        'phone_number': 'str',
        'password': 'str',
        'email_password_delivery': 'str',
        'sms_password_delivery': 'str'
    }

    attribute_map = {
        'user_group_id': 'user_group_id',
        'name': 'name',
        'user_name': 'user_name',
        'organization': 'organization',
        'visit_purpose': 'visit_purpose',
        'description': 'description',
        'email_address': 'email_address',
        'phone_number': 'phone_number',
        'password': 'password',
        'email_password_delivery': 'email_password_delivery',
        'sms_password_delivery': 'sms_password_delivery'
    }

    def __init__(self, user_group_id=None, name=None, user_name=None, organization=None, visit_purpose=None, description=None, email_address=None, phone_number=None, password=None, email_password_delivery=None, sms_password_delivery=None, local_vars_configuration=None):  # noqa: E501
        """XiqCreateEndUserRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_group_id = None
        self._name = None
        self._user_name = None
        self._organization = None
        self._visit_purpose = None
        self._description = None
        self._email_address = None
        self._phone_number = None
        self._password = None
        self._email_password_delivery = None
        self._sms_password_delivery = None
        self.discriminator = None

        self.user_group_id = user_group_id
        if name is not None:
            self.name = name
        self.user_name = user_name
        if organization is not None:
            self.organization = organization
        if visit_purpose is not None:
            self.visit_purpose = visit_purpose
        if description is not None:
            self.description = description
        if email_address is not None:
            self.email_address = email_address
        if phone_number is not None:
            self.phone_number = phone_number
        if password is not None:
            self.password = password
        if email_password_delivery is not None:
            self.email_password_delivery = email_password_delivery
        if sms_password_delivery is not None:
            self.sms_password_delivery = sms_password_delivery

    @property
    def user_group_id(self):
        """Gets the user_group_id of this XiqCreateEndUserRequest.  # noqa: E501

        The user group ID  # noqa: E501

        :return: The user_group_id of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: int
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this XiqCreateEndUserRequest.

        The user group ID  # noqa: E501

        :param user_group_id: The user_group_id of this XiqCreateEndUserRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_group_id`, must not be `None`")  # noqa: E501

        self._user_group_id = user_group_id

    @property
    def name(self):
        """Gets the name of this XiqCreateEndUserRequest.  # noqa: E501

        The user common name  # noqa: E501

        :return: The name of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqCreateEndUserRequest.

        The user common name  # noqa: E501

        :param name: The name of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_name(self):
        """Gets the user_name of this XiqCreateEndUserRequest.  # noqa: E501

        The designated username, must match either the user's name, emailAddress, or phoneNumber  # noqa: E501

        :return: The user_name of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this XiqCreateEndUserRequest.

        The designated username, must match either the user's name, emailAddress, or phoneNumber  # noqa: E501

        :param user_name: The user_name of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def organization(self):
        """Gets the organization of this XiqCreateEndUserRequest.  # noqa: E501

        The organization name  # noqa: E501

        :return: The organization of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this XiqCreateEndUserRequest.

        The organization name  # noqa: E501

        :param organization: The organization of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def visit_purpose(self):
        """Gets the visit_purpose of this XiqCreateEndUserRequest.  # noqa: E501

        The purpose of visit  # noqa: E501

        :return: The visit_purpose of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._visit_purpose

    @visit_purpose.setter
    def visit_purpose(self, visit_purpose):
        """Sets the visit_purpose of this XiqCreateEndUserRequest.

        The purpose of visit  # noqa: E501

        :param visit_purpose: The visit_purpose of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._visit_purpose = visit_purpose

    @property
    def description(self):
        """Gets the description of this XiqCreateEndUserRequest.  # noqa: E501

        The user description  # noqa: E501

        :return: The description of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqCreateEndUserRequest.

        The user description  # noqa: E501

        :param description: The description of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_address(self):
        """Gets the email_address of this XiqCreateEndUserRequest.  # noqa: E501

        The user email  # noqa: E501

        :return: The email_address of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this XiqCreateEndUserRequest.

        The user email  # noqa: E501

        :param email_address: The email_address of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def phone_number(self):
        """Gets the phone_number of this XiqCreateEndUserRequest.  # noqa: E501

        The user phone number  # noqa: E501

        :return: The phone_number of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this XiqCreateEndUserRequest.

        The user phone number  # noqa: E501

        :param phone_number: The phone_number of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def password(self):
        """Gets the password of this XiqCreateEndUserRequest.  # noqa: E501

        The user password, if null a random password will be generated base on the user group rule  # noqa: E501

        :return: The password of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this XiqCreateEndUserRequest.

        The user password, if null a random password will be generated base on the user group rule  # noqa: E501

        :param password: The password of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email_password_delivery(self):
        """Gets the email_password_delivery of this XiqCreateEndUserRequest.  # noqa: E501

        The password delivery Email  # noqa: E501

        :return: The email_password_delivery of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_password_delivery

    @email_password_delivery.setter
    def email_password_delivery(self, email_password_delivery):
        """Sets the email_password_delivery of this XiqCreateEndUserRequest.

        The password delivery Email  # noqa: E501

        :param email_password_delivery: The email_password_delivery of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._email_password_delivery = email_password_delivery

    @property
    def sms_password_delivery(self):
        """Gets the sms_password_delivery of this XiqCreateEndUserRequest.  # noqa: E501

        The password delivery SMS  # noqa: E501

        :return: The sms_password_delivery of this XiqCreateEndUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._sms_password_delivery

    @sms_password_delivery.setter
    def sms_password_delivery(self, sms_password_delivery):
        """Sets the sms_password_delivery of this XiqCreateEndUserRequest.

        The password delivery SMS  # noqa: E501

        :param sms_password_delivery: The sms_password_delivery of this XiqCreateEndUserRequest.  # noqa: E501
        :type: str
        """

        self._sms_password_delivery = sms_password_delivery

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
        if not isinstance(other, XiqCreateEndUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCreateEndUserRequest):
            return True

        return self.to_dict() != other.to_dict()
