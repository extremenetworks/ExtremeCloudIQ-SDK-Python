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


class XiqCreateVlanObjectClassifiedEntryRequest(object):
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
        'vlan_id': 'int',
        'classification_rule_id': 'int'
    }

    attribute_map = {
        'vlan_id': 'vlan_id',
        'classification_rule_id': 'classification_rule_id'
    }

    def __init__(self, vlan_id=None, classification_rule_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqCreateVlanObjectClassifiedEntryRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vlan_id = None
        self._classification_rule_id = None
        self.discriminator = None

        self.vlan_id = vlan_id
        self.classification_rule_id = classification_rule_id

    @property
    def vlan_id(self):
        """Gets the vlan_id of this XiqCreateVlanObjectClassifiedEntryRequest.  # noqa: E501

        The VLAN ID  # noqa: E501

        :return: The vlan_id of this XiqCreateVlanObjectClassifiedEntryRequest.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this XiqCreateVlanObjectClassifiedEntryRequest.

        The VLAN ID  # noqa: E501

        :param vlan_id: The vlan_id of this XiqCreateVlanObjectClassifiedEntryRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and vlan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def classification_rule_id(self):
        """Gets the classification_rule_id of this XiqCreateVlanObjectClassifiedEntryRequest.  # noqa: E501

        The classification rule ID  # noqa: E501

        :return: The classification_rule_id of this XiqCreateVlanObjectClassifiedEntryRequest.  # noqa: E501
        :rtype: int
        """
        return self._classification_rule_id

    @classification_rule_id.setter
    def classification_rule_id(self, classification_rule_id):
        """Sets the classification_rule_id of this XiqCreateVlanObjectClassifiedEntryRequest.

        The classification rule ID  # noqa: E501

        :param classification_rule_id: The classification_rule_id of this XiqCreateVlanObjectClassifiedEntryRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and classification_rule_id is None:  # noqa: E501
            raise ValueError("Invalid value for `classification_rule_id`, must not be `None`")  # noqa: E501

        self._classification_rule_id = classification_rule_id

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
        if not isinstance(other, XiqCreateVlanObjectClassifiedEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCreateVlanObjectClassifiedEntryRequest):
            return True

        return self.to_dict() != other.to_dict()
