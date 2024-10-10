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


class XiqPacketCapture(object):
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
        'start_time': 'datetime',
        'end_time': 'datetime',
        'org_id': 'int',
        'name': 'str',
        'duration': 'int',
        'capture_id_type': 'XiqCaptureIdentifierType',
        'ap_serial_number': 'str',
        'device_ids': 'list[int]',
        'location_id': 'int',
        'destination': 'XiqDestinationType',
        'filter': 'XiqCaptureFilter',
        'capture_if': 'XiqCaptureLocation',
        'status': 'XiqPacketCaptureStatus',
        'results': 'list[XiqCaptureResult]',
        'cloud_storage': 'str'
    }

    attribute_map = {
        'id': 'id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'org_id': 'org_id',
        'name': 'name',
        'duration': 'duration',
        'capture_id_type': 'capture_id_type',
        'ap_serial_number': 'ap_serial_number',
        'device_ids': 'device_ids',
        'location_id': 'location_id',
        'destination': 'destination',
        'filter': 'filter',
        'capture_if': 'capture_if',
        'status': 'status',
        'results': 'results',
        'cloud_storage': 'cloud_storage'
    }

    def __init__(self, id=None, start_time=None, end_time=None, org_id=None, name=None, duration=None, capture_id_type=None, ap_serial_number=None, device_ids=None, location_id=None, destination=None, filter=None, capture_if=None, status=None, results=None, cloud_storage=None, local_vars_configuration=None):  # noqa: E501
        """XiqPacketCapture - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._start_time = None
        self._end_time = None
        self._org_id = None
        self._name = None
        self._duration = None
        self._capture_id_type = None
        self._ap_serial_number = None
        self._device_ids = None
        self._location_id = None
        self._destination = None
        self._filter = None
        self._capture_if = None
        self._status = None
        self._results = None
        self._cloud_storage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        if capture_id_type is not None:
            self.capture_id_type = capture_id_type
        if ap_serial_number is not None:
            self.ap_serial_number = ap_serial_number
        if device_ids is not None:
            self.device_ids = device_ids
        if location_id is not None:
            self.location_id = location_id
        if destination is not None:
            self.destination = destination
        if filter is not None:
            self.filter = filter
        if capture_if is not None:
            self.capture_if = capture_if
        if status is not None:
            self.status = status
        if results is not None:
            self.results = results
        if cloud_storage is not None:
            self.cloud_storage = cloud_storage

    @property
    def id(self):
        """Gets the id of this XiqPacketCapture.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqPacketCapture.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqPacketCapture.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqPacketCapture.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def start_time(self):
        """Gets the start_time of this XiqPacketCapture.  # noqa: E501

        The packet capture start time  # noqa: E501

        :return: The start_time of this XiqPacketCapture.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this XiqPacketCapture.

        The packet capture start time  # noqa: E501

        :param start_time: The start_time of this XiqPacketCapture.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this XiqPacketCapture.  # noqa: E501

        The packet capture end time  # noqa: E501

        :return: The end_time of this XiqPacketCapture.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this XiqPacketCapture.

        The packet capture end time  # noqa: E501

        :param end_time: The end_time of this XiqPacketCapture.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqPacketCapture.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqPacketCapture.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqPacketCapture.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqPacketCapture.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqPacketCapture.  # noqa: E501

        The packet capture session name. If the name is null or empty, it will be auto generated.  # noqa: E501

        :return: The name of this XiqPacketCapture.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqPacketCapture.

        The packet capture session name. If the name is null or empty, it will be auto generated.  # noqa: E501

        :param name: The name of this XiqPacketCapture.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def duration(self):
        """Gets the duration of this XiqPacketCapture.  # noqa: E501

        An integer containing the set packet capture duration in seconds, from 5 to a maximum of 604800 seconds (1 week). If duration is set to 0 or unspecified, capture stops when platform-maximum size is reached.  # noqa: E501

        :return: The duration of this XiqPacketCapture.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this XiqPacketCapture.

        An integer containing the set packet capture duration in seconds, from 5 to a maximum of 604800 seconds (1 week). If duration is set to 0 or unspecified, capture stops when platform-maximum size is reached.  # noqa: E501

        :param duration: The duration of this XiqPacketCapture.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration > 604800):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value less than or equal to `604800`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and duration < 0):  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration = duration

    @property
    def capture_id_type(self):
        """Gets the capture_id_type of this XiqPacketCapture.  # noqa: E501


        :return: The capture_id_type of this XiqPacketCapture.  # noqa: E501
        :rtype: XiqCaptureIdentifierType
        """
        return self._capture_id_type

    @capture_id_type.setter
    def capture_id_type(self, capture_id_type):
        """Sets the capture_id_type of this XiqPacketCapture.


        :param capture_id_type: The capture_id_type of this XiqPacketCapture.  # noqa: E501
        :type: XiqCaptureIdentifierType
        """

        self._capture_id_type = capture_id_type

    @property
    def ap_serial_number(self):
        """Gets the ap_serial_number of this XiqPacketCapture.  # noqa: E501

        The globally unique serial number of the device being registered. The serial number is represented as a string.  # noqa: E501

        :return: The ap_serial_number of this XiqPacketCapture.  # noqa: E501
        :rtype: str
        """
        return self._ap_serial_number

    @ap_serial_number.setter
    def ap_serial_number(self, ap_serial_number):
        """Sets the ap_serial_number of this XiqPacketCapture.

        The globally unique serial number of the device being registered. The serial number is represented as a string.  # noqa: E501

        :param ap_serial_number: The ap_serial_number of this XiqPacketCapture.  # noqa: E501
        :type: str
        """

        self._ap_serial_number = ap_serial_number

    @property
    def device_ids(self):
        """Gets the device_ids of this XiqPacketCapture.  # noqa: E501

        The device ID list.  # noqa: E501

        :return: The device_ids of this XiqPacketCapture.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_ids

    @device_ids.setter
    def device_ids(self, device_ids):
        """Sets the device_ids of this XiqPacketCapture.

        The device ID list.  # noqa: E501

        :param device_ids: The device_ids of this XiqPacketCapture.  # noqa: E501
        :type: list[int]
        """

        self._device_ids = device_ids

    @property
    def location_id(self):
        """Gets the location_id of this XiqPacketCapture.  # noqa: E501

        The assigned location ID, it must be FLOOR type  # noqa: E501

        :return: The location_id of this XiqPacketCapture.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this XiqPacketCapture.

        The assigned location ID, it must be FLOOR type  # noqa: E501

        :param location_id: The location_id of this XiqPacketCapture.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def destination(self):
        """Gets the destination of this XiqPacketCapture.  # noqa: E501


        :return: The destination of this XiqPacketCapture.  # noqa: E501
        :rtype: XiqDestinationType
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this XiqPacketCapture.


        :param destination: The destination of this XiqPacketCapture.  # noqa: E501
        :type: XiqDestinationType
        """

        self._destination = destination

    @property
    def filter(self):
        """Gets the filter of this XiqPacketCapture.  # noqa: E501


        :return: The filter of this XiqPacketCapture.  # noqa: E501
        :rtype: XiqCaptureFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this XiqPacketCapture.


        :param filter: The filter of this XiqPacketCapture.  # noqa: E501
        :type: XiqCaptureFilter
        """

        self._filter = filter

    @property
    def capture_if(self):
        """Gets the capture_if of this XiqPacketCapture.  # noqa: E501


        :return: The capture_if of this XiqPacketCapture.  # noqa: E501
        :rtype: XiqCaptureLocation
        """
        return self._capture_if

    @capture_if.setter
    def capture_if(self, capture_if):
        """Sets the capture_if of this XiqPacketCapture.


        :param capture_if: The capture_if of this XiqPacketCapture.  # noqa: E501
        :type: XiqCaptureLocation
        """

        self._capture_if = capture_if

    @property
    def status(self):
        """Gets the status of this XiqPacketCapture.  # noqa: E501


        :return: The status of this XiqPacketCapture.  # noqa: E501
        :rtype: XiqPacketCaptureStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqPacketCapture.


        :param status: The status of this XiqPacketCapture.  # noqa: E501
        :type: XiqPacketCaptureStatus
        """

        self._status = status

    @property
    def results(self):
        """Gets the results of this XiqPacketCapture.  # noqa: E501

        The list of packet capture results - a PacketCaptureResult for each device's interface  # noqa: E501

        :return: The results of this XiqPacketCapture.  # noqa: E501
        :rtype: list[XiqCaptureResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this XiqPacketCapture.

        The list of packet capture results - a PacketCaptureResult for each device's interface  # noqa: E501

        :param results: The results of this XiqPacketCapture.  # noqa: E501
        :type: list[XiqCaptureResult]
        """

        self._results = results

    @property
    def cloud_storage(self):
        """Gets the cloud_storage of this XiqPacketCapture.  # noqa: E501

        XIQ cloud storage location for the archive of all capture files in this capture session, if available.  # noqa: E501

        :return: The cloud_storage of this XiqPacketCapture.  # noqa: E501
        :rtype: str
        """
        return self._cloud_storage

    @cloud_storage.setter
    def cloud_storage(self, cloud_storage):
        """Sets the cloud_storage of this XiqPacketCapture.

        XIQ cloud storage location for the archive of all capture files in this capture session, if available.  # noqa: E501

        :param cloud_storage: The cloud_storage of this XiqPacketCapture.  # noqa: E501
        :type: str
        """

        self._cloud_storage = cloud_storage

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
        if not isinstance(other, XiqPacketCapture):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqPacketCapture):
            return True

        return self.to_dict() != other.to_dict()
