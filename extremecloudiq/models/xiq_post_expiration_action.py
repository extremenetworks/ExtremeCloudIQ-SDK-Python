# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqPostExpirationAction(object):
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
        'enable_credentials_renewal': 'bool',
        'enable_delete_immediately': 'bool',
        'delete_after_value': 'int',
        'delete_after_unit': 'XiqDateTimeUnitType'
    }

    attribute_map = {
        'enable_credentials_renewal': 'enable_credentials_renewal',
        'enable_delete_immediately': 'enable_delete_immediately',
        'delete_after_value': 'delete_after_value',
        'delete_after_unit': 'delete_after_unit'
    }

    def __init__(self, enable_credentials_renewal=None, enable_delete_immediately=None, delete_after_value=None, delete_after_unit=None, local_vars_configuration=None):  # noqa: E501
        """XiqPostExpirationAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_credentials_renewal = None
        self._enable_delete_immediately = None
        self._delete_after_value = None
        self._delete_after_unit = None
        self.discriminator = None

        if enable_credentials_renewal is not None:
            self.enable_credentials_renewal = enable_credentials_renewal
        if enable_delete_immediately is not None:
            self.enable_delete_immediately = enable_delete_immediately
        if delete_after_value is not None:
            self.delete_after_value = delete_after_value
        if delete_after_unit is not None:
            self.delete_after_unit = delete_after_unit

    @property
    def enable_credentials_renewal(self):
        """Gets the enable_credentials_renewal of this XiqPostExpirationAction.  # noqa: E501

        The renew user credentials option or null for other option.  # noqa: E501

        :return: The enable_credentials_renewal of this XiqPostExpirationAction.  # noqa: E501
        :rtype: bool
        """
        return self._enable_credentials_renewal

    @enable_credentials_renewal.setter
    def enable_credentials_renewal(self, enable_credentials_renewal):
        """Sets the enable_credentials_renewal of this XiqPostExpirationAction.

        The renew user credentials option or null for other option.  # noqa: E501

        :param enable_credentials_renewal: The enable_credentials_renewal of this XiqPostExpirationAction.  # noqa: E501
        :type: bool
        """

        self._enable_credentials_renewal = enable_credentials_renewal

    @property
    def enable_delete_immediately(self):
        """Gets the enable_delete_immediately of this XiqPostExpirationAction.  # noqa: E501

        The immediate delete option or null to schedule the delete.  # noqa: E501

        :return: The enable_delete_immediately of this XiqPostExpirationAction.  # noqa: E501
        :rtype: bool
        """
        return self._enable_delete_immediately

    @enable_delete_immediately.setter
    def enable_delete_immediately(self, enable_delete_immediately):
        """Sets the enable_delete_immediately of this XiqPostExpirationAction.

        The immediate delete option or null to schedule the delete.  # noqa: E501

        :param enable_delete_immediately: The enable_delete_immediately of this XiqPostExpirationAction.  # noqa: E501
        :type: bool
        """

        self._enable_delete_immediately = enable_delete_immediately

    @property
    def delete_after_value(self):
        """Gets the delete_after_value of this XiqPostExpirationAction.  # noqa: E501

        The after expiration scheduled time to delete or null to not delete..  # noqa: E501

        :return: The delete_after_value of this XiqPostExpirationAction.  # noqa: E501
        :rtype: int
        """
        return self._delete_after_value

    @delete_after_value.setter
    def delete_after_value(self, delete_after_value):
        """Sets the delete_after_value of this XiqPostExpirationAction.

        The after expiration scheduled time to delete or null to not delete..  # noqa: E501

        :param delete_after_value: The delete_after_value of this XiqPostExpirationAction.  # noqa: E501
        :type: int
        """

        self._delete_after_value = delete_after_value

    @property
    def delete_after_unit(self):
        """Gets the delete_after_unit of this XiqPostExpirationAction.  # noqa: E501


        :return: The delete_after_unit of this XiqPostExpirationAction.  # noqa: E501
        :rtype: XiqDateTimeUnitType
        """
        return self._delete_after_unit

    @delete_after_unit.setter
    def delete_after_unit(self, delete_after_unit):
        """Sets the delete_after_unit of this XiqPostExpirationAction.


        :param delete_after_unit: The delete_after_unit of this XiqPostExpirationAction.  # noqa: E501
        :type: XiqDateTimeUnitType
        """

        self._delete_after_unit = delete_after_unit

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
        if not isinstance(other, XiqPostExpirationAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPostExpirationAction):
            return True

        return self.to_dict() != other.to_dict()
