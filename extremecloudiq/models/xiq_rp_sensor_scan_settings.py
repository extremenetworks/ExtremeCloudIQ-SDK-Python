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


class XiqRpSensorScanSettings(object):
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
        'enable_scan_all_channels': 'bool',
        'dwell_time': 'str',
        'scan_channels': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enable_scan_all_channels': 'enable_scan_all_channels',
        'dwell_time': 'dwell_time',
        'scan_channels': 'scan_channels'
    }

    def __init__(self, id=None, create_time=None, update_time=None, enable_scan_all_channels=None, dwell_time=None, scan_channels=None, local_vars_configuration=None):  # noqa: E501
        """XiqRpSensorScanSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._enable_scan_all_channels = None
        self._dwell_time = None
        self._scan_channels = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if enable_scan_all_channels is not None:
            self.enable_scan_all_channels = enable_scan_all_channels
        if dwell_time is not None:
            self.dwell_time = dwell_time
        if scan_channels is not None:
            self.scan_channels = scan_channels

    @property
    def id(self):
        """Gets the id of this XiqRpSensorScanSettings.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRpSensorScanSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRpSensorScanSettings.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRpSensorScanSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRpSensorScanSettings.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRpSensorScanSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRpSensorScanSettings.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRpSensorScanSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRpSensorScanSettings.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRpSensorScanSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRpSensorScanSettings.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRpSensorScanSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def enable_scan_all_channels(self):
        """Gets the enable_scan_all_channels of this XiqRpSensorScanSettings.  # noqa: E501

        Whether to enable scanning all channels  # noqa: E501

        :return: The enable_scan_all_channels of this XiqRpSensorScanSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_scan_all_channels

    @enable_scan_all_channels.setter
    def enable_scan_all_channels(self, enable_scan_all_channels):
        """Sets the enable_scan_all_channels of this XiqRpSensorScanSettings.

        Whether to enable scanning all channels  # noqa: E501

        :param enable_scan_all_channels: The enable_scan_all_channels of this XiqRpSensorScanSettings.  # noqa: E501
        :type: bool
        """

        self._enable_scan_all_channels = enable_scan_all_channels

    @property
    def dwell_time(self):
        """Gets the dwell_time of this XiqRpSensorScanSettings.  # noqa: E501

        The dwell time in ms  # noqa: E501

        :return: The dwell_time of this XiqRpSensorScanSettings.  # noqa: E501
        :rtype: str
        """
        return self._dwell_time

    @dwell_time.setter
    def dwell_time(self, dwell_time):
        """Sets the dwell_time of this XiqRpSensorScanSettings.

        The dwell time in ms  # noqa: E501

        :param dwell_time: The dwell_time of this XiqRpSensorScanSettings.  # noqa: E501
        :type: str
        """

        self._dwell_time = dwell_time

    @property
    def scan_channels(self):
        """Gets the scan_channels of this XiqRpSensorScanSettings.  # noqa: E501

        The comma separated list of scan channels  # noqa: E501

        :return: The scan_channels of this XiqRpSensorScanSettings.  # noqa: E501
        :rtype: str
        """
        return self._scan_channels

    @scan_channels.setter
    def scan_channels(self, scan_channels):
        """Sets the scan_channels of this XiqRpSensorScanSettings.

        The comma separated list of scan channels  # noqa: E501

        :param scan_channels: The scan_channels of this XiqRpSensorScanSettings.  # noqa: E501
        :type: str
        """

        self._scan_channels = scan_channels

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
        if not isinstance(other, XiqRpSensorScanSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRpSensorScanSettings):
            return True

        return self.to_dict() != other.to_dict()
