# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.3.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDevice(object):
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
        'serial_number': 'str',
        'service_tag': 'str',
        'mac_address': 'str',
        'device_function': 'XiqDeviceFunction',
        'product_type': 'str',
        'hostname': 'str',
        'ip_address': 'str',
        'software_version': 'str',
        'device_admin_state': 'XiqDeviceAdminState',
        'connected': 'bool',
        'last_connect_time': 'datetime',
        'network_policy_name': 'str',
        'network_policy_id': 'int',
        'primary_ntp_server_address': 'str',
        'primary_dns_server_address': 'str',
        'subnet_mask': 'str',
        'default_gateway': 'str',
        'ipv6_address': 'str',
        'ipv6_netmask': 'int',
        'simulated': 'bool',
        'display_version': 'str',
        'active_clients': 'int',
        'location_id': 'int',
        'locations': 'list[XiqLocationLegend]',
        'country_code': 'int',
        'description': 'str',
        'lldp_cdp_infos': 'list[XiqDeviceLldpCdpInfo]',
        'system_up_time': 'int',
        'config_mismatch': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'serial_number': 'serial_number',
        'service_tag': 'service_tag',
        'mac_address': 'mac_address',
        'device_function': 'device_function',
        'product_type': 'product_type',
        'hostname': 'hostname',
        'ip_address': 'ip_address',
        'software_version': 'software_version',
        'device_admin_state': 'device_admin_state',
        'connected': 'connected',
        'last_connect_time': 'last_connect_time',
        'network_policy_name': 'network_policy_name',
        'network_policy_id': 'network_policy_id',
        'primary_ntp_server_address': 'primary_ntp_server_address',
        'primary_dns_server_address': 'primary_dns_server_address',
        'subnet_mask': 'subnet_mask',
        'default_gateway': 'default_gateway',
        'ipv6_address': 'ipv6_address',
        'ipv6_netmask': 'ipv6_netmask',
        'simulated': 'simulated',
        'display_version': 'display_version',
        'active_clients': 'active_clients',
        'location_id': 'location_id',
        'locations': 'locations',
        'country_code': 'country_code',
        'description': 'description',
        'lldp_cdp_infos': 'lldp_cdp_infos',
        'system_up_time': 'system_up_time',
        'config_mismatch': 'config_mismatch'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, serial_number=None, service_tag=None, mac_address=None, device_function=None, product_type=None, hostname=None, ip_address=None, software_version=None, device_admin_state=None, connected=None, last_connect_time=None, network_policy_name=None, network_policy_id=None, primary_ntp_server_address=None, primary_dns_server_address=None, subnet_mask=None, default_gateway=None, ipv6_address=None, ipv6_netmask=None, simulated=None, display_version=None, active_clients=None, location_id=None, locations=None, country_code=None, description=None, lldp_cdp_infos=None, system_up_time=None, config_mismatch=None, local_vars_configuration=None):  # noqa: E501
        """XiqDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._serial_number = None
        self._service_tag = None
        self._mac_address = None
        self._device_function = None
        self._product_type = None
        self._hostname = None
        self._ip_address = None
        self._software_version = None
        self._device_admin_state = None
        self._connected = None
        self._last_connect_time = None
        self._network_policy_name = None
        self._network_policy_id = None
        self._primary_ntp_server_address = None
        self._primary_dns_server_address = None
        self._subnet_mask = None
        self._default_gateway = None
        self._ipv6_address = None
        self._ipv6_netmask = None
        self._simulated = None
        self._display_version = None
        self._active_clients = None
        self._location_id = None
        self._locations = None
        self._country_code = None
        self._description = None
        self._lldp_cdp_infos = None
        self._system_up_time = None
        self._config_mismatch = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if serial_number is not None:
            self.serial_number = serial_number
        if service_tag is not None:
            self.service_tag = service_tag
        if mac_address is not None:
            self.mac_address = mac_address
        if device_function is not None:
            self.device_function = device_function
        if product_type is not None:
            self.product_type = product_type
        if hostname is not None:
            self.hostname = hostname
        if ip_address is not None:
            self.ip_address = ip_address
        if software_version is not None:
            self.software_version = software_version
        if device_admin_state is not None:
            self.device_admin_state = device_admin_state
        if connected is not None:
            self.connected = connected
        if last_connect_time is not None:
            self.last_connect_time = last_connect_time
        if network_policy_name is not None:
            self.network_policy_name = network_policy_name
        if network_policy_id is not None:
            self.network_policy_id = network_policy_id
        if primary_ntp_server_address is not None:
            self.primary_ntp_server_address = primary_ntp_server_address
        if primary_dns_server_address is not None:
            self.primary_dns_server_address = primary_dns_server_address
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask
        if default_gateway is not None:
            self.default_gateway = default_gateway
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if ipv6_netmask is not None:
            self.ipv6_netmask = ipv6_netmask
        if simulated is not None:
            self.simulated = simulated
        if display_version is not None:
            self.display_version = display_version
        if active_clients is not None:
            self.active_clients = active_clients
        if location_id is not None:
            self.location_id = location_id
        if locations is not None:
            self.locations = locations
        if country_code is not None:
            self.country_code = country_code
        if description is not None:
            self.description = description
        if lldp_cdp_infos is not None:
            self.lldp_cdp_infos = lldp_cdp_infos
        if system_up_time is not None:
            self.system_up_time = system_up_time
        if config_mismatch is not None:
            self.config_mismatch = config_mismatch

    @property
    def id(self):
        """Gets the id of this XiqDevice.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqDevice.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqDevice.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqDevice.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqDevice.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqDevice.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqDevice.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqDevice.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqDevice.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqDevice.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqDevice.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def serial_number(self):
        """Gets the serial_number of this XiqDevice.  # noqa: E501

        The device serial number, valid for all non-HAC devices  # noqa: E501

        :return: The serial_number of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this XiqDevice.

        The device serial number, valid for all non-HAC devices  # noqa: E501

        :param serial_number: The serial_number of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def service_tag(self):
        """Gets the service_tag of this XiqDevice.  # noqa: E501

        The device service tag, valid for all HAC devices  # noqa: E501

        :return: The service_tag of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._service_tag

    @service_tag.setter
    def service_tag(self, service_tag):
        """Sets the service_tag of this XiqDevice.

        The device service tag, valid for all HAC devices  # noqa: E501

        :param service_tag: The service_tag of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._service_tag = service_tag

    @property
    def mac_address(self):
        """Gets the mac_address of this XiqDevice.  # noqa: E501

        The device MAC address  # noqa: E501

        :return: The mac_address of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this XiqDevice.

        The device MAC address  # noqa: E501

        :param mac_address: The mac_address of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def device_function(self):
        """Gets the device_function of this XiqDevice.  # noqa: E501


        :return: The device_function of this XiqDevice.  # noqa: E501
        :rtype: XiqDeviceFunction
        """
        return self._device_function

    @device_function.setter
    def device_function(self, device_function):
        """Sets the device_function of this XiqDevice.


        :param device_function: The device_function of this XiqDevice.  # noqa: E501
        :type: XiqDeviceFunction
        """

        self._device_function = device_function

    @property
    def product_type(self):
        """Gets the product_type of this XiqDevice.  # noqa: E501

        The product type, such as: AP_230, BR_100, NX9600, etc.  # noqa: E501

        :return: The product_type of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this XiqDevice.

        The product type, such as: AP_230, BR_100, NX9600, etc.  # noqa: E501

        :param product_type: The product_type of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def hostname(self):
        """Gets the hostname of this XiqDevice.  # noqa: E501

        The device hostname  # noqa: E501

        :return: The hostname of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this XiqDevice.

        The device hostname  # noqa: E501

        :param hostname: The hostname of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ip_address(self):
        """Gets the ip_address of this XiqDevice.  # noqa: E501

        The device IPv4 address  # noqa: E501

        :return: The ip_address of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this XiqDevice.

        The device IPv4 address  # noqa: E501

        :param ip_address: The ip_address of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def software_version(self):
        """Gets the software_version of this XiqDevice.  # noqa: E501

        The device OS software version  # noqa: E501

        :return: The software_version of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this XiqDevice.

        The device OS software version  # noqa: E501

        :param software_version: The software_version of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def device_admin_state(self):
        """Gets the device_admin_state of this XiqDevice.  # noqa: E501


        :return: The device_admin_state of this XiqDevice.  # noqa: E501
        :rtype: XiqDeviceAdminState
        """
        return self._device_admin_state

    @device_admin_state.setter
    def device_admin_state(self, device_admin_state):
        """Sets the device_admin_state of this XiqDevice.


        :param device_admin_state: The device_admin_state of this XiqDevice.  # noqa: E501
        :type: XiqDeviceAdminState
        """

        self._device_admin_state = device_admin_state

    @property
    def connected(self):
        """Gets the connected of this XiqDevice.  # noqa: E501

        The device connection status  # noqa: E501

        :return: The connected of this XiqDevice.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this XiqDevice.

        The device connection status  # noqa: E501

        :param connected: The connected of this XiqDevice.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def last_connect_time(self):
        """Gets the last_connect_time of this XiqDevice.  # noqa: E501

        The device last connect time  # noqa: E501

        :return: The last_connect_time of this XiqDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._last_connect_time

    @last_connect_time.setter
    def last_connect_time(self, last_connect_time):
        """Sets the last_connect_time of this XiqDevice.

        The device last connect time  # noqa: E501

        :param last_connect_time: The last_connect_time of this XiqDevice.  # noqa: E501
        :type: datetime
        """

        self._last_connect_time = last_connect_time

    @property
    def network_policy_name(self):
        """Gets the network_policy_name of this XiqDevice.  # noqa: E501

        The network policy name for the device  # noqa: E501

        :return: The network_policy_name of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._network_policy_name

    @network_policy_name.setter
    def network_policy_name(self, network_policy_name):
        """Sets the network_policy_name of this XiqDevice.

        The network policy name for the device  # noqa: E501

        :param network_policy_name: The network_policy_name of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._network_policy_name = network_policy_name

    @property
    def network_policy_id(self):
        """Gets the network_policy_id of this XiqDevice.  # noqa: E501

        The network policy ID for the device  # noqa: E501

        :return: The network_policy_id of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._network_policy_id

    @network_policy_id.setter
    def network_policy_id(self, network_policy_id):
        """Sets the network_policy_id of this XiqDevice.

        The network policy ID for the device  # noqa: E501

        :param network_policy_id: The network_policy_id of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._network_policy_id = network_policy_id

    @property
    def primary_ntp_server_address(self):
        """Gets the primary_ntp_server_address of this XiqDevice.  # noqa: E501

        The primary NTP server address for the device  # noqa: E501

        :return: The primary_ntp_server_address of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._primary_ntp_server_address

    @primary_ntp_server_address.setter
    def primary_ntp_server_address(self, primary_ntp_server_address):
        """Sets the primary_ntp_server_address of this XiqDevice.

        The primary NTP server address for the device  # noqa: E501

        :param primary_ntp_server_address: The primary_ntp_server_address of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._primary_ntp_server_address = primary_ntp_server_address

    @property
    def primary_dns_server_address(self):
        """Gets the primary_dns_server_address of this XiqDevice.  # noqa: E501

        The primary DNS server address for the device  # noqa: E501

        :return: The primary_dns_server_address of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._primary_dns_server_address

    @primary_dns_server_address.setter
    def primary_dns_server_address(self, primary_dns_server_address):
        """Sets the primary_dns_server_address of this XiqDevice.

        The primary DNS server address for the device  # noqa: E501

        :param primary_dns_server_address: The primary_dns_server_address of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._primary_dns_server_address = primary_dns_server_address

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this XiqDevice.  # noqa: E501

        The subnet mask for the device  # noqa: E501

        :return: The subnet_mask of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this XiqDevice.

        The subnet mask for the device  # noqa: E501

        :param subnet_mask: The subnet_mask of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

    @property
    def default_gateway(self):
        """Gets the default_gateway of this XiqDevice.  # noqa: E501

        The default gateway for the device  # noqa: E501

        :return: The default_gateway of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._default_gateway

    @default_gateway.setter
    def default_gateway(self, default_gateway):
        """Sets the default_gateway of this XiqDevice.

        The default gateway for the device  # noqa: E501

        :param default_gateway: The default_gateway of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._default_gateway = default_gateway

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this XiqDevice.  # noqa: E501

        The ipv6 address for the device  # noqa: E501

        :return: The ipv6_address of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this XiqDevice.

        The ipv6 address for the device  # noqa: E501

        :param ipv6_address: The ipv6_address of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._ipv6_address = ipv6_address

    @property
    def ipv6_netmask(self):
        """Gets the ipv6_netmask of this XiqDevice.  # noqa: E501

        The ipv6 netmask for the device  # noqa: E501

        :return: The ipv6_netmask of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._ipv6_netmask

    @ipv6_netmask.setter
    def ipv6_netmask(self, ipv6_netmask):
        """Sets the ipv6_netmask of this XiqDevice.

        The ipv6 netmask for the device  # noqa: E501

        :param ipv6_netmask: The ipv6_netmask of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._ipv6_netmask = ipv6_netmask

    @property
    def simulated(self):
        """Gets the simulated of this XiqDevice.  # noqa: E501

        The device is simulated or not  # noqa: E501

        :return: The simulated of this XiqDevice.  # noqa: E501
        :rtype: bool
        """
        return self._simulated

    @simulated.setter
    def simulated(self, simulated):
        """Sets the simulated of this XiqDevice.

        The device is simulated or not  # noqa: E501

        :param simulated: The simulated of this XiqDevice.  # noqa: E501
        :type: bool
        """

        self._simulated = simulated

    @property
    def display_version(self):
        """Gets the display_version of this XiqDevice.  # noqa: E501

        The display version for the device  # noqa: E501

        :return: The display_version of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._display_version

    @display_version.setter
    def display_version(self, display_version):
        """Sets the display_version of this XiqDevice.

        The display version for the device  # noqa: E501

        :param display_version: The display_version of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._display_version = display_version

    @property
    def active_clients(self):
        """Gets the active_clients of this XiqDevice.  # noqa: E501

        The active client count for the device  # noqa: E501

        :return: The active_clients of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._active_clients

    @active_clients.setter
    def active_clients(self, active_clients):
        """Sets the active_clients of this XiqDevice.

        The active client count for the device  # noqa: E501

        :param active_clients: The active_clients of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._active_clients = active_clients

    @property
    def location_id(self):
        """Gets the location_id of this XiqDevice.  # noqa: E501

        The location ID for the device  # noqa: E501

        :return: The location_id of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqDevice.

        The location ID for the device  # noqa: E501

        :param location_id: The location_id of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def locations(self):
        """Gets the locations of this XiqDevice.  # noqa: E501

        The detailed location  # noqa: E501

        :return: The locations of this XiqDevice.  # noqa: E501
        :rtype: list[XiqLocationLegend]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this XiqDevice.

        The detailed location  # noqa: E501

        :param locations: The locations of this XiqDevice.  # noqa: E501
        :type: list[XiqLocationLegend]
        """

        self._locations = locations

    @property
    def country_code(self):
        """Gets the country_code of this XiqDevice.  # noqa: E501

        The assigned country code on the device  # noqa: E501

        :return: The country_code of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this XiqDevice.

        The assigned country code on the device  # noqa: E501

        :param country_code: The country_code of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._country_code = country_code

    @property
    def description(self):
        """Gets the description of this XiqDevice.  # noqa: E501

        The device description  # noqa: E501

        :return: The description of this XiqDevice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqDevice.

        The device description  # noqa: E501

        :param description: The description of this XiqDevice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def lldp_cdp_infos(self):
        """Gets the lldp_cdp_infos of this XiqDevice.  # noqa: E501

        The device LLDP/CDP information  # noqa: E501

        :return: The lldp_cdp_infos of this XiqDevice.  # noqa: E501
        :rtype: list[XiqDeviceLldpCdpInfo]
        """
        return self._lldp_cdp_infos

    @lldp_cdp_infos.setter
    def lldp_cdp_infos(self, lldp_cdp_infos):
        """Sets the lldp_cdp_infos of this XiqDevice.

        The device LLDP/CDP information  # noqa: E501

        :param lldp_cdp_infos: The lldp_cdp_infos of this XiqDevice.  # noqa: E501
        :type: list[XiqDeviceLldpCdpInfo]
        """

        self._lldp_cdp_infos = lldp_cdp_infos

    @property
    def system_up_time(self):
        """Gets the system_up_time of this XiqDevice.  # noqa: E501

        The device uptime  # noqa: E501

        :return: The system_up_time of this XiqDevice.  # noqa: E501
        :rtype: int
        """
        return self._system_up_time

    @system_up_time.setter
    def system_up_time(self, system_up_time):
        """Sets the system_up_time of this XiqDevice.

        The device uptime  # noqa: E501

        :param system_up_time: The system_up_time of this XiqDevice.  # noqa: E501
        :type: int
        """

        self._system_up_time = system_up_time

    @property
    def config_mismatch(self):
        """Gets the config_mismatch of this XiqDevice.  # noqa: E501

        Config audit status(MATCHED or UNMATCHED)  # noqa: E501

        :return: The config_mismatch of this XiqDevice.  # noqa: E501
        :rtype: bool
        """
        return self._config_mismatch

    @config_mismatch.setter
    def config_mismatch(self, config_mismatch):
        """Sets the config_mismatch of this XiqDevice.

        Config audit status(MATCHED or UNMATCHED)  # noqa: E501

        :param config_mismatch: The config_mismatch of this XiqDevice.  # noqa: E501
        :type: bool
        """

        self._config_mismatch = config_mismatch

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
        if not isinstance(other, XiqDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDevice):
            return True

        return self.to_dict() != other.to_dict()
