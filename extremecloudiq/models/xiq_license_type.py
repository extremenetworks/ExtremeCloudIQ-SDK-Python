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


class XiqLicenseType(object):
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
        'license_type': 'str',
        'license_type_display_name': 'str',
        'license_description': 'str',
        'license_entitlement_count': 'int',
        'application_id': 'str',
        'application_name': 'str',
        'status': 'XiqLicenseStatus',
        'total_licenses': 'int',
        'active_licenses': 'int',
        'available_licenses': 'int'
    }

    attribute_map = {
        'license_type': 'license_type',
        'license_type_display_name': 'license_type_display_name',
        'license_description': 'license_description',
        'license_entitlement_count': 'license_entitlement_count',
        'application_id': 'application_id',
        'application_name': 'application_name',
        'status': 'status',
        'total_licenses': 'total_licenses',
        'active_licenses': 'active_licenses',
        'available_licenses': 'available_licenses'
    }

    def __init__(self, license_type=None, license_type_display_name=None, license_description=None, license_entitlement_count=None, application_id=None, application_name=None, status=None, total_licenses=None, active_licenses=None, available_licenses=None, local_vars_configuration=None):  # noqa: E501
        """XiqLicenseType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._license_type = None
        self._license_type_display_name = None
        self._license_description = None
        self._license_entitlement_count = None
        self._application_id = None
        self._application_name = None
        self._status = None
        self._total_licenses = None
        self._active_licenses = None
        self._available_licenses = None
        self.discriminator = None

        if license_type is not None:
            self.license_type = license_type
        if license_type_display_name is not None:
            self.license_type_display_name = license_type_display_name
        if license_description is not None:
            self.license_description = license_description
        if license_entitlement_count is not None:
            self.license_entitlement_count = license_entitlement_count
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if status is not None:
            self.status = status
        if total_licenses is not None:
            self.total_licenses = total_licenses
        if active_licenses is not None:
            self.active_licenses = active_licenses
        if available_licenses is not None:
            self.available_licenses = available_licenses

    @property
    def license_type(self):
        """Gets the license_type of this XiqLicenseType.  # noqa: E501

        License type  # noqa: E501

        :return: The license_type of this XiqLicenseType.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this XiqLicenseType.

        License type  # noqa: E501

        :param license_type: The license_type of this XiqLicenseType.  # noqa: E501
        :type: str
        """

        self._license_type = license_type

    @property
    def license_type_display_name(self):
        """Gets the license_type_display_name of this XiqLicenseType.  # noqa: E501

        License type display name  # noqa: E501

        :return: The license_type_display_name of this XiqLicenseType.  # noqa: E501
        :rtype: str
        """
        return self._license_type_display_name

    @license_type_display_name.setter
    def license_type_display_name(self, license_type_display_name):
        """Sets the license_type_display_name of this XiqLicenseType.

        License type display name  # noqa: E501

        :param license_type_display_name: The license_type_display_name of this XiqLicenseType.  # noqa: E501
        :type: str
        """

        self._license_type_display_name = license_type_display_name

    @property
    def license_description(self):
        """Gets the license_description of this XiqLicenseType.  # noqa: E501

        License description  # noqa: E501

        :return: The license_description of this XiqLicenseType.  # noqa: E501
        :rtype: str
        """
        return self._license_description

    @license_description.setter
    def license_description(self, license_description):
        """Sets the license_description of this XiqLicenseType.

        License description  # noqa: E501

        :param license_description: The license_description of this XiqLicenseType.  # noqa: E501
        :type: str
        """

        self._license_description = license_description

    @property
    def license_entitlement_count(self):
        """Gets the license_entitlement_count of this XiqLicenseType.  # noqa: E501

        Entitlement count of this license type  # noqa: E501

        :return: The license_entitlement_count of this XiqLicenseType.  # noqa: E501
        :rtype: int
        """
        return self._license_entitlement_count

    @license_entitlement_count.setter
    def license_entitlement_count(self, license_entitlement_count):
        """Sets the license_entitlement_count of this XiqLicenseType.

        Entitlement count of this license type  # noqa: E501

        :param license_entitlement_count: The license_entitlement_count of this XiqLicenseType.  # noqa: E501
        :type: int
        """

        self._license_entitlement_count = license_entitlement_count

    @property
    def application_id(self):
        """Gets the application_id of this XiqLicenseType.  # noqa: E501

        Application Id  # noqa: E501

        :return: The application_id of this XiqLicenseType.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this XiqLicenseType.

        Application Id  # noqa: E501

        :param application_id: The application_id of this XiqLicenseType.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this XiqLicenseType.  # noqa: E501

        Application name  # noqa: E501

        :return: The application_name of this XiqLicenseType.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this XiqLicenseType.

        Application name  # noqa: E501

        :param application_name: The application_name of this XiqLicenseType.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def status(self):
        """Gets the status of this XiqLicenseType.  # noqa: E501


        :return: The status of this XiqLicenseType.  # noqa: E501
        :rtype: XiqLicenseStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqLicenseType.


        :param status: The status of this XiqLicenseType.  # noqa: E501
        :type: XiqLicenseStatus
        """

        self._status = status

    @property
    def total_licenses(self):
        """Gets the total_licenses of this XiqLicenseType.  # noqa: E501

        Total licenses  # noqa: E501

        :return: The total_licenses of this XiqLicenseType.  # noqa: E501
        :rtype: int
        """
        return self._total_licenses

    @total_licenses.setter
    def total_licenses(self, total_licenses):
        """Sets the total_licenses of this XiqLicenseType.

        Total licenses  # noqa: E501

        :param total_licenses: The total_licenses of this XiqLicenseType.  # noqa: E501
        :type: int
        """

        self._total_licenses = total_licenses

    @property
    def active_licenses(self):
        """Gets the active_licenses of this XiqLicenseType.  # noqa: E501

        Activated licenses  # noqa: E501

        :return: The active_licenses of this XiqLicenseType.  # noqa: E501
        :rtype: int
        """
        return self._active_licenses

    @active_licenses.setter
    def active_licenses(self, active_licenses):
        """Sets the active_licenses of this XiqLicenseType.

        Activated licenses  # noqa: E501

        :param active_licenses: The active_licenses of this XiqLicenseType.  # noqa: E501
        :type: int
        """

        self._active_licenses = active_licenses

    @property
    def available_licenses(self):
        """Gets the available_licenses of this XiqLicenseType.  # noqa: E501

        Available licenses  # noqa: E501

        :return: The available_licenses of this XiqLicenseType.  # noqa: E501
        :rtype: int
        """
        return self._available_licenses

    @available_licenses.setter
    def available_licenses(self, available_licenses):
        """Sets the available_licenses of this XiqLicenseType.

        Available licenses  # noqa: E501

        :param available_licenses: The available_licenses of this XiqLicenseType.  # noqa: E501
        :type: int
        """

        self._available_licenses = available_licenses

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
        if not isinstance(other, XiqLicenseType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqLicenseType):
            return True

        return self.to_dict() != other.to_dict()
