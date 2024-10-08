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


class XiqDeliverySettings(object):
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
        'email_template_id': 'int',
        'sms_template_id': 'int'
    }

    attribute_map = {
        'email_template_id': 'email_template_id',
        'sms_template_id': 'sms_template_id'
    }

    def __init__(self, email_template_id=None, sms_template_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeliverySettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_template_id = None
        self._sms_template_id = None
        self.discriminator = None

        if email_template_id is not None:
            self.email_template_id = email_template_id
        if sms_template_id is not None:
            self.sms_template_id = sms_template_id

    @property
    def email_template_id(self):
        """Gets the email_template_id of this XiqDeliverySettings.  # noqa: E501

        The Email Template ID  # noqa: E501

        :return: The email_template_id of this XiqDeliverySettings.  # noqa: E501
        :rtype: int
        """
        return self._email_template_id

    @email_template_id.setter
    def email_template_id(self, email_template_id):
        """Sets the email_template_id of this XiqDeliverySettings.

        The Email Template ID  # noqa: E501

        :param email_template_id: The email_template_id of this XiqDeliverySettings.  # noqa: E501
        :type: int
        """

        self._email_template_id = email_template_id

    @property
    def sms_template_id(self):
        """Gets the sms_template_id of this XiqDeliverySettings.  # noqa: E501

        The SMS Template ID   # noqa: E501

        :return: The sms_template_id of this XiqDeliverySettings.  # noqa: E501
        :rtype: int
        """
        return self._sms_template_id

    @sms_template_id.setter
    def sms_template_id(self, sms_template_id):
        """Sets the sms_template_id of this XiqDeliverySettings.

        The SMS Template ID   # noqa: E501

        :param sms_template_id: The sms_template_id of this XiqDeliverySettings.  # noqa: E501
        :type: int
        """

        self._sms_template_id = sms_template_id

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
        if not isinstance(other, XiqDeliverySettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeliverySettings):
            return True

        return self.to_dict() != other.to_dict()
