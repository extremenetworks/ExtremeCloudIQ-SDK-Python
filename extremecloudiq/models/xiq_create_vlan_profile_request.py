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


class XiqCreateVlanProfileRequest(object):
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
        'default_vlan_id': 'int',
        'enable_classification': 'bool',
        'classified_entries': 'list[XiqCreateVlanObjectClassifiedEntryRequest]'
    }

    attribute_map = {
        'name': 'name',
        'default_vlan_id': 'default_vlan_id',
        'enable_classification': 'enable_classification',
        'classified_entries': 'classified_entries'
    }

    def __init__(self, name=None, default_vlan_id=None, enable_classification=None, classified_entries=None, local_vars_configuration=None):  # noqa: E501
        """XiqCreateVlanProfileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._default_vlan_id = None
        self._enable_classification = None
        self._classified_entries = None
        self.discriminator = None

        self.name = name
        self.default_vlan_id = default_vlan_id
        self.enable_classification = enable_classification
        if classified_entries is not None:
            self.classified_entries = classified_entries

    @property
    def name(self):
        """Gets the name of this XiqCreateVlanProfileRequest.  # noqa: E501

        The VLAN profile name  # noqa: E501

        :return: The name of this XiqCreateVlanProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqCreateVlanProfileRequest.

        The VLAN profile name  # noqa: E501

        :param name: The name of this XiqCreateVlanProfileRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def default_vlan_id(self):
        """Gets the default_vlan_id of this XiqCreateVlanProfileRequest.  # noqa: E501

        The default VLAN ID  # noqa: E501

        :return: The default_vlan_id of this XiqCreateVlanProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._default_vlan_id

    @default_vlan_id.setter
    def default_vlan_id(self, default_vlan_id):
        """Sets the default_vlan_id of this XiqCreateVlanProfileRequest.

        The default VLAN ID  # noqa: E501

        :param default_vlan_id: The default_vlan_id of this XiqCreateVlanProfileRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and default_vlan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `default_vlan_id`, must not be `None`")  # noqa: E501

        self._default_vlan_id = default_vlan_id

    @property
    def enable_classification(self):
        """Gets the enable_classification of this XiqCreateVlanProfileRequest.  # noqa: E501

        If apply VLANs to devices using classification  # noqa: E501

        :return: The enable_classification of this XiqCreateVlanProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_classification

    @enable_classification.setter
    def enable_classification(self, enable_classification):
        """Sets the enable_classification of this XiqCreateVlanProfileRequest.

        If apply VLANs to devices using classification  # noqa: E501

        :param enable_classification: The enable_classification of this XiqCreateVlanProfileRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enable_classification is None:  # noqa: E501
            raise ValueError("Invalid value for `enable_classification`, must not be `None`")  # noqa: E501

        self._enable_classification = enable_classification

    @property
    def classified_entries(self):
        """Gets the classified_entries of this XiqCreateVlanProfileRequest.  # noqa: E501

        The VLAN object classified entries  # noqa: E501

        :return: The classified_entries of this XiqCreateVlanProfileRequest.  # noqa: E501
        :rtype: list[XiqCreateVlanObjectClassifiedEntryRequest]
        """
        return self._classified_entries

    @classified_entries.setter
    def classified_entries(self, classified_entries):
        """Sets the classified_entries of this XiqCreateVlanProfileRequest.

        The VLAN object classified entries  # noqa: E501

        :param classified_entries: The classified_entries of this XiqCreateVlanProfileRequest.  # noqa: E501
        :type: list[XiqCreateVlanObjectClassifiedEntryRequest]
        """

        self._classified_entries = classified_entries

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
        if not isinstance(other, XiqCreateVlanProfileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCreateVlanProfileRequest):
            return True

        return self.to_dict() != other.to_dict()
