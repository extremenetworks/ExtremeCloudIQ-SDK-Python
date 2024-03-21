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


class XiqZsubelementAboveFloor(object):
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
        'height': 'float',
        'height_uncertainty': 'float'
    }

    attribute_map = {
        'height': 'height',
        'height_uncertainty': 'height_uncertainty'
    }

    def __init__(self, height=None, height_uncertainty=None, local_vars_configuration=None):  # noqa: E501
        """XiqZsubelementAboveFloor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._height = None
        self._height_uncertainty = None
        self.discriminator = None

        self.height = height
        self.height_uncertainty = height_uncertainty

    @property
    def height(self):
        """Gets the height of this XiqZsubelementAboveFloor.  # noqa: E501

        Height above floor in meters  # noqa: E501

        :return: The height of this XiqZsubelementAboveFloor.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this XiqZsubelementAboveFloor.

        Height above floor in meters  # noqa: E501

        :param height: The height of this XiqZsubelementAboveFloor.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def height_uncertainty(self):
        """Gets the height_uncertainty of this XiqZsubelementAboveFloor.  # noqa: E501

        Height uncertainty in meters  # noqa: E501

        :return: The height_uncertainty of this XiqZsubelementAboveFloor.  # noqa: E501
        :rtype: float
        """
        return self._height_uncertainty

    @height_uncertainty.setter
    def height_uncertainty(self, height_uncertainty):
        """Sets the height_uncertainty of this XiqZsubelementAboveFloor.

        Height uncertainty in meters  # noqa: E501

        :param height_uncertainty: The height_uncertainty of this XiqZsubelementAboveFloor.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and height_uncertainty is None:  # noqa: E501
            raise ValueError("Invalid value for `height_uncertainty`, must not be `None`")  # noqa: E501

        self._height_uncertainty = height_uncertainty

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
        if not isinstance(other, XiqZsubelementAboveFloor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqZsubelementAboveFloor):
            return True

        return self.to_dict() != other.to_dict()
