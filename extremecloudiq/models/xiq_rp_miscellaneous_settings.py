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


class XiqRpMiscellaneousSettings(object):
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
        'sla_throughput_level': 'str',
        'radio_range': 'int',
        'wmm_qos_settings': 'list[XiqRpWmmQosSettings]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'sla_throughput_level': 'sla_throughput_level',
        'radio_range': 'radio_range',
        'wmm_qos_settings': 'wmm_qos_settings'
    }

    def __init__(self, id=None, create_time=None, update_time=None, sla_throughput_level=None, radio_range=None, wmm_qos_settings=None, local_vars_configuration=None):  # noqa: E501
        """XiqRpMiscellaneousSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._sla_throughput_level = None
        self._radio_range = None
        self._wmm_qos_settings = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if sla_throughput_level is not None:
            self.sla_throughput_level = sla_throughput_level
        if radio_range is not None:
            self.radio_range = radio_range
        if wmm_qos_settings is not None:
            self.wmm_qos_settings = wmm_qos_settings

    @property
    def id(self):
        """Gets the id of this XiqRpMiscellaneousSettings.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRpMiscellaneousSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRpMiscellaneousSettings.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRpMiscellaneousSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRpMiscellaneousSettings.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRpMiscellaneousSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRpMiscellaneousSettings.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRpMiscellaneousSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRpMiscellaneousSettings.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRpMiscellaneousSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRpMiscellaneousSettings.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRpMiscellaneousSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def sla_throughput_level(self):
        """Gets the sla_throughput_level of this XiqRpMiscellaneousSettings.  # noqa: E501

        The Client SLA options -- \"NORMAL_DENSITY\", \"HIGH_DENSITY\" (performance-oriented), or \"LOW_DENSITY\" (coverage-oriented)  # noqa: E501

        :return: The sla_throughput_level of this XiqRpMiscellaneousSettings.  # noqa: E501
        :rtype: str
        """
        return self._sla_throughput_level

    @sla_throughput_level.setter
    def sla_throughput_level(self, sla_throughput_level):
        """Sets the sla_throughput_level of this XiqRpMiscellaneousSettings.

        The Client SLA options -- \"NORMAL_DENSITY\", \"HIGH_DENSITY\" (performance-oriented), or \"LOW_DENSITY\" (coverage-oriented)  # noqa: E501

        :param sla_throughput_level: The sla_throughput_level of this XiqRpMiscellaneousSettings.  # noqa: E501
        :type: str
        """

        self._sla_throughput_level = sla_throughput_level

    @property
    def radio_range(self):
        """Gets the radio_range of this XiqRpMiscellaneousSettings.  # noqa: E501

        The Outdoor Deployment for signal distance from 300 to 10000 meters  # noqa: E501

        :return: The radio_range of this XiqRpMiscellaneousSettings.  # noqa: E501
        :rtype: int
        """
        return self._radio_range

    @radio_range.setter
    def radio_range(self, radio_range):
        """Sets the radio_range of this XiqRpMiscellaneousSettings.

        The Outdoor Deployment for signal distance from 300 to 10000 meters  # noqa: E501

        :param radio_range: The radio_range of this XiqRpMiscellaneousSettings.  # noqa: E501
        :type: int
        """

        self._radio_range = radio_range

    @property
    def wmm_qos_settings(self):
        """Gets the wmm_qos_settings of this XiqRpMiscellaneousSettings.  # noqa: E501

        The WMM QoS settings for various media types  # noqa: E501

        :return: The wmm_qos_settings of this XiqRpMiscellaneousSettings.  # noqa: E501
        :rtype: list[XiqRpWmmQosSettings]
        """
        return self._wmm_qos_settings

    @wmm_qos_settings.setter
    def wmm_qos_settings(self, wmm_qos_settings):
        """Sets the wmm_qos_settings of this XiqRpMiscellaneousSettings.

        The WMM QoS settings for various media types  # noqa: E501

        :param wmm_qos_settings: The wmm_qos_settings of this XiqRpMiscellaneousSettings.  # noqa: E501
        :type: list[XiqRpWmmQosSettings]
        """

        self._wmm_qos_settings = wmm_qos_settings

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
        if not isinstance(other, XiqRpMiscellaneousSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRpMiscellaneousSettings):
            return True

        return self.to_dict() != other.to_dict()
