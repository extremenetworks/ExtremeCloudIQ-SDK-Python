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


class XiqHiqContext(object):
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
        'reading_org_ids': 'list[int]',
        'creating_org_id': 'int'
    }

    attribute_map = {
        'reading_org_ids': 'reading_org_ids',
        'creating_org_id': 'creating_org_id'
    }

    def __init__(self, reading_org_ids=None, creating_org_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqHiqContext - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reading_org_ids = None
        self._creating_org_id = None
        self.discriminator = None

        self.reading_org_ids = reading_org_ids
        self.creating_org_id = creating_org_id

    @property
    def reading_org_ids(self):
        """Gets the reading_org_ids of this XiqHiqContext.  # noqa: E501

        The organization ID list for reading data (Empty means read data from all organizations in the HIQ)  # noqa: E501

        :return: The reading_org_ids of this XiqHiqContext.  # noqa: E501
        :rtype: list[int]
        """
        return self._reading_org_ids

    @reading_org_ids.setter
    def reading_org_ids(self, reading_org_ids):
        """Sets the reading_org_ids of this XiqHiqContext.

        The organization ID list for reading data (Empty means read data from all organizations in the HIQ)  # noqa: E501

        :param reading_org_ids: The reading_org_ids of this XiqHiqContext.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and reading_org_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `reading_org_ids`, must not be `None`")  # noqa: E501

        self._reading_org_ids = reading_org_ids

    @property
    def creating_org_id(self):
        """Gets the creating_org_id of this XiqHiqContext.  # noqa: E501

        The organization ID for creating new data  # noqa: E501

        :return: The creating_org_id of this XiqHiqContext.  # noqa: E501
        :rtype: int
        """
        return self._creating_org_id

    @creating_org_id.setter
    def creating_org_id(self, creating_org_id):
        """Sets the creating_org_id of this XiqHiqContext.

        The organization ID for creating new data  # noqa: E501

        :param creating_org_id: The creating_org_id of this XiqHiqContext.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and creating_org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `creating_org_id`, must not be `None`")  # noqa: E501

        self._creating_org_id = creating_org_id

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
        if not isinstance(other, XiqHiqContext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqHiqContext):
            return True

        return self.to_dict() != other.to_dict()
