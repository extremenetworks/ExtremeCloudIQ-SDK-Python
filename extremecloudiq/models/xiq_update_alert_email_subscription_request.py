# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateAlertEmailSubscriptionRequest(object):
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
        'email': 'str',
        'is_enabled': 'bool',
        'is_subscribe_all': 'bool',
        'alert_policy_ids': 'list[int]'
    }

    attribute_map = {
        'email': 'email',
        'is_enabled': 'is_enabled',
        'is_subscribe_all': 'is_subscribe_all',
        'alert_policy_ids': 'alert_policy_ids'
    }

    def __init__(self, email=None, is_enabled=None, is_subscribe_all=None, alert_policy_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateAlertEmailSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._is_enabled = None
        self._is_subscribe_all = None
        self._alert_policy_ids = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_subscribe_all is not None:
            self.is_subscribe_all = is_subscribe_all
        self.alert_policy_ids = alert_policy_ids

    @property
    def email(self):
        """Gets the email of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501

        The email address.  # noqa: E501

        :return: The email of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this XiqUpdateAlertEmailSubscriptionRequest.

        The email address.  # noqa: E501

        :param email: The email of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def is_enabled(self):
        """Gets the is_enabled of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501

        Enable/disable alert notifications for an email.  # noqa: E501

        :return: The is_enabled of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this XiqUpdateAlertEmailSubscriptionRequest.

        Enable/disable alert notifications for an email.  # noqa: E501

        :param is_enabled: The is_enabled of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_subscribe_all(self):
        """Gets the is_subscribe_all of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501

        The all alert policy selected flag.  # noqa: E501

        :return: The is_subscribe_all of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribe_all

    @is_subscribe_all.setter
    def is_subscribe_all(self, is_subscribe_all):
        """Sets the is_subscribe_all of this XiqUpdateAlertEmailSubscriptionRequest.

        The all alert policy selected flag.  # noqa: E501

        :param is_subscribe_all: The is_subscribe_all of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._is_subscribe_all = is_subscribe_all

    @property
    def alert_policy_ids(self):
        """Gets the alert_policy_ids of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501

        The selected alert policy list.  # noqa: E501

        :return: The alert_policy_ids of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._alert_policy_ids

    @alert_policy_ids.setter
    def alert_policy_ids(self, alert_policy_ids):
        """Sets the alert_policy_ids of this XiqUpdateAlertEmailSubscriptionRequest.

        The selected alert policy list.  # noqa: E501

        :param alert_policy_ids: The alert_policy_ids of this XiqUpdateAlertEmailSubscriptionRequest.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and alert_policy_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_policy_ids`, must not be `None`")  # noqa: E501

        self._alert_policy_ids = alert_policy_ids

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
        if not isinstance(other, XiqUpdateAlertEmailSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateAlertEmailSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
