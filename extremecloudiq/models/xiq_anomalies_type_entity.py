# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAnomaliesTypeEntity(object):
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
        'anomalies_count_by_type': 'int'
    }

    attribute_map = {
        'anomaly_type': 'anomaly_type',
        'anomalies_count_by_type': 'anomalies_count_by_type'
    }

    def __init__(self, anomaly_type=None, anomalies_count_by_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomaliesTypeEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._anomaly_type = None
        self._anomalies_count_by_type = None
        self.discriminator = None

        if anomaly_type is not None:
            self.anomaly_type = anomaly_type
        if anomalies_count_by_type is not None:
            self.anomalies_count_by_type = anomalies_count_by_type

    @property
    def anomaly_type(self):
        """Gets the anomaly_type of this XiqAnomaliesTypeEntity.  # noqa: E501


        :return: The anomaly_type of this XiqAnomaliesTypeEntity.  # noqa: E501
        :rtype: XiqAnomalyType
        """
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, anomaly_type):
        """Sets the anomaly_type of this XiqAnomaliesTypeEntity.


        :param anomaly_type: The anomaly_type of this XiqAnomaliesTypeEntity.  # noqa: E501
        :type: XiqAnomalyType
        """

        self._anomaly_type = anomaly_type

    @property
    def anomalies_count_by_type(self):
        """Gets the anomalies_count_by_type of this XiqAnomaliesTypeEntity.  # noqa: E501

        Anomalies count with low severity  # noqa: E501

        :return: The anomalies_count_by_type of this XiqAnomaliesTypeEntity.  # noqa: E501
        :rtype: int
        """
        return self._anomalies_count_by_type

    @anomalies_count_by_type.setter
    def anomalies_count_by_type(self, anomalies_count_by_type):
        """Sets the anomalies_count_by_type of this XiqAnomaliesTypeEntity.

        Anomalies count with low severity  # noqa: E501

        :param anomalies_count_by_type: The anomalies_count_by_type of this XiqAnomaliesTypeEntity.  # noqa: E501
        :type: int
        """

        self._anomalies_count_by_type = anomalies_count_by_type

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
        if not isinstance(other, XiqAnomaliesTypeEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomaliesTypeEntity):
            return True

        return self.to_dict() != other.to_dict()
