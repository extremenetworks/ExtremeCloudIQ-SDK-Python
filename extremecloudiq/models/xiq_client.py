# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqClient(object):
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
        'org_id': 'int',
        'location_id': 'int',
        'device_id': 'int',
        'hostname': 'str',
        'mac_address': 'str',
        'ip_address': 'str',
        'ipv6_address': 'str',
        'os_type': 'str',
        'username': 'str',
        'user_profile_name': 'str',
        'connected': 'bool',
        'online_time': 'datetime',
        'offline_time': 'datetime',
        'vlan': 'int',
        'connection_type': 'int',
        'ssid': 'str',
        'port': 'str',
        'org_name': 'str',
        'device_function': 'int',
        'device_mac_address': 'str',
        'device_name': 'str',
        'auth': 'int',
        'channel': 'int',
        'client_health': 'int',
        'application_health': 'int',
        'radio_health': 'int',
        'network_health': 'int',
        'radio_type': 'int',
        'encryption_method': 'int',
        'interface_name': 'str',
        'bssid': 'str',
        'rssi': 'int',
        'snr': 'int',
        'description': 'str',
        'category': 'str',
        'mobility': 'str',
        'port_type_name': 'str',
        'wing_ap': 'bool',
        'vendor': 'str',
        'locations': 'list[XiqLocationLegend]',
        'product_type': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'location_id': 'location_id',
        'device_id': 'device_id',
        'hostname': 'hostname',
        'mac_address': 'mac_address',
        'ip_address': 'ip_address',
        'ipv6_address': 'ipv6_address',
        'os_type': 'os_type',
        'username': 'username',
        'user_profile_name': 'user_profile_name',
        'connected': 'connected',
        'online_time': 'online_time',
        'offline_time': 'offline_time',
        'vlan': 'vlan',
        'connection_type': 'connection_type',
        'ssid': 'ssid',
        'port': 'port',
        'org_name': 'org_name',
        'device_function': 'device_function',
        'device_mac_address': 'device_mac_address',
        'device_name': 'device_name',
        'auth': 'auth',
        'channel': 'channel',
        'client_health': 'client_health',
        'application_health': 'application_health',
        'radio_health': 'radio_health',
        'network_health': 'network_health',
        'radio_type': 'radio_type',
        'encryption_method': 'encryption_method',
        'interface_name': 'interface_name',
        'bssid': 'bssid',
        'rssi': 'rssi',
        'snr': 'snr',
        'description': 'description',
        'category': 'category',
        'mobility': 'mobility',
        'port_type_name': 'port_type_name',
        'wing_ap': 'wing_ap',
        'vendor': 'vendor',
        'locations': 'locations',
        'product_type': 'product_type',
        'alias': 'alias'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, location_id=None, device_id=None, hostname=None, mac_address=None, ip_address=None, ipv6_address=None, os_type=None, username=None, user_profile_name=None, connected=None, online_time=None, offline_time=None, vlan=None, connection_type=None, ssid=None, port=None, org_name=None, device_function=None, device_mac_address=None, device_name=None, auth=None, channel=None, client_health=None, application_health=None, radio_health=None, network_health=None, radio_type=None, encryption_method=None, interface_name=None, bssid=None, rssi=None, snr=None, description=None, category=None, mobility=None, port_type_name=None, wing_ap=None, vendor=None, locations=None, product_type=None, alias=None, local_vars_configuration=None):  # noqa: E501
        """XiqClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._location_id = None
        self._device_id = None
        self._hostname = None
        self._mac_address = None
        self._ip_address = None
        self._ipv6_address = None
        self._os_type = None
        self._username = None
        self._user_profile_name = None
        self._connected = None
        self._online_time = None
        self._offline_time = None
        self._vlan = None
        self._connection_type = None
        self._ssid = None
        self._port = None
        self._org_name = None
        self._device_function = None
        self._device_mac_address = None
        self._device_name = None
        self._auth = None
        self._channel = None
        self._client_health = None
        self._application_health = None
        self._radio_health = None
        self._network_health = None
        self._radio_type = None
        self._encryption_method = None
        self._interface_name = None
        self._bssid = None
        self._rssi = None
        self._snr = None
        self._description = None
        self._category = None
        self._mobility = None
        self._port_type_name = None
        self._wing_ap = None
        self._vendor = None
        self._locations = None
        self._product_type = None
        self._alias = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if location_id is not None:
            self.location_id = location_id
        if device_id is not None:
            self.device_id = device_id
        if hostname is not None:
            self.hostname = hostname
        if mac_address is not None:
            self.mac_address = mac_address
        if ip_address is not None:
            self.ip_address = ip_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if os_type is not None:
            self.os_type = os_type
        if username is not None:
            self.username = username
        if user_profile_name is not None:
            self.user_profile_name = user_profile_name
        if connected is not None:
            self.connected = connected
        if online_time is not None:
            self.online_time = online_time
        if offline_time is not None:
            self.offline_time = offline_time
        if vlan is not None:
            self.vlan = vlan
        if connection_type is not None:
            self.connection_type = connection_type
        if ssid is not None:
            self.ssid = ssid
        if port is not None:
            self.port = port
        if org_name is not None:
            self.org_name = org_name
        if device_function is not None:
            self.device_function = device_function
        if device_mac_address is not None:
            self.device_mac_address = device_mac_address
        if device_name is not None:
            self.device_name = device_name
        if auth is not None:
            self.auth = auth
        if channel is not None:
            self.channel = channel
        if client_health is not None:
            self.client_health = client_health
        if application_health is not None:
            self.application_health = application_health
        if radio_health is not None:
            self.radio_health = radio_health
        if network_health is not None:
            self.network_health = network_health
        if radio_type is not None:
            self.radio_type = radio_type
        if encryption_method is not None:
            self.encryption_method = encryption_method
        if interface_name is not None:
            self.interface_name = interface_name
        if bssid is not None:
            self.bssid = bssid
        if rssi is not None:
            self.rssi = rssi
        if snr is not None:
            self.snr = snr
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if mobility is not None:
            self.mobility = mobility
        if port_type_name is not None:
            self.port_type_name = port_type_name
        if wing_ap is not None:
            self.wing_ap = wing_ap
        if vendor is not None:
            self.vendor = vendor
        if locations is not None:
            self.locations = locations
        if product_type is not None:
            self.product_type = product_type
        if alias is not None:
            self.alias = alias

    @property
    def id(self):
        """Gets the id of this XiqClient.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqClient.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqClient.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqClient.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqClient.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqClient.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqClient.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqClient.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqClient.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqClient.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqClient.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqClient.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqClient.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqClient.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def location_id(self):
        """Gets the location_id of this XiqClient.  # noqa: E501

        The location ID  # noqa: E501

        :return: The location_id of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqClient.

        The location ID  # noqa: E501

        :param location_id: The location_id of this XiqClient.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def device_id(self):
        """Gets the device_id of this XiqClient.  # noqa: E501

        The device ID  # noqa: E501

        :return: The device_id of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this XiqClient.

        The device ID  # noqa: E501

        :param device_id: The device_id of this XiqClient.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

    @property
    def hostname(self):
        """Gets the hostname of this XiqClient.  # noqa: E501

        The hostname of the client  # noqa: E501

        :return: The hostname of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this XiqClient.

        The hostname of the client  # noqa: E501

        :param hostname: The hostname of this XiqClient.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqClient.  # noqa: E501

        The MAC address of the client  # noqa: E501

        :return: The mac_address of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqClient.

        The MAC address of the client  # noqa: E501

        :param mac_address: The mac_address of this XiqClient.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def ip_address(self):
        """Gets the ip_address of this XiqClient.  # noqa: E501

        The IP address of the client  # noqa: E501

        :return: The ip_address of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this XiqClient.

        The IP address of the client  # noqa: E501

        :param ip_address: The ip_address of this XiqClient.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this XiqClient.  # noqa: E501

        The IPv6 address of the client  # noqa: E501

        :return: The ipv6_address of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this XiqClient.

        The IPv6 address of the client  # noqa: E501

        :param ipv6_address: The ipv6_address of this XiqClient.  # noqa: E501
        :type: str
        """

        self._ipv6_address = ipv6_address

    @property
    def os_type(self):
        """Gets the os_type of this XiqClient.  # noqa: E501

        The OS type of the client  # noqa: E501

        :return: The os_type of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this XiqClient.

        The OS type of the client  # noqa: E501

        :param os_type: The os_type of this XiqClient.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def username(self):
        """Gets the username of this XiqClient.  # noqa: E501

        The username of the client.  # noqa: E501

        :return: The username of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this XiqClient.

        The username of the client.  # noqa: E501

        :param username: The username of this XiqClient.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_profile_name(self):
        """Gets the user_profile_name of this XiqClient.  # noqa: E501

        The user profile name of the client  # noqa: E501

        :return: The user_profile_name of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._user_profile_name

    @user_profile_name.setter
    def user_profile_name(self, user_profile_name):
        """Sets the user_profile_name of this XiqClient.

        The user profile name of the client  # noqa: E501

        :param user_profile_name: The user_profile_name of this XiqClient.  # noqa: E501
        :type: str
        """

        self._user_profile_name = user_profile_name

    @property
    def connected(self):
        """Gets the connected of this XiqClient.  # noqa: E501

        Client is connected or not  # noqa: E501

        :return: The connected of this XiqClient.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this XiqClient.

        Client is connected or not  # noqa: E501

        :param connected: The connected of this XiqClient.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def online_time(self):
        """Gets the online_time of this XiqClient.  # noqa: E501

        The online time for the client  # noqa: E501

        :return: The online_time of this XiqClient.  # noqa: E501
        :rtype: datetime
        """
        return self._online_time

    @online_time.setter
    def online_time(self, online_time):
        """Sets the online_time of this XiqClient.

        The online time for the client  # noqa: E501

        :param online_time: The online_time of this XiqClient.  # noqa: E501
        :type: datetime
        """

        self._online_time = online_time

    @property
    def offline_time(self):
        """Gets the offline_time of this XiqClient.  # noqa: E501

        The offline time for the client  # noqa: E501

        :return: The offline_time of this XiqClient.  # noqa: E501
        :rtype: datetime
        """
        return self._offline_time

    @offline_time.setter
    def offline_time(self, offline_time):
        """Sets the offline_time of this XiqClient.

        The offline time for the client  # noqa: E501

        :param offline_time: The offline_time of this XiqClient.  # noqa: E501
        :type: datetime
        """

        self._offline_time = offline_time

    @property
    def vlan(self):
        """Gets the vlan of this XiqClient.  # noqa: E501

        The associate VLAN  # noqa: E501

        :return: The vlan of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._vlan

    @vlan.setter
    def vlan(self, vlan):
        """Sets the vlan of this XiqClient.

        The associate VLAN  # noqa: E501

        :param vlan: The vlan of this XiqClient.  # noqa: E501
        :type: int
        """

        self._vlan = vlan

    @property
    def connection_type(self):
        """Gets the connection_type of this XiqClient.  # noqa: E501

        The connection type  # noqa: E501

        :return: The connection_type of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this XiqClient.

        The connection type  # noqa: E501

        :param connection_type: The connection_type of this XiqClient.  # noqa: E501
        :type: int
        """

        self._connection_type = connection_type

    @property
    def ssid(self):
        """Gets the ssid of this XiqClient.  # noqa: E501

        The SSID  # noqa: E501

        :return: The ssid of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this XiqClient.

        The SSID  # noqa: E501

        :param ssid: The ssid of this XiqClient.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def port(self):
        """Gets the port of this XiqClient.  # noqa: E501

        The associate device port  # noqa: E501

        :return: The port of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this XiqClient.

        The associate device port  # noqa: E501

        :param port: The port of this XiqClient.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def org_name(self):
        """Gets the org_name of this XiqClient.  # noqa: E501

        The organization name  # noqa: E501

        :return: The org_name of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this XiqClient.

        The organization name  # noqa: E501

        :param org_name: The org_name of this XiqClient.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def device_function(self):
        """Gets the device_function of this XiqClient.  # noqa: E501

        The associated device function  # noqa: E501

        :return: The device_function of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._device_function

    @device_function.setter
    def device_function(self, device_function):
        """Sets the device_function of this XiqClient.

        The associated device function  # noqa: E501

        :param device_function: The device_function of this XiqClient.  # noqa: E501
        :type: int
        """

        self._device_function = device_function

    @property
    def device_mac_address(self):
        """Gets the device_mac_address of this XiqClient.  # noqa: E501

        The associated device mac address  # noqa: E501

        :return: The device_mac_address of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._device_mac_address

    @device_mac_address.setter
    def device_mac_address(self, device_mac_address):
        """Sets the device_mac_address of this XiqClient.

        The associated device mac address  # noqa: E501

        :param device_mac_address: The device_mac_address of this XiqClient.  # noqa: E501
        :type: str
        """

        self._device_mac_address = device_mac_address

    @property
    def device_name(self):
        """Gets the device_name of this XiqClient.  # noqa: E501

        The associated device name  # noqa: E501

        :return: The device_name of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this XiqClient.

        The associated device name  # noqa: E501

        :param device_name: The device_name of this XiqClient.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def auth(self):
        """Gets the auth of this XiqClient.  # noqa: E501

        The authentication type  # noqa: E501

        :return: The auth of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this XiqClient.

        The authentication type  # noqa: E501

        :param auth: The auth of this XiqClient.  # noqa: E501
        :type: int
        """

        self._auth = auth

    @property
    def channel(self):
        """Gets the channel of this XiqClient.  # noqa: E501

        The channel value  # noqa: E501

        :return: The channel of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this XiqClient.

        The channel value  # noqa: E501

        :param channel: The channel of this XiqClient.  # noqa: E501
        :type: int
        """

        self._channel = channel

    @property
    def client_health(self):
        """Gets the client_health of this XiqClient.  # noqa: E501

        The health score of client  # noqa: E501

        :return: The client_health of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._client_health

    @client_health.setter
    def client_health(self, client_health):
        """Sets the client_health of this XiqClient.

        The health score of client  # noqa: E501

        :param client_health: The client_health of this XiqClient.  # noqa: E501
        :type: int
        """

        self._client_health = client_health

    @property
    def application_health(self):
        """Gets the application_health of this XiqClient.  # noqa: E501

        The health score of application  # noqa: E501

        :return: The application_health of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._application_health

    @application_health.setter
    def application_health(self, application_health):
        """Sets the application_health of this XiqClient.

        The health score of application  # noqa: E501

        :param application_health: The application_health of this XiqClient.  # noqa: E501
        :type: int
        """

        self._application_health = application_health

    @property
    def radio_health(self):
        """Gets the radio_health of this XiqClient.  # noqa: E501

        The health score of radio  # noqa: E501

        :return: The radio_health of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._radio_health

    @radio_health.setter
    def radio_health(self, radio_health):
        """Sets the radio_health of this XiqClient.

        The health score of radio  # noqa: E501

        :param radio_health: The radio_health of this XiqClient.  # noqa: E501
        :type: int
        """

        self._radio_health = radio_health

    @property
    def network_health(self):
        """Gets the network_health of this XiqClient.  # noqa: E501

        The health score of network  # noqa: E501

        :return: The network_health of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._network_health

    @network_health.setter
    def network_health(self, network_health):
        """Sets the network_health of this XiqClient.

        The health score of network  # noqa: E501

        :param network_health: The network_health of this XiqClient.  # noqa: E501
        :type: int
        """

        self._network_health = network_health

    @property
    def radio_type(self):
        """Gets the radio_type of this XiqClient.  # noqa: E501

        The radio type  # noqa: E501

        :return: The radio_type of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._radio_type

    @radio_type.setter
    def radio_type(self, radio_type):
        """Sets the radio_type of this XiqClient.

        The radio type  # noqa: E501

        :param radio_type: The radio_type of this XiqClient.  # noqa: E501
        :type: int
        """

        self._radio_type = radio_type

    @property
    def encryption_method(self):
        """Gets the encryption_method of this XiqClient.  # noqa: E501

        The encryption method  # noqa: E501

        :return: The encryption_method of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._encryption_method

    @encryption_method.setter
    def encryption_method(self, encryption_method):
        """Sets the encryption_method of this XiqClient.

        The encryption method  # noqa: E501

        :param encryption_method: The encryption_method of this XiqClient.  # noqa: E501
        :type: int
        """

        self._encryption_method = encryption_method

    @property
    def interface_name(self):
        """Gets the interface_name of this XiqClient.  # noqa: E501

        The interface name  # noqa: E501

        :return: The interface_name of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this XiqClient.

        The interface name  # noqa: E501

        :param interface_name: The interface_name of this XiqClient.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def bssid(self):
        """Gets the bssid of this XiqClient.  # noqa: E501

        The bssid  # noqa: E501

        :return: The bssid of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._bssid

    @bssid.setter
    def bssid(self, bssid):
        """Sets the bssid of this XiqClient.

        The bssid  # noqa: E501

        :param bssid: The bssid of this XiqClient.  # noqa: E501
        :type: str
        """

        self._bssid = bssid

    @property
    def rssi(self):
        """Gets the rssi of this XiqClient.  # noqa: E501

        The RSSI  # noqa: E501

        :return: The rssi of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._rssi

    @rssi.setter
    def rssi(self, rssi):
        """Sets the rssi of this XiqClient.

        The RSSI  # noqa: E501

        :param rssi: The rssi of this XiqClient.  # noqa: E501
        :type: int
        """

        self._rssi = rssi

    @property
    def snr(self):
        """Gets the snr of this XiqClient.  # noqa: E501

        The SNR  # noqa: E501

        :return: The snr of this XiqClient.  # noqa: E501
        :rtype: int
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this XiqClient.

        The SNR  # noqa: E501

        :param snr: The snr of this XiqClient.  # noqa: E501
        :type: int
        """

        self._snr = snr

    @property
    def description(self):
        """Gets the description of this XiqClient.  # noqa: E501

        The description of client  # noqa: E501

        :return: The description of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqClient.

        The description of client  # noqa: E501

        :param description: The description of this XiqClient.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this XiqClient.  # noqa: E501

        The category of client  # noqa: E501

        :return: The category of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this XiqClient.

        The category of client  # noqa: E501

        :param category: The category of this XiqClient.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def mobility(self):
        """Gets the mobility of this XiqClient.  # noqa: E501

        The client mobility  # noqa: E501

        :return: The mobility of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._mobility

    @mobility.setter
    def mobility(self, mobility):
        """Sets the mobility of this XiqClient.

        The client mobility  # noqa: E501

        :param mobility: The mobility of this XiqClient.  # noqa: E501
        :type: str
        """

        self._mobility = mobility

    @property
    def port_type_name(self):
        """Gets the port_type_name of this XiqClient.  # noqa: E501

        The client port type name  # noqa: E501

        :return: The port_type_name of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._port_type_name

    @port_type_name.setter
    def port_type_name(self, port_type_name):
        """Sets the port_type_name of this XiqClient.

        The client port type name  # noqa: E501

        :param port_type_name: The port_type_name of this XiqClient.  # noqa: E501
        :type: str
        """

        self._port_type_name = port_type_name

    @property
    def wing_ap(self):
        """Gets the wing_ap of this XiqClient.  # noqa: E501

        Wing ap flag  # noqa: E501

        :return: The wing_ap of this XiqClient.  # noqa: E501
        :rtype: bool
        """
        return self._wing_ap

    @wing_ap.setter
    def wing_ap(self, wing_ap):
        """Sets the wing_ap of this XiqClient.

        Wing ap flag  # noqa: E501

        :param wing_ap: The wing_ap of this XiqClient.  # noqa: E501
        :type: bool
        """

        self._wing_ap = wing_ap

    @property
    def vendor(self):
        """Gets the vendor of this XiqClient.  # noqa: E501

        The vendor of client  # noqa: E501

        :return: The vendor of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this XiqClient.

        The vendor of client  # noqa: E501

        :param vendor: The vendor of this XiqClient.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def locations(self):
        """Gets the locations of this XiqClient.  # noqa: E501

        The detailed location  # noqa: E501

        :return: The locations of this XiqClient.  # noqa: E501
        :rtype: list[XiqLocationLegend]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this XiqClient.

        The detailed location  # noqa: E501

        :param locations: The locations of this XiqClient.  # noqa: E501
        :type: list[XiqLocationLegend]
        """

        self._locations = locations

    @property
    def product_type(self):
        """Gets the product_type of this XiqClient.  # noqa: E501

        The Category which describes the Extreme device types(For example:For example:SR_2208P, AP_4000, AP_5010)  # noqa: E501

        :return: The product_type of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this XiqClient.

        The Category which describes the Extreme device types(For example:For example:SR_2208P, AP_4000, AP_5010)  # noqa: E501

        :param product_type: The product_type of this XiqClient.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def alias(self):
        """Gets the alias of this XiqClient.  # noqa: E501

        The alias of the client  # noqa: E501

        :return: The alias of this XiqClient.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this XiqClient.

        The alias of the client  # noqa: E501

        :param alias: The alias of this XiqClient.  # noqa: E501
        :type: str
        """

        self._alias = alias

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
        if not isinstance(other, XiqClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqClient):
            return True

        return self.to_dict() != other.to_dict()
