# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.2.1
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCreateWebhookSubscriptionRequest(object):
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
        'application': 'str',
        'url': 'str',
        'secret': 'str',
        'message_type': 'XiqSubscriptionMessageType'
    }

    attribute_map = {
        'application': 'application',
        'url': 'url',
        'secret': 'secret',
        'message_type': 'message_type'
    }

    def __init__(self, application=None, url=None, secret=None, message_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqCreateWebhookSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application = None
        self._url = None
        self._secret = None
        self._message_type = None
        self.discriminator = None

        self.application = application
        self.url = url
        if secret is not None:
            self.secret = secret
        self.message_type = message_type

    @property
    def application(self):
        """Gets the application of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501

        The external application name.  # noqa: E501

        :return: The application of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this XiqCreateWebhookSubscriptionRequest.

        The external application name.  # noqa: E501

        :param application: The application of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application is None:  # noqa: E501
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501

        self._application = application

    @property
    def url(self):
        """Gets the url of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501

        The webhook endpoint URL.  # noqa: E501

        :return: The url of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this XiqCreateWebhookSubscriptionRequest.

        The webhook endpoint URL.  # noqa: E501

        :param url: The url of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501

        The basic auth secret for the webhook endpoint.  # noqa: E501

        :return: The secret of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this XiqCreateWebhookSubscriptionRequest.

        The basic auth secret for the webhook endpoint.  # noqa: E501

        :param secret: The secret of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def message_type(self):
        """Gets the message_type of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501


        :return: The message_type of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :rtype: XiqSubscriptionMessageType
        """
        return self._message_type

    @message_type.setter
    def message_type(self, message_type):
        """Sets the message_type of this XiqCreateWebhookSubscriptionRequest.


        :param message_type: The message_type of this XiqCreateWebhookSubscriptionRequest.  # noqa: E501
        :type: XiqSubscriptionMessageType
        """
        if self.local_vars_configuration.client_side_validation and message_type is None:  # noqa: E501
            raise ValueError("Invalid value for `message_type`, must not be `None`")  # noqa: E501

        self._message_type = message_type

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
        if not isinstance(other, XiqCreateWebhookSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCreateWebhookSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
