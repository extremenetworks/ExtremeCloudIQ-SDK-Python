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


class XiqRadioProfile(object):
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
        'name': 'str',
        'predefined': 'bool',
        'description': 'str',
        'transmission_power': 'int',
        'max_transmit_power': 'int',
        'transmission_power_floor': 'int',
        'transmission_power_max_drop': 'int',
        'max_clients': 'int',
        'enable_client_transmission_power': 'bool',
        'client_transmission_power': 'int',
        'enable_ofdma': 'bool',
        'radio_mode': 'XiqRadioMode',
        'neighborhood_analysis_id': 'int',
        'channel_selection_id': 'int',
        'radio_usage_optimization_id': 'int',
        'miscellaneous_settings_id': 'int',
        'presence_server_settings_id': 'int',
        'sensor_scan_settings_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'predefined': 'predefined',
        'description': 'description',
        'transmission_power': 'transmission_power',
        'max_transmit_power': 'max_transmit_power',
        'transmission_power_floor': 'transmission_power_floor',
        'transmission_power_max_drop': 'transmission_power_max_drop',
        'max_clients': 'max_clients',
        'enable_client_transmission_power': 'enable_client_transmission_power',
        'client_transmission_power': 'client_transmission_power',
        'enable_ofdma': 'enable_ofdma',
        'radio_mode': 'radio_mode',
        'neighborhood_analysis_id': 'neighborhood_analysis_id',
        'channel_selection_id': 'channel_selection_id',
        'radio_usage_optimization_id': 'radio_usage_optimization_id',
        'miscellaneous_settings_id': 'miscellaneous_settings_id',
        'presence_server_settings_id': 'presence_server_settings_id',
        'sensor_scan_settings_id': 'sensor_scan_settings_id'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, predefined=None, description=None, transmission_power=None, max_transmit_power=None, transmission_power_floor=None, transmission_power_max_drop=None, max_clients=None, enable_client_transmission_power=None, client_transmission_power=None, enable_ofdma=None, radio_mode=None, neighborhood_analysis_id=None, channel_selection_id=None, radio_usage_optimization_id=None, miscellaneous_settings_id=None, presence_server_settings_id=None, sensor_scan_settings_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqRadioProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._predefined = None
        self._description = None
        self._transmission_power = None
        self._max_transmit_power = None
        self._transmission_power_floor = None
        self._transmission_power_max_drop = None
        self._max_clients = None
        self._enable_client_transmission_power = None
        self._client_transmission_power = None
        self._enable_ofdma = None
        self._radio_mode = None
        self._neighborhood_analysis_id = None
        self._channel_selection_id = None
        self._radio_usage_optimization_id = None
        self._miscellaneous_settings_id = None
        self._presence_server_settings_id = None
        self._sensor_scan_settings_id = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if name is not None:
            self.name = name
        if predefined is not None:
            self.predefined = predefined
        if description is not None:
            self.description = description
        if transmission_power is not None:
            self.transmission_power = transmission_power
        if max_transmit_power is not None:
            self.max_transmit_power = max_transmit_power
        if transmission_power_floor is not None:
            self.transmission_power_floor = transmission_power_floor
        if transmission_power_max_drop is not None:
            self.transmission_power_max_drop = transmission_power_max_drop
        if max_clients is not None:
            self.max_clients = max_clients
        if enable_client_transmission_power is not None:
            self.enable_client_transmission_power = enable_client_transmission_power
        if client_transmission_power is not None:
            self.client_transmission_power = client_transmission_power
        if enable_ofdma is not None:
            self.enable_ofdma = enable_ofdma
        if radio_mode is not None:
            self.radio_mode = radio_mode
        if neighborhood_analysis_id is not None:
            self.neighborhood_analysis_id = neighborhood_analysis_id
        if channel_selection_id is not None:
            self.channel_selection_id = channel_selection_id
        if radio_usage_optimization_id is not None:
            self.radio_usage_optimization_id = radio_usage_optimization_id
        if miscellaneous_settings_id is not None:
            self.miscellaneous_settings_id = miscellaneous_settings_id
        if presence_server_settings_id is not None:
            self.presence_server_settings_id = presence_server_settings_id
        if sensor_scan_settings_id is not None:
            self.sensor_scan_settings_id = sensor_scan_settings_id

    @property
    def id(self):
        """Gets the id of this XiqRadioProfile.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRadioProfile.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRadioProfile.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRadioProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRadioProfile.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRadioProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRadioProfile.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRadioProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRadioProfile.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRadioProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqRadioProfile.  # noqa: E501

        The radio profile name  # noqa: E501

        :return: The name of this XiqRadioProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqRadioProfile.

        The radio profile name  # noqa: E501

        :param name: The name of this XiqRadioProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def predefined(self):
        """Gets the predefined of this XiqRadioProfile.  # noqa: E501

        Whether the radio profile is predefined or user-customized.  # noqa: E501

        :return: The predefined of this XiqRadioProfile.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqRadioProfile.

        Whether the radio profile is predefined or user-customized.  # noqa: E501

        :param predefined: The predefined of this XiqRadioProfile.  # noqa: E501
        :type: bool
        """

        self._predefined = predefined

    @property
    def description(self):
        """Gets the description of this XiqRadioProfile.  # noqa: E501

        The radio profile description.  # noqa: E501

        :return: The description of this XiqRadioProfile.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqRadioProfile.

        The radio profile description.  # noqa: E501

        :param description: The description of this XiqRadioProfile.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def transmission_power(self):
        """Gets the transmission_power of this XiqRadioProfile.  # noqa: E501

        The transmission power floor from 1 up to 20 dBm or null for Auto.  # noqa: E501

        :return: The transmission_power of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._transmission_power

    @transmission_power.setter
    def transmission_power(self, transmission_power):
        """Sets the transmission_power of this XiqRadioProfile.

        The transmission power floor from 1 up to 20 dBm or null for Auto.  # noqa: E501

        :param transmission_power: The transmission_power of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._transmission_power = transmission_power

    @property
    def max_transmit_power(self):
        """Gets the max_transmit_power of this XiqRadioProfile.  # noqa: E501

        The maximum transmit power from 10 up to 20 dBm.  # noqa: E501

        :return: The max_transmit_power of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_transmit_power

    @max_transmit_power.setter
    def max_transmit_power(self, max_transmit_power):
        """Sets the max_transmit_power of this XiqRadioProfile.

        The maximum transmit power from 10 up to 20 dBm.  # noqa: E501

        :param max_transmit_power: The max_transmit_power of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._max_transmit_power = max_transmit_power

    @property
    def transmission_power_floor(self):
        """Gets the transmission_power_floor of this XiqRadioProfile.  # noqa: E501

        The transmission power floor from 2 up to 20 dBm.  # noqa: E501

        :return: The transmission_power_floor of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._transmission_power_floor

    @transmission_power_floor.setter
    def transmission_power_floor(self, transmission_power_floor):
        """Sets the transmission_power_floor of this XiqRadioProfile.

        The transmission power floor from 2 up to 20 dBm.  # noqa: E501

        :param transmission_power_floor: The transmission_power_floor of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._transmission_power_floor = transmission_power_floor

    @property
    def transmission_power_max_drop(self):
        """Gets the transmission_power_max_drop of this XiqRadioProfile.  # noqa: E501

        The transmission power max drop from 0 up to 18 dB.  # noqa: E501

        :return: The transmission_power_max_drop of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._transmission_power_max_drop

    @transmission_power_max_drop.setter
    def transmission_power_max_drop(self, transmission_power_max_drop):
        """Sets the transmission_power_max_drop of this XiqRadioProfile.

        The transmission power max drop from 0 up to 18 dB.  # noqa: E501

        :param transmission_power_max_drop: The transmission_power_max_drop of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._transmission_power_max_drop = transmission_power_max_drop

    @property
    def max_clients(self):
        """Gets the max_clients of this XiqRadioProfile.  # noqa: E501

        The maximum number of clients from 1 up to 255.  # noqa: E501

        :return: The max_clients of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._max_clients

    @max_clients.setter
    def max_clients(self, max_clients):
        """Sets the max_clients of this XiqRadioProfile.

        The maximum number of clients from 1 up to 255.  # noqa: E501

        :param max_clients: The max_clients of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._max_clients = max_clients

    @property
    def enable_client_transmission_power(self):
        """Gets the enable_client_transmission_power of this XiqRadioProfile.  # noqa: E501

        Whether or not client transmission power control (802.11h) is enabled.  # noqa: E501

        :return: The enable_client_transmission_power of this XiqRadioProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_client_transmission_power

    @enable_client_transmission_power.setter
    def enable_client_transmission_power(self, enable_client_transmission_power):
        """Sets the enable_client_transmission_power of this XiqRadioProfile.

        Whether or not client transmission power control (802.11h) is enabled.  # noqa: E501

        :param enable_client_transmission_power: The enable_client_transmission_power of this XiqRadioProfile.  # noqa: E501
        :type: bool
        """

        self._enable_client_transmission_power = enable_client_transmission_power

    @property
    def client_transmission_power(self):
        """Gets the client_transmission_power of this XiqRadioProfile.  # noqa: E501

        The client transmission power from 1 up to 20 dBm if it is enabled.  # noqa: E501

        :return: The client_transmission_power of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._client_transmission_power

    @client_transmission_power.setter
    def client_transmission_power(self, client_transmission_power):
        """Sets the client_transmission_power of this XiqRadioProfile.

        The client transmission power from 1 up to 20 dBm if it is enabled.  # noqa: E501

        :param client_transmission_power: The client_transmission_power of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._client_transmission_power = client_transmission_power

    @property
    def enable_ofdma(self):
        """Gets the enable_ofdma of this XiqRadioProfile.  # noqa: E501

        Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel.  # noqa: E501

        :return: The enable_ofdma of this XiqRadioProfile.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ofdma

    @enable_ofdma.setter
    def enable_ofdma(self, enable_ofdma):
        """Sets the enable_ofdma of this XiqRadioProfile.

        Whether to enable Orthogonal Frequency Division Multiple Access (802.11ax) for multiple-user access by subdividing a channel.  # noqa: E501

        :param enable_ofdma: The enable_ofdma of this XiqRadioProfile.  # noqa: E501
        :type: bool
        """

        self._enable_ofdma = enable_ofdma

    @property
    def radio_mode(self):
        """Gets the radio_mode of this XiqRadioProfile.  # noqa: E501


        :return: The radio_mode of this XiqRadioProfile.  # noqa: E501
        :rtype: XiqRadioMode
        """
        return self._radio_mode

    @radio_mode.setter
    def radio_mode(self, radio_mode):
        """Sets the radio_mode of this XiqRadioProfile.


        :param radio_mode: The radio_mode of this XiqRadioProfile.  # noqa: E501
        :type: XiqRadioMode
        """

        self._radio_mode = radio_mode

    @property
    def neighborhood_analysis_id(self):
        """Gets the neighborhood_analysis_id of this XiqRadioProfile.  # noqa: E501

        The neighborhood analysis Id.  # noqa: E501

        :return: The neighborhood_analysis_id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._neighborhood_analysis_id

    @neighborhood_analysis_id.setter
    def neighborhood_analysis_id(self, neighborhood_analysis_id):
        """Sets the neighborhood_analysis_id of this XiqRadioProfile.

        The neighborhood analysis Id.  # noqa: E501

        :param neighborhood_analysis_id: The neighborhood_analysis_id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._neighborhood_analysis_id = neighborhood_analysis_id

    @property
    def channel_selection_id(self):
        """Gets the channel_selection_id of this XiqRadioProfile.  # noqa: E501

        The channel selection Id.  # noqa: E501

        :return: The channel_selection_id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._channel_selection_id

    @channel_selection_id.setter
    def channel_selection_id(self, channel_selection_id):
        """Sets the channel_selection_id of this XiqRadioProfile.

        The channel selection Id.  # noqa: E501

        :param channel_selection_id: The channel_selection_id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._channel_selection_id = channel_selection_id

    @property
    def radio_usage_optimization_id(self):
        """Gets the radio_usage_optimization_id of this XiqRadioProfile.  # noqa: E501

        The radio usage optimization Id.  # noqa: E501

        :return: The radio_usage_optimization_id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._radio_usage_optimization_id

    @radio_usage_optimization_id.setter
    def radio_usage_optimization_id(self, radio_usage_optimization_id):
        """Sets the radio_usage_optimization_id of this XiqRadioProfile.

        The radio usage optimization Id.  # noqa: E501

        :param radio_usage_optimization_id: The radio_usage_optimization_id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._radio_usage_optimization_id = radio_usage_optimization_id

    @property
    def miscellaneous_settings_id(self):
        """Gets the miscellaneous_settings_id of this XiqRadioProfile.  # noqa: E501

        The miscellaneous settings Id  # noqa: E501

        :return: The miscellaneous_settings_id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._miscellaneous_settings_id

    @miscellaneous_settings_id.setter
    def miscellaneous_settings_id(self, miscellaneous_settings_id):
        """Sets the miscellaneous_settings_id of this XiqRadioProfile.

        The miscellaneous settings Id  # noqa: E501

        :param miscellaneous_settings_id: The miscellaneous_settings_id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._miscellaneous_settings_id = miscellaneous_settings_id

    @property
    def presence_server_settings_id(self):
        """Gets the presence_server_settings_id of this XiqRadioProfile.  # noqa: E501

        The presence server settings Id.  # noqa: E501

        :return: The presence_server_settings_id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._presence_server_settings_id

    @presence_server_settings_id.setter
    def presence_server_settings_id(self, presence_server_settings_id):
        """Sets the presence_server_settings_id of this XiqRadioProfile.

        The presence server settings Id.  # noqa: E501

        :param presence_server_settings_id: The presence_server_settings_id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._presence_server_settings_id = presence_server_settings_id

    @property
    def sensor_scan_settings_id(self):
        """Gets the sensor_scan_settings_id of this XiqRadioProfile.  # noqa: E501

        The sensor scan settings Id.  # noqa: E501

        :return: The sensor_scan_settings_id of this XiqRadioProfile.  # noqa: E501
        :rtype: int
        """
        return self._sensor_scan_settings_id

    @sensor_scan_settings_id.setter
    def sensor_scan_settings_id(self, sensor_scan_settings_id):
        """Sets the sensor_scan_settings_id of this XiqRadioProfile.

        The sensor scan settings Id.  # noqa: E501

        :param sensor_scan_settings_id: The sensor_scan_settings_id of this XiqRadioProfile.  # noqa: E501
        :type: int
        """

        self._sensor_scan_settings_id = sensor_scan_settings_id

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
        if not isinstance(other, XiqRadioProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRadioProfile):
            return True

        return self.to_dict() != other.to_dict()