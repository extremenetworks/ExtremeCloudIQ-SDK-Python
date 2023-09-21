# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateActionAnomalyDetails(object):
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
        'building_id': 'int',
        'location_id': 'int',
        'anomaly_id': 'str',
        'anomaly_type': 'XiqAnomalyType'
    }

    attribute_map = {
        'building_id': 'buildingId',
        'location_id': 'locationId',
        'anomaly_id': 'anomalyId',
        'anomaly_type': 'anomalyType'
    }

    def __init__(self, building_id=None, location_id=None, anomaly_id=None, anomaly_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateActionAnomalyDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._building_id = None
        self._location_id = None
        self._anomaly_id = None
        self._anomaly_type = None
        self.discriminator = None

        self.building_id = building_id
        self.location_id = location_id
        self.anomaly_id = anomaly_id
        self.anomaly_type = anomaly_type

    @property
    def building_id(self):
        """Gets the building_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501

        The building ID  # noqa: E501

        :return: The building_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this XiqUpdateActionAnomalyDetails.

        The building ID  # noqa: E501

        :param building_id: The building_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and building_id is None:  # noqa: E501
            raise ValueError("Invalid value for `building_id`, must not be `None`")  # noqa: E501

        self._building_id = building_id

    @property
    def location_id(self):
        """Gets the location_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501

        The location ID  # noqa: E501

        :return: The location_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqUpdateActionAnomalyDetails.

        The location ID  # noqa: E501

        :param location_id: The location_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and location_id is None:  # noqa: E501
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def anomaly_id(self):
        """Gets the anomaly_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501

        The anomaly ID  # noqa: E501

        :return: The anomaly_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_id

    @anomaly_id.setter
    def anomaly_id(self, anomaly_id):
        """Sets the anomaly_id of this XiqUpdateActionAnomalyDetails.

        The anomaly ID  # noqa: E501

        :param anomaly_id: The anomaly_id of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and anomaly_id is None:  # noqa: E501
            raise ValueError("Invalid value for `anomaly_id`, must not be `None`")  # noqa: E501

        self._anomaly_id = anomaly_id

    @property
    def anomaly_type(self):
        """Gets the anomaly_type of this XiqUpdateActionAnomalyDetails.  # noqa: E501


        :return: The anomaly_type of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :rtype: XiqAnomalyType
        """
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, anomaly_type):
        """Sets the anomaly_type of this XiqUpdateActionAnomalyDetails.


        :param anomaly_type: The anomaly_type of this XiqUpdateActionAnomalyDetails.  # noqa: E501
        :type: XiqAnomalyType
        """
        if self.local_vars_configuration.client_side_validation and anomaly_type is None:  # noqa: E501
            raise ValueError("Invalid value for `anomaly_type`, must not be `None`")  # noqa: E501

        self._anomaly_type = anomaly_type

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
        if not isinstance(other, XiqUpdateActionAnomalyDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateActionAnomalyDetails):
            return True

        return self.to_dict() != other.to_dict()
