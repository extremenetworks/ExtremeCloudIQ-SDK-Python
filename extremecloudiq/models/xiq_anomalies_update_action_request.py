# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAnomaliesUpdateActionRequest(object):
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
        'anomaly_type': 'XiqAnomalyType',
        'action_type': 'XiqActionType',
        'building_id': 'int'
    }

    attribute_map = {
        'anomaly_type': 'anomaly_type',
        'action_type': 'action_type',
        'building_id': 'building_id'
    }

    def __init__(self, anomaly_type=None, action_type=None, building_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomaliesUpdateActionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._anomaly_type = None
        self._action_type = None
        self._building_id = None
        self.discriminator = None

        if anomaly_type is not None:
            self.anomaly_type = anomaly_type
        if action_type is not None:
            self.action_type = action_type
        if building_id is not None:
            self.building_id = building_id

    @property
    def anomaly_type(self):
        """Gets the anomaly_type of this XiqAnomaliesUpdateActionRequest.  # noqa: E501


        :return: The anomaly_type of this XiqAnomaliesUpdateActionRequest.  # noqa: E501
        :rtype: XiqAnomalyType
        """
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, anomaly_type):
        """Sets the anomaly_type of this XiqAnomaliesUpdateActionRequest.


        :param anomaly_type: The anomaly_type of this XiqAnomaliesUpdateActionRequest.  # noqa: E501
        :type: XiqAnomalyType
        """

        self._anomaly_type = anomaly_type

    @property
    def action_type(self):
        """Gets the action_type of this XiqAnomaliesUpdateActionRequest.  # noqa: E501


        :return: The action_type of this XiqAnomaliesUpdateActionRequest.  # noqa: E501
        :rtype: XiqActionType
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this XiqAnomaliesUpdateActionRequest.


        :param action_type: The action_type of this XiqAnomaliesUpdateActionRequest.  # noqa: E501
        :type: XiqActionType
        """

        self._action_type = action_type

    @property
    def building_id(self):
        """Gets the building_id of this XiqAnomaliesUpdateActionRequest.  # noqa: E501

        The location id  # noqa: E501

        :return: The building_id of this XiqAnomaliesUpdateActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this XiqAnomaliesUpdateActionRequest.

        The location id  # noqa: E501

        :param building_id: The building_id of this XiqAnomaliesUpdateActionRequest.  # noqa: E501
        :type: int
        """

        self._building_id = building_id

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
        if not isinstance(other, XiqAnomaliesUpdateActionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomaliesUpdateActionRequest):
            return True

        return self.to_dict() != other.to_dict()