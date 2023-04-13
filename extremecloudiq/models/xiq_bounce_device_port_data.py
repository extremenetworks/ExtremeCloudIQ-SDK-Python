# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.2.1.4
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqBounceDevicePortData(object):
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
        'status': 'int',
        'request_id': 'int',
        'results': 'list[XiqBounceDevicePortOperationResult]'
    }

    attribute_map = {
        'status': 'status',
        'request_id': 'request_id',
        'results': 'results'
    }

    def __init__(self, status=None, request_id=None, results=None, local_vars_configuration=None):  # noqa: E501
        """XiqBounceDevicePortData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._request_id = None
        self._results = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if request_id is not None:
            self.request_id = request_id
        if results is not None:
            self.results = results

    @property
    def status(self):
        """Gets the status of this XiqBounceDevicePortData.  # noqa: E501

        The status value  # noqa: E501

        :return: The status of this XiqBounceDevicePortData.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqBounceDevicePortData.

        The status value  # noqa: E501

        :param status: The status of this XiqBounceDevicePortData.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def request_id(self):
        """Gets the request_id of this XiqBounceDevicePortData.  # noqa: E501

        The requestId of the response  # noqa: E501

        :return: The request_id of this XiqBounceDevicePortData.  # noqa: E501
        :rtype: int
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this XiqBounceDevicePortData.

        The requestId of the response  # noqa: E501

        :param request_id: The request_id of this XiqBounceDevicePortData.  # noqa: E501
        :type: int
        """

        self._request_id = request_id

    @property
    def results(self):
        """Gets the results of this XiqBounceDevicePortData.  # noqa: E501

        The list of results  # noqa: E501

        :return: The results of this XiqBounceDevicePortData.  # noqa: E501
        :rtype: list[XiqBounceDevicePortOperationResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this XiqBounceDevicePortData.

        The list of results  # noqa: E501

        :param results: The results of this XiqBounceDevicePortData.  # noqa: E501
        :type: list[XiqBounceDevicePortOperationResult]
        """

        self._results = results

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
        if not isinstance(other, XiqBounceDevicePortData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqBounceDevicePortData):
            return True

        return self.to_dict() != other.to_dict()
