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


class XiqApplicationDetectionRule(object):
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
        'value': 'str',
        'protocol': 'XiqApplicationDetectionProtocol',
        'type': 'XiqApplicationDetectionType'
    }

    attribute_map = {
        'value': 'value',
        'protocol': 'protocol',
        'type': 'type'
    }

    def __init__(self, value=None, protocol=None, type=None, local_vars_configuration=None):  # noqa: E501
        """XiqApplicationDetectionRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._protocol = None
        self._type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if protocol is not None:
            self.protocol = protocol
        if type is not None:
            self.type = type

    @property
    def value(self):
        """Gets the value of this XiqApplicationDetectionRule.  # noqa: E501

        The value of detection rule type  # noqa: E501

        :return: The value of this XiqApplicationDetectionRule.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this XiqApplicationDetectionRule.

        The value of detection rule type  # noqa: E501

        :param value: The value of this XiqApplicationDetectionRule.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def protocol(self):
        """Gets the protocol of this XiqApplicationDetectionRule.  # noqa: E501


        :return: The protocol of this XiqApplicationDetectionRule.  # noqa: E501
        :rtype: XiqApplicationDetectionProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this XiqApplicationDetectionRule.


        :param protocol: The protocol of this XiqApplicationDetectionRule.  # noqa: E501
        :type: XiqApplicationDetectionProtocol
        """

        self._protocol = protocol

    @property
    def type(self):
        """Gets the type of this XiqApplicationDetectionRule.  # noqa: E501


        :return: The type of this XiqApplicationDetectionRule.  # noqa: E501
        :rtype: XiqApplicationDetectionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this XiqApplicationDetectionRule.


        :param type: The type of this XiqApplicationDetectionRule.  # noqa: E501
        :type: XiqApplicationDetectionType
        """

        self._type = type

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
        if not isinstance(other, XiqApplicationDetectionRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqApplicationDetectionRule):
            return True

        return self.to_dict() != other.to_dict()
