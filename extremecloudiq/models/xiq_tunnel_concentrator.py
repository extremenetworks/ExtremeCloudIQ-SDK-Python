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


class XiqTunnelConcentrator(object):
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
        'description': 'str',
        'redundant': 'bool',
        'primary_tc': 'int',
        'backup_tc': 'int',
        'primary_listening_interface': 'int',
        'backup_listening_interface': 'int',
        'primary_bridging_interface': 'int',
        'backup_bridging_interface': 'int',
        'primary_ip': 'str',
        'backup_ip': 'str',
        'primary_vlan': 'int',
        'backup_vlan': 'int',
        'primary_tagged': 'bool',
        'backup_tagged': 'bool',
        'tunnel_address': 'str',
        'router_id': 'int',
        'gateway': 'str',
        'native_vlan': 'int'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'description': 'description',
        'redundant': 'redundant',
        'primary_tc': 'primary_tc',
        'backup_tc': 'backup_tc',
        'primary_listening_interface': 'primary_listening_interface',
        'backup_listening_interface': 'backup_listening_interface',
        'primary_bridging_interface': 'primary_bridging_interface',
        'backup_bridging_interface': 'backup_bridging_interface',
        'primary_ip': 'primary_ip',
        'backup_ip': 'backup_ip',
        'primary_vlan': 'primary_vlan',
        'backup_vlan': 'backup_vlan',
        'primary_tagged': 'primary_tagged',
        'backup_tagged': 'backup_tagged',
        'tunnel_address': 'tunnel_address',
        'router_id': 'router_id',
        'gateway': 'gateway',
        'native_vlan': 'native_vlan'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, description=None, redundant=None, primary_tc=None, backup_tc=None, primary_listening_interface=None, backup_listening_interface=None, primary_bridging_interface=None, backup_bridging_interface=None, primary_ip=None, backup_ip=None, primary_vlan=None, backup_vlan=None, primary_tagged=None, backup_tagged=None, tunnel_address=None, router_id=None, gateway=None, native_vlan=None, local_vars_configuration=None):  # noqa: E501
        """XiqTunnelConcentrator - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._description = None
        self._redundant = None
        self._primary_tc = None
        self._backup_tc = None
        self._primary_listening_interface = None
        self._backup_listening_interface = None
        self._primary_bridging_interface = None
        self._backup_bridging_interface = None
        self._primary_ip = None
        self._backup_ip = None
        self._primary_vlan = None
        self._backup_vlan = None
        self._primary_tagged = None
        self._backup_tagged = None
        self._tunnel_address = None
        self._router_id = None
        self._gateway = None
        self._native_vlan = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.name = name
        self.description = description
        if redundant is not None:
            self.redundant = redundant
        self.primary_tc = primary_tc
        if backup_tc is not None:
            self.backup_tc = backup_tc
        self.primary_listening_interface = primary_listening_interface
        if backup_listening_interface is not None:
            self.backup_listening_interface = backup_listening_interface
        self.primary_bridging_interface = primary_bridging_interface
        if backup_bridging_interface is not None:
            self.backup_bridging_interface = backup_bridging_interface
        if primary_ip is not None:
            self.primary_ip = primary_ip
        if backup_ip is not None:
            self.backup_ip = backup_ip
        self.primary_vlan = primary_vlan
        if backup_vlan is not None:
            self.backup_vlan = backup_vlan
        self.primary_tagged = primary_tagged
        if backup_tagged is not None:
            self.backup_tagged = backup_tagged
        self.tunnel_address = tunnel_address
        if router_id is not None:
            self.router_id = router_id
        if gateway is not None:
            self.gateway = gateway
        self.native_vlan = native_vlan

    @property
    def id(self):
        """Gets the id of this XiqTunnelConcentrator.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqTunnelConcentrator.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqTunnelConcentrator.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqTunnelConcentrator.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqTunnelConcentrator.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqTunnelConcentrator.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqTunnelConcentrator.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqTunnelConcentrator.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqTunnelConcentrator.  # noqa: E501

         The Tunnel Concentrator Service name  # noqa: E501

        :return: The name of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqTunnelConcentrator.

         The Tunnel Concentrator Service name  # noqa: E501

        :param name: The name of this XiqTunnelConcentrator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqTunnelConcentrator.  # noqa: E501

         The Tunnel Concentrator Service description  # noqa: E501

        :return: The description of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqTunnelConcentrator.

         The Tunnel Concentrator Service description  # noqa: E501

        :param description: The description of this XiqTunnelConcentrator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def redundant(self):
        """Gets the redundant of this XiqTunnelConcentrator.  # noqa: E501

        Indicates if redundant Tunnel Concentrators (primary and backup) are configured   # noqa: E501

        :return: The redundant of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: bool
        """
        return self._redundant

    @redundant.setter
    def redundant(self, redundant):
        """Sets the redundant of this XiqTunnelConcentrator.

        Indicates if redundant Tunnel Concentrators (primary and backup) are configured   # noqa: E501

        :param redundant: The redundant of this XiqTunnelConcentrator.  # noqa: E501
        :type: bool
        """

        self._redundant = redundant

    @property
    def primary_tc(self):
        """Gets the primary_tc of this XiqTunnelConcentrator.  # noqa: E501

         The Primary Tunnel Concentrator device ID  # noqa: E501

        :return: The primary_tc of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._primary_tc

    @primary_tc.setter
    def primary_tc(self, primary_tc):
        """Sets the primary_tc of this XiqTunnelConcentrator.

         The Primary Tunnel Concentrator device ID  # noqa: E501

        :param primary_tc: The primary_tc of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and primary_tc is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_tc`, must not be `None`")  # noqa: E501

        self._primary_tc = primary_tc

    @property
    def backup_tc(self):
        """Gets the backup_tc of this XiqTunnelConcentrator.  # noqa: E501

        The Backup Tunnel Concentrator device ID  # noqa: E501

        :return: The backup_tc of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._backup_tc

    @backup_tc.setter
    def backup_tc(self, backup_tc):
        """Sets the backup_tc of this XiqTunnelConcentrator.

        The Backup Tunnel Concentrator device ID  # noqa: E501

        :param backup_tc: The backup_tc of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """

        self._backup_tc = backup_tc

    @property
    def primary_listening_interface(self):
        """Gets the primary_listening_interface of this XiqTunnelConcentrator.  # noqa: E501

        Primary Listening Interface ID.  # noqa: E501

        :return: The primary_listening_interface of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._primary_listening_interface

    @primary_listening_interface.setter
    def primary_listening_interface(self, primary_listening_interface):
        """Sets the primary_listening_interface of this XiqTunnelConcentrator.

        Primary Listening Interface ID.  # noqa: E501

        :param primary_listening_interface: The primary_listening_interface of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and primary_listening_interface is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_listening_interface`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_listening_interface is not None and primary_listening_interface > 4):  # noqa: E501
            raise ValueError("Invalid value for `primary_listening_interface`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_listening_interface is not None and primary_listening_interface < 1):  # noqa: E501
            raise ValueError("Invalid value for `primary_listening_interface`, must be a value greater than or equal to `1`")  # noqa: E501

        self._primary_listening_interface = primary_listening_interface

    @property
    def backup_listening_interface(self):
        """Gets the backup_listening_interface of this XiqTunnelConcentrator.  # noqa: E501

        Backup Listening Interface ID.  # noqa: E501

        :return: The backup_listening_interface of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._backup_listening_interface

    @backup_listening_interface.setter
    def backup_listening_interface(self, backup_listening_interface):
        """Sets the backup_listening_interface of this XiqTunnelConcentrator.

        Backup Listening Interface ID.  # noqa: E501

        :param backup_listening_interface: The backup_listening_interface of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                backup_listening_interface is not None and backup_listening_interface > 4):  # noqa: E501
            raise ValueError("Invalid value for `backup_listening_interface`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                backup_listening_interface is not None and backup_listening_interface < 1):  # noqa: E501
            raise ValueError("Invalid value for `backup_listening_interface`, must be a value greater than or equal to `1`")  # noqa: E501

        self._backup_listening_interface = backup_listening_interface

    @property
    def primary_bridging_interface(self):
        """Gets the primary_bridging_interface of this XiqTunnelConcentrator.  # noqa: E501

        Primary Bridging Interface ID.  # noqa: E501

        :return: The primary_bridging_interface of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._primary_bridging_interface

    @primary_bridging_interface.setter
    def primary_bridging_interface(self, primary_bridging_interface):
        """Sets the primary_bridging_interface of this XiqTunnelConcentrator.

        Primary Bridging Interface ID.  # noqa: E501

        :param primary_bridging_interface: The primary_bridging_interface of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and primary_bridging_interface is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_bridging_interface`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_bridging_interface is not None and primary_bridging_interface > 4):  # noqa: E501
            raise ValueError("Invalid value for `primary_bridging_interface`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_bridging_interface is not None and primary_bridging_interface < 1):  # noqa: E501
            raise ValueError("Invalid value for `primary_bridging_interface`, must be a value greater than or equal to `1`")  # noqa: E501

        self._primary_bridging_interface = primary_bridging_interface

    @property
    def backup_bridging_interface(self):
        """Gets the backup_bridging_interface of this XiqTunnelConcentrator.  # noqa: E501

        Backup Bridging Interface ID.  # noqa: E501

        :return: The backup_bridging_interface of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._backup_bridging_interface

    @backup_bridging_interface.setter
    def backup_bridging_interface(self, backup_bridging_interface):
        """Sets the backup_bridging_interface of this XiqTunnelConcentrator.

        Backup Bridging Interface ID.  # noqa: E501

        :param backup_bridging_interface: The backup_bridging_interface of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                backup_bridging_interface is not None and backup_bridging_interface > 4):  # noqa: E501
            raise ValueError("Invalid value for `backup_bridging_interface`, must be a value less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                backup_bridging_interface is not None and backup_bridging_interface < 1):  # noqa: E501
            raise ValueError("Invalid value for `backup_bridging_interface`, must be a value greater than or equal to `1`")  # noqa: E501

        self._backup_bridging_interface = backup_bridging_interface

    @property
    def primary_ip(self):
        """Gets the primary_ip of this XiqTunnelConcentrator.  # noqa: E501

        The primary IP address of network interface for accepting connections from APs (listening interface).  # noqa: E501

        :return: The primary_ip of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip

    @primary_ip.setter
    def primary_ip(self, primary_ip):
        """Sets the primary_ip of this XiqTunnelConcentrator.

        The primary IP address of network interface for accepting connections from APs (listening interface).  # noqa: E501

        :param primary_ip: The primary_ip of this XiqTunnelConcentrator.  # noqa: E501
        :type: str
        """

        self._primary_ip = primary_ip

    @property
    def backup_ip(self):
        """Gets the backup_ip of this XiqTunnelConcentrator.  # noqa: E501

        The backup IP address of network interface for accepting connections from APs (listening interface)  # noqa: E501

        :return: The backup_ip of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: str
        """
        return self._backup_ip

    @backup_ip.setter
    def backup_ip(self, backup_ip):
        """Sets the backup_ip of this XiqTunnelConcentrator.

        The backup IP address of network interface for accepting connections from APs (listening interface)  # noqa: E501

        :param backup_ip: The backup_ip of this XiqTunnelConcentrator.  # noqa: E501
        :type: str
        """

        self._backup_ip = backup_ip

    @property
    def primary_vlan(self):
        """Gets the primary_vlan of this XiqTunnelConcentrator.  # noqa: E501

        The VLAN ID for the primary listening interface  # noqa: E501

        :return: The primary_vlan of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._primary_vlan

    @primary_vlan.setter
    def primary_vlan(self, primary_vlan):
        """Sets the primary_vlan of this XiqTunnelConcentrator.

        The VLAN ID for the primary listening interface  # noqa: E501

        :param primary_vlan: The primary_vlan of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and primary_vlan is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_vlan`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_vlan is not None and primary_vlan > 4094):  # noqa: E501
            raise ValueError("Invalid value for `primary_vlan`, must be a value less than or equal to `4094`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_vlan is not None and primary_vlan < 1):  # noqa: E501
            raise ValueError("Invalid value for `primary_vlan`, must be a value greater than or equal to `1`")  # noqa: E501

        self._primary_vlan = primary_vlan

    @property
    def backup_vlan(self):
        """Gets the backup_vlan of this XiqTunnelConcentrator.  # noqa: E501

        The VLAN ID for the backup listening interface  # noqa: E501

        :return: The backup_vlan of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._backup_vlan

    @backup_vlan.setter
    def backup_vlan(self, backup_vlan):
        """Sets the backup_vlan of this XiqTunnelConcentrator.

        The VLAN ID for the backup listening interface  # noqa: E501

        :param backup_vlan: The backup_vlan of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                backup_vlan is not None and backup_vlan > 4094):  # noqa: E501
            raise ValueError("Invalid value for `backup_vlan`, must be a value less than or equal to `4094`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                backup_vlan is not None and backup_vlan < 1):  # noqa: E501
            raise ValueError("Invalid value for `backup_vlan`, must be a value greater than or equal to `1`")  # noqa: E501

        self._backup_vlan = backup_vlan

    @property
    def primary_tagged(self):
        """Gets the primary_tagged of this XiqTunnelConcentrator.  # noqa: E501

        Indicates if primary VLAN is tagged.  # noqa: E501

        :return: The primary_tagged of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: bool
        """
        return self._primary_tagged

    @primary_tagged.setter
    def primary_tagged(self, primary_tagged):
        """Sets the primary_tagged of this XiqTunnelConcentrator.

        Indicates if primary VLAN is tagged.  # noqa: E501

        :param primary_tagged: The primary_tagged of this XiqTunnelConcentrator.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and primary_tagged is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_tagged`, must not be `None`")  # noqa: E501

        self._primary_tagged = primary_tagged

    @property
    def backup_tagged(self):
        """Gets the backup_tagged of this XiqTunnelConcentrator.  # noqa: E501

        Indicates if backup VLAN is tagged  # noqa: E501

        :return: The backup_tagged of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: bool
        """
        return self._backup_tagged

    @backup_tagged.setter
    def backup_tagged(self, backup_tagged):
        """Sets the backup_tagged of this XiqTunnelConcentrator.

        Indicates if backup VLAN is tagged  # noqa: E501

        :param backup_tagged: The backup_tagged of this XiqTunnelConcentrator.  # noqa: E501
        :type: bool
        """

        self._backup_tagged = backup_tagged

    @property
    def tunnel_address(self):
        """Gets the tunnel_address of this XiqTunnelConcentrator.  # noqa: E501

        IP address/CIDR of listening interface.  # noqa: E501

        :return: The tunnel_address of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: str
        """
        return self._tunnel_address

    @tunnel_address.setter
    def tunnel_address(self, tunnel_address):
        """Sets the tunnel_address of this XiqTunnelConcentrator.

        IP address/CIDR of listening interface.  # noqa: E501

        :param tunnel_address: The tunnel_address of this XiqTunnelConcentrator.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tunnel_address is None:  # noqa: E501
            raise ValueError("Invalid value for `tunnel_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tunnel_address is not None and not re.search(r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\/([1-9]|[12][0-9]|3[012])$', tunnel_address)):  # noqa: E501
            raise ValueError(r"Invalid value for `tunnel_address`, must be a follow pattern or equal to `/^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\/([1-9]|[12][0-9]|3[012])$/`")  # noqa: E501

        self._tunnel_address = tunnel_address

    @property
    def router_id(self):
        """Gets the router_id of this XiqTunnelConcentrator.  # noqa: E501

        Virtual Router group ID  # noqa: E501

        :return: The router_id of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this XiqTunnelConcentrator.

        Virtual Router group ID  # noqa: E501

        :param router_id: The router_id of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """

        self._router_id = router_id

    @property
    def gateway(self):
        """Gets the gateway of this XiqTunnelConcentrator.  # noqa: E501

        The TunnelConcentrator optional gateway ip address  # noqa: E501

        :return: The gateway of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this XiqTunnelConcentrator.

        The TunnelConcentrator optional gateway ip address  # noqa: E501

        :param gateway: The gateway of this XiqTunnelConcentrator.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def native_vlan(self):
        """Gets the native_vlan of this XiqTunnelConcentrator.  # noqa: E501

        Specifies which VLAN ID is transmitted untagged on the bridged interface.  # noqa: E501

        :return: The native_vlan of this XiqTunnelConcentrator.  # noqa: E501
        :rtype: int
        """
        return self._native_vlan

    @native_vlan.setter
    def native_vlan(self, native_vlan):
        """Sets the native_vlan of this XiqTunnelConcentrator.

        Specifies which VLAN ID is transmitted untagged on the bridged interface.  # noqa: E501

        :param native_vlan: The native_vlan of this XiqTunnelConcentrator.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and native_vlan is None:  # noqa: E501
            raise ValueError("Invalid value for `native_vlan`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                native_vlan is not None and native_vlan > 4094):  # noqa: E501
            raise ValueError("Invalid value for `native_vlan`, must be a value less than or equal to `4094`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                native_vlan is not None and native_vlan < 1):  # noqa: E501
            raise ValueError("Invalid value for `native_vlan`, must be a value greater than or equal to `1`")  # noqa: E501

        self._native_vlan = native_vlan

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
        if not isinstance(other, XiqTunnelConcentrator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqTunnelConcentrator):
            return True

        return self.to_dict() != other.to_dict()
