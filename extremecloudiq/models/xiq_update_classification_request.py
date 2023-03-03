# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUpdateClassificationRequest(object):
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
        'classification_type': 'str',
        'match': 'bool',
        'classification_type_id': 'int'
    }

    attribute_map = {
        'classification_type': 'classification_type',
        'match': 'match',
        'classification_type_id': 'classification_type_id'
    }

    def __init__(self, classification_type=None, match=None, classification_type_id=None, local_vars_configuration=None):  # noqa: E501
        """XiqUpdateClassificationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._classification_type = None
        self._match = None
        self._classification_type_id = None
        self.discriminator = None

        self.classification_type = classification_type
        self.match = match
        self.classification_type_id = classification_type_id

    @property
    def classification_type(self):
        """Gets the classification_type of this XiqUpdateClassificationRequest.  # noqa: E501

        Classification type  # noqa: E501

        :return: The classification_type of this XiqUpdateClassificationRequest.  # noqa: E501
        :rtype: str
        """
        return self._classification_type

    @classification_type.setter
    def classification_type(self, classification_type):
        """Sets the classification_type of this XiqUpdateClassificationRequest.

        Classification type  # noqa: E501

        :param classification_type: The classification_type of this XiqUpdateClassificationRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and classification_type is None:  # noqa: E501
            raise ValueError("Invalid value for `classification_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CLASSIFICATION_TYPE_UNSPECIFIED", "CLASSIFICATION_TYPE_LOCATION", "CLASSIFICATION_TYPE_CLOUD_CONFIG_GROUP", "CLASSIFICATION_TYPE_IP_ADDRESS", "CLASSIFICATION_TYPE_IP_SUBNET", "CLASSIFICATION_TYPE_IP_RANGE", "UNRECOGNIZED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and classification_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `classification_type` ({0}), must be one of {1}"  # noqa: E501
                .format(classification_type, allowed_values)
            )

        self._classification_type = classification_type

    @property
    def match(self):
        """Gets the match of this XiqUpdateClassificationRequest.  # noqa: E501

        Contains or not contains)  # noqa: E501

        :return: The match of this XiqUpdateClassificationRequest.  # noqa: E501
        :rtype: bool
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this XiqUpdateClassificationRequest.

        Contains or not contains)  # noqa: E501

        :param match: The match of this XiqUpdateClassificationRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and match is None:  # noqa: E501
            raise ValueError("Invalid value for `match`, must not be `None`")  # noqa: E501

        self._match = match

    @property
    def classification_type_id(self):
        """Gets the classification_type_id of this XiqUpdateClassificationRequest.  # noqa: E501

        The ID of location, cloud config group, IP address, IP subnet or IP range.  # noqa: E501

        :return: The classification_type_id of this XiqUpdateClassificationRequest.  # noqa: E501
        :rtype: int
        """
        return self._classification_type_id

    @classification_type_id.setter
    def classification_type_id(self, classification_type_id):
        """Sets the classification_type_id of this XiqUpdateClassificationRequest.

        The ID of location, cloud config group, IP address, IP subnet or IP range.  # noqa: E501

        :param classification_type_id: The classification_type_id of this XiqUpdateClassificationRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and classification_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `classification_type_id`, must not be `None`")  # noqa: E501

        self._classification_type_id = classification_type_id

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
        if not isinstance(other, XiqUpdateClassificationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUpdateClassificationRequest):
            return True

        return self.to_dict() != other.to_dict()
