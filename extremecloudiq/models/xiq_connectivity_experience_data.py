# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.1.0.65
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqConnectivityExperienceData(object):
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
        'id': 'str',
        'info': 'str',
        'name': 'str',
        'quality_index': 'int',
        'quality_index_value': 'XiqQualityIndex',
        'client_type': 'XiqClientType',
        'trend_indicator': 'XiqTrendIndicator',
        'quality_index_graph': 'list[XiqDataPoint]'
    }

    attribute_map = {
        'id': 'id',
        'info': 'info',
        'name': 'name',
        'quality_index': 'quality_index',
        'quality_index_value': 'quality_index_value',
        'client_type': 'client_type',
        'trend_indicator': 'trend_indicator',
        'quality_index_graph': 'quality_index_graph'
    }

    def __init__(self, id=None, info=None, name=None, quality_index=None, quality_index_value=None, client_type=None, trend_indicator=None, quality_index_graph=None, local_vars_configuration=None):  # noqa: E501
        """XiqConnectivityExperienceData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._info = None
        self._name = None
        self._quality_index = None
        self._quality_index_value = None
        self._client_type = None
        self._trend_indicator = None
        self._quality_index_graph = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if info is not None:
            self.info = info
        self.name = name
        self.quality_index = quality_index
        self.quality_index_value = quality_index_value
        self.client_type = client_type
        self.trend_indicator = trend_indicator
        self.quality_index_graph = quality_index_graph

    @property
    def id(self):
        """Gets the id of this XiqConnectivityExperienceData.  # noqa: E501

        the unique identifier  # noqa: E501

        :return: The id of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqConnectivityExperienceData.

        the unique identifier  # noqa: E501

        :param id: The id of this XiqConnectivityExperienceData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def info(self):
        """Gets the info of this XiqConnectivityExperienceData.  # noqa: E501

        the info related to connectivity experience view type  # noqa: E501

        :return: The info of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this XiqConnectivityExperienceData.

        the info related to connectivity experience view type  # noqa: E501

        :param info: The info of this XiqConnectivityExperienceData.  # noqa: E501
        :type: str
        """

        self._info = info

    @property
    def name(self):
        """Gets the name of this XiqConnectivityExperienceData.  # noqa: E501

        the location/ssid/os-name based on view type  # noqa: E501

        :return: The name of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqConnectivityExperienceData.

        the location/ssid/os-name based on view type  # noqa: E501

        :param name: The name of this XiqConnectivityExperienceData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def quality_index(self):
        """Gets the quality_index of this XiqConnectivityExperienceData.  # noqa: E501

        the quality index  # noqa: E501

        :return: The quality_index of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: int
        """
        return self._quality_index

    @quality_index.setter
    def quality_index(self, quality_index):
        """Sets the quality_index of this XiqConnectivityExperienceData.

        the quality index  # noqa: E501

        :param quality_index: The quality_index of this XiqConnectivityExperienceData.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and quality_index is None:  # noqa: E501
            raise ValueError("Invalid value for `quality_index`, must not be `None`")  # noqa: E501

        self._quality_index = quality_index

    @property
    def quality_index_value(self):
        """Gets the quality_index_value of this XiqConnectivityExperienceData.  # noqa: E501


        :return: The quality_index_value of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: XiqQualityIndex
        """
        return self._quality_index_value

    @quality_index_value.setter
    def quality_index_value(self, quality_index_value):
        """Sets the quality_index_value of this XiqConnectivityExperienceData.


        :param quality_index_value: The quality_index_value of this XiqConnectivityExperienceData.  # noqa: E501
        :type: XiqQualityIndex
        """
        if self.local_vars_configuration.client_side_validation and quality_index_value is None:  # noqa: E501
            raise ValueError("Invalid value for `quality_index_value`, must not be `None`")  # noqa: E501

        self._quality_index_value = quality_index_value

    @property
    def client_type(self):
        """Gets the client_type of this XiqConnectivityExperienceData.  # noqa: E501


        :return: The client_type of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: XiqClientType
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this XiqConnectivityExperienceData.


        :param client_type: The client_type of this XiqConnectivityExperienceData.  # noqa: E501
        :type: XiqClientType
        """
        if self.local_vars_configuration.client_side_validation and client_type is None:  # noqa: E501
            raise ValueError("Invalid value for `client_type`, must not be `None`")  # noqa: E501

        self._client_type = client_type

    @property
    def trend_indicator(self):
        """Gets the trend_indicator of this XiqConnectivityExperienceData.  # noqa: E501


        :return: The trend_indicator of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: XiqTrendIndicator
        """
        return self._trend_indicator

    @trend_indicator.setter
    def trend_indicator(self, trend_indicator):
        """Sets the trend_indicator of this XiqConnectivityExperienceData.


        :param trend_indicator: The trend_indicator of this XiqConnectivityExperienceData.  # noqa: E501
        :type: XiqTrendIndicator
        """
        if self.local_vars_configuration.client_side_validation and trend_indicator is None:  # noqa: E501
            raise ValueError("Invalid value for `trend_indicator`, must not be `None`")  # noqa: E501

        self._trend_indicator = trend_indicator

    @property
    def quality_index_graph(self):
        """Gets the quality_index_graph of this XiqConnectivityExperienceData.  # noqa: E501

        the quality index graph  # noqa: E501

        :return: The quality_index_graph of this XiqConnectivityExperienceData.  # noqa: E501
        :rtype: list[XiqDataPoint]
        """
        return self._quality_index_graph

    @quality_index_graph.setter
    def quality_index_graph(self, quality_index_graph):
        """Sets the quality_index_graph of this XiqConnectivityExperienceData.

        the quality index graph  # noqa: E501

        :param quality_index_graph: The quality_index_graph of this XiqConnectivityExperienceData.  # noqa: E501
        :type: list[XiqDataPoint]
        """
        if self.local_vars_configuration.client_side_validation and quality_index_graph is None:  # noqa: E501
            raise ValueError("Invalid value for `quality_index_graph`, must not be `None`")  # noqa: E501

        self._quality_index_graph = quality_index_graph

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
        if not isinstance(other, XiqConnectivityExperienceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqConnectivityExperienceData):
            return True

        return self.to_dict() != other.to_dict()
