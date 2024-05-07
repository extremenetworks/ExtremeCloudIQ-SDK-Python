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


class XiqAlertSource(object):
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
        'source_type_id': 'int',
        'source_name': 'str',
        'source_type_name': 'str',
        'source_id': 'str'
    }

    attribute_map = {
        'source_type_id': 'source_type_id',
        'source_name': 'source_name',
        'source_type_name': 'source_type_name',
        'source_id': 'source_id'
    }

    def __init__(self, source_type_id=None, source_name=None, source_type_name=None, source_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_type_id = None
        self._source_name = None
        self._source_type_name = None
        self._source_id = None
        self.discriminator = None

        if source_type_id is not None:
            self.source_type_id = source_type_id
        if source_name is not None:
            self.source_name = source_name
        if source_type_name is not None:
            self.source_type_name = source_type_name
        if source_id is not None:
            self.source_id = source_id

    @property
    def source_type_id(self):
        """Gets the source_type_id of this XiqAlertSource.  # noqa: E501

        The alert source type ID  # noqa: E501

        :return: The source_type_id of this XiqAlertSource.  # noqa: E501
        :rtype: int
        """
        return self._source_type_id

    @source_type_id.setter
    def source_type_id(self, source_type_id):
        """Sets the source_type_id of this XiqAlertSource.

        The alert source type ID  # noqa: E501

        :param source_type_id: The source_type_id of this XiqAlertSource.  # noqa: E501
        :type: int
        """

        self._source_type_id = source_type_id

    @property
    def source_name(self):
        """Gets the source_name of this XiqAlertSource.  # noqa: E501

        The alert source name  # noqa: E501

        :return: The source_name of this XiqAlertSource.  # noqa: E501
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """Sets the source_name of this XiqAlertSource.

        The alert source name  # noqa: E501

        :param source_name: The source_name of this XiqAlertSource.  # noqa: E501
        :type: str
        """

        self._source_name = source_name

    @property
    def source_type_name(self):
        """Gets the source_type_name of this XiqAlertSource.  # noqa: E501

        The alert source type name  # noqa: E501

        :return: The source_type_name of this XiqAlertSource.  # noqa: E501
        :rtype: str
        """
        return self._source_type_name

    @source_type_name.setter
    def source_type_name(self, source_type_name):
        """Sets the source_type_name of this XiqAlertSource.

        The alert source type name  # noqa: E501

        :param source_type_name: The source_type_name of this XiqAlertSource.  # noqa: E501
        :type: str
        """

        self._source_type_name = source_type_name

    @property
    def source_id(self):
        """Gets the source_id of this XiqAlertSource.  # noqa: E501

        The alert source ID  # noqa: E501

        :return: The source_id of this XiqAlertSource.  # noqa: E501
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this XiqAlertSource.

        The alert source ID  # noqa: E501

        :param source_id: The source_id of this XiqAlertSource.  # noqa: E501
        :type: str
        """

        self._source_id = source_id

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
        if not isinstance(other, XiqAlertSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertSource):
            return True

        return self.to_dict() != other.to_dict()
