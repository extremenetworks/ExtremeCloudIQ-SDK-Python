# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.3.1.13
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqRpChannelSelection(object):
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
        'enable_dynamic_channel_switching': 'bool',
        'channel_width': 'str',
        'enable_dynamic_frequency_selection': 'bool',
        'enable_static_channel': 'bool',
        'enable_zero_wait_dfs': 'bool',
        'enable_use_last_selection': 'bool',
        'exclude_channels': 'str',
        'exclude_channels_width': 'str',
        'channel': 'int',
        'enable_limit_channel_selection': 'bool',
        'channel_region': 'str',
        'channel_model': 'int',
        'channels': 'str',
        'enable_channel_auto_selection': 'bool',
        'channel_selection_start_time': 'str',
        'channel_selection_end_time': 'str',
        'enable_avoid_switch_channel_if_clients_connected': 'bool',
        'channel_selection_max_clients': 'int',
        'enable_switch_channel_if_exceed_threshold': 'bool',
        'rf_interference_threshold': 'int',
        'crc_error_threshold': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enable_dynamic_channel_switching': 'enable_dynamic_channel_switching',
        'channel_width': 'channel_width',
        'enable_dynamic_frequency_selection': 'enable_dynamic_frequency_selection',
        'enable_static_channel': 'enable_static_channel',
        'enable_zero_wait_dfs': 'enable_zero_wait_dfs',
        'enable_use_last_selection': 'enable_use_last_selection',
        'exclude_channels': 'exclude_channels',
        'exclude_channels_width': 'exclude_channels_width',
        'channel': 'channel',
        'enable_limit_channel_selection': 'enable_limit_channel_selection',
        'channel_region': 'channel_region',
        'channel_model': 'channel_model',
        'channels': 'channels',
        'enable_channel_auto_selection': 'enable_channel_auto_selection',
        'channel_selection_start_time': 'channel_selection_start_time',
        'channel_selection_end_time': 'channel_selection_end_time',
        'enable_avoid_switch_channel_if_clients_connected': 'enable_avoid_switch_channel_if_clients_connected',
        'channel_selection_max_clients': 'channel_selection_max_clients',
        'enable_switch_channel_if_exceed_threshold': 'enable_switch_channel_if_exceed_threshold',
        'rf_interference_threshold': 'rf_interference_threshold',
        'crc_error_threshold': 'crc_error_threshold'
    }

    def __init__(self, id=None, create_time=None, update_time=None, enable_dynamic_channel_switching=None, channel_width=None, enable_dynamic_frequency_selection=None, enable_static_channel=None, enable_zero_wait_dfs=None, enable_use_last_selection=None, exclude_channels=None, exclude_channels_width=None, channel=None, enable_limit_channel_selection=None, channel_region=None, channel_model=None, channels=None, enable_channel_auto_selection=None, channel_selection_start_time=None, channel_selection_end_time=None, enable_avoid_switch_channel_if_clients_connected=None, channel_selection_max_clients=None, enable_switch_channel_if_exceed_threshold=None, rf_interference_threshold=None, crc_error_threshold=None, local_vars_configuration=None):  # noqa: E501
        """XiqRpChannelSelection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._enable_dynamic_channel_switching = None
        self._channel_width = None
        self._enable_dynamic_frequency_selection = None
        self._enable_static_channel = None
        self._enable_zero_wait_dfs = None
        self._enable_use_last_selection = None
        self._exclude_channels = None
        self._exclude_channels_width = None
        self._channel = None
        self._enable_limit_channel_selection = None
        self._channel_region = None
        self._channel_model = None
        self._channels = None
        self._enable_channel_auto_selection = None
        self._channel_selection_start_time = None
        self._channel_selection_end_time = None
        self._enable_avoid_switch_channel_if_clients_connected = None
        self._channel_selection_max_clients = None
        self._enable_switch_channel_if_exceed_threshold = None
        self._rf_interference_threshold = None
        self._crc_error_threshold = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if enable_dynamic_channel_switching is not None:
            self.enable_dynamic_channel_switching = enable_dynamic_channel_switching
        if channel_width is not None:
            self.channel_width = channel_width
        if enable_dynamic_frequency_selection is not None:
            self.enable_dynamic_frequency_selection = enable_dynamic_frequency_selection
        if enable_static_channel is not None:
            self.enable_static_channel = enable_static_channel
        if enable_zero_wait_dfs is not None:
            self.enable_zero_wait_dfs = enable_zero_wait_dfs
        if enable_use_last_selection is not None:
            self.enable_use_last_selection = enable_use_last_selection
        if exclude_channels is not None:
            self.exclude_channels = exclude_channels
        if exclude_channels_width is not None:
            self.exclude_channels_width = exclude_channels_width
        if channel is not None:
            self.channel = channel
        if enable_limit_channel_selection is not None:
            self.enable_limit_channel_selection = enable_limit_channel_selection
        if channel_region is not None:
            self.channel_region = channel_region
        if channel_model is not None:
            self.channel_model = channel_model
        if channels is not None:
            self.channels = channels
        if enable_channel_auto_selection is not None:
            self.enable_channel_auto_selection = enable_channel_auto_selection
        if channel_selection_start_time is not None:
            self.channel_selection_start_time = channel_selection_start_time
        if channel_selection_end_time is not None:
            self.channel_selection_end_time = channel_selection_end_time
        if enable_avoid_switch_channel_if_clients_connected is not None:
            self.enable_avoid_switch_channel_if_clients_connected = enable_avoid_switch_channel_if_clients_connected
        if channel_selection_max_clients is not None:
            self.channel_selection_max_clients = channel_selection_max_clients
        if enable_switch_channel_if_exceed_threshold is not None:
            self.enable_switch_channel_if_exceed_threshold = enable_switch_channel_if_exceed_threshold
        if rf_interference_threshold is not None:
            self.rf_interference_threshold = rf_interference_threshold
        if crc_error_threshold is not None:
            self.crc_error_threshold = crc_error_threshold

    @property
    def id(self):
        """Gets the id of this XiqRpChannelSelection.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRpChannelSelection.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRpChannelSelection.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRpChannelSelection.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRpChannelSelection.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRpChannelSelection.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRpChannelSelection.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRpChannelSelection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRpChannelSelection.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRpChannelSelection.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRpChannelSelection.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRpChannelSelection.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def enable_dynamic_channel_switching(self):
        """Gets the enable_dynamic_channel_switching of this XiqRpChannelSelection.  # noqa: E501

        Whether to dynamically select and switch channels based on the defined criteria.  # noqa: E501

        :return: The enable_dynamic_channel_switching of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dynamic_channel_switching

    @enable_dynamic_channel_switching.setter
    def enable_dynamic_channel_switching(self, enable_dynamic_channel_switching):
        """Sets the enable_dynamic_channel_switching of this XiqRpChannelSelection.

        Whether to dynamically select and switch channels based on the defined criteria.  # noqa: E501

        :param enable_dynamic_channel_switching: The enable_dynamic_channel_switching of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_dynamic_channel_switching = enable_dynamic_channel_switching

    @property
    def channel_width(self):
        """Gets the channel_width of this XiqRpChannelSelection.  # noqa: E501

        The channel frequency range  # noqa: E501

        :return: The channel_width of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._channel_width

    @channel_width.setter
    def channel_width(self, channel_width):
        """Sets the channel_width of this XiqRpChannelSelection.

        The channel frequency range  # noqa: E501

        :param channel_width: The channel_width of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._channel_width = channel_width

    @property
    def enable_dynamic_frequency_selection(self):
        """Gets the enable_dynamic_frequency_selection of this XiqRpChannelSelection.  # noqa: E501

        Whether dynamic frequency selection is enabled (a/n, a, ac mode)  # noqa: E501

        :return: The enable_dynamic_frequency_selection of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dynamic_frequency_selection

    @enable_dynamic_frequency_selection.setter
    def enable_dynamic_frequency_selection(self, enable_dynamic_frequency_selection):
        """Sets the enable_dynamic_frequency_selection of this XiqRpChannelSelection.

        Whether dynamic frequency selection is enabled (a/n, a, ac mode)  # noqa: E501

        :param enable_dynamic_frequency_selection: The enable_dynamic_frequency_selection of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_dynamic_frequency_selection = enable_dynamic_frequency_selection

    @property
    def enable_static_channel(self):
        """Gets the enable_static_channel of this XiqRpChannelSelection.  # noqa: E501

        Whether static channel is enabled (manual channel selection return)  # noqa: E501

        :return: The enable_static_channel of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_static_channel

    @enable_static_channel.setter
    def enable_static_channel(self, enable_static_channel):
        """Sets the enable_static_channel of this XiqRpChannelSelection.

        Whether static channel is enabled (manual channel selection return)  # noqa: E501

        :param enable_static_channel: The enable_static_channel of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_static_channel = enable_static_channel

    @property
    def enable_zero_wait_dfs(self):
        """Gets the enable_zero_wait_dfs of this XiqRpChannelSelection.  # noqa: E501

        Whether ZeroWait DFS is enabled  # noqa: E501

        :return: The enable_zero_wait_dfs of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_zero_wait_dfs

    @enable_zero_wait_dfs.setter
    def enable_zero_wait_dfs(self, enable_zero_wait_dfs):
        """Sets the enable_zero_wait_dfs of this XiqRpChannelSelection.

        Whether ZeroWait DFS is enabled  # noqa: E501

        :param enable_zero_wait_dfs: The enable_zero_wait_dfs of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_zero_wait_dfs = enable_zero_wait_dfs

    @property
    def enable_use_last_selection(self):
        """Gets the enable_use_last_selection of this XiqRpChannelSelection.  # noqa: E501

        Whether to use the last known power and channel during the AP boot up process  # noqa: E501

        :return: The enable_use_last_selection of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_use_last_selection

    @enable_use_last_selection.setter
    def enable_use_last_selection(self, enable_use_last_selection):
        """Sets the enable_use_last_selection of this XiqRpChannelSelection.

        Whether to use the last known power and channel during the AP boot up process  # noqa: E501

        :param enable_use_last_selection: The enable_use_last_selection of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_use_last_selection = enable_use_last_selection

    @property
    def exclude_channels(self):
        """Gets the exclude_channels of this XiqRpChannelSelection.  # noqa: E501

        The comma-separated list of excluded channels not on the selected channel width.  # noqa: E501

        :return: The exclude_channels of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._exclude_channels

    @exclude_channels.setter
    def exclude_channels(self, exclude_channels):
        """Sets the exclude_channels of this XiqRpChannelSelection.

        The comma-separated list of excluded channels not on the selected channel width.  # noqa: E501

        :param exclude_channels: The exclude_channels of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._exclude_channels = exclude_channels

    @property
    def exclude_channels_width(self):
        """Gets the exclude_channels_width of this XiqRpChannelSelection.  # noqa: E501

        The comma-separated list of excluded channels on the selected channel width.  # noqa: E501

        :return: The exclude_channels_width of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._exclude_channels_width

    @exclude_channels_width.setter
    def exclude_channels_width(self, exclude_channels_width):
        """Sets the exclude_channels_width of this XiqRpChannelSelection.

        The comma-separated list of excluded channels on the selected channel width.  # noqa: E501

        :param exclude_channels_width: The exclude_channels_width of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._exclude_channels_width = exclude_channels_width

    @property
    def channel(self):
        """Gets the channel of this XiqRpChannelSelection.  # noqa: E501

        The number of channel selections from 1 up to 165 or AUTO for default selection.  # noqa: E501

        :return: The channel of this XiqRpChannelSelection.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this XiqRpChannelSelection.

        The number of channel selections from 1 up to 165 or AUTO for default selection.  # noqa: E501

        :param channel: The channel of this XiqRpChannelSelection.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def enable_limit_channel_selection(self):
        """Gets the enable_limit_channel_selection of this XiqRpChannelSelection.  # noqa: E501

        Whether to allow for limiting the channel selection to non-overlapping channels. (b/g,g/n/, axes modes)  # noqa: E501

        :return: The enable_limit_channel_selection of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_limit_channel_selection

    @enable_limit_channel_selection.setter
    def enable_limit_channel_selection(self, enable_limit_channel_selection):
        """Sets the enable_limit_channel_selection of this XiqRpChannelSelection.

        Whether to allow for limiting the channel selection to non-overlapping channels. (b/g,g/n/, axes modes)  # noqa: E501

        :param enable_limit_channel_selection: The enable_limit_channel_selection of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_limit_channel_selection = enable_limit_channel_selection

    @property
    def channel_region(self):
        """Gets the channel_region of this XiqRpChannelSelection.  # noqa: E501

        The channel region -- \"USA\", \"Canada\", \"Europe\", or \"World\"  # noqa: E501

        :return: The channel_region of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._channel_region

    @channel_region.setter
    def channel_region(self, channel_region):
        """Sets the channel_region of this XiqRpChannelSelection.

        The channel region -- \"USA\", \"Canada\", \"Europe\", or \"World\"  # noqa: E501

        :param channel_region: The channel_region of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._channel_region = channel_region

    @property
    def channel_model(self):
        """Gets the channel_model of this XiqRpChannelSelection.  # noqa: E501

        The number of channel models to limit.  # noqa: E501

        :return: The channel_model of this XiqRpChannelSelection.  # noqa: E501
        :rtype: int
        """
        return self._channel_model

    @channel_model.setter
    def channel_model(self, channel_model):
        """Sets the channel_model of this XiqRpChannelSelection.

        The number of channel models to limit.  # noqa: E501

        :param channel_model: The channel_model of this XiqRpChannelSelection.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                channel_model is not None and channel_model > 4):  # noqa: E501
            raise ValueError("Invalid value for `channel_model`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                channel_model is not None and channel_model < 3):  # noqa: E501
            raise ValueError("Invalid value for `channel_model`, must be a value greater than or equal to `3`")  # noqa: E501

        self._channel_model = channel_model

    @property
    def channels(self):
        """Gets the channels of this XiqRpChannelSelection.  # noqa: E501

        The comma separated list of channels allowed channel switching  # noqa: E501

        :return: The channels of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this XiqRpChannelSelection.

        The comma separated list of channels allowed channel switching  # noqa: E501

        :param channels: The channels of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._channels = channels

    @property
    def enable_channel_auto_selection(self):
        """Gets the enable_channel_auto_selection of this XiqRpChannelSelection.  # noqa: E501

        Whether to enable automatic channel switching during specified time interval.  # noqa: E501

        :return: The enable_channel_auto_selection of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_channel_auto_selection

    @enable_channel_auto_selection.setter
    def enable_channel_auto_selection(self, enable_channel_auto_selection):
        """Sets the enable_channel_auto_selection of this XiqRpChannelSelection.

        Whether to enable automatic channel switching during specified time interval.  # noqa: E501

        :param enable_channel_auto_selection: The enable_channel_auto_selection of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_channel_auto_selection = enable_channel_auto_selection

    @property
    def channel_selection_start_time(self):
        """Gets the channel_selection_start_time of this XiqRpChannelSelection.  # noqa: E501

        The start time for channel switching in 24-hr time format of hh:mm  # noqa: E501

        :return: The channel_selection_start_time of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._channel_selection_start_time

    @channel_selection_start_time.setter
    def channel_selection_start_time(self, channel_selection_start_time):
        """Sets the channel_selection_start_time of this XiqRpChannelSelection.

        The start time for channel switching in 24-hr time format of hh:mm  # noqa: E501

        :param channel_selection_start_time: The channel_selection_start_time of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._channel_selection_start_time = channel_selection_start_time

    @property
    def channel_selection_end_time(self):
        """Gets the channel_selection_end_time of this XiqRpChannelSelection.  # noqa: E501

        The end time for channel switching in 24-hr time format of hh:mm  # noqa: E501

        :return: The channel_selection_end_time of this XiqRpChannelSelection.  # noqa: E501
        :rtype: str
        """
        return self._channel_selection_end_time

    @channel_selection_end_time.setter
    def channel_selection_end_time(self, channel_selection_end_time):
        """Sets the channel_selection_end_time of this XiqRpChannelSelection.

        The end time for channel switching in 24-hr time format of hh:mm  # noqa: E501

        :param channel_selection_end_time: The channel_selection_end_time of this XiqRpChannelSelection.  # noqa: E501
        :type: str
        """

        self._channel_selection_end_time = channel_selection_end_time

    @property
    def enable_avoid_switch_channel_if_clients_connected(self):
        """Gets the enable_avoid_switch_channel_if_clients_connected of this XiqRpChannelSelection.  # noqa: E501

        Whether to avoid channel switching if there are already max connected clients  # noqa: E501

        :return: The enable_avoid_switch_channel_if_clients_connected of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_avoid_switch_channel_if_clients_connected

    @enable_avoid_switch_channel_if_clients_connected.setter
    def enable_avoid_switch_channel_if_clients_connected(self, enable_avoid_switch_channel_if_clients_connected):
        """Sets the enable_avoid_switch_channel_if_clients_connected of this XiqRpChannelSelection.

        Whether to avoid channel switching if there are already max connected clients  # noqa: E501

        :param enable_avoid_switch_channel_if_clients_connected: The enable_avoid_switch_channel_if_clients_connected of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_avoid_switch_channel_if_clients_connected = enable_avoid_switch_channel_if_clients_connected

    @property
    def channel_selection_max_clients(self):
        """Gets the channel_selection_max_clients of this XiqRpChannelSelection.  # noqa: E501

        The maximum number of connected clients from 0 up to 100 to avoid switching  # noqa: E501

        :return: The channel_selection_max_clients of this XiqRpChannelSelection.  # noqa: E501
        :rtype: int
        """
        return self._channel_selection_max_clients

    @channel_selection_max_clients.setter
    def channel_selection_max_clients(self, channel_selection_max_clients):
        """Sets the channel_selection_max_clients of this XiqRpChannelSelection.

        The maximum number of connected clients from 0 up to 100 to avoid switching  # noqa: E501

        :param channel_selection_max_clients: The channel_selection_max_clients of this XiqRpChannelSelection.  # noqa: E501
        :type: int
        """

        self._channel_selection_max_clients = channel_selection_max_clients

    @property
    def enable_switch_channel_if_exceed_threshold(self):
        """Gets the enable_switch_channel_if_exceed_threshold of this XiqRpChannelSelection.  # noqa: E501

        Whether to enable channel switching when RF interference exceeds the threshold  # noqa: E501

        :return: The enable_switch_channel_if_exceed_threshold of this XiqRpChannelSelection.  # noqa: E501
        :rtype: bool
        """
        return self._enable_switch_channel_if_exceed_threshold

    @enable_switch_channel_if_exceed_threshold.setter
    def enable_switch_channel_if_exceed_threshold(self, enable_switch_channel_if_exceed_threshold):
        """Sets the enable_switch_channel_if_exceed_threshold of this XiqRpChannelSelection.

        Whether to enable channel switching when RF interference exceeds the threshold  # noqa: E501

        :param enable_switch_channel_if_exceed_threshold: The enable_switch_channel_if_exceed_threshold of this XiqRpChannelSelection.  # noqa: E501
        :type: bool
        """

        self._enable_switch_channel_if_exceed_threshold = enable_switch_channel_if_exceed_threshold

    @property
    def rf_interference_threshold(self):
        """Gets the rf_interference_threshold of this XiqRpChannelSelection.  # noqa: E501

        The RF interference threshold from 10 up to 80 for channel switching.  # noqa: E501

        :return: The rf_interference_threshold of this XiqRpChannelSelection.  # noqa: E501
        :rtype: int
        """
        return self._rf_interference_threshold

    @rf_interference_threshold.setter
    def rf_interference_threshold(self, rf_interference_threshold):
        """Sets the rf_interference_threshold of this XiqRpChannelSelection.

        The RF interference threshold from 10 up to 80 for channel switching.  # noqa: E501

        :param rf_interference_threshold: The rf_interference_threshold of this XiqRpChannelSelection.  # noqa: E501
        :type: int
        """

        self._rf_interference_threshold = rf_interference_threshold

    @property
    def crc_error_threshold(self):
        """Gets the crc_error_threshold of this XiqRpChannelSelection.  # noqa: E501

        The CRC error threshold from 10 up to 80 for channel switching.  # noqa: E501

        :return: The crc_error_threshold of this XiqRpChannelSelection.  # noqa: E501
        :rtype: int
        """
        return self._crc_error_threshold

    @crc_error_threshold.setter
    def crc_error_threshold(self, crc_error_threshold):
        """Sets the crc_error_threshold of this XiqRpChannelSelection.

        The CRC error threshold from 10 up to 80 for channel switching.  # noqa: E501

        :param crc_error_threshold: The crc_error_threshold of this XiqRpChannelSelection.  # noqa: E501
        :type: int
        """

        self._crc_error_threshold = crc_error_threshold

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
        if not isinstance(other, XiqRpChannelSelection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRpChannelSelection):
            return True

        return self.to_dict() != other.to_dict()
