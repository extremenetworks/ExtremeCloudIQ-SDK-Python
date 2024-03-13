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


class XiqAccountingLog(object):
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
        'username': 'str',
        'org_id': 'int',
        'timestamp': 'int',
        'vhm_id': 'str',
        'device_serial_number': 'str',
        'acct_session_id': 'str',
        'acct_multi_id': 'str',
        'group_name': 'str',
        'nas_ip_address': 'str',
        'nas_port': 'str',
        'nas_port_type': 'str',
        'acct_start_time': 'int',
        'acct_stop_time': 'int',
        'acct_session_time': 'int',
        'acct_authentic': 'str',
        'connect_info': 'str',
        'acct_input_octets': 'int',
        'acct_output_octets': 'int',
        'called_station_id': 'str',
        'calling_station_id': 'str',
        'acct_terminate_cause': 'str',
        'service_type': 'str',
        'framed_ip_address': 'str',
        'acct_start_delay': 'int',
        'acct_stop_delay': 'int',
        'ssid': 'str',
        'identity': 'str',
        'nas_identifier': 'str',
        'mgmt_mac_address': 'str',
        'attribute_num': 'int',
        'event_time': 'int',
        'usage': 'int'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'org_id': 'org_id',
        'timestamp': 'timestamp',
        'vhm_id': 'vhm_id',
        'device_serial_number': 'device_serial_number',
        'acct_session_id': 'acct_session_id',
        'acct_multi_id': 'acct_multi_id',
        'group_name': 'group_name',
        'nas_ip_address': 'nas_ip_address',
        'nas_port': 'nas_port',
        'nas_port_type': 'nas_port_type',
        'acct_start_time': 'acct_start_time',
        'acct_stop_time': 'acct_stop_time',
        'acct_session_time': 'acct_session_time',
        'acct_authentic': 'acct_authentic',
        'connect_info': 'connect_info',
        'acct_input_octets': 'acct_input_octets',
        'acct_output_octets': 'acct_output_octets',
        'called_station_id': 'called_station_id',
        'calling_station_id': 'calling_station_id',
        'acct_terminate_cause': 'acct_terminate_cause',
        'service_type': 'service_type',
        'framed_ip_address': 'framed_ip_address',
        'acct_start_delay': 'acct_start_delay',
        'acct_stop_delay': 'acct_stop_delay',
        'ssid': 'ssid',
        'identity': 'identity',
        'nas_identifier': 'nas_identifier',
        'mgmt_mac_address': 'mgmt_mac_address',
        'attribute_num': 'attribute_num',
        'event_time': 'event_time',
        'usage': 'usage'
    }

    def __init__(self, id=None, username=None, org_id=None, timestamp=None, vhm_id=None, device_serial_number=None, acct_session_id=None, acct_multi_id=None, group_name=None, nas_ip_address=None, nas_port=None, nas_port_type=None, acct_start_time=None, acct_stop_time=None, acct_session_time=None, acct_authentic=None, connect_info=None, acct_input_octets=None, acct_output_octets=None, called_station_id=None, calling_station_id=None, acct_terminate_cause=None, service_type=None, framed_ip_address=None, acct_start_delay=None, acct_stop_delay=None, ssid=None, identity=None, nas_identifier=None, mgmt_mac_address=None, attribute_num=None, event_time=None, usage=None, local_vars_configuration=None):  # noqa: E501
        """XiqAccountingLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._org_id = None
        self._timestamp = None
        self._vhm_id = None
        self._device_serial_number = None
        self._acct_session_id = None
        self._acct_multi_id = None
        self._group_name = None
        self._nas_ip_address = None
        self._nas_port = None
        self._nas_port_type = None
        self._acct_start_time = None
        self._acct_stop_time = None
        self._acct_session_time = None
        self._acct_authentic = None
        self._connect_info = None
        self._acct_input_octets = None
        self._acct_output_octets = None
        self._called_station_id = None
        self._calling_station_id = None
        self._acct_terminate_cause = None
        self._service_type = None
        self._framed_ip_address = None
        self._acct_start_delay = None
        self._acct_stop_delay = None
        self._ssid = None
        self._identity = None
        self._nas_identifier = None
        self._mgmt_mac_address = None
        self._attribute_num = None
        self._event_time = None
        self._usage = None
        self.discriminator = None

        self.id = id
        if username is not None:
            self.username = username
        if org_id is not None:
            self.org_id = org_id
        if timestamp is not None:
            self.timestamp = timestamp
        if vhm_id is not None:
            self.vhm_id = vhm_id
        if device_serial_number is not None:
            self.device_serial_number = device_serial_number
        if acct_session_id is not None:
            self.acct_session_id = acct_session_id
        if acct_multi_id is not None:
            self.acct_multi_id = acct_multi_id
        if group_name is not None:
            self.group_name = group_name
        if nas_ip_address is not None:
            self.nas_ip_address = nas_ip_address
        if nas_port is not None:
            self.nas_port = nas_port
        if nas_port_type is not None:
            self.nas_port_type = nas_port_type
        if acct_start_time is not None:
            self.acct_start_time = acct_start_time
        if acct_stop_time is not None:
            self.acct_stop_time = acct_stop_time
        if acct_session_time is not None:
            self.acct_session_time = acct_session_time
        if acct_authentic is not None:
            self.acct_authentic = acct_authentic
        if connect_info is not None:
            self.connect_info = connect_info
        if acct_input_octets is not None:
            self.acct_input_octets = acct_input_octets
        if acct_output_octets is not None:
            self.acct_output_octets = acct_output_octets
        if called_station_id is not None:
            self.called_station_id = called_station_id
        if calling_station_id is not None:
            self.calling_station_id = calling_station_id
        if acct_terminate_cause is not None:
            self.acct_terminate_cause = acct_terminate_cause
        if service_type is not None:
            self.service_type = service_type
        if framed_ip_address is not None:
            self.framed_ip_address = framed_ip_address
        if acct_start_delay is not None:
            self.acct_start_delay = acct_start_delay
        if acct_stop_delay is not None:
            self.acct_stop_delay = acct_stop_delay
        if ssid is not None:
            self.ssid = ssid
        if identity is not None:
            self.identity = identity
        if nas_identifier is not None:
            self.nas_identifier = nas_identifier
        if mgmt_mac_address is not None:
            self.mgmt_mac_address = mgmt_mac_address
        if attribute_num is not None:
            self.attribute_num = attribute_num
        if event_time is not None:
            self.event_time = event_time
        if usage is not None:
            self.usage = usage

    @property
    def id(self):
        """Gets the id of this XiqAccountingLog.  # noqa: E501

        The Accounting log id  # noqa: E501

        :return: The id of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqAccountingLog.

        The Accounting log id  # noqa: E501

        :param id: The id of this XiqAccountingLog.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this XiqAccountingLog.  # noqa: E501

        The username  # noqa: E501

        :return: The username of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this XiqAccountingLog.

        The username  # noqa: E501

        :param username: The username of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def org_id(self):
        """Gets the org_id of this XiqAccountingLog.  # noqa: E501

        The org id  # noqa: E501

        :return: The org_id of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqAccountingLog.

        The org id  # noqa: E501

        :param org_id: The org_id of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def timestamp(self):
        """Gets the timestamp of this XiqAccountingLog.  # noqa: E501

        The email log timestamp  # noqa: E501

        :return: The timestamp of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this XiqAccountingLog.

        The email log timestamp  # noqa: E501

        :param timestamp: The timestamp of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def vhm_id(self):
        """Gets the vhm_id of this XiqAccountingLog.  # noqa: E501

        The vhm id  # noqa: E501

        :return: The vhm_id of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._vhm_id

    @vhm_id.setter
    def vhm_id(self, vhm_id):
        """Sets the vhm_id of this XiqAccountingLog.

        The vhm id  # noqa: E501

        :param vhm_id: The vhm_id of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._vhm_id = vhm_id

    @property
    def device_serial_number(self):
        """Gets the device_serial_number of this XiqAccountingLog.  # noqa: E501

        The device serial number  # noqa: E501

        :return: The device_serial_number of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._device_serial_number

    @device_serial_number.setter
    def device_serial_number(self, device_serial_number):
        """Sets the device_serial_number of this XiqAccountingLog.

        The device serial number  # noqa: E501

        :param device_serial_number: The device_serial_number of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._device_serial_number = device_serial_number

    @property
    def acct_session_id(self):
        """Gets the acct_session_id of this XiqAccountingLog.  # noqa: E501

        The acct session id  # noqa: E501

        :return: The acct_session_id of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._acct_session_id

    @acct_session_id.setter
    def acct_session_id(self, acct_session_id):
        """Sets the acct_session_id of this XiqAccountingLog.

        The acct session id  # noqa: E501

        :param acct_session_id: The acct_session_id of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._acct_session_id = acct_session_id

    @property
    def acct_multi_id(self):
        """Gets the acct_multi_id of this XiqAccountingLog.  # noqa: E501

        The acct multi id  # noqa: E501

        :return: The acct_multi_id of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._acct_multi_id

    @acct_multi_id.setter
    def acct_multi_id(self, acct_multi_id):
        """Sets the acct_multi_id of this XiqAccountingLog.

        The acct multi id  # noqa: E501

        :param acct_multi_id: The acct_multi_id of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._acct_multi_id = acct_multi_id

    @property
    def group_name(self):
        """Gets the group_name of this XiqAccountingLog.  # noqa: E501

        The group name  # noqa: E501

        :return: The group_name of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this XiqAccountingLog.

        The group name  # noqa: E501

        :param group_name: The group_name of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._group_name = group_name

    @property
    def nas_ip_address(self):
        """Gets the nas_ip_address of this XiqAccountingLog.  # noqa: E501

        The nas ip address  # noqa: E501

        :return: The nas_ip_address of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._nas_ip_address

    @nas_ip_address.setter
    def nas_ip_address(self, nas_ip_address):
        """Sets the nas_ip_address of this XiqAccountingLog.

        The nas ip address  # noqa: E501

        :param nas_ip_address: The nas_ip_address of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._nas_ip_address = nas_ip_address

    @property
    def nas_port(self):
        """Gets the nas_port of this XiqAccountingLog.  # noqa: E501

        The nas port  # noqa: E501

        :return: The nas_port of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._nas_port

    @nas_port.setter
    def nas_port(self, nas_port):
        """Sets the nas_port of this XiqAccountingLog.

        The nas port  # noqa: E501

        :param nas_port: The nas_port of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._nas_port = nas_port

    @property
    def nas_port_type(self):
        """Gets the nas_port_type of this XiqAccountingLog.  # noqa: E501

        The nas port type  # noqa: E501

        :return: The nas_port_type of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._nas_port_type

    @nas_port_type.setter
    def nas_port_type(self, nas_port_type):
        """Sets the nas_port_type of this XiqAccountingLog.

        The nas port type  # noqa: E501

        :param nas_port_type: The nas_port_type of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._nas_port_type = nas_port_type

    @property
    def acct_start_time(self):
        """Gets the acct_start_time of this XiqAccountingLog.  # noqa: E501

        The acct start time  # noqa: E501

        :return: The acct_start_time of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_start_time

    @acct_start_time.setter
    def acct_start_time(self, acct_start_time):
        """Sets the acct_start_time of this XiqAccountingLog.

        The acct start time  # noqa: E501

        :param acct_start_time: The acct_start_time of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_start_time = acct_start_time

    @property
    def acct_stop_time(self):
        """Gets the acct_stop_time of this XiqAccountingLog.  # noqa: E501

        The acct stop time  # noqa: E501

        :return: The acct_stop_time of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_stop_time

    @acct_stop_time.setter
    def acct_stop_time(self, acct_stop_time):
        """Sets the acct_stop_time of this XiqAccountingLog.

        The acct stop time  # noqa: E501

        :param acct_stop_time: The acct_stop_time of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_stop_time = acct_stop_time

    @property
    def acct_session_time(self):
        """Gets the acct_session_time of this XiqAccountingLog.  # noqa: E501

        The acct session time  # noqa: E501

        :return: The acct_session_time of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_session_time

    @acct_session_time.setter
    def acct_session_time(self, acct_session_time):
        """Sets the acct_session_time of this XiqAccountingLog.

        The acct session time  # noqa: E501

        :param acct_session_time: The acct_session_time of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_session_time = acct_session_time

    @property
    def acct_authentic(self):
        """Gets the acct_authentic of this XiqAccountingLog.  # noqa: E501

        The acct authentic  # noqa: E501

        :return: The acct_authentic of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._acct_authentic

    @acct_authentic.setter
    def acct_authentic(self, acct_authentic):
        """Sets the acct_authentic of this XiqAccountingLog.

        The acct authentic  # noqa: E501

        :param acct_authentic: The acct_authentic of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._acct_authentic = acct_authentic

    @property
    def connect_info(self):
        """Gets the connect_info of this XiqAccountingLog.  # noqa: E501

        The connect info  # noqa: E501

        :return: The connect_info of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._connect_info

    @connect_info.setter
    def connect_info(self, connect_info):
        """Sets the connect_info of this XiqAccountingLog.

        The connect info  # noqa: E501

        :param connect_info: The connect_info of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._connect_info = connect_info

    @property
    def acct_input_octets(self):
        """Gets the acct_input_octets of this XiqAccountingLog.  # noqa: E501

        The acct input octets  # noqa: E501

        :return: The acct_input_octets of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_input_octets

    @acct_input_octets.setter
    def acct_input_octets(self, acct_input_octets):
        """Sets the acct_input_octets of this XiqAccountingLog.

        The acct input octets  # noqa: E501

        :param acct_input_octets: The acct_input_octets of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_input_octets = acct_input_octets

    @property
    def acct_output_octets(self):
        """Gets the acct_output_octets of this XiqAccountingLog.  # noqa: E501

        The acct output octets  # noqa: E501

        :return: The acct_output_octets of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_output_octets

    @acct_output_octets.setter
    def acct_output_octets(self, acct_output_octets):
        """Sets the acct_output_octets of this XiqAccountingLog.

        The acct output octets  # noqa: E501

        :param acct_output_octets: The acct_output_octets of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_output_octets = acct_output_octets

    @property
    def called_station_id(self):
        """Gets the called_station_id of this XiqAccountingLog.  # noqa: E501

        The called station id  # noqa: E501

        :return: The called_station_id of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._called_station_id

    @called_station_id.setter
    def called_station_id(self, called_station_id):
        """Sets the called_station_id of this XiqAccountingLog.

        The called station id  # noqa: E501

        :param called_station_id: The called_station_id of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._called_station_id = called_station_id

    @property
    def calling_station_id(self):
        """Gets the calling_station_id of this XiqAccountingLog.  # noqa: E501

        The calling station id  # noqa: E501

        :return: The calling_station_id of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._calling_station_id

    @calling_station_id.setter
    def calling_station_id(self, calling_station_id):
        """Sets the calling_station_id of this XiqAccountingLog.

        The calling station id  # noqa: E501

        :param calling_station_id: The calling_station_id of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._calling_station_id = calling_station_id

    @property
    def acct_terminate_cause(self):
        """Gets the acct_terminate_cause of this XiqAccountingLog.  # noqa: E501

        The acct terminate cause  # noqa: E501

        :return: The acct_terminate_cause of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._acct_terminate_cause

    @acct_terminate_cause.setter
    def acct_terminate_cause(self, acct_terminate_cause):
        """Sets the acct_terminate_cause of this XiqAccountingLog.

        The acct terminate cause  # noqa: E501

        :param acct_terminate_cause: The acct_terminate_cause of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._acct_terminate_cause = acct_terminate_cause

    @property
    def service_type(self):
        """Gets the service_type of this XiqAccountingLog.  # noqa: E501

        The service type  # noqa: E501

        :return: The service_type of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this XiqAccountingLog.

        The service type  # noqa: E501

        :param service_type: The service_type of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def framed_ip_address(self):
        """Gets the framed_ip_address of this XiqAccountingLog.  # noqa: E501

        The framed ip address  # noqa: E501

        :return: The framed_ip_address of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._framed_ip_address

    @framed_ip_address.setter
    def framed_ip_address(self, framed_ip_address):
        """Sets the framed_ip_address of this XiqAccountingLog.

        The framed ip address  # noqa: E501

        :param framed_ip_address: The framed_ip_address of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._framed_ip_address = framed_ip_address

    @property
    def acct_start_delay(self):
        """Gets the acct_start_delay of this XiqAccountingLog.  # noqa: E501

        The acct start delay  # noqa: E501

        :return: The acct_start_delay of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_start_delay

    @acct_start_delay.setter
    def acct_start_delay(self, acct_start_delay):
        """Sets the acct_start_delay of this XiqAccountingLog.

        The acct start delay  # noqa: E501

        :param acct_start_delay: The acct_start_delay of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_start_delay = acct_start_delay

    @property
    def acct_stop_delay(self):
        """Gets the acct_stop_delay of this XiqAccountingLog.  # noqa: E501

        The acct stop delay  # noqa: E501

        :return: The acct_stop_delay of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._acct_stop_delay

    @acct_stop_delay.setter
    def acct_stop_delay(self, acct_stop_delay):
        """Sets the acct_stop_delay of this XiqAccountingLog.

        The acct stop delay  # noqa: E501

        :param acct_stop_delay: The acct_stop_delay of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._acct_stop_delay = acct_stop_delay

    @property
    def ssid(self):
        """Gets the ssid of this XiqAccountingLog.  # noqa: E501

        The ssid  # noqa: E501

        :return: The ssid of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this XiqAccountingLog.

        The ssid  # noqa: E501

        :param ssid: The ssid of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    @property
    def identity(self):
        """Gets the identity of this XiqAccountingLog.  # noqa: E501

        The identity  # noqa: E501

        :return: The identity of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this XiqAccountingLog.

        The identity  # noqa: E501

        :param identity: The identity of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def nas_identifier(self):
        """Gets the nas_identifier of this XiqAccountingLog.  # noqa: E501

        The nas identifier  # noqa: E501

        :return: The nas_identifier of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._nas_identifier

    @nas_identifier.setter
    def nas_identifier(self, nas_identifier):
        """Sets the nas_identifier of this XiqAccountingLog.

        The nas identifier  # noqa: E501

        :param nas_identifier: The nas_identifier of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._nas_identifier = nas_identifier

    @property
    def mgmt_mac_address(self):
        """Gets the mgmt_mac_address of this XiqAccountingLog.  # noqa: E501

        The management mac address  # noqa: E501

        :return: The mgmt_mac_address of this XiqAccountingLog.  # noqa: E501
        :rtype: str
        """
        return self._mgmt_mac_address

    @mgmt_mac_address.setter
    def mgmt_mac_address(self, mgmt_mac_address):
        """Sets the mgmt_mac_address of this XiqAccountingLog.

        The management mac address  # noqa: E501

        :param mgmt_mac_address: The mgmt_mac_address of this XiqAccountingLog.  # noqa: E501
        :type: str
        """

        self._mgmt_mac_address = mgmt_mac_address

    @property
    def attribute_num(self):
        """Gets the attribute_num of this XiqAccountingLog.  # noqa: E501

        The attribute num  # noqa: E501

        :return: The attribute_num of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._attribute_num

    @attribute_num.setter
    def attribute_num(self, attribute_num):
        """Sets the attribute_num of this XiqAccountingLog.

        The attribute num  # noqa: E501

        :param attribute_num: The attribute_num of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._attribute_num = attribute_num

    @property
    def event_time(self):
        """Gets the event_time of this XiqAccountingLog.  # noqa: E501

        The event time  # noqa: E501

        :return: The event_time of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this XiqAccountingLog.

        The event time  # noqa: E501

        :param event_time: The event_time of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._event_time = event_time

    @property
    def usage(self):
        """Gets the usage of this XiqAccountingLog.  # noqa: E501

        The usage  # noqa: E501

        :return: The usage of this XiqAccountingLog.  # noqa: E501
        :rtype: int
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this XiqAccountingLog.

        The usage  # noqa: E501

        :param usage: The usage of this XiqAccountingLog.  # noqa: E501
        :type: int
        """

        self._usage = usage

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
        if not isinstance(other, XiqAccountingLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAccountingLog):
            return True

        return self.to_dict() != other.to_dict()
