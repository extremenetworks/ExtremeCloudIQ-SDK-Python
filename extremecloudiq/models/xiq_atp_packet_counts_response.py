# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.6.0.46
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAtpPacketCountsResponse(object):
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
        'summary': 'str',
        'atp_packet_counts_entities': 'list[XiqAtpPacketCountsEntity]'
    }

    attribute_map = {
        'summary': 'summary',
        'atp_packet_counts_entities': 'atp_packet_counts_entities'
    }

    def __init__(self, summary=None, atp_packet_counts_entities=None, local_vars_configuration=None):  # noqa: E501
        """XiqAtpPacketCountsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._summary = None
        self._atp_packet_counts_entities = None
        self.discriminator = None

        if summary is not None:
            self.summary = summary
        if atp_packet_counts_entities is not None:
            self.atp_packet_counts_entities = atp_packet_counts_entities

    @property
    def summary(self):
        """Gets the summary of this XiqAtpPacketCountsResponse.  # noqa: E501

        the anomaly location  # noqa: E501

        :return: The summary of this XiqAtpPacketCountsResponse.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this XiqAtpPacketCountsResponse.

        the anomaly location  # noqa: E501

        :param summary: The summary of this XiqAtpPacketCountsResponse.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def atp_packet_counts_entities(self):
        """Gets the atp_packet_counts_entities of this XiqAtpPacketCountsResponse.  # noqa: E501

        the anomaly device data  # noqa: E501

        :return: The atp_packet_counts_entities of this XiqAtpPacketCountsResponse.  # noqa: E501
        :rtype: list[XiqAtpPacketCountsEntity]
        """
        return self._atp_packet_counts_entities

    @atp_packet_counts_entities.setter
    def atp_packet_counts_entities(self, atp_packet_counts_entities):
        """Sets the atp_packet_counts_entities of this XiqAtpPacketCountsResponse.

        the anomaly device data  # noqa: E501

        :param atp_packet_counts_entities: The atp_packet_counts_entities of this XiqAtpPacketCountsResponse.  # noqa: E501
        :type: list[XiqAtpPacketCountsEntity]
        """

        self._atp_packet_counts_entities = atp_packet_counts_entities

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
        if not isinstance(other, XiqAtpPacketCountsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAtpPacketCountsResponse):
            return True

        return self.to_dict() != other.to_dict()
