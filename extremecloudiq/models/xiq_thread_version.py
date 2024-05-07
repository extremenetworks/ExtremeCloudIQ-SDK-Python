# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqThreadVersion(object):
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
        'thread_version': 'str',
        'build_version': 'str',
        'api_version': 'str',
        'rcp_version': 'str'
    }

    attribute_map = {
        'thread_version': 'thread_version',
        'build_version': 'build_version',
        'api_version': 'api_version',
        'rcp_version': 'rcp_version'
    }

    def __init__(self, thread_version=None, build_version=None, api_version=None, rcp_version=None, local_vars_configuration=None):  # noqa: E501
        """XiqThreadVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._thread_version = None
        self._build_version = None
        self._api_version = None
        self._rcp_version = None
        self.discriminator = None

        if thread_version is not None:
            self.thread_version = thread_version
        if build_version is not None:
            self.build_version = build_version
        if api_version is not None:
            self.api_version = api_version
        if rcp_version is not None:
            self.rcp_version = rcp_version

    @property
    def thread_version(self):
        """Gets the thread_version of this XiqThreadVersion.  # noqa: E501


        :return: The thread_version of this XiqThreadVersion.  # noqa: E501
        :rtype: str
        """
        return self._thread_version

    @thread_version.setter
    def thread_version(self, thread_version):
        """Sets the thread_version of this XiqThreadVersion.


        :param thread_version: The thread_version of this XiqThreadVersion.  # noqa: E501
        :type: str
        """

        self._thread_version = thread_version

    @property
    def build_version(self):
        """Gets the build_version of this XiqThreadVersion.  # noqa: E501


        :return: The build_version of this XiqThreadVersion.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this XiqThreadVersion.


        :param build_version: The build_version of this XiqThreadVersion.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

    @property
    def api_version(self):
        """Gets the api_version of this XiqThreadVersion.  # noqa: E501


        :return: The api_version of this XiqThreadVersion.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this XiqThreadVersion.


        :param api_version: The api_version of this XiqThreadVersion.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def rcp_version(self):
        """Gets the rcp_version of this XiqThreadVersion.  # noqa: E501


        :return: The rcp_version of this XiqThreadVersion.  # noqa: E501
        :rtype: str
        """
        return self._rcp_version

    @rcp_version.setter
    def rcp_version(self, rcp_version):
        """Sets the rcp_version of this XiqThreadVersion.


        :param rcp_version: The rcp_version of this XiqThreadVersion.  # noqa: E501
        :type: str
        """

        self._rcp_version = rcp_version

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
        if not isinstance(other, XiqThreadVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqThreadVersion):
            return True

        return self.to_dict() != other.to_dict()
