# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqListLicensesResponse(object):
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
        'group_by_application': 'bool',
        'application_id': 'str',
        'application_name': 'str',
        'license_type_count': 'int',
        'license_entitlement_count': 'int',
        'license_types': 'list[XiqLicenseType]'
    }

    attribute_map = {
        'group_by_application': 'group_by_application',
        'application_id': 'application_id',
        'application_name': 'application_name',
        'license_type_count': 'license_type_count',
        'license_entitlement_count': 'license_entitlement_count',
        'license_types': 'license_types'
    }

    def __init__(self, group_by_application=None, application_id=None, application_name=None, license_type_count=None, license_entitlement_count=None, license_types=None, local_vars_configuration=None):  # noqa: E501
        """XiqListLicensesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group_by_application = None
        self._application_id = None
        self._application_name = None
        self._license_type_count = None
        self._license_entitlement_count = None
        self._license_types = None
        self.discriminator = None

        if group_by_application is not None:
            self.group_by_application = group_by_application
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if license_type_count is not None:
            self.license_type_count = license_type_count
        if license_entitlement_count is not None:
            self.license_entitlement_count = license_entitlement_count
        if license_types is not None:
            self.license_types = license_types

    @property
    def group_by_application(self):
        """Gets the group_by_application of this XiqListLicensesResponse.  # noqa: E501

        Whether group by application  # noqa: E501

        :return: The group_by_application of this XiqListLicensesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._group_by_application

    @group_by_application.setter
    def group_by_application(self, group_by_application):
        """Sets the group_by_application of this XiqListLicensesResponse.

        Whether group by application  # noqa: E501

        :param group_by_application: The group_by_application of this XiqListLicensesResponse.  # noqa: E501
        :type: bool
        """

        self._group_by_application = group_by_application

    @property
    def application_id(self):
        """Gets the application_id of this XiqListLicensesResponse.  # noqa: E501

        Application Id of current group, valid when groupByApplication is true  # noqa: E501

        :return: The application_id of this XiqListLicensesResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this XiqListLicensesResponse.

        Application Id of current group, valid when groupByApplication is true  # noqa: E501

        :param application_id: The application_id of this XiqListLicensesResponse.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this XiqListLicensesResponse.  # noqa: E501

        Application name of current group, valid when groupByApplication is true  # noqa: E501

        :return: The application_name of this XiqListLicensesResponse.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this XiqListLicensesResponse.

        Application name of current group, valid when groupByApplication is true  # noqa: E501

        :param application_name: The application_name of this XiqListLicensesResponse.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def license_type_count(self):
        """Gets the license_type_count of this XiqListLicensesResponse.  # noqa: E501

        License type count of current group, valid when groupByApplication is true  # noqa: E501

        :return: The license_type_count of this XiqListLicensesResponse.  # noqa: E501
        :rtype: int
        """
        return self._license_type_count

    @license_type_count.setter
    def license_type_count(self, license_type_count):
        """Sets the license_type_count of this XiqListLicensesResponse.

        License type count of current group, valid when groupByApplication is true  # noqa: E501

        :param license_type_count: The license_type_count of this XiqListLicensesResponse.  # noqa: E501
        :type: int
        """

        self._license_type_count = license_type_count

    @property
    def license_entitlement_count(self):
        """Gets the license_entitlement_count of this XiqListLicensesResponse.  # noqa: E501

        License entitlement count of current group, valid when groupByApplication is true  # noqa: E501

        :return: The license_entitlement_count of this XiqListLicensesResponse.  # noqa: E501
        :rtype: int
        """
        return self._license_entitlement_count

    @license_entitlement_count.setter
    def license_entitlement_count(self, license_entitlement_count):
        """Sets the license_entitlement_count of this XiqListLicensesResponse.

        License entitlement count of current group, valid when groupByApplication is true  # noqa: E501

        :param license_entitlement_count: The license_entitlement_count of this XiqListLicensesResponse.  # noqa: E501
        :type: int
        """

        self._license_entitlement_count = license_entitlement_count

    @property
    def license_types(self):
        """Gets the license_types of this XiqListLicensesResponse.  # noqa: E501

        License type list  # noqa: E501

        :return: The license_types of this XiqListLicensesResponse.  # noqa: E501
        :rtype: list[XiqLicenseType]
        """
        return self._license_types

    @license_types.setter
    def license_types(self, license_types):
        """Sets the license_types of this XiqListLicensesResponse.

        License type list  # noqa: E501

        :param license_types: The license_types of this XiqListLicensesResponse.  # noqa: E501
        :type: list[XiqLicenseType]
        """

        self._license_types = license_types

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
        if not isinstance(other, XiqListLicensesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqListLicensesResponse):
            return True

        return self.to_dict() != other.to_dict()
