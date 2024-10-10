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


class XiqAfcApsInfoElement(object):
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
        'afc_status': 'XiqAfcStatusSummary',
        'geo_location': 'XiqAfcGeolocationSummary',
        'spectrum_mismatch': 'XiqSpectrumMismatchSummary'
    }

    attribute_map = {
        'afc_status': 'afc_status',
        'geo_location': 'geo_location',
        'spectrum_mismatch': 'spectrum_mismatch'
    }

    def __init__(self, afc_status=None, geo_location=None, spectrum_mismatch=None, local_vars_configuration=None):  # noqa: E501
        """XiqAfcApsInfoElement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._afc_status = None
        self._geo_location = None
        self._spectrum_mismatch = None
        self.discriminator = None

        if afc_status is not None:
            self.afc_status = afc_status
        if geo_location is not None:
            self.geo_location = geo_location
        if spectrum_mismatch is not None:
            self.spectrum_mismatch = spectrum_mismatch

    @property
    def afc_status(self):
        """Gets the afc_status of this XiqAfcApsInfoElement.  # noqa: E501


        :return: The afc_status of this XiqAfcApsInfoElement.  # noqa: E501
        :rtype: XiqAfcStatusSummary
        """
        return self._afc_status

    @afc_status.setter
    def afc_status(self, afc_status):
        """Sets the afc_status of this XiqAfcApsInfoElement.


        :param afc_status: The afc_status of this XiqAfcApsInfoElement.  # noqa: E501
        :type: XiqAfcStatusSummary
        """

        self._afc_status = afc_status

    @property
    def geo_location(self):
        """Gets the geo_location of this XiqAfcApsInfoElement.  # noqa: E501


        :return: The geo_location of this XiqAfcApsInfoElement.  # noqa: E501
        :rtype: XiqAfcGeolocationSummary
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """Sets the geo_location of this XiqAfcApsInfoElement.


        :param geo_location: The geo_location of this XiqAfcApsInfoElement.  # noqa: E501
        :type: XiqAfcGeolocationSummary
        """

        self._geo_location = geo_location

    @property
    def spectrum_mismatch(self):
        """Gets the spectrum_mismatch of this XiqAfcApsInfoElement.  # noqa: E501


        :return: The spectrum_mismatch of this XiqAfcApsInfoElement.  # noqa: E501
        :rtype: XiqSpectrumMismatchSummary
        """
        return self._spectrum_mismatch

    @spectrum_mismatch.setter
    def spectrum_mismatch(self, spectrum_mismatch):
        """Sets the spectrum_mismatch of this XiqAfcApsInfoElement.


        :param spectrum_mismatch: The spectrum_mismatch of this XiqAfcApsInfoElement.  # noqa: E501
        :type: XiqSpectrumMismatchSummary
        """

        self._spectrum_mismatch = spectrum_mismatch

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
        if not isinstance(other, XiqAfcApsInfoElement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAfcApsInfoElement):
            return True

        return self.to_dict() != other.to_dict()