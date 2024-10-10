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


class XiqEkahauFloorToFloorAssociation(object):
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
        'floor_name': 'str',
        'parent_building_id': 'int'
    }

    attribute_map = {
        'floor_name': 'floorName',
        'parent_building_id': 'parentBuildingId'
    }

    def __init__(self, floor_name=None, parent_building_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqEkahauFloorToFloorAssociation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._floor_name = None
        self._parent_building_id = None
        self.discriminator = None

        self.floor_name = floor_name
        self.parent_building_id = parent_building_id

    @property
    def floor_name(self):
        """Gets the floor_name of this XiqEkahauFloorToFloorAssociation.  # noqa: E501

        The name of the Ekahau floor to import into the parent building  # noqa: E501

        :return: The floor_name of this XiqEkahauFloorToFloorAssociation.  # noqa: E501
        :rtype: str
        """
        return self._floor_name

    @floor_name.setter
    def floor_name(self, floor_name):
        """Sets the floor_name of this XiqEkahauFloorToFloorAssociation.

        The name of the Ekahau floor to import into the parent building  # noqa: E501

        :param floor_name: The floor_name of this XiqEkahauFloorToFloorAssociation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and floor_name is None:  # noqa: E501
            raise ValueError("Invalid value for `floor_name`, must not be `None`")  # noqa: E501

        self._floor_name = floor_name

    @property
    def parent_building_id(self):
        """Gets the parent_building_id of this XiqEkahauFloorToFloorAssociation.  # noqa: E501

        The parent building ID  # noqa: E501

        :return: The parent_building_id of this XiqEkahauFloorToFloorAssociation.  # noqa: E501
        :rtype: int
        """
        return self._parent_building_id

    @parent_building_id.setter
    def parent_building_id(self, parent_building_id):
        """Sets the parent_building_id of this XiqEkahauFloorToFloorAssociation.

        The parent building ID  # noqa: E501

        :param parent_building_id: The parent_building_id of this XiqEkahauFloorToFloorAssociation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and parent_building_id is None:  # noqa: E501
            raise ValueError("Invalid value for `parent_building_id`, must not be `None`")  # noqa: E501

        self._parent_building_id = parent_building_id

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
        if not isinstance(other, XiqEkahauFloorToFloorAssociation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqEkahauFloorToFloorAssociation):
            return True

        return self.to_dict() != other.to_dict()