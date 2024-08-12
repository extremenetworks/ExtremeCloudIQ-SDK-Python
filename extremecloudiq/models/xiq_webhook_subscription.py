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


class XiqWebhookSubscription(object):
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
        'application': 'str',
        'url': 'str',
        'secret': 'str',
        'data_type': 'XiqSubscriptionDataType',
        'message_type': 'XiqSubscriptionMessageType',
        'status': 'XiqSubscriptionStatus'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'application': 'application',
        'url': 'url',
        'secret': 'secret',
        'data_type': 'data_type',
        'message_type': 'message_type',
        'status': 'status'
    }

    def __init__(self, id=None, create_time=None, update_time=None, application=None, url=None, secret=None, data_type=None, message_type=None, status=None, local_vars_configuration=None):  # noqa: E501
        """XiqWebhookSubscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._application = None
        self._url = None
        self._secret = None
        self._data_type = None
        self._message_type = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.application = application
        self.url = url
        self.secret = secret
        self.data_type = data_type
        self.message_type = message_type
        self.status = status

    @property
    def id(self):
        """Gets the id of this XiqWebhookSubscription.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqWebhookSubscription.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqWebhookSubscription.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqWebhookSubscription.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqWebhookSubscription.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqWebhookSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqWebhookSubscription.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqWebhookSubscription.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqWebhookSubscription.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqWebhookSubscription.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqWebhookSubscription.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqWebhookSubscription.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def application(self):
        """Gets the application of this XiqWebhookSubscription.  # noqa: E501

        The external application name.  # noqa: E501

        :return: The application of this XiqWebhookSubscription.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this XiqWebhookSubscription.

        The external application name.  # noqa: E501

        :param application: The application of this XiqWebhookSubscription.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application is None:  # noqa: E501
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def url(self):
        """Gets the url of this XiqWebhookSubscription.  # noqa: E501

        The webhook endpoint URL.  # noqa: E501

        :return: The url of this XiqWebhookSubscription.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this XiqWebhookSubscription.

        The webhook endpoint URL.  # noqa: E501

        :param url: The url of this XiqWebhookSubscription.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this XiqWebhookSubscription.  # noqa: E501

        The basic auth secret for the webhook endpoint.  # noqa: E501

        :return: The secret of this XiqWebhookSubscription.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this XiqWebhookSubscription.

        The basic auth secret for the webhook endpoint.  # noqa: E501

        :param secret: The secret of this XiqWebhookSubscription.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secret is None:  # noqa: E501
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def data_type(self):
        """Gets the data_type of this XiqWebhookSubscription.  # noqa: E501


        :return: The data_type of this XiqWebhookSubscription.  # noqa: E501
        :rtype: XiqSubscriptionDataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this XiqWebhookSubscription.


        :param data_type: The data_type of this XiqWebhookSubscription.  # noqa: E501
        :type: XiqSubscriptionDataType
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def message_type(self):
        """Gets the message_type of this XiqWebhookSubscription.  # noqa: E501


        :return: The message_type of this XiqWebhookSubscription.  # noqa: E501
        :rtype: XiqSubscriptionMessageType
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this XiqWebhookSubscription.


        :param message_type: The message_type of this XiqWebhookSubscription.  # noqa: E501
        :type: XiqSubscriptionMessageType
        """
        if self.local_vars_configuration.client_side_validation and message_type is None:  # noqa: E501
            raise ValueError("Invalid value for `message_type`, must not be `None`")  # noqa: E501

        self._message_type = message_type

    @property
    def status(self):
        """Gets the status of this XiqWebhookSubscription.  # noqa: E501


        :return: The status of this XiqWebhookSubscription.  # noqa: E501
        :rtype: XiqSubscriptionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqWebhookSubscription.


        :param status: The status of this XiqWebhookSubscription.  # noqa: E501
        :type: XiqSubscriptionStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, XiqWebhookSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqWebhookSubscription):
            return True

        return self.to_dict() != other.to_dict()
