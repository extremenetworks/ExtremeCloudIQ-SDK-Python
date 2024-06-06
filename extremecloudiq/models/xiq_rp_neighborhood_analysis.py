# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqRpNeighborhoodAnalysis(object):
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
        'create_time': 'datetime',
        'update_time': 'datetime',
        'enable_background_scan': 'bool',
        'background_scan_interval': 'int',
        'enable_skip_scan_when_clients_connected': 'bool',
        'enable_skip_scan_when_clients_in_power_save_mode': 'bool',
        'enable_skip_scan_when_process_voice_traffic': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enable_background_scan': 'enable_background_scan',
        'background_scan_interval': 'background_scan_interval',
        'enable_skip_scan_when_clients_connected': 'enable_skip_scan_when_clients_connected',
        'enable_skip_scan_when_clients_in_power_save_mode': 'enable_skip_scan_when_clients_in_power_save_mode',
        'enable_skip_scan_when_process_voice_traffic': 'enable_skip_scan_when_process_voice_traffic'
    }

    def __init__(self, id=None, create_time=None, update_time=None, enable_background_scan=None, background_scan_interval=None, enable_skip_scan_when_clients_connected=None, enable_skip_scan_when_clients_in_power_save_mode=None, enable_skip_scan_when_process_voice_traffic=None, local_vars_configuration=None):  # noqa: E501
        """XiqRpNeighborhoodAnalysis - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._enable_background_scan = None
        self._background_scan_interval = None
        self._enable_skip_scan_when_clients_connected = None
        self._enable_skip_scan_when_clients_in_power_save_mode = None
        self._enable_skip_scan_when_process_voice_traffic = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if enable_background_scan is not None:
            self.enable_background_scan = enable_background_scan
        if background_scan_interval is not None:
            self.background_scan_interval = background_scan_interval
        if enable_skip_scan_when_clients_connected is not None:
            self.enable_skip_scan_when_clients_connected = enable_skip_scan_when_clients_connected
        if enable_skip_scan_when_clients_in_power_save_mode is not None:
            self.enable_skip_scan_when_clients_in_power_save_mode = enable_skip_scan_when_clients_in_power_save_mode
        if enable_skip_scan_when_process_voice_traffic is not None:
            self.enable_skip_scan_when_process_voice_traffic = enable_skip_scan_when_process_voice_traffic

    @property
    def id(self):
        """Gets the id of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRpNeighborhoodAnalysis.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRpNeighborhoodAnalysis.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRpNeighborhoodAnalysis.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def enable_background_scan(self):
        """Gets the enable_background_scan of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        Whether to enable background scanning of neighboring devices  # noqa: E501

        :return: The enable_background_scan of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._enable_background_scan

    @enable_background_scan.setter
    def enable_background_scan(self, enable_background_scan):
        """Sets the enable_background_scan of this XiqRpNeighborhoodAnalysis.

        Whether to enable background scanning of neighboring devices  # noqa: E501

        :param enable_background_scan: The enable_background_scan of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: bool
        """

        self._enable_background_scan = enable_background_scan

    @property
    def background_scan_interval(self):
        """Gets the background_scan_interval of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        The background scan interval from 1 up to 1440 minutes  # noqa: E501

        :return: The background_scan_interval of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: int
        """
        return self._background_scan_interval

    @background_scan_interval.setter
    def background_scan_interval(self, background_scan_interval):
        """Sets the background_scan_interval of this XiqRpNeighborhoodAnalysis.

        The background scan interval from 1 up to 1440 minutes  # noqa: E501

        :param background_scan_interval: The background_scan_interval of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: int
        """

        self._background_scan_interval = background_scan_interval

    @property
    def enable_skip_scan_when_clients_connected(self):
        """Gets the enable_skip_scan_when_clients_connected of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        Whether to enable skipping of background scan when devices have client connections  # noqa: E501

        :return: The enable_skip_scan_when_clients_connected of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._enable_skip_scan_when_clients_connected

    @enable_skip_scan_when_clients_connected.setter
    def enable_skip_scan_when_clients_connected(self, enable_skip_scan_when_clients_connected):
        """Sets the enable_skip_scan_when_clients_connected of this XiqRpNeighborhoodAnalysis.

        Whether to enable skipping of background scan when devices have client connections  # noqa: E501

        :param enable_skip_scan_when_clients_connected: The enable_skip_scan_when_clients_connected of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: bool
        """

        self._enable_skip_scan_when_clients_connected = enable_skip_scan_when_clients_connected

    @property
    def enable_skip_scan_when_clients_in_power_save_mode(self):
        """Gets the enable_skip_scan_when_clients_in_power_save_mode of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        Whether to skipping of background scan when connected devices are in power save mode  # noqa: E501

        :return: The enable_skip_scan_when_clients_in_power_save_mode of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._enable_skip_scan_when_clients_in_power_save_mode

    @enable_skip_scan_when_clients_in_power_save_mode.setter
    def enable_skip_scan_when_clients_in_power_save_mode(self, enable_skip_scan_when_clients_in_power_save_mode):
        """Sets the enable_skip_scan_when_clients_in_power_save_mode of this XiqRpNeighborhoodAnalysis.

        Whether to skipping of background scan when connected devices are in power save mode  # noqa: E501

        :param enable_skip_scan_when_clients_in_power_save_mode: The enable_skip_scan_when_clients_in_power_save_mode of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: bool
        """

        self._enable_skip_scan_when_clients_in_power_save_mode = enable_skip_scan_when_clients_in_power_save_mode

    @property
    def enable_skip_scan_when_process_voice_traffic(self):
        """Gets the enable_skip_scan_when_process_voice_traffic of this XiqRpNeighborhoodAnalysis.  # noqa: E501

        Whether to enable skipping of background scan when devices have network traffic with voice priority  # noqa: E501

        :return: The enable_skip_scan_when_process_voice_traffic of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :rtype: bool
        """
        return self._enable_skip_scan_when_process_voice_traffic

    @enable_skip_scan_when_process_voice_traffic.setter
    def enable_skip_scan_when_process_voice_traffic(self, enable_skip_scan_when_process_voice_traffic):
        """Sets the enable_skip_scan_when_process_voice_traffic of this XiqRpNeighborhoodAnalysis.

        Whether to enable skipping of background scan when devices have network traffic with voice priority  # noqa: E501

        :param enable_skip_scan_when_process_voice_traffic: The enable_skip_scan_when_process_voice_traffic of this XiqRpNeighborhoodAnalysis.  # noqa: E501
        :type: bool
        """

        self._enable_skip_scan_when_process_voice_traffic = enable_skip_scan_when_process_voice_traffic

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
        if not isinstance(other, XiqRpNeighborhoodAnalysis):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRpNeighborhoodAnalysis):
            return True

        return self.to_dict() != other.to_dict()
