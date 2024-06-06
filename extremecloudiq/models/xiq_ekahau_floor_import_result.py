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


class XiqEkahauFloorImportResult(object):
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
        'name': 'str',
        'status': 'XiqEkahauFloorImportStatus',
        'issues': 'XiqEkahauImportIssues'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'issues': 'issues'
    }

    def __init__(self, name=None, status=None, issues=None, local_vars_configuration=None):  # noqa: E501
        """XiqEkahauFloorImportResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._status = None
        self._issues = None
        self.discriminator = None

        self.name = name
        self.status = status
        self.issues = issues

    @property
    def name(self):
        """Gets the name of this XiqEkahauFloorImportResult.  # noqa: E501

        Name of the imported floor  # noqa: E501

        :return: The name of this XiqEkahauFloorImportResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqEkahauFloorImportResult.

        Name of the imported floor  # noqa: E501

        :param name: The name of this XiqEkahauFloorImportResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this XiqEkahauFloorImportResult.  # noqa: E501


        :return: The status of this XiqEkahauFloorImportResult.  # noqa: E501
        :rtype: XiqEkahauFloorImportStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqEkahauFloorImportResult.


        :param status: The status of this XiqEkahauFloorImportResult.  # noqa: E501
        :type: XiqEkahauFloorImportStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def issues(self):
        """Gets the issues of this XiqEkahauFloorImportResult.  # noqa: E501


        :return: The issues of this XiqEkahauFloorImportResult.  # noqa: E501
        :rtype: XiqEkahauImportIssues
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this XiqEkahauFloorImportResult.


        :param issues: The issues of this XiqEkahauFloorImportResult.  # noqa: E501
        :type: XiqEkahauImportIssues
        """
        if self.local_vars_configuration.client_side_validation and issues is None:  # noqa: E501
            raise ValueError("Invalid value for `issues`, must not be `None`")  # noqa: E501

        self._issues = issues

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
        if not isinstance(other, XiqEkahauFloorImportResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqEkahauFloorImportResult):
            return True

        return self.to_dict() != other.to_dict()
