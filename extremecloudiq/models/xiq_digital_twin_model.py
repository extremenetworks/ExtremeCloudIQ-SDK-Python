# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.0.35
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDigitalTwinModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _5320_16P_4XE = "DT_5320_16P_4XE"
    _5320_16P_4XE_DC = "DT_5320_16P_4XE_DC"
    _5320_24P_8XE = "DT_5320_24P_8XE"
    _5320_24T_8XE = "DT_5320_24T_8XE"
    _5320_48P_8XE = "DT_5320_48P_8XE"
    _5320_48T_8XE = "DT_5320_48T_8XE"
    _5420F_16MW_32P_4XE = "DT_5420F_16MW_32P_4XE"
    _5420F_16W_32P_4XE = "DT_5420F_16W_32P_4XE"
    _5420F_24P_4XE = "DT_5420F_24P_4XE"
    _5420F_24S_4XE = "DT_5420F_24S_4XE"
    _5420F_24T_4XE = "DT_5420F_24T_4XE"
    _5420F_48P_4XE = "DT_5420F_48P_4XE"
    _5420F_48P_4XL = "DT_5420F_48P_4XL"
    _5420F_48T_4XE = "DT_5420F_48T_4XE"
    _5420F_8W_16P_4XE = "DT_5420F_8W_16P_4XE"
    _5420M_16MW_32P_4YE = "DT_5420M_16MW_32P_4YE"
    _5420M_24T_4YE = "DT_5420M_24T_4YE"
    _5420M_24W_4YE = "DT_5420M_24W_4YE"
    _5420M_48T_4YE = "DT_5420M_48T_4YE"
    _5420M_48W_4YE = "DT_5420M_48W_4YE"
    _5520_12MW_36W = "DT_5520_12MW_36W"
    _5520_24T = "DT_5520_24T"
    _5520_24W = "DT_5520_24W"
    _5520_24X = "DT_5520_24X"
    _5520_48SE = "DT_5520_48SE"
    _5520_48T = "DT_5520_48T"
    _5520_48W = "DT_5520_48W"
    _5720_24MW = "DT_5720_24MW"
    _5720_24MXW = "DT_5720_24MXW"
    _5720_48MW = "DT_5720_48MW"
    _5720_48MXW = "DT_5720_48MXW"

    allowable_values = [_5320_16P_4XE, _5320_16P_4XE_DC, _5320_24P_8XE, _5320_24T_8XE, _5320_48P_8XE, _5320_48T_8XE, _5420F_16MW_32P_4XE, _5420F_16W_32P_4XE, _5420F_24P_4XE, _5420F_24S_4XE, _5420F_24T_4XE, _5420F_48P_4XE, _5420F_48P_4XL, _5420F_48T_4XE, _5420F_8W_16P_4XE, _5420M_16MW_32P_4YE, _5420M_24T_4YE, _5420M_24W_4YE, _5420M_48T_4YE, _5420M_48W_4YE, _5520_12MW_36W, _5520_24T, _5520_24W, _5520_24X, _5520_48SE, _5520_48T, _5520_48W, _5720_24MW, _5720_24MXW, _5720_48MW, _5720_48MXW]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """XiqDigitalTwinModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

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
        if not isinstance(other, XiqDigitalTwinModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDigitalTwinModel):
            return True

        return self.to_dict() != other.to_dict()