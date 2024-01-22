# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.1.7
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAnomalyLocationEntity(object):
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
        'location_type': 'XiqLocationType',
        'location_ids': 'list[int]',
        'building_id': 'int',
        'location_name': 'str',
        'pinned': 'bool',
        'muted': 'bool',
        'severity': 'XiqAnomalySeverity',
        'severity_id': 'int',
        'summary': 'str',
        'affected_device_count': 'int',
        'last_detected_time': 'int',
        'anomaly_type': 'XiqAnomalyType'
    }

    attribute_map = {
        'location_type': 'location_type',
        'location_ids': 'location_ids',
        'building_id': 'building_id',
        'location_name': 'location_name',
        'pinned': 'pinned',
        'muted': 'muted',
        'severity': 'severity',
        'severity_id': 'severity_id',
        'summary': 'summary',
        'affected_device_count': 'affected_device_count',
        'last_detected_time': 'last_detected_time',
        'anomaly_type': 'anomaly_type'
    }

    def __init__(self, location_type=None, location_ids=None, building_id=None, location_name=None, pinned=None, muted=None, severity=None, severity_id=None, summary=None, affected_device_count=None, last_detected_time=None, anomaly_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomalyLocationEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location_type = None
        self._location_ids = None
        self._building_id = None
        self._location_name = None
        self._pinned = None
        self._muted = None
        self._severity = None
        self._severity_id = None
        self._summary = None
        self._affected_device_count = None
        self._last_detected_time = None
        self._anomaly_type = None
        self.discriminator = None

        if location_type is not None:
            self.location_type = location_type
        if location_ids is not None:
            self.location_ids = location_ids
        if building_id is not None:
            self.building_id = building_id
        if location_name is not None:
            self.location_name = location_name
        if pinned is not None:
            self.pinned = pinned
        if muted is not None:
            self.muted = muted
        if severity is not None:
            self.severity = severity
        if severity_id is not None:
            self.severity_id = severity_id
        if summary is not None:
            self.summary = summary
        if affected_device_count is not None:
            self.affected_device_count = affected_device_count
        if last_detected_time is not None:
            self.last_detected_time = last_detected_time
        if anomaly_type is not None:
            self.anomaly_type = anomaly_type

    @property
    def location_type(self):
        """Gets the location_type of this XiqAnomalyLocationEntity.  # noqa: E501


        :return: The location_type of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: XiqLocationType
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this XiqAnomalyLocationEntity.


        :param location_type: The location_type of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: XiqLocationType
        """

        self._location_type = location_type

    @property
    def location_ids(self):
        """Gets the location_ids of this XiqAnomalyLocationEntity.  # noqa: E501

        the location id  # noqa: E501

        :return: The location_ids of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: list[int]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """Sets the location_ids of this XiqAnomalyLocationEntity.

        the location id  # noqa: E501

        :param location_ids: The location_ids of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: list[int]
        """

        self._location_ids = location_ids

    @property
    def building_id(self):
        """Gets the building_id of this XiqAnomalyLocationEntity.  # noqa: E501

        the building id  # noqa: E501

        :return: The building_id of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this XiqAnomalyLocationEntity.

        the building id  # noqa: E501

        :param building_id: The building_id of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: int
        """

        self._building_id = building_id

    @property
    def location_name(self):
        """Gets the location_name of this XiqAnomalyLocationEntity.  # noqa: E501

        the location name  # noqa: E501

        :return: The location_name of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this XiqAnomalyLocationEntity.

        the location name  # noqa: E501

        :param location_name: The location_name of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def pinned(self):
        """Gets the pinned of this XiqAnomalyLocationEntity.  # noqa: E501

        is location pinned  # noqa: E501

        :return: The pinned of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this XiqAnomalyLocationEntity.

        is location pinned  # noqa: E501

        :param pinned: The pinned of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def muted(self):
        """Gets the muted of this XiqAnomalyLocationEntity.  # noqa: E501

        the location muted  # noqa: E501

        :return: The muted of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this XiqAnomalyLocationEntity.

        the location muted  # noqa: E501

        :param muted: The muted of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: bool
        """

        self._muted = muted

    @property
    def severity(self):
        """Gets the severity of this XiqAnomalyLocationEntity.  # noqa: E501


        :return: The severity of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: XiqAnomalySeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this XiqAnomalyLocationEntity.


        :param severity: The severity of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: XiqAnomalySeverity
        """

        self._severity = severity

    @property
    def severity_id(self):
        """Gets the severity_id of this XiqAnomalyLocationEntity.  # noqa: E501

        the severity id  # noqa: E501

        :return: The severity_id of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: int
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        """Sets the severity_id of this XiqAnomalyLocationEntity.

        the severity id  # noqa: E501

        :param severity_id: The severity_id of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: int
        """

        self._severity_id = severity_id

    @property
    def summary(self):
        """Gets the summary of this XiqAnomalyLocationEntity.  # noqa: E501

        the anomaly summary  # noqa: E501

        :return: The summary of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this XiqAnomalyLocationEntity.

        the anomaly summary  # noqa: E501

        :param summary: The summary of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def affected_device_count(self):
        """Gets the affected_device_count of this XiqAnomalyLocationEntity.  # noqa: E501

        the affected number of devices  # noqa: E501

        :return: The affected_device_count of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: int
        """
        return self._affected_device_count

    @affected_device_count.setter
    def affected_device_count(self, affected_device_count):
        """Sets the affected_device_count of this XiqAnomalyLocationEntity.

        the affected number of devices  # noqa: E501

        :param affected_device_count: The affected_device_count of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: int
        """

        self._affected_device_count = affected_device_count

    @property
    def last_detected_time(self):
        """Gets the last_detected_time of this XiqAnomalyLocationEntity.  # noqa: E501

        the last detected time  # noqa: E501

        :return: The last_detected_time of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: int
        """
        return self._last_detected_time

    @last_detected_time.setter
    def last_detected_time(self, last_detected_time):
        """Sets the last_detected_time of this XiqAnomalyLocationEntity.

        the last detected time  # noqa: E501

        :param last_detected_time: The last_detected_time of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: int
        """

        self._last_detected_time = last_detected_time

    @property
    def anomaly_type(self):
        """Gets the anomaly_type of this XiqAnomalyLocationEntity.  # noqa: E501


        :return: The anomaly_type of this XiqAnomalyLocationEntity.  # noqa: E501
        :rtype: XiqAnomalyType
        """
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, anomaly_type):
        """Sets the anomaly_type of this XiqAnomalyLocationEntity.


        :param anomaly_type: The anomaly_type of this XiqAnomalyLocationEntity.  # noqa: E501
        :type: XiqAnomalyType
        """

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
        if not isinstance(other, XiqAnomalyLocationEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomalyLocationEntity):
            return True

        return self.to_dict() != other.to_dict()
