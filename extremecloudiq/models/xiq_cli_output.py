# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqCliOutput(object):
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
        'cli': 'str',
        'response_code': 'XiqCliResponseCode',
        'output': 'str'
    }

    attribute_map = {
        'cli': 'cli',
        'response_code': 'response_code',
        'output': 'output'
    }

    def __init__(self, cli=None, response_code=None, output=None, local_vars_configuration=None):  # noqa: E501
        """XiqCliOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cli = None
        self._response_code = None
        self._output = None
        self.discriminator = None

        self.cli = cli
        self.response_code = response_code
        if output is not None:
            self.output = output

    @property
    def cli(self):
        """Gets the cli of this XiqCliOutput.  # noqa: E501

        The CLI sent to the device  # noqa: E501

        :return: The cli of this XiqCliOutput.  # noqa: E501
        :rtype: str
        """
        return self._cli

    @cli.setter
    def cli(self, cli):
        """Sets the cli of this XiqCliOutput.

        The CLI sent to the device  # noqa: E501

        :param cli: The cli of this XiqCliOutput.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cli is None:  # noqa: E501
            raise ValueError("Invalid value for `cli`, must not be `None`")  # noqa: E501

        self._cli = cli

    @property
    def response_code(self):
        """Gets the response_code of this XiqCliOutput.  # noqa: E501


        :return: The response_code of this XiqCliOutput.  # noqa: E501
        :rtype: XiqCliResponseCode
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        """Sets the response_code of this XiqCliOutput.


        :param response_code: The response_code of this XiqCliOutput.  # noqa: E501
        :type: XiqCliResponseCode
        """
        if self.local_vars_configuration.client_side_validation and response_code is None:  # noqa: E501
            raise ValueError("Invalid value for `response_code`, must not be `None`")  # noqa: E501

        self._response_code = response_code

    @property
    def output(self):
        """Gets the output of this XiqCliOutput.  # noqa: E501

        The CLI output  # noqa: E501

        :return: The output of this XiqCliOutput.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this XiqCliOutput.

        The CLI output  # noqa: E501

        :param output: The output of this XiqCliOutput.  # noqa: E501
        :type: str
        """

        self._output = output

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
        if not isinstance(other, XiqCliOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCliOutput):
            return True

        return self.to_dict() != other.to_dict()
