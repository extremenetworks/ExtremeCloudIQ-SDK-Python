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


class XiqGetDeviceInfoByNos(object):
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
        'status_code': 'int',
        'status_message': 'str',
        'body': 'str'
    }

    attribute_map = {
        'status_code': 'status_code',
        'status_message': 'status_message',
        'body': 'body'
    }

    def __init__(self, status_code=None, status_message=None, body=None, local_vars_configuration=None):  # noqa: E501
        """XiqGetDeviceInfoByNos - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status_code = None
        self._status_message = None
        self._body = None
        self.discriminator = None

        self.status_code = status_code
        self.status_message = status_message
        if body is not None:
            self.body = body

    @property
    def status_code(self):
        """Gets the status_code of this XiqGetDeviceInfoByNos.  # noqa: E501

        The url name  # noqa: E501

        :return: The status_code of this XiqGetDeviceInfoByNos.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this XiqGetDeviceInfoByNos.

        The url name  # noqa: E501

        :param status_code: The status_code of this XiqGetDeviceInfoByNos.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and status_code is None:  # noqa: E501
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501

        self._status_code = status_code

    @property
    def status_message(self):
        """Gets the status_message of this XiqGetDeviceInfoByNos.  # noqa: E501

        The http method sent  # noqa: E501

        :return: The status_message of this XiqGetDeviceInfoByNos.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this XiqGetDeviceInfoByNos.

        The http method sent  # noqa: E501

        :param status_message: The status_message of this XiqGetDeviceInfoByNos.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status_message is None:  # noqa: E501
            raise ValueError("Invalid value for `status_message`, must not be `None`")  # noqa: E501

        self._status_message = status_message

    @property
    def body(self):
        """Gets the body of this XiqGetDeviceInfoByNos.  # noqa: E501

        body for POST request  # noqa: E501

        :return: The body of this XiqGetDeviceInfoByNos.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this XiqGetDeviceInfoByNos.

        body for POST request  # noqa: E501

        :param body: The body of this XiqGetDeviceInfoByNos.  # noqa: E501
        :type: str
        """

        self._body = body

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
        if not isinstance(other, XiqGetDeviceInfoByNos):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqGetDeviceInfoByNos):
            return True

        return self.to_dict() != other.to_dict()
