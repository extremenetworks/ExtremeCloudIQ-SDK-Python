# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.5.0.51
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAlertWebhookSubscription(object):
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
        'url': 'str',
        'secret': 'str',
        'is_enabled': 'bool',
        'is_subscribe_all': 'bool',
        'alert_policy_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'url': 'url',
        'secret': 'secret',
        'is_enabled': 'is_enabled',
        'is_subscribe_all': 'is_subscribe_all',
        'alert_policy_ids': 'alert_policy_ids'
    }

    def __init__(self, id=None, create_time=None, update_time=None, url=None, secret=None, is_enabled=None, is_subscribe_all=None, alert_policy_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertWebhookSubscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._url = None
        self._secret = None
        self._is_enabled = None
        self._is_subscribe_all = None
        self._alert_policy_ids = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.url = url
        self.secret = secret
        self.is_enabled = is_enabled
        self.is_subscribe_all = is_subscribe_all
        if alert_policy_ids is not None:
            self.alert_policy_ids = alert_policy_ids

    @property
    def id(self):
        """Gets the id of this XiqAlertWebhookSubscription.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqAlertWebhookSubscription.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqAlertWebhookSubscription.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqAlertWebhookSubscription.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqAlertWebhookSubscription.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqAlertWebhookSubscription.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def url(self):
        """Gets the url of this XiqAlertWebhookSubscription.  # noqa: E501

        The webhook endpoint URL.  # noqa: E501

        :return: The url of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this XiqAlertWebhookSubscription.

        The webhook endpoint URL.  # noqa: E501

        :param url: The url of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this XiqAlertWebhookSubscription.  # noqa: E501

        The auth secret for the webhook endpoint.  # noqa: E501

        :return: The secret of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this XiqAlertWebhookSubscription.

        The auth secret for the webhook endpoint.  # noqa: E501

        :param secret: The secret of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def is_enabled(self):
        """Gets the is_enabled of this XiqAlertWebhookSubscription.  # noqa: E501

        Enable/disable alert notifications for a webhook endpoint.  # noqa: E501

        :return: The is_enabled of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this XiqAlertWebhookSubscription.

        Enable/disable alert notifications for a webhook endpoint.  # noqa: E501

        :param is_enabled: The is_enabled of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def is_subscribe_all(self):
        """Gets the is_subscribe_all of this XiqAlertWebhookSubscription.  # noqa: E501

        The all alert policy selected flag.  # noqa: E501

        :return: The is_subscribe_all of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: bool
        """
        return self._is_subscribe_all

    @is_subscribe_all.setter
    def is_subscribe_all(self, is_subscribe_all):
        """Sets the is_subscribe_all of this XiqAlertWebhookSubscription.

        The all alert policy selected flag.  # noqa: E501

        :param is_subscribe_all: The is_subscribe_all of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_subscribe_all is None:  # noqa: E501
            raise ValueError("Invalid value for `is_subscribe_all`, must not be `None`")  # noqa: E501

        self._is_subscribe_all = is_subscribe_all

    @property
    def alert_policy_ids(self):
        """Gets the alert_policy_ids of this XiqAlertWebhookSubscription.  # noqa: E501

        The selected alert policy list.  # noqa: E501

        :return: The alert_policy_ids of this XiqAlertWebhookSubscription.  # noqa: E501
        :rtype: list[int]
        """
        return self._alert_policy_ids

    @alert_policy_ids.setter
    def alert_policy_ids(self, alert_policy_ids):
        """Sets the alert_policy_ids of this XiqAlertWebhookSubscription.

        The selected alert policy list.  # noqa: E501

        :param alert_policy_ids: The alert_policy_ids of this XiqAlertWebhookSubscription.  # noqa: E501
        :type: list[int]
        """

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
        if not isinstance(other, XiqAlertWebhookSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertWebhookSubscription):
            return True

        return self.to_dict() != other.to_dict()
