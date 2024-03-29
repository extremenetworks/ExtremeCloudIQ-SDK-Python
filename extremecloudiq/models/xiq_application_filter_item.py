# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.52
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqApplicationFilterItem(object):
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
        '_global': 'bool',
        'application_id': 'str',
        'application_name': 'str',
        'license_health_color': 'XiqLicenseHealthColor'
    }

    attribute_map = {
        '_global': 'global',
        'application_id': 'application_id',
        'application_name': 'application_name',
        'license_health_color': 'license_health_color'
    }

    def __init__(self, _global=None, application_id=None, application_name=None, license_health_color=None, local_vars_configuration=None):  # noqa: E501
        """XiqApplicationFilterItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__global = None
        self._application_id = None
        self._application_name = None
        self._license_health_color = None
        self.discriminator = None

        if _global is not None:
            self._global = _global
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if license_health_color is not None:
            self.license_health_color = license_health_color

    @property
    def _global(self):
        """Gets the _global of this XiqApplicationFilterItem.  # noqa: E501

        Whether it is an item for all applications  # noqa: E501

        :return: The _global of this XiqApplicationFilterItem.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this XiqApplicationFilterItem.

        Whether it is an item for all applications  # noqa: E501

        :param _global: The _global of this XiqApplicationFilterItem.  # noqa: E501
        :type: bool
        """

        self.__global = _global

    @property
    def application_id(self):
        """Gets the application_id of this XiqApplicationFilterItem.  # noqa: E501

        Application ID, valid when global is false  # noqa: E501

        :return: The application_id of this XiqApplicationFilterItem.  # noqa: E501
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this XiqApplicationFilterItem.

        Application ID, valid when global is false  # noqa: E501

        :param application_id: The application_id of this XiqApplicationFilterItem.  # noqa: E501
        :type: str
        """

        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this XiqApplicationFilterItem.  # noqa: E501

        Application Name, valid when global is false  # noqa: E501

        :return: The application_name of this XiqApplicationFilterItem.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this XiqApplicationFilterItem.

        Application Name, valid when global is false  # noqa: E501

        :param application_name: The application_name of this XiqApplicationFilterItem.  # noqa: E501
        :type: str
        """

        self._application_name = application_name

    @property
    def license_health_color(self):
        """Gets the license_health_color of this XiqApplicationFilterItem.  # noqa: E501


        :return: The license_health_color of this XiqApplicationFilterItem.  # noqa: E501
        :rtype: XiqLicenseHealthColor
        """
        return self._license_health_color

    @license_health_color.setter
    def license_health_color(self, license_health_color):
        """Sets the license_health_color of this XiqApplicationFilterItem.


        :param license_health_color: The license_health_color of this XiqApplicationFilterItem.  # noqa: E501
        :type: XiqLicenseHealthColor
        """

        self._license_health_color = license_health_color

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
        if not isinstance(other, XiqApplicationFilterItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqApplicationFilterItem):
            return True

        return self.to_dict() != other.to_dict()
