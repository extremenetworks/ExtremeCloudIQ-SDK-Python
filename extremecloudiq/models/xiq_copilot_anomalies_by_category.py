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


class XiqCopilotAnomaliesByCategory(object):
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
        'anomalies_by_location': 'list[XiqAnomaliesSiteEntity]',
        'anomalies_by_severity': 'XiqAnomaliesSeverityEntity',
        'anomalies_by_type': 'list[XiqAnomaliesTypeEntity]'
    }

    attribute_map = {
        'anomalies_by_location': 'anomalies_by_location',
        'anomalies_by_severity': 'anomalies_by_severity',
        'anomalies_by_type': 'anomalies_by_type'
    }

    def __init__(self, anomalies_by_location=None, anomalies_by_severity=None, anomalies_by_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqCopilotAnomaliesByCategory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._anomalies_by_location = None
        self._anomalies_by_severity = None
        self._anomalies_by_type = None
        self.discriminator = None

        if anomalies_by_location is not None:
            self.anomalies_by_location = anomalies_by_location
        if anomalies_by_severity is not None:
            self.anomalies_by_severity = anomalies_by_severity
        if anomalies_by_type is not None:
            self.anomalies_by_type = anomalies_by_type

    @property
    def anomalies_by_location(self):
        """Gets the anomalies_by_location of this XiqCopilotAnomaliesByCategory.  # noqa: E501

        The total anomalies by location  # noqa: E501

        :return: The anomalies_by_location of this XiqCopilotAnomaliesByCategory.  # noqa: E501
        :rtype: list[XiqAnomaliesSiteEntity]
        """
        return self._anomalies_by_location

    @anomalies_by_location.setter
    def anomalies_by_location(self, anomalies_by_location):
        """Sets the anomalies_by_location of this XiqCopilotAnomaliesByCategory.

        The total anomalies by location  # noqa: E501

        :param anomalies_by_location: The anomalies_by_location of this XiqCopilotAnomaliesByCategory.  # noqa: E501
        :type: list[XiqAnomaliesSiteEntity]
        """

        self._anomalies_by_location = anomalies_by_location

    @property
    def anomalies_by_severity(self):
        """Gets the anomalies_by_severity of this XiqCopilotAnomaliesByCategory.  # noqa: E501


        :return: The anomalies_by_severity of this XiqCopilotAnomaliesByCategory.  # noqa: E501
        :rtype: XiqAnomaliesSeverityEntity
        """
        return self._anomalies_by_severity

    @anomalies_by_severity.setter
    def anomalies_by_severity(self, anomalies_by_severity):
        """Sets the anomalies_by_severity of this XiqCopilotAnomaliesByCategory.


        :param anomalies_by_severity: The anomalies_by_severity of this XiqCopilotAnomaliesByCategory.  # noqa: E501
        :type: XiqAnomaliesSeverityEntity
        """

        self._anomalies_by_severity = anomalies_by_severity

    @property
    def anomalies_by_type(self):
        """Gets the anomalies_by_type of this XiqCopilotAnomaliesByCategory.  # noqa: E501

        The total anomalies by type  # noqa: E501

        :return: The anomalies_by_type of this XiqCopilotAnomaliesByCategory.  # noqa: E501
        :rtype: list[XiqAnomaliesTypeEntity]
        """
        return self._anomalies_by_type

    @anomalies_by_type.setter
    def anomalies_by_type(self, anomalies_by_type):
        """Sets the anomalies_by_type of this XiqCopilotAnomaliesByCategory.

        The total anomalies by type  # noqa: E501

        :param anomalies_by_type: The anomalies_by_type of this XiqCopilotAnomaliesByCategory.  # noqa: E501
        :type: list[XiqAnomaliesTypeEntity]
        """

        self._anomalies_by_type = anomalies_by_type

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
        if not isinstance(other, XiqCopilotAnomaliesByCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqCopilotAnomaliesByCategory):
            return True

        return self.to_dict() != other.to_dict()
