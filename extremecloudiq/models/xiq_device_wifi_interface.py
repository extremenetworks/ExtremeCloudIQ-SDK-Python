# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.2.0.39
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeviceWifiInterface(object):
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
        'frequency': 'str',
        'ssid_count': 'int',
        'client_count': 'int',
        'neighbor_clients': 'int',
        'channel_util': 'int',
        'channel': 'int',
        'channel_width': 'int',
        'tx_utilization': 'int',
        'rx_utilization': 'int',
        'tx_byte_count': 'int',
        'rx_byte_count': 'int',
        'noise_floor': 'int',
        'crc_error_frame': 'int',
        'tx_retry_frame': 'int',
        'rx_retry_frame': 'int',
        'unicast_tx_packet_count': 'int',
        'unicast_rx_packet_count': 'int',
        'broadcast_tx_packet_count': 'int',
        'broadcast_rx_packet_count': 'int',
        'tx_air_time': 'int',
        'rx_air_time': 'int',
        'total_utilization': 'int',
        'scan_avg_interference': 'int',
        'mac_address': 'str',
        'power': 'int',
        'rx_errors': 'int',
        'tx_errors': 'int',
        'interface_name': 'str',
        'radio_profile_name': 'str'
    }

    attribute_map = {
        'frequency': 'frequency',
        'ssid_count': 'ssid_count',
        'client_count': 'client_count',
        'neighbor_clients': 'neighbor_clients',
        'channel_util': 'channel_util',
        'channel': 'channel',
        'channel_width': 'channel_width',
        'tx_utilization': 'tx_utilization',
        'rx_utilization': 'rx_utilization',
        'tx_byte_count': 'tx_byte_count',
        'rx_byte_count': 'rx_byte_count',
        'noise_floor': 'noise_floor',
        'crc_error_frame': 'crc_error_frame',
        'tx_retry_frame': 'tx_retry_frame',
        'rx_retry_frame': 'rx_retry_frame',
        'unicast_tx_packet_count': 'unicast_tx_packet_count',
        'unicast_rx_packet_count': 'unicast_rx_packet_count',
        'broadcast_tx_packet_count': 'broadcast_tx_packet_count',
        'broadcast_rx_packet_count': 'broadcast_rx_packet_count',
        'tx_air_time': 'tx_air_time',
        'rx_air_time': 'rx_air_time',
        'total_utilization': 'total_utilization',
        'scan_avg_interference': 'scan_avg_interference',
        'mac_address': 'mac_address',
        'power': 'power',
        'rx_errors': 'rx_errors',
        'tx_errors': 'tx_errors',
        'interface_name': 'interface_name',
        'radio_profile_name': 'radio_profile_name'
    }

    def __init__(self, frequency=None, ssid_count=None, client_count=None, neighbor_clients=None, channel_util=None, channel=None, channel_width=None, tx_utilization=None, rx_utilization=None, tx_byte_count=None, rx_byte_count=None, noise_floor=None, crc_error_frame=None, tx_retry_frame=None, rx_retry_frame=None, unicast_tx_packet_count=None, unicast_rx_packet_count=None, broadcast_tx_packet_count=None, broadcast_rx_packet_count=None, tx_air_time=None, rx_air_time=None, total_utilization=None, scan_avg_interference=None, mac_address=None, power=None, rx_errors=None, tx_errors=None, interface_name=None, radio_profile_name=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeviceWifiInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._frequency = None
        self._ssid_count = None
        self._client_count = None
        self._neighbor_clients = None
        self._channel_util = None
        self._channel = None
        self._channel_width = None
        self._tx_utilization = None
        self._rx_utilization = None
        self._tx_byte_count = None
        self._rx_byte_count = None
        self._noise_floor = None
        self._crc_error_frame = None
        self._tx_retry_frame = None
        self._rx_retry_frame = None
        self._unicast_tx_packet_count = None
        self._unicast_rx_packet_count = None
        self._broadcast_tx_packet_count = None
        self._broadcast_rx_packet_count = None
        self._tx_air_time = None
        self._rx_air_time = None
        self._total_utilization = None
        self._scan_avg_interference = None
        self._mac_address = None
        self._power = None
        self._rx_errors = None
        self._tx_errors = None
        self._interface_name = None
        self._radio_profile_name = None
        self.discriminator = None

        if frequency is not None:
            self.frequency = frequency
        if ssid_count is not None:
            self.ssid_count = ssid_count
        if client_count is not None:
            self.client_count = client_count
        if neighbor_clients is not None:
            self.neighbor_clients = neighbor_clients
        if channel_util is not None:
            self.channel_util = channel_util
        if channel is not None:
            self.channel = channel
        if channel_width is not None:
            self.channel_width = channel_width
        if tx_utilization is not None:
            self.tx_utilization = tx_utilization
        if rx_utilization is not None:
            self.rx_utilization = rx_utilization
        if tx_byte_count is not None:
            self.tx_byte_count = tx_byte_count
        if rx_byte_count is not None:
            self.rx_byte_count = rx_byte_count
        if noise_floor is not None:
            self.noise_floor = noise_floor
        if crc_error_frame is not None:
            self.crc_error_frame = crc_error_frame
        if tx_retry_frame is not None:
            self.tx_retry_frame = tx_retry_frame
        if rx_retry_frame is not None:
            self.rx_retry_frame = rx_retry_frame
        if unicast_tx_packet_count is not None:
            self.unicast_tx_packet_count = unicast_tx_packet_count
        if unicast_rx_packet_count is not None:
            self.unicast_rx_packet_count = unicast_rx_packet_count
        if broadcast_tx_packet_count is not None:
            self.broadcast_tx_packet_count = broadcast_tx_packet_count
        if broadcast_rx_packet_count is not None:
            self.broadcast_rx_packet_count = broadcast_rx_packet_count
        if tx_air_time is not None:
            self.tx_air_time = tx_air_time
        if rx_air_time is not None:
            self.rx_air_time = rx_air_time
        if total_utilization is not None:
            self.total_utilization = total_utilization
        if scan_avg_interference is not None:
            self.scan_avg_interference = scan_avg_interference
        if mac_address is not None:
            self.mac_address = mac_address
        if power is not None:
            self.power = power
        if rx_errors is not None:
            self.rx_errors = rx_errors
        if tx_errors is not None:
            self.tx_errors = tx_errors
        if interface_name is not None:
            self.interface_name = interface_name
        if radio_profile_name is not None:
            self.radio_profile_name = radio_profile_name

    @property
    def frequency(self):
        """Gets the frequency of this XiqDeviceWifiInterface.  # noqa: E501

        The WiFi frequency.  # noqa: E501

        :return: The frequency of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this XiqDeviceWifiInterface.

        The WiFi frequency.  # noqa: E501

        :param frequency: The frequency of this XiqDeviceWifiInterface.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def ssid_count(self):
        """Gets the ssid_count of this XiqDeviceWifiInterface.  # noqa: E501

        The number of SSID assigned on this wireless interface.  # noqa: E501

        :return: The ssid_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._ssid_count

    @ssid_count.setter
    def ssid_count(self, ssid_count):
        """Sets the ssid_count of this XiqDeviceWifiInterface.

        The number of SSID assigned on this wireless interface.  # noqa: E501

        :param ssid_count: The ssid_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._ssid_count = ssid_count

    @property
    def client_count(self):
        """Gets the client_count of this XiqDeviceWifiInterface.  # noqa: E501

        The number of clients associated to this wireless interface.  # noqa: E501

        :return: The client_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._client_count

    @client_count.setter
    def client_count(self, client_count):
        """Sets the client_count of this XiqDeviceWifiInterface.

        The number of clients associated to this wireless interface.  # noqa: E501

        :param client_count: The client_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._client_count = client_count

    @property
    def neighbor_clients(self):
        """Gets the neighbor_clients of this XiqDeviceWifiInterface.  # noqa: E501

        The number of neighboring clients.  # noqa: E501

        :return: The neighbor_clients of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._neighbor_clients

    @neighbor_clients.setter
    def neighbor_clients(self, neighbor_clients):
        """Sets the neighbor_clients of this XiqDeviceWifiInterface.

        The number of neighboring clients.  # noqa: E501

        :param neighbor_clients: The neighbor_clients of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._neighbor_clients = neighbor_clients

    @property
    def channel_util(self):
        """Gets the channel_util of this XiqDeviceWifiInterface.  # noqa: E501

        The channel utilization.  # noqa: E501

        :return: The channel_util of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._channel_util

    @channel_util.setter
    def channel_util(self, channel_util):
        """Sets the channel_util of this XiqDeviceWifiInterface.

        The channel utilization.  # noqa: E501

        :param channel_util: The channel_util of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._channel_util = channel_util

    @property
    def channel(self):
        """Gets the channel of this XiqDeviceWifiInterface.  # noqa: E501

        The channel associated.  # noqa: E501

        :return: The channel of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this XiqDeviceWifiInterface.

        The channel associated.  # noqa: E501

        :param channel: The channel of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def channel_width(self):
        """Gets the channel_width of this XiqDeviceWifiInterface.  # noqa: E501

        The channel width.  # noqa: E501

        :return: The channel_width of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._channel_width

    @channel_width.setter
    def channel_width(self, channel_width):
        """Sets the channel_width of this XiqDeviceWifiInterface.

        The channel width.  # noqa: E501

        :param channel_width: The channel_width of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._channel_width = channel_width

    @property
    def tx_utilization(self):
        """Gets the tx_utilization of this XiqDeviceWifiInterface.  # noqa: E501

        The total tx utilization.  # noqa: E501

        :return: The tx_utilization of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._tx_utilization

    @tx_utilization.setter
    def tx_utilization(self, tx_utilization):
        """Sets the tx_utilization of this XiqDeviceWifiInterface.

        The total tx utilization.  # noqa: E501

        :param tx_utilization: The tx_utilization of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._tx_utilization = tx_utilization

    @property
    def rx_utilization(self):
        """Gets the rx_utilization of this XiqDeviceWifiInterface.  # noqa: E501

        The total rx utilization.  # noqa: E501

        :return: The rx_utilization of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._rx_utilization

    @rx_utilization.setter
    def rx_utilization(self, rx_utilization):
        """Sets the rx_utilization of this XiqDeviceWifiInterface.

        The total rx utilization.  # noqa: E501

        :param rx_utilization: The rx_utilization of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._rx_utilization = rx_utilization

    @property
    def tx_byte_count(self):
        """Gets the tx_byte_count of this XiqDeviceWifiInterface.  # noqa: E501

        The total tx byte count.  # noqa: E501

        :return: The tx_byte_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._tx_byte_count

    @tx_byte_count.setter
    def tx_byte_count(self, tx_byte_count):
        """Sets the tx_byte_count of this XiqDeviceWifiInterface.

        The total tx byte count.  # noqa: E501

        :param tx_byte_count: The tx_byte_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._tx_byte_count = tx_byte_count

    @property
    def rx_byte_count(self):
        """Gets the rx_byte_count of this XiqDeviceWifiInterface.  # noqa: E501

        The total rx byte count.  # noqa: E501

        :return: The rx_byte_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._rx_byte_count

    @rx_byte_count.setter
    def rx_byte_count(self, rx_byte_count):
        """Sets the rx_byte_count of this XiqDeviceWifiInterface.

        The total rx byte count.  # noqa: E501

        :param rx_byte_count: The rx_byte_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._rx_byte_count = rx_byte_count

    @property
    def noise_floor(self):
        """Gets the noise_floor of this XiqDeviceWifiInterface.  # noqa: E501

        The noise floor.  # noqa: E501

        :return: The noise_floor of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._noise_floor

    @noise_floor.setter
    def noise_floor(self, noise_floor):
        """Sets the noise_floor of this XiqDeviceWifiInterface.

        The noise floor.  # noqa: E501

        :param noise_floor: The noise_floor of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._noise_floor = noise_floor

    @property
    def crc_error_frame(self):
        """Gets the crc_error_frame of this XiqDeviceWifiInterface.  # noqa: E501

        The crc error frame count.  # noqa: E501

        :return: The crc_error_frame of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._crc_error_frame

    @crc_error_frame.setter
    def crc_error_frame(self, crc_error_frame):
        """Sets the crc_error_frame of this XiqDeviceWifiInterface.

        The crc error frame count.  # noqa: E501

        :param crc_error_frame: The crc_error_frame of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._crc_error_frame = crc_error_frame

    @property
    def tx_retry_frame(self):
        """Gets the tx_retry_frame of this XiqDeviceWifiInterface.  # noqa: E501

        The tx retry frame  # noqa: E501

        :return: The tx_retry_frame of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._tx_retry_frame

    @tx_retry_frame.setter
    def tx_retry_frame(self, tx_retry_frame):
        """Sets the tx_retry_frame of this XiqDeviceWifiInterface.

        The tx retry frame  # noqa: E501

        :param tx_retry_frame: The tx_retry_frame of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._tx_retry_frame = tx_retry_frame

    @property
    def rx_retry_frame(self):
        """Gets the rx_retry_frame of this XiqDeviceWifiInterface.  # noqa: E501

        The rx retry fram.  # noqa: E501

        :return: The rx_retry_frame of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._rx_retry_frame

    @rx_retry_frame.setter
    def rx_retry_frame(self, rx_retry_frame):
        """Sets the rx_retry_frame of this XiqDeviceWifiInterface.

        The rx retry fram.  # noqa: E501

        :param rx_retry_frame: The rx_retry_frame of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._rx_retry_frame = rx_retry_frame

    @property
    def unicast_tx_packet_count(self):
        """Gets the unicast_tx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501

        The unicast tx packet count.  # noqa: E501

        :return: The unicast_tx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._unicast_tx_packet_count

    @unicast_tx_packet_count.setter
    def unicast_tx_packet_count(self, unicast_tx_packet_count):
        """Sets the unicast_tx_packet_count of this XiqDeviceWifiInterface.

        The unicast tx packet count.  # noqa: E501

        :param unicast_tx_packet_count: The unicast_tx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._unicast_tx_packet_count = unicast_tx_packet_count

    @property
    def unicast_rx_packet_count(self):
        """Gets the unicast_rx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501

        The unicast rx packet count.  # noqa: E501

        :return: The unicast_rx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._unicast_rx_packet_count

    @unicast_rx_packet_count.setter
    def unicast_rx_packet_count(self, unicast_rx_packet_count):
        """Sets the unicast_rx_packet_count of this XiqDeviceWifiInterface.

        The unicast rx packet count.  # noqa: E501

        :param unicast_rx_packet_count: The unicast_rx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._unicast_rx_packet_count = unicast_rx_packet_count

    @property
    def broadcast_tx_packet_count(self):
        """Gets the broadcast_tx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501

        The broadcast tx packet count.  # noqa: E501

        :return: The broadcast_tx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._broadcast_tx_packet_count

    @broadcast_tx_packet_count.setter
    def broadcast_tx_packet_count(self, broadcast_tx_packet_count):
        """Sets the broadcast_tx_packet_count of this XiqDeviceWifiInterface.

        The broadcast tx packet count.  # noqa: E501

        :param broadcast_tx_packet_count: The broadcast_tx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._broadcast_tx_packet_count = broadcast_tx_packet_count

    @property
    def broadcast_rx_packet_count(self):
        """Gets the broadcast_rx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501

        The broadcast rx packet count.  # noqa: E501

        :return: The broadcast_rx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._broadcast_rx_packet_count

    @broadcast_rx_packet_count.setter
    def broadcast_rx_packet_count(self, broadcast_rx_packet_count):
        """Sets the broadcast_rx_packet_count of this XiqDeviceWifiInterface.

        The broadcast rx packet count.  # noqa: E501

        :param broadcast_rx_packet_count: The broadcast_rx_packet_count of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._broadcast_rx_packet_count = broadcast_rx_packet_count

    @property
    def tx_air_time(self):
        """Gets the tx_air_time of this XiqDeviceWifiInterface.  # noqa: E501

        The tx air time.  # noqa: E501

        :return: The tx_air_time of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._tx_air_time

    @tx_air_time.setter
    def tx_air_time(self, tx_air_time):
        """Sets the tx_air_time of this XiqDeviceWifiInterface.

        The tx air time.  # noqa: E501

        :param tx_air_time: The tx_air_time of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._tx_air_time = tx_air_time

    @property
    def rx_air_time(self):
        """Gets the rx_air_time of this XiqDeviceWifiInterface.  # noqa: E501

        The rx air time.  # noqa: E501

        :return: The rx_air_time of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._rx_air_time

    @rx_air_time.setter
    def rx_air_time(self, rx_air_time):
        """Sets the rx_air_time of this XiqDeviceWifiInterface.

        The rx air time.  # noqa: E501

        :param rx_air_time: The rx_air_time of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._rx_air_time = rx_air_time

    @property
    def total_utilization(self):
        """Gets the total_utilization of this XiqDeviceWifiInterface.  # noqa: E501

        The total utilization.  # noqa: E501

        :return: The total_utilization of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._total_utilization

    @total_utilization.setter
    def total_utilization(self, total_utilization):
        """Sets the total_utilization of this XiqDeviceWifiInterface.

        The total utilization.  # noqa: E501

        :param total_utilization: The total_utilization of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._total_utilization = total_utilization

    @property
    def scan_avg_interference(self):
        """Gets the scan_avg_interference of this XiqDeviceWifiInterface.  # noqa: E501

        The average interference.  # noqa: E501

        :return: The scan_avg_interference of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._scan_avg_interference

    @scan_avg_interference.setter
    def scan_avg_interference(self, scan_avg_interference):
        """Sets the scan_avg_interference of this XiqDeviceWifiInterface.

        The average interference.  # noqa: E501

        :param scan_avg_interference: The scan_avg_interference of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._scan_avg_interference = scan_avg_interference

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqDeviceWifiInterface.  # noqa: E501

        The bssid.  # noqa: E501

        :return: The mac_address of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqDeviceWifiInterface.

        The bssid.  # noqa: E501

        :param mac_address: The mac_address of this XiqDeviceWifiInterface.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def power(self):
        """Gets the power of this XiqDeviceWifiInterface.  # noqa: E501

        The radio power.  # noqa: E501

        :return: The power of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this XiqDeviceWifiInterface.

        The radio power.  # noqa: E501

        :param power: The power of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._power = power

    @property
    def rx_errors(self):
        """Gets the rx_errors of this XiqDeviceWifiInterface.  # noqa: E501

        The rx errors.  # noqa: E501

        :return: The rx_errors of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._rx_errors

    @rx_errors.setter
    def rx_errors(self, rx_errors):
        """Sets the rx_errors of this XiqDeviceWifiInterface.

        The rx errors.  # noqa: E501

        :param rx_errors: The rx_errors of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._rx_errors = rx_errors

    @property
    def tx_errors(self):
        """Gets the tx_errors of this XiqDeviceWifiInterface.  # noqa: E501

        The tx errors.  # noqa: E501

        :return: The tx_errors of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: int
        """
        return self._tx_errors

    @tx_errors.setter
    def tx_errors(self, tx_errors):
        """Sets the tx_errors of this XiqDeviceWifiInterface.

        The tx errors.  # noqa: E501

        :param tx_errors: The tx_errors of this XiqDeviceWifiInterface.  # noqa: E501
        :type: int
        """

        self._tx_errors = tx_errors

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqDeviceWifiInterface.  # noqa: E501

        The interface name.  # noqa: E501

        :return: The interface_name of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqDeviceWifiInterface.

        The interface name.  # noqa: E501

        :param interface_name: The interface_name of this XiqDeviceWifiInterface.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def radio_profile_name(self):
        """Gets the radio_profile_name of this XiqDeviceWifiInterface.  # noqa: E501

        The ExtremecloudIQ radio profile name.  # noqa: E501

        :return: The radio_profile_name of this XiqDeviceWifiInterface.  # noqa: E501
        :rtype: str
        """
        return self._radio_profile_name

    @radio_profile_name.setter
    def radio_profile_name(self, radio_profile_name):
        """Sets the radio_profile_name of this XiqDeviceWifiInterface.

        The ExtremecloudIQ radio profile name.  # noqa: E501

        :param radio_profile_name: The radio_profile_name of this XiqDeviceWifiInterface.  # noqa: E501
        :type: str
        """

        self._radio_profile_name = radio_profile_name

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
        if not isinstance(other, XiqDeviceWifiInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeviceWifiInterface):
            return True

        return self.to_dict() != other.to_dict()
