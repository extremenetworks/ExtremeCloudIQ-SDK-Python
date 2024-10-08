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


class XiqAnomalyDeviceWithLocation(object):
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
        'location_name': 'str',
        'muted': 'bool',
        'severity': 'XiqAnomalySeverity',
        'anomaly_type': 'XiqAnomalyType',
        'last_detected_time': 'int',
        'device_id': 'int',
        'device_name': 'str',
        'device_model': 'str',
        'device_make': 'str',
        'switch_stack': 'bool',
        'category': 'XiqDeviceCategory',
        'interface_name': 'str',
        'location_id': 'int',
        'anomaly_id': 'str',
        'frequency': 'str',
        'channel_number': 'int',
        'channel_mode': 'str',
        'recommended_action': 'str',
        'issue': 'str',
        'current_poe_mode': 'str',
        'device_status': 'bool',
        'anomaly_subtypes': 'str'
    }

    attribute_map = {
        'building_id': 'building_id',
        'location_name': 'location_name',
        'muted': 'muted',
        'severity': 'severity',
        'anomaly_type': 'anomaly_type',
        'last_detected_time': 'last_detected_time',
        'device_id': 'device_id',
        'device_name': 'device_name',
        'device_model': 'device_model',
        'device_make': 'device_make',
        'switch_stack': 'switch_stack',
        'category': 'category',
        'interface_name': 'interface_name',
        'location_id': 'location_id',
        'anomaly_id': 'anomaly_id',
        'frequency': 'frequency',
        'channel_number': 'channel_number',
        'channel_mode': 'channel_mode',
        'recommended_action': 'recommended_action',
        'issue': 'issue',
        'current_poe_mode': 'current_poe_mode',
        'device_status': 'device_status',
        'anomaly_subtypes': 'anomaly_subtypes'
    }

    def __init__(self, building_id=None, location_name=None, muted=None, severity=None, anomaly_type=None, last_detected_time=None, device_id=None, device_name=None, device_model=None, device_make=None, switch_stack=None, category=None, interface_name=None, location_id=None, anomaly_id=None, frequency=None, channel_number=None, channel_mode=None, recommended_action=None, issue=None, current_poe_mode=None, device_status=None, anomaly_subtypes=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomalyDeviceWithLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._building_id = None
        self._location_name = None
        self._muted = None
        self._severity = None
        self._anomaly_type = None
        self._last_detected_time = None
        self._device_id = None
        self._device_name = None
        self._device_model = None
        self._device_make = None
        self._switch_stack = None
        self._category = None
        self._interface_name = None
        self._location_id = None
        self._anomaly_id = None
        self._frequency = None
        self._channel_number = None
        self._channel_mode = None
        self._recommended_action = None
        self._issue = None
        self._current_poe_mode = None
        self._device_status = None
        self._anomaly_subtypes = None
        self.discriminator = None

        self.building_id = building_id
        self.location_name = location_name
        self.muted = muted
        self.severity = severity
        self.anomaly_type = anomaly_type
        self.last_detected_time = last_detected_time
        self.device_id = device_id
        self.device_name = device_name
        self.device_model = device_model
        self.device_make = device_make
        self.switch_stack = switch_stack
        self.category = category
        self.interface_name = interface_name
        if location_id is not None:
            self.location_id = location_id
        if anomaly_id is not None:
            self.anomaly_id = anomaly_id
        if frequency is not None:
            self.frequency = frequency
        if channel_number is not None:
            self.channel_number = channel_number
        if channel_mode is not None:
            self.channel_mode = channel_mode
        if recommended_action is not None:
            self.recommended_action = recommended_action
        if issue is not None:
            self.issue = issue
        if current_poe_mode is not None:
            self.current_poe_mode = current_poe_mode
        if device_status is not None:
            self.device_status = device_status
        if anomaly_subtypes is not None:
            self.anomaly_subtypes = anomaly_subtypes

    @property
    def building_id(self):
        """Gets the building_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The building ID  # noqa: E501

        :return: The building_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: int
        """
        return self._building_id

    @building_id.setter
    def building_id(self, building_id):
        """Sets the building_id of this XiqAnomalyDeviceWithLocation.

        The building ID  # noqa: E501

        :param building_id: The building_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and building_id is None:  # noqa: E501
            raise ValueError("Invalid value for `building_id`, must not be `None`")  # noqa: E501

        self._building_id = building_id

    @property
    def location_name(self):
        """Gets the location_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The location name  # noqa: E501

        :return: The location_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this XiqAnomalyDeviceWithLocation.

        The location name  # noqa: E501

        :param location_name: The location_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and location_name is None:  # noqa: E501
            raise ValueError("Invalid value for `location_name`, must not be `None`")  # noqa: E501

        self._location_name = location_name

    @property
    def muted(self):
        """Gets the muted of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        To filter muted anomalies  # noqa: E501

        :return: The muted of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this XiqAnomalyDeviceWithLocation.

        To filter muted anomalies  # noqa: E501

        :param muted: The muted of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and muted is None:  # noqa: E501
            raise ValueError("Invalid value for `muted`, must not be `None`")  # noqa: E501

        self._muted = muted

    @property
    def severity(self):
        """Gets the severity of this XiqAnomalyDeviceWithLocation.  # noqa: E501


        :return: The severity of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: XiqAnomalySeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this XiqAnomalyDeviceWithLocation.


        :param severity: The severity of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: XiqAnomalySeverity
        """
        if self.local_vars_configuration.client_side_validation and severity is None:  # noqa: E501
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501

        self._severity = severity

    @property
    def anomaly_type(self):
        """Gets the anomaly_type of this XiqAnomalyDeviceWithLocation.  # noqa: E501


        :return: The anomaly_type of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: XiqAnomalyType
        """
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, anomaly_type):
        """Sets the anomaly_type of this XiqAnomalyDeviceWithLocation.


        :param anomaly_type: The anomaly_type of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: XiqAnomalyType
        """
        if self.local_vars_configuration.client_side_validation and anomaly_type is None:  # noqa: E501
            raise ValueError("Invalid value for `anomaly_type`, must not be `None`")  # noqa: E501

        self._anomaly_type = anomaly_type

    @property
    def last_detected_time(self):
        """Gets the last_detected_time of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The last detected time of anomaly  # noqa: E501

        :return: The last_detected_time of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: int
        """
        return self._last_detected_time

    @last_detected_time.setter
    def last_detected_time(self, last_detected_time):
        """Sets the last_detected_time of this XiqAnomalyDeviceWithLocation.

        The last detected time of anomaly  # noqa: E501

        :param last_detected_time: The last_detected_time of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and last_detected_time is None:  # noqa: E501
            raise ValueError("Invalid value for `last_detected_time`, must not be `None`")  # noqa: E501

        self._last_detected_time = last_detected_time

    @property
    def device_id(self):
        """Gets the device_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The device ID  # noqa: E501

        :return: The device_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqAnomalyDeviceWithLocation.

        The device ID  # noqa: E501

        :param device_id: The device_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and device_id is None:  # noqa: E501
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def device_name(self):
        """Gets the device_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The device name  # noqa: E501

        :return: The device_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this XiqAnomalyDeviceWithLocation.

        The device name  # noqa: E501

        :param device_name: The device_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_name is None:  # noqa: E501
            raise ValueError("Invalid value for `device_name`, must not be `None`")  # noqa: E501

        self._device_name = device_name

    @property
    def device_model(self):
        """Gets the device_model of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The device model  # noqa: E501

        :return: The device_model of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this XiqAnomalyDeviceWithLocation.

        The device model  # noqa: E501

        :param device_model: The device_model of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_model is None:  # noqa: E501
            raise ValueError("Invalid value for `device_model`, must not be `None`")  # noqa: E501

        self._device_model = device_model

    @property
    def device_make(self):
        """Gets the device_make of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The device make  # noqa: E501

        :return: The device_make of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._device_make

    @device_make.setter
    def device_make(self, device_make):
        """Sets the device_make of this XiqAnomalyDeviceWithLocation.

        The device make  # noqa: E501

        :param device_make: The device_make of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and device_make is None:  # noqa: E501
            raise ValueError("Invalid value for `device_make`, must not be `None`")  # noqa: E501

        self._device_make = device_make

    @property
    def switch_stack(self):
        """Gets the switch_stack of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The device model  # noqa: E501

        :return: The switch_stack of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: bool
        """
        return self._switch_stack

    @switch_stack.setter
    def switch_stack(self, switch_stack):
        """Sets the switch_stack of this XiqAnomalyDeviceWithLocation.

        The device model  # noqa: E501

        :param switch_stack: The switch_stack of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and switch_stack is None:  # noqa: E501
            raise ValueError("Invalid value for `switch_stack`, must not be `None`")  # noqa: E501

        self._switch_stack = switch_stack

    @property
    def category(self):
        """Gets the category of this XiqAnomalyDeviceWithLocation.  # noqa: E501


        :return: The category of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: XiqDeviceCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this XiqAnomalyDeviceWithLocation.


        :param category: The category of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: XiqDeviceCategory
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The interface name  # noqa: E501

        :return: The interface_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqAnomalyDeviceWithLocation.

        The interface name  # noqa: E501

        :param interface_name: The interface_name of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and interface_name is None:  # noqa: E501
            raise ValueError("Invalid value for `interface_name`, must not be `None`")  # noqa: E501

        self._interface_name = interface_name

    @property
    def location_id(self):
        """Gets the location_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The location ID  # noqa: E501

        :return: The location_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqAnomalyDeviceWithLocation.

        The location ID  # noqa: E501

        :param location_id: The location_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def anomaly_id(self):
        """Gets the anomaly_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The anomaly ID  # noqa: E501

        :return: The anomaly_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_id

    @anomaly_id.setter
    def anomaly_id(self, anomaly_id):
        """Sets the anomaly_id of this XiqAnomalyDeviceWithLocation.

        The anomaly ID  # noqa: E501

        :param anomaly_id: The anomaly_id of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._anomaly_id = anomaly_id

    @property
    def frequency(self):
        """Gets the frequency of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The frequency  # noqa: E501

        :return: The frequency of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this XiqAnomalyDeviceWithLocation.

        The frequency  # noqa: E501

        :param frequency: The frequency of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def channel_number(self):
        """Gets the channel_number of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The channel number  # noqa: E501

        :return: The channel_number of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this XiqAnomalyDeviceWithLocation.

        The channel number  # noqa: E501

        :param channel_number: The channel_number of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: int
        """

        self._channel_number = channel_number

    @property
    def channel_mode(self):
        """Gets the channel_mode of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The channel mode  # noqa: E501

        :return: The channel_mode of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._channel_mode

    @channel_mode.setter
    def channel_mode(self, channel_mode):
        """Sets the channel_mode of this XiqAnomalyDeviceWithLocation.

        The channel mode  # noqa: E501

        :param channel_mode: The channel_mode of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._channel_mode = channel_mode

    @property
    def recommended_action(self):
        """Gets the recommended_action of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The recommended action  # noqa: E501

        :return: The recommended_action of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._recommended_action

    @recommended_action.setter
    def recommended_action(self, recommended_action):
        """Sets the recommended_action of this XiqAnomalyDeviceWithLocation.

        The recommended action  # noqa: E501

        :param recommended_action: The recommended_action of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._recommended_action = recommended_action

    @property
    def issue(self):
        """Gets the issue of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The issue  # noqa: E501

        :return: The issue of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this XiqAnomalyDeviceWithLocation.

        The issue  # noqa: E501

        :param issue: The issue of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._issue = issue

    @property
    def current_poe_mode(self):
        """Gets the current_poe_mode of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The current poe mode  # noqa: E501

        :return: The current_poe_mode of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._current_poe_mode

    @current_poe_mode.setter
    def current_poe_mode(self, current_poe_mode):
        """Sets the current_poe_mode of this XiqAnomalyDeviceWithLocation.

        The current poe mode  # noqa: E501

        :param current_poe_mode: The current_poe_mode of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._current_poe_mode = current_poe_mode

    @property
    def device_status(self):
        """Gets the device_status of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The device status  # noqa: E501

        :return: The device_status of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: bool
        """
        return self._device_status

    @device_status.setter
    def device_status(self, device_status):
        """Sets the device_status of this XiqAnomalyDeviceWithLocation.

        The device status  # noqa: E501

        :param device_status: The device_status of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: bool
        """

        self._device_status = device_status

    @property
    def anomaly_subtypes(self):
        """Gets the anomaly_subtypes of this XiqAnomalyDeviceWithLocation.  # noqa: E501

        The Anomaly Subtypes  # noqa: E501

        :return: The anomaly_subtypes of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_subtypes

    @anomaly_subtypes.setter
    def anomaly_subtypes(self, anomaly_subtypes):
        """Sets the anomaly_subtypes of this XiqAnomalyDeviceWithLocation.

        The Anomaly Subtypes  # noqa: E501

        :param anomaly_subtypes: The anomaly_subtypes of this XiqAnomalyDeviceWithLocation.  # noqa: E501
        :type: str
        """

        self._anomaly_subtypes = anomaly_subtypes

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
        if not isinstance(other, XiqAnomalyDeviceWithLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomalyDeviceWithLocation):
            return True

        return self.to_dict() != other.to_dict()
