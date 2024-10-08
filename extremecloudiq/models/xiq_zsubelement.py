# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqZsubelement(object):
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
        'expected_to_move': 'bool',
        'floor_number': 'int',
        'above_floor': 'XiqZsubelementAboveFloor'
    }

    attribute_map = {
        'expected_to_move': 'expected_to_move',
        'floor_number': 'floor_number',
        'above_floor': 'above_floor'
    }

    def __init__(self, expected_to_move=None, floor_number=None, above_floor=None, local_vars_configuration=None):  # noqa: E501
        """XiqZsubelement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expected_to_move = None
        self._floor_number = None
        self._above_floor = None
        self.discriminator = None

        self.expected_to_move = expected_to_move
        self.floor_number = floor_number
        if above_floor is not None:
            self.above_floor = above_floor

    @property
    def expected_to_move(self):
        """Gets the expected_to_move of this XiqZsubelement.  # noqa: E501

        Is the device expected to move?  # noqa: E501

        :return: The expected_to_move of this XiqZsubelement.  # noqa: E501
        :rtype: bool
        """
        return self._expected_to_move

    @expected_to_move.setter
    def expected_to_move(self, expected_to_move):
        """Sets the expected_to_move of this XiqZsubelement.

        Is the device expected to move?  # noqa: E501

        :param expected_to_move: The expected_to_move of this XiqZsubelement.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and expected_to_move is None:  # noqa: E501
            raise ValueError("Invalid value for `expected_to_move`, must not be `None`")  # noqa: E501

        self._expected_to_move = expected_to_move

    @property
    def floor_number(self):
        """Gets the floor_number of this XiqZsubelement.  # noqa: E501

        Floor number where the device is installed.  # noqa: E501

        :return: The floor_number of this XiqZsubelement.  # noqa: E501
        :rtype: int
        """
        return self._floor_number

    @floor_number.setter
    def floor_number(self, floor_number):
        """Sets the floor_number of this XiqZsubelement.

        Floor number where the device is installed.  # noqa: E501

        :param floor_number: The floor_number of this XiqZsubelement.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and floor_number is None:  # noqa: E501
            raise ValueError("Invalid value for `floor_number`, must not be `None`")  # noqa: E501

        self._floor_number = floor_number

    @property
    def above_floor(self):
        """Gets the above_floor of this XiqZsubelement.  # noqa: E501


        :return: The above_floor of this XiqZsubelement.  # noqa: E501
        :rtype: XiqZsubelementAboveFloor
        """
        return self._above_floor

    @above_floor.setter
    def above_floor(self, above_floor):
        """Sets the above_floor of this XiqZsubelement.


        :param above_floor: The above_floor of this XiqZsubelement.  # noqa: E501
        :type: XiqZsubelementAboveFloor
        """

        self._above_floor = above_floor

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
        if not isinstance(other, XiqZsubelement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqZsubelement):
            return True

        return self.to_dict() != other.to_dict()
