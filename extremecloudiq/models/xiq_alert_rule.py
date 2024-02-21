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


class XiqAlertRule(object):
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
        'id': 'int',
        'message_metadata_id': 'int',
        'message_metadata_name': 'str',
        'message_metadata_type': 'str',
        'description': 'str',
        'severity_id': 'int',
        'severity_name': 'str',
        'is_enabled': 'bool',
        'trigger_type': 'str',
        'duration': 'int',
        'time_window': 'int',
        'count': 'int',
        'threshold': 'float',
        'unit': 'str',
        'operator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message_metadata_id': 'message_metadata_id',
        'message_metadata_name': 'message_metadata_name',
        'message_metadata_type': 'message_metadata_type',
        'description': 'description',
        'severity_id': 'severity_id',
        'severity_name': 'severity_name',
        'is_enabled': 'is_enabled',
        'trigger_type': 'trigger_type',
        'duration': 'duration',
        'time_window': 'time_window',
        'count': 'count',
        'threshold': 'threshold',
        'unit': 'unit',
        'operator': 'operator'
    }

    def __init__(self, id=None, message_metadata_id=None, message_metadata_name=None, message_metadata_type=None, description=None, severity_id=None, severity_name=None, is_enabled=None, trigger_type=None, duration=None, time_window=None, count=None, threshold=None, unit=None, operator=None, local_vars_configuration=None):  # noqa: E501
        """XiqAlertRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._message_metadata_id = None
        self._message_metadata_name = None
        self._message_metadata_type = None
        self._description = None
        self._severity_id = None
        self._severity_name = None
        self._is_enabled = None
        self._trigger_type = None
        self._duration = None
        self._time_window = None
        self._count = None
        self._threshold = None
        self._unit = None
        self._operator = None
        self.discriminator = None

        self.id = id
        self.message_metadata_id = message_metadata_id
        if message_metadata_name is not None:
            self.message_metadata_name = message_metadata_name
        if message_metadata_type is not None:
            self.message_metadata_type = message_metadata_type
        if description is not None:
            self.description = description
        self.severity_id = severity_id
        if severity_name is not None:
            self.severity_name = severity_name
        self.is_enabled = is_enabled
        self.trigger_type = trigger_type
        if duration is not None:
            self.duration = duration
        if time_window is not None:
            self.time_window = time_window
        if count is not None:
            self.count = count
        if threshold is not None:
            self.threshold = threshold
        if unit is not None:
            self.unit = unit
        if operator is not None:
            self.operator = operator

    @property
    def id(self):
        """Gets the id of this XiqAlertRule.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqAlertRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqAlertRule.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqAlertRule.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def message_metadata_id(self):
        """Gets the message_metadata_id of this XiqAlertRule.  # noqa: E501

        The identifier for the unique message type that corresponds to this rule.  # noqa: E501

        :return: The message_metadata_id of this XiqAlertRule.  # noqa: E501
        :rtype: int
        """
        return self._message_metadata_id

    @message_metadata_id.setter
    def message_metadata_id(self, message_metadata_id):
        """Sets the message_metadata_id of this XiqAlertRule.

        The identifier for the unique message type that corresponds to this rule.  # noqa: E501

        :param message_metadata_id: The message_metadata_id of this XiqAlertRule.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and message_metadata_id is None:  # noqa: E501
            raise ValueError("Invalid value for `message_metadata_id`, must not be `None`")  # noqa: E501

        self._message_metadata_id = message_metadata_id

    @property
    def message_metadata_name(self):
        """Gets the message_metadata_name of this XiqAlertRule.  # noqa: E501

        The display name for the message.  # noqa: E501

        :return: The message_metadata_name of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._message_metadata_name

    @message_metadata_name.setter
    def message_metadata_name(self, message_metadata_name):
        """Sets the message_metadata_name of this XiqAlertRule.

        The display name for the message.  # noqa: E501

        :param message_metadata_name: The message_metadata_name of this XiqAlertRule.  # noqa: E501
        :type: str
        """

        self._message_metadata_name = message_metadata_name

    @property
    def message_metadata_type(self):
        """Gets the message_metadata_type of this XiqAlertRule.  # noqa: E501

        The type of the message.  # noqa: E501

        :return: The message_metadata_type of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._message_metadata_type

    @message_metadata_type.setter
    def message_metadata_type(self, message_metadata_type):
        """Sets the message_metadata_type of this XiqAlertRule.

        The type of the message.  # noqa: E501

        :param message_metadata_type: The message_metadata_type of this XiqAlertRule.  # noqa: E501
        :type: str
        """

        self._message_metadata_type = message_metadata_type

    @property
    def description(self):
        """Gets the description of this XiqAlertRule.  # noqa: E501

        This is a description for the alert rule.  # noqa: E501

        :return: The description of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqAlertRule.

        This is a description for the alert rule.  # noqa: E501

        :param description: The description of this XiqAlertRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def severity_id(self):
        """Gets the severity_id of this XiqAlertRule.  # noqa: E501

        The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info.  # noqa: E501

        :return: The severity_id of this XiqAlertRule.  # noqa: E501
        :rtype: int
        """
        return self._severity_id

    @severity_id.setter
    def severity_id(self, severity_id):
        """Sets the severity_id of this XiqAlertRule.

        The severity identifier. The currently supported severity IDs are 1 for critical, 2 for warning, and 3 for info.  # noqa: E501

        :param severity_id: The severity_id of this XiqAlertRule.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and severity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `severity_id`, must not be `None`")  # noqa: E501

        self._severity_id = severity_id

    @property
    def severity_name(self):
        """Gets the severity_name of this XiqAlertRule.  # noqa: E501

        The display name for the alert severity.  # noqa: E501

        :return: The severity_name of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._severity_name

    @severity_name.setter
    def severity_name(self, severity_name):
        """Sets the severity_name of this XiqAlertRule.

        The display name for the alert severity.  # noqa: E501

        :param severity_name: The severity_name of this XiqAlertRule.  # noqa: E501
        :type: str
        """

        self._severity_name = severity_name

    @property
    def is_enabled(self):
        """Gets the is_enabled of this XiqAlertRule.  # noqa: E501

        True if this rule is active and enabled.  # noqa: E501

        :return: The is_enabled of this XiqAlertRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this XiqAlertRule.

        True if this rule is active and enabled.  # noqa: E501

        :param is_enabled: The is_enabled of this XiqAlertRule.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `is_enabled`, must not be `None`")  # noqa: E501

        self._is_enabled = is_enabled

    @property
    def trigger_type(self):
        """Gets the trigger_type of this XiqAlertRule.  # noqa: E501

        The configured trigger type of the rule.  # noqa: E501

        :return: The trigger_type of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this XiqAlertRule.

        The configured trigger type of the rule.  # noqa: E501

        :param trigger_type: The trigger_type of this XiqAlertRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and trigger_type is None:  # noqa: E501
            raise ValueError("Invalid value for `trigger_type`, must not be `None`")  # noqa: E501

        self._trigger_type = trigger_type

    @property
    def duration(self):
        """Gets the duration of this XiqAlertRule.  # noqa: E501

        Has value when trigger_type is \"DEFERRED\". The deferred duration, in seconds.  # noqa: E501

        :return: The duration of this XiqAlertRule.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this XiqAlertRule.

        Has value when trigger_type is \"DEFERRED\". The deferred duration, in seconds.  # noqa: E501

        :param duration: The duration of this XiqAlertRule.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def time_window(self):
        """Gets the time_window of this XiqAlertRule.  # noqa: E501

        Has value when trigger_type is \"REPEATED\". The time window to count the number of repeated messages, in seconds.  # noqa: E501

        :return: The time_window of this XiqAlertRule.  # noqa: E501
        :rtype: int
        """
        return self._time_window

    @time_window.setter
    def time_window(self, time_window):
        """Sets the time_window of this XiqAlertRule.

        Has value when trigger_type is \"REPEATED\". The time window to count the number of repeated messages, in seconds.  # noqa: E501

        :param time_window: The time_window of this XiqAlertRule.  # noqa: E501
        :type: int
        """

        self._time_window = time_window

    @property
    def count(self):
        """Gets the count of this XiqAlertRule.  # noqa: E501

        Has value when trigger_type is \"REPEATED\". The lower bound of the number of messages required to trigger this rule.  # noqa: E501

        :return: The count of this XiqAlertRule.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this XiqAlertRule.

        Has value when trigger_type is \"REPEATED\". The lower bound of the number of messages required to trigger this rule.  # noqa: E501

        :param count: The count of this XiqAlertRule.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def threshold(self):
        """Gets the threshold of this XiqAlertRule.  # noqa: E501

        Has value when type is \"METRIC\". The threshold for the message.  # noqa: E501

        :return: The threshold of this XiqAlertRule.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this XiqAlertRule.

        Has value when type is \"METRIC\". The threshold for the message.  # noqa: E501

        :param threshold: The threshold of this XiqAlertRule.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def unit(self):
        """Gets the unit of this XiqAlertRule.  # noqa: E501

        The unit of this threshold  # noqa: E501

        :return: The unit of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this XiqAlertRule.

        The unit of this threshold  # noqa: E501

        :param unit: The unit of this XiqAlertRule.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def operator(self):
        """Gets the operator of this XiqAlertRule.  # noqa: E501

        Has value when message_metadata_type is \"METRIC\". The operator to compare against the threshold.  # noqa: E501

        :return: The operator of this XiqAlertRule.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this XiqAlertRule.

        Has value when message_metadata_type is \"METRIC\". The operator to compare against the threshold.  # noqa: E501

        :param operator: The operator of this XiqAlertRule.  # noqa: E501
        :type: str
        """

        self._operator = operator

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
        if not isinstance(other, XiqAlertRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAlertRule):
            return True

        return self.to_dict() != other.to_dict()
