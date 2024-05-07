# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.3.1.2
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqRpWmmQosSettings(object):
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
        'access_category': 'str',
        'arbitration_interframe_space': 'int',
        'min_contention_window': 'int',
        'max_contention_window': 'int',
        'transmission_opportunity_limit': 'int',
        'enable_no_ack': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'access_category': 'access_category',
        'arbitration_interframe_space': 'arbitration_interframe_space',
        'min_contention_window': 'min_contention_window',
        'max_contention_window': 'max_contention_window',
        'transmission_opportunity_limit': 'transmission_opportunity_limit',
        'enable_no_ack': 'enable_no_ack'
    }

    def __init__(self, id=None, create_time=None, update_time=None, access_category=None, arbitration_interframe_space=None, min_contention_window=None, max_contention_window=None, transmission_opportunity_limit=None, enable_no_ack=None, local_vars_configuration=None):  # noqa: E501
        """XiqRpWmmQosSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._access_category = None
        self._arbitration_interframe_space = None
        self._min_contention_window = None
        self._max_contention_window = None
        self._transmission_opportunity_limit = None
        self._enable_no_ack = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if access_category is not None:
            self.access_category = access_category
        if arbitration_interframe_space is not None:
            self.arbitration_interframe_space = arbitration_interframe_space
        if min_contention_window is not None:
            self.min_contention_window = min_contention_window
        if max_contention_window is not None:
            self.max_contention_window = max_contention_window
        if transmission_opportunity_limit is not None:
            self.transmission_opportunity_limit = transmission_opportunity_limit
        if enable_no_ack is not None:
            self.enable_no_ack = enable_no_ack

    @property
    def id(self):
        """Gets the id of this XiqRpWmmQosSettings.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqRpWmmQosSettings.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqRpWmmQosSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqRpWmmQosSettings.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqRpWmmQosSettings.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqRpWmmQosSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqRpWmmQosSettings.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqRpWmmQosSettings.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqRpWmmQosSettings.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def access_category(self):
        """Gets the access_category of this XiqRpWmmQosSettings.  # noqa: E501

        The media categories, including \"VOICE\", \"VIDEO\", \"BEST_EFFORT\", and \"BACKGROUND\"  # noqa: E501

        :return: The access_category of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: str
        """
        return self._access_category

    @access_category.setter
    def access_category(self, access_category):
        """Sets the access_category of this XiqRpWmmQosSettings.

        The media categories, including \"VOICE\", \"VIDEO\", \"BEST_EFFORT\", and \"BACKGROUND\"  # noqa: E501

        :param access_category: The access_category of this XiqRpWmmQosSettings.  # noqa: E501
        :type: str
        """

        self._access_category = access_category

    @property
    def arbitration_interframe_space(self):
        """Gets the arbitration_interframe_space of this XiqRpWmmQosSettings.  # noqa: E501

        The Arbitration Interframe space from 1 up to 15.  # noqa: E501

        :return: The arbitration_interframe_space of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: int
        """
        return self._arbitration_interframe_space

    @arbitration_interframe_space.setter
    def arbitration_interframe_space(self, arbitration_interframe_space):
        """Sets the arbitration_interframe_space of this XiqRpWmmQosSettings.

        The Arbitration Interframe space from 1 up to 15.  # noqa: E501

        :param arbitration_interframe_space: The arbitration_interframe_space of this XiqRpWmmQosSettings.  # noqa: E501
        :type: int
        """

        self._arbitration_interframe_space = arbitration_interframe_space

    @property
    def min_contention_window(self):
        """Gets the min_contention_window of this XiqRpWmmQosSettings.  # noqa: E501

        The Minimum Contention window from 1 up to 15.  # noqa: E501

        :return: The min_contention_window of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: int
        """
        return self._min_contention_window

    @min_contention_window.setter
    def min_contention_window(self, min_contention_window):
        """Sets the min_contention_window of this XiqRpWmmQosSettings.

        The Minimum Contention window from 1 up to 15.  # noqa: E501

        :param min_contention_window: The min_contention_window of this XiqRpWmmQosSettings.  # noqa: E501
        :type: int
        """

        self._min_contention_window = min_contention_window

    @property
    def max_contention_window(self):
        """Gets the max_contention_window of this XiqRpWmmQosSettings.  # noqa: E501

        The Maximum Contention window from 1 up to 15.  # noqa: E501

        :return: The max_contention_window of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_contention_window

    @max_contention_window.setter
    def max_contention_window(self, max_contention_window):
        """Sets the max_contention_window of this XiqRpWmmQosSettings.

        The Maximum Contention window from 1 up to 15.  # noqa: E501

        :param max_contention_window: The max_contention_window of this XiqRpWmmQosSettings.  # noqa: E501
        :type: int
        """

        self._max_contention_window = max_contention_window

    @property
    def transmission_opportunity_limit(self):
        """Gets the transmission_opportunity_limit of this XiqRpWmmQosSettings.  # noqa: E501

        The Transmission Opportunity limit from 0 up to 8192.  # noqa: E501

        :return: The transmission_opportunity_limit of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: int
        """
        return self._transmission_opportunity_limit

    @transmission_opportunity_limit.setter
    def transmission_opportunity_limit(self, transmission_opportunity_limit):
        """Sets the transmission_opportunity_limit of this XiqRpWmmQosSettings.

        The Transmission Opportunity limit from 0 up to 8192.  # noqa: E501

        :param transmission_opportunity_limit: The transmission_opportunity_limit of this XiqRpWmmQosSettings.  # noqa: E501
        :type: int
        """

        self._transmission_opportunity_limit = transmission_opportunity_limit

    @property
    def enable_no_ack(self):
        """Gets the enable_no_ack of this XiqRpWmmQosSettings.  # noqa: E501

        Whether to enable No Acknowledgment  # noqa: E501

        :return: The enable_no_ack of this XiqRpWmmQosSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enable_no_ack

    @enable_no_ack.setter
    def enable_no_ack(self, enable_no_ack):
        """Sets the enable_no_ack of this XiqRpWmmQosSettings.

        Whether to enable No Acknowledgment  # noqa: E501

        :param enable_no_ack: The enable_no_ack of this XiqRpWmmQosSettings.  # noqa: E501
        :type: bool
        """

        self._enable_no_ack = enable_no_ack

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
        if not isinstance(other, XiqRpWmmQosSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqRpWmmQosSettings):
            return True

        return self.to_dict() != other.to_dict()
