# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.0.30
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAnomalyDeviceEntity(object):
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
        'device_id': 'int',
        'device_name': 'str',
        'pinned': 'bool',
        'wired': 'bool',
        'anomaly_id': 'str',
        'severity': 'XiqAnomalySeverity',
        'summary': 'str',
        'last_detected_time': 'int',
        'recommended_action': 'str',
        'anomaly_subtypes': 'str',
        'interface_name': 'str'
    }

    attribute_map = {
        'device_id': 'device_id',
        'device_name': 'device_name',
        'pinned': 'pinned',
        'wired': 'wired',
        'anomaly_id': 'anomaly_id',
        'severity': 'severity',
        'summary': 'summary',
        'last_detected_time': 'last_detected_time',
        'recommended_action': 'recommended_action',
        'anomaly_subtypes': 'anomaly_subtypes',
        'interface_name': 'interface_name'
    }

    def __init__(self, device_id=None, device_name=None, pinned=None, wired=None, anomaly_id=None, severity=None, summary=None, last_detected_time=None, recommended_action=None, anomaly_subtypes=None, interface_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomalyDeviceEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device_id = None
        self._device_name = None
        self._pinned = None
        self._wired = None
        self._anomaly_id = None
        self._severity = None
        self._summary = None
        self._last_detected_time = None
        self._recommended_action = None
        self._anomaly_subtypes = None
        self._interface_name = None
        self.discriminator = None

        if device_id is not None:
            self.device_id = device_id
        if device_name is not None:
            self.device_name = device_name
        if pinned is not None:
            self.pinned = pinned
        if wired is not None:
            self.wired = wired
        if anomaly_id is not None:
            self.anomaly_id = anomaly_id
        if severity is not None:
            self.severity = severity
        if summary is not None:
            self.summary = summary
        if last_detected_time is not None:
            self.last_detected_time = last_detected_time
        if recommended_action is not None:
            self.recommended_action = recommended_action
        if anomaly_subtypes is not None:
            self.anomaly_subtypes = anomaly_subtypes
        if interface_name is not None:
            self.interface_name = interface_name

    @property
    def device_id(self):
        """Gets the device_id of this XiqAnomalyDeviceEntity.  # noqa: E501

        the device id  # noqa: E501

        :return: The device_id of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqAnomalyDeviceEntity.

        the device id  # noqa: E501

        :param device_id: The device_id of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def device_name(self):
        """Gets the device_name of this XiqAnomalyDeviceEntity.  # noqa: E501

        the device name  # noqa: E501

        :return: The device_name of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this XiqAnomalyDeviceEntity.

        the device name  # noqa: E501

        :param device_name: The device_name of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def pinned(self):
        """Gets the pinned of this XiqAnomalyDeviceEntity.  # noqa: E501

        is device pinned  # noqa: E501

        :return: The pinned of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """Sets the pinned of this XiqAnomalyDeviceEntity.

        is device pinned  # noqa: E501

        :param pinned: The pinned of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: bool
        """

        self._pinned = pinned

    @property
    def wired(self):
        """Gets the wired of this XiqAnomalyDeviceEntity.  # noqa: E501

        is device wired  # noqa: E501

        :return: The wired of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: bool
        """
        return self._wired

    @wired.setter
    def wired(self, wired):
        """Sets the wired of this XiqAnomalyDeviceEntity.

        is device wired  # noqa: E501

        :param wired: The wired of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: bool
        """

        self._wired = wired

    @property
    def anomaly_id(self):
        """Gets the anomaly_id of this XiqAnomalyDeviceEntity.  # noqa: E501

        the anomaly id  # noqa: E501

        :return: The anomaly_id of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_id

    @anomaly_id.setter
    def anomaly_id(self, anomaly_id):
        """Sets the anomaly_id of this XiqAnomalyDeviceEntity.

        the anomaly id  # noqa: E501

        :param anomaly_id: The anomaly_id of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: str
        """

        self._anomaly_id = anomaly_id

    @property
    def severity(self):
        """Gets the severity of this XiqAnomalyDeviceEntity.  # noqa: E501


        :return: The severity of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: XiqAnomalySeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this XiqAnomalyDeviceEntity.


        :param severity: The severity of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: XiqAnomalySeverity
        """

        self._severity = severity

    @property
    def summary(self):
        """Gets the summary of this XiqAnomalyDeviceEntity.  # noqa: E501

        the anomaly summary  # noqa: E501

        :return: The summary of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this XiqAnomalyDeviceEntity.

        the anomaly summary  # noqa: E501

        :param summary: The summary of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def last_detected_time(self):
        """Gets the last_detected_time of this XiqAnomalyDeviceEntity.  # noqa: E501

        the last detected time  # noqa: E501

        :return: The last_detected_time of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: int
        """
        return self._last_detected_time

    @last_detected_time.setter
    def last_detected_time(self, last_detected_time):
        """Sets the last_detected_time of this XiqAnomalyDeviceEntity.

        the last detected time  # noqa: E501

        :param last_detected_time: The last_detected_time of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: int
        """

        self._last_detected_time = last_detected_time

    @property
    def recommended_action(self):
        """Gets the recommended_action of this XiqAnomalyDeviceEntity.  # noqa: E501

        the recommended action  # noqa: E501

        :return: The recommended_action of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: str
        """
        return self._recommended_action

    @recommended_action.setter
    def recommended_action(self, recommended_action):
        """Sets the recommended_action of this XiqAnomalyDeviceEntity.

        the recommended action  # noqa: E501

        :param recommended_action: The recommended_action of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: str
        """

        self._recommended_action = recommended_action

    @property
    def anomaly_subtypes(self):
        """Gets the anomaly_subtypes of this XiqAnomalyDeviceEntity.  # noqa: E501

        the anomaly sub-type  # noqa: E501

        :return: The anomaly_subtypes of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_subtypes

    @anomaly_subtypes.setter
    def anomaly_subtypes(self, anomaly_subtypes):
        """Sets the anomaly_subtypes of this XiqAnomalyDeviceEntity.

        the anomaly sub-type  # noqa: E501

        :param anomaly_subtypes: The anomaly_subtypes of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: str
        """

        self._anomaly_subtypes = anomaly_subtypes

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqAnomalyDeviceEntity.  # noqa: E501

        the interface name  # noqa: E501

        :return: The interface_name of this XiqAnomalyDeviceEntity.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqAnomalyDeviceEntity.

        the interface name  # noqa: E501

        :param interface_name: The interface_name of this XiqAnomalyDeviceEntity.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

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
        if not isinstance(other, XiqAnomalyDeviceEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomalyDeviceEntity):
            return True

        return self.to_dict() != other.to_dict()