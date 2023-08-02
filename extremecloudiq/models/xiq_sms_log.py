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


class XiqSmsLog(object):
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
        'user_id': 'int',
        'customer_id': 'str',
        'tel': 'str',
        'profile_name': 'str',
        'status': 'XiqSmsLogStatus',
        'message_id': 'str',
        'status_from_provider': 'str',
        'provider_type': 'str',
        'org_id': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'customer_id': 'customer_id',
        'tel': 'tel',
        'profile_name': 'profile_name',
        'status': 'status',
        'message_id': 'message_id',
        'status_from_provider': 'status_from_provider',
        'provider_type': 'provider_type',
        'org_id': 'org_id',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, user_id=None, customer_id=None, tel=None, profile_name=None, status=None, message_id=None, status_from_provider=None, provider_type=None, org_id=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """XiqSmsLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._customer_id = None
        self._tel = None
        self._profile_name = None
        self._status = None
        self._message_id = None
        self._status_from_provider = None
        self._provider_type = None
        self._org_id = None
        self._timestamp = None
        self.discriminator = None

        self.id = id
        if user_id is not None:
            self.user_id = user_id
        if customer_id is not None:
            self.customer_id = customer_id
        if tel is not None:
            self.tel = tel
        if profile_name is not None:
            self.profile_name = profile_name
        if status is not None:
            self.status = status
        if message_id is not None:
            self.message_id = message_id
        if status_from_provider is not None:
            self.status_from_provider = status_from_provider
        if provider_type is not None:
            self.provider_type = provider_type
        if org_id is not None:
            self.org_id = org_id
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this XiqSmsLog.  # noqa: E501

        The SMS log id  # noqa: E501

        :return: The id of this XiqSmsLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqSmsLog.

        The SMS log id  # noqa: E501

        :param id: The id of this XiqSmsLog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this XiqSmsLog.  # noqa: E501

        The user id  # noqa: E501

        :return: The user_id of this XiqSmsLog.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this XiqSmsLog.

        The user id  # noqa: E501

        :param user_id: The user_id of this XiqSmsLog.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def customer_id(self):
        """Gets the customer_id of this XiqSmsLog.  # noqa: E501

        The customer id  # noqa: E501

        :return: The customer_id of this XiqSmsLog.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this XiqSmsLog.

        The customer id  # noqa: E501

        :param customer_id: The customer_id of this XiqSmsLog.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def tel(self):
        """Gets the tel of this XiqSmsLog.  # noqa: E501

        The phone number  # noqa: E501

        :return: The tel of this XiqSmsLog.  # noqa: E501
        :rtype: str
        """
        return self._tel

    @tel.setter
    def tel(self, tel):
        """Sets the tel of this XiqSmsLog.

        The phone number  # noqa: E501

        :param tel: The tel of this XiqSmsLog.  # noqa: E501
        :type: str
        """

        self._tel = tel

    @property
    def profile_name(self):
        """Gets the profile_name of this XiqSmsLog.  # noqa: E501

        The profile name  # noqa: E501

        :return: The profile_name of this XiqSmsLog.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this XiqSmsLog.

        The profile name  # noqa: E501

        :param profile_name: The profile_name of this XiqSmsLog.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def status(self):
        """Gets the status of this XiqSmsLog.  # noqa: E501


        :return: The status of this XiqSmsLog.  # noqa: E501
        :rtype: XiqSmsLogStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqSmsLog.


        :param status: The status of this XiqSmsLog.  # noqa: E501
        :type: XiqSmsLogStatus
        """

        self._status = status

    @property
    def message_id(self):
        """Gets the message_id of this XiqSmsLog.  # noqa: E501

        The message id from 3rd provider  # noqa: E501

        :return: The message_id of this XiqSmsLog.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this XiqSmsLog.

        The message id from 3rd provider  # noqa: E501

        :param message_id: The message_id of this XiqSmsLog.  # noqa: E501
        :type: str
        """

        self._message_id = message_id

    @property
    def status_from_provider(self):
        """Gets the status_from_provider of this XiqSmsLog.  # noqa: E501

        The status from provider  # noqa: E501

        :return: The status_from_provider of this XiqSmsLog.  # noqa: E501
        :rtype: str
        """
        return self._status_from_provider

    @status_from_provider.setter
    def status_from_provider(self, status_from_provider):
        """Sets the status_from_provider of this XiqSmsLog.

        The status from provider  # noqa: E501

        :param status_from_provider: The status_from_provider of this XiqSmsLog.  # noqa: E501
        :type: str
        """

        self._status_from_provider = status_from_provider

    @property
    def provider_type(self):
        """Gets the provider_type of this XiqSmsLog.  # noqa: E501

        The provider type  # noqa: E501

        :return: The provider_type of this XiqSmsLog.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this XiqSmsLog.

        The provider type  # noqa: E501

        :param provider_type: The provider_type of this XiqSmsLog.  # noqa: E501
        :type: str
        """

        self._provider_type = provider_type

    @property
    def org_id(self):
        """Gets the org_id of this XiqSmsLog.  # noqa: E501

        The org id  # noqa: E501

        :return: The org_id of this XiqSmsLog.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqSmsLog.

        The org id  # noqa: E501

        :param org_id: The org_id of this XiqSmsLog.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqSmsLog.  # noqa: E501

        The audit log timestamp  # noqa: E501

        :return: The timestamp of this XiqSmsLog.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqSmsLog.

        The audit log timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqSmsLog.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, XiqSmsLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSmsLog):
            return True

        return self.to_dict() != other.to_dict()
