# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateRpNeighborhoodAnalysisRequest(object):
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
        'enable_background_scan': 'bool',
        'background_scan_interval': 'int',
        'enable_skip_scan_when_clients_connected': 'bool',
        'enable_skip_scan_when_clients_in_power_save_mode': 'bool',
        'enable_skip_scan_when_process_voice_traffic': 'bool'
    }

    attribute_map = {
        'enable_background_scan': 'enable_background_scan',
        'background_scan_interval': 'background_scan_interval',
        'enable_skip_scan_when_clients_connected': 'enable_skip_scan_when_clients_connected',
        'enable_skip_scan_when_clients_in_power_save_mode': 'enable_skip_scan_when_clients_in_power_save_mode',
        'enable_skip_scan_when_process_voice_traffic': 'enable_skip_scan_when_process_voice_traffic'
    }

    def __init__(self, enable_background_scan=None, background_scan_interval=None, enable_skip_scan_when_clients_connected=None, enable_skip_scan_when_clients_in_power_save_mode=None, enable_skip_scan_when_process_voice_traffic=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateRpNeighborhoodAnalysisRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_background_scan = None
        self._background_scan_interval = None
        self._enable_skip_scan_when_clients_connected = None
        self._enable_skip_scan_when_clients_in_power_save_mode = None
        self._enable_skip_scan_when_process_voice_traffic = None
        self.discriminator = None

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
    def enable_background_scan(self):
        """Gets the enable_background_scan of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501

        Whether background scan of neighboring devices is enabled  # noqa: E501

        :return: The enable_background_scan of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_background_scan

    @enable_background_scan.setter
    def enable_background_scan(self, enable_background_scan):
        """Sets the enable_background_scan of this XiqUpdateRpNeighborhoodAnalysisRequest.

        Whether background scan of neighboring devices is enabled  # noqa: E501

        :param enable_background_scan: The enable_background_scan of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :type: bool
        """

        self._enable_background_scan = enable_background_scan

    @property
    def background_scan_interval(self):
        """Gets the background_scan_interval of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501

        The background scan interval in the range of 1 to 1440 minutes  # noqa: E501

        :return: The background_scan_interval of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :rtype: int
        """
        return self._background_scan_interval

    @background_scan_interval.setter
    def background_scan_interval(self, background_scan_interval):
        """Sets the background_scan_interval of this XiqUpdateRpNeighborhoodAnalysisRequest.

        The background scan interval in the range of 1 to 1440 minutes  # noqa: E501

        :param background_scan_interval: The background_scan_interval of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                background_scan_interval is not None and background_scan_interval > 1440):  # noqa: E501
            raise ValueError("Invalid value for `background_scan_interval`, must be a value less than or equal to `1440`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                background_scan_interval is not None and background_scan_interval < 1):  # noqa: E501
            raise ValueError("Invalid value for `background_scan_interval`, must be a value greater than or equal to `1`")  # noqa: E501

        self._background_scan_interval = background_scan_interval

    @property
    def enable_skip_scan_when_clients_connected(self):
        """Gets the enable_skip_scan_when_clients_connected of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501

        Whether to skip background scan when devices have client connections  # noqa: E501

        :return: The enable_skip_scan_when_clients_connected of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_skip_scan_when_clients_connected

    @enable_skip_scan_when_clients_connected.setter
    def enable_skip_scan_when_clients_connected(self, enable_skip_scan_when_clients_connected):
        """Sets the enable_skip_scan_when_clients_connected of this XiqUpdateRpNeighborhoodAnalysisRequest.

        Whether to skip background scan when devices have client connections  # noqa: E501

        :param enable_skip_scan_when_clients_connected: The enable_skip_scan_when_clients_connected of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :type: bool
        """

        self._enable_skip_scan_when_clients_connected = enable_skip_scan_when_clients_connected

    @property
    def enable_skip_scan_when_clients_in_power_save_mode(self):
        """Gets the enable_skip_scan_when_clients_in_power_save_mode of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501

        Whether to skip background scan when connected devices are in power save mode  # noqa: E501

        :return: The enable_skip_scan_when_clients_in_power_save_mode of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_skip_scan_when_clients_in_power_save_mode

    @enable_skip_scan_when_clients_in_power_save_mode.setter
    def enable_skip_scan_when_clients_in_power_save_mode(self, enable_skip_scan_when_clients_in_power_save_mode):
        """Sets the enable_skip_scan_when_clients_in_power_save_mode of this XiqUpdateRpNeighborhoodAnalysisRequest.

        Whether to skip background scan when connected devices are in power save mode  # noqa: E501

        :param enable_skip_scan_when_clients_in_power_save_mode: The enable_skip_scan_when_clients_in_power_save_mode of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :type: bool
        """

        self._enable_skip_scan_when_clients_in_power_save_mode = enable_skip_scan_when_clients_in_power_save_mode

    @property
    def enable_skip_scan_when_process_voice_traffic(self):
        """Gets the enable_skip_scan_when_process_voice_traffic of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501

        Whether to skip background scan when devices have network traffic with voice priority  # noqa: E501

        :return: The enable_skip_scan_when_process_voice_traffic of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_skip_scan_when_process_voice_traffic

    @enable_skip_scan_when_process_voice_traffic.setter
    def enable_skip_scan_when_process_voice_traffic(self, enable_skip_scan_when_process_voice_traffic):
        """Sets the enable_skip_scan_when_process_voice_traffic of this XiqUpdateRpNeighborhoodAnalysisRequest.

        Whether to skip background scan when devices have network traffic with voice priority  # noqa: E501

        :param enable_skip_scan_when_process_voice_traffic: The enable_skip_scan_when_process_voice_traffic of this XiqUpdateRpNeighborhoodAnalysisRequest.  # noqa: E501
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
        if not isinstance(other, XiqUpdateRpNeighborhoodAnalysisRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateRpNeighborhoodAnalysisRequest):
            return True

        return self.to_dict() != other.to_dict()
