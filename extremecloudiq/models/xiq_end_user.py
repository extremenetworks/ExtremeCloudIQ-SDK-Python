# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqEndUser(object):
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
        'id': 'int',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'org_id': 'int',
        'name': 'str',
        'description': 'str',
        'email_address': 'str',
        'phone_number': 'str',
        'password': 'str',
        'user_name': 'str',
        'organization': 'str',
        'visit_purpose': 'str',
        'email_password_delivery': 'str',
        'sms_password_delivery': 'str',
        'user_group_id': 'int',
        'user_group_name': 'str',
        'approval_type': 'str',
        'expired_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'email_address': 'email_address',
        'phone_number': 'phone_number',
        'password': 'password',
        'user_name': 'user_name',
        'organization': 'organization',
        'visit_purpose': 'visit_purpose',
        'email_password_delivery': 'email_password_delivery',
        'sms_password_delivery': 'sms_password_delivery',
        'user_group_id': 'user_group_id',
        'user_group_name': 'user_group_name',
        'approval_type': 'approval_type',
        'expired_time': 'expired_time'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, email_address=None, phone_number=None, password=None, user_name=None, organization=None, visit_purpose=None, email_password_delivery=None, sms_password_delivery=None, user_group_id=None, user_group_name=None, approval_type=None, expired_time=None, local_vars_configuration=None):  # noqa: E501
        """XiqEndUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._email_address = None
        self._phone_number = None
        self._password = None
        self._user_name = None
        self._organization = None
        self._visit_purpose = None
        self._email_password_delivery = None
        self._sms_password_delivery = None
        self._user_group_id = None
        self._user_group_name = None
        self._approval_type = None
        self._expired_time = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.name = name
        if description is not None:
            self.description = description
        self.email_address = email_address
        self.phone_number = phone_number
        if password is not None:
            self.password = password
        self.user_name = user_name
        if organization is not None:
            self.organization = organization
        if visit_purpose is not None:
            self.visit_purpose = visit_purpose
        if email_password_delivery is not None:
            self.email_password_delivery = email_password_delivery
        if sms_password_delivery is not None:
            self.sms_password_delivery = sms_password_delivery
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name
        self.approval_type = approval_type
        self.expired_time = expired_time

    @property
    def id(self):
        """Gets the id of this XiqEndUser.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqEndUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqEndUser.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqEndUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqEndUser.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqEndUser.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqEndUser.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqEndUser.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqEndUser.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqEndUser.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqEndUser.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqEndUser.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqEndUser.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqEndUser.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqEndUser.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqEndUser.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqEndUser.  # noqa: E501

        The user common name  # noqa: E501

        :return: The name of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqEndUser.

        The user common name  # noqa: E501

        :param name: The name of this XiqEndUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqEndUser.  # noqa: E501

        The user description  # noqa: E501

        :return: The description of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqEndUser.

        The user description  # noqa: E501

        :param description: The description of this XiqEndUser.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_address(self):
        """Gets the email_address of this XiqEndUser.  # noqa: E501

        The user email address  # noqa: E501

        :return: The email_address of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this XiqEndUser.

        The user email address  # noqa: E501

        :param email_address: The email_address of this XiqEndUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def phone_number(self):
        """Gets the phone_number of this XiqEndUser.  # noqa: E501

        The user phone number  # noqa: E501

        :return: The phone_number of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this XiqEndUser.

        The user phone number  # noqa: E501

        :param phone_number: The phone_number of this XiqEndUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and phone_number is None:  # noqa: E501
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def password(self):
        """Gets the password of this XiqEndUser.  # noqa: E501

        The user password  # noqa: E501

        :return: The password of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this XiqEndUser.

        The user password  # noqa: E501

        :param password: The password of this XiqEndUser.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def user_name(self):
        """Gets the user_name of this XiqEndUser.  # noqa: E501

        The user identifiable name or the same one from common name, emailAddress or phoneNumber  # noqa: E501

        :return: The user_name of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this XiqEndUser.

        The user identifiable name or the same one from common name, emailAddress or phoneNumber  # noqa: E501

        :param user_name: The user_name of this XiqEndUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_name`, must not be `None`")  # noqa: E501

        self._user_name = user_name

    @property
    def organization(self):
        """Gets the organization of this XiqEndUser.  # noqa: E501

        The organization name  # noqa: E501

        :return: The organization of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this XiqEndUser.

        The organization name  # noqa: E501

        :param organization: The organization of this XiqEndUser.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def visit_purpose(self):
        """Gets the visit_purpose of this XiqEndUser.  # noqa: E501

        The purpose of visit  # noqa: E501

        :return: The visit_purpose of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._visit_purpose

    @visit_purpose.setter
    def visit_purpose(self, visit_purpose):
        """Sets the visit_purpose of this XiqEndUser.

        The purpose of visit  # noqa: E501

        :param visit_purpose: The visit_purpose of this XiqEndUser.  # noqa: E501
        :type: str
        """

        self._visit_purpose = visit_purpose

    @property
    def email_password_delivery(self):
        """Gets the email_password_delivery of this XiqEndUser.  # noqa: E501

        The email address for password delivery  # noqa: E501

        :return: The email_password_delivery of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._email_password_delivery

    @email_password_delivery.setter
    def email_password_delivery(self, email_password_delivery):
        """Sets the email_password_delivery of this XiqEndUser.

        The email address for password delivery  # noqa: E501

        :param email_password_delivery: The email_password_delivery of this XiqEndUser.  # noqa: E501
        :type: str
        """

        self._email_password_delivery = email_password_delivery

    @property
    def sms_password_delivery(self):
        """Gets the sms_password_delivery of this XiqEndUser.  # noqa: E501

        The sms number for password delivery  # noqa: E501

        :return: The sms_password_delivery of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._sms_password_delivery

    @sms_password_delivery.setter
    def sms_password_delivery(self, sms_password_delivery):
        """Sets the sms_password_delivery of this XiqEndUser.

        The sms number for password delivery  # noqa: E501

        :param sms_password_delivery: The sms_password_delivery of this XiqEndUser.  # noqa: E501
        :type: str
        """

        self._sms_password_delivery = sms_password_delivery

    @property
    def user_group_id(self):
        """Gets the user_group_id of this XiqEndUser.  # noqa: E501

        The user group ID  # noqa: E501

        :return: The user_group_id of this XiqEndUser.  # noqa: E501
        :rtype: int
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this XiqEndUser.

        The user group ID  # noqa: E501

        :param user_group_id: The user_group_id of this XiqEndUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and user_group_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_group_id`, must not be `None`")  # noqa: E501

        self._user_group_id = user_group_id

    @property
    def user_group_name(self):
        """Gets the user_group_name of this XiqEndUser.  # noqa: E501

        The user group name  # noqa: E501

        :return: The user_group_name of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this XiqEndUser.

        The user group name  # noqa: E501

        :param user_group_name: The user_group_name of this XiqEndUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `user_group_name`, must not be `None`")  # noqa: E501

        self._user_group_name = user_group_name

    @property
    def approval_type(self):
        """Gets the approval_type of this XiqEndUser.  # noqa: E501

        The approval type  # noqa: E501

        :return: The approval_type of this XiqEndUser.  # noqa: E501
        :rtype: str
        """
        return self._approval_type

    @approval_type.setter
    def approval_type(self, approval_type):
        """Sets the approval_type of this XiqEndUser.

        The approval type  # noqa: E501

        :param approval_type: The approval_type of this XiqEndUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and approval_type is None:  # noqa: E501
            raise ValueError("Invalid value for `approval_type`, must not be `None`")  # noqa: E501

        self._approval_type = approval_type

    @property
    def expired_time(self):
        """Gets the expired_time of this XiqEndUser.  # noqa: E501

        The password expired time  # noqa: E501

        :return: The expired_time of this XiqEndUser.  # noqa: E501
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this XiqEndUser.

        The password expired time  # noqa: E501

        :param expired_time: The expired_time of this XiqEndUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expired_time is None:  # noqa: E501
            raise ValueError("Invalid value for `expired_time`, must not be `None`")  # noqa: E501

        self._expired_time = expired_time

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
        if not isinstance(other, XiqEndUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqEndUser):
            return True

        return self.to_dict() != other.to_dict()
