# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCliResponseCode(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    UNSPECIFIED = "UNSPECIFIED"
    SUCCEED = "SUCCEED"
    ERR_DEVICE_NOT_EXIST = "ERR_DEVICE_NOT_EXIST"
    ERR_DEVICE_NOT_ACTIVE = "ERR_DEVICE_NOT_ACTIVE"
    ERR_SEND_MESSAGE = "ERR_SEND_MESSAGE"
    ERR_CLI_EXECUTED = "ERR_CLI_EXECUTED"
    ERR_DEVICE_NOT_SUPPORTED = "ERR_DEVICE_NOT_SUPPORTED"
    ERR_SIMULATE_NOT_SUPPORTED = "ERR_SIMULATE_NOT_SUPPORTED"
    ERR_VERSION_NOT_SUPPORTED = "ERR_VERSION_NOT_SUPPORTED"
    ERR_PARSE_FILE = "ERR_PARSE_FILE"
    ERR_UNMANAGED_DEVICE = "ERR_UNMANAGED_DEVICE"
    ERR_CLI_NOT_SENT = "ERR_CLI_NOT_SENT"
    ERR_TIMEOUT = "ERR_TIMEOUT"
    ERR_VPN_USING = "ERR_VPN_USING"
    CLI_SENT_SUCCEED = "CLI_SENT_SUCCEED"
    ERR_CLI_MAX_CLI_LIMIT_EXCEEDED = "ERR_CLI_MAX_CLI_LIMIT_EXCEEDED"

    allowable_values = [UNSPECIFIED, SUCCEED, ERR_DEVICE_NOT_EXIST, ERR_DEVICE_NOT_ACTIVE, ERR_SEND_MESSAGE, ERR_CLI_EXECUTED, ERR_DEVICE_NOT_SUPPORTED, ERR_SIMULATE_NOT_SUPPORTED, ERR_VERSION_NOT_SUPPORTED, ERR_PARSE_FILE, ERR_UNMANAGED_DEVICE, ERR_CLI_NOT_SENT, ERR_TIMEOUT, ERR_VPN_USING, CLI_SENT_SUCCEED, ERR_CLI_MAX_CLI_LIMIT_EXCEEDED]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """XiqCliResponseCode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, XiqCliResponseCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCliResponseCode):
            return True

        return self.to_dict() != other.to_dict()
