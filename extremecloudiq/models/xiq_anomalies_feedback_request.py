# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.4.0.61
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqAnomaliesFeedbackRequest(object):
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
        'anomaly_type': 'XiqAnomalyType',
        'anomaly_id': 'str',
        'feedback_type': 'XiqFeedbackType',
        'feedback': 'str'
    }

    attribute_map = {
        'anomaly_type': 'anomaly_type',
        'anomaly_id': 'anomaly_id',
        'feedback_type': 'feedback_type',
        'feedback': 'feedback'
    }

    def __init__(self, anomaly_type=None, anomaly_id=None, feedback_type=None, feedback=None, local_vars_configuration=None):  # noqa: E501
        """XiqAnomaliesFeedbackRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._anomaly_type = None
        self._anomaly_id = None
        self._feedback_type = None
        self._feedback = None
        self.discriminator = None

        if anomaly_type is not None:
            self.anomaly_type = anomaly_type
        if anomaly_id is not None:
            self.anomaly_id = anomaly_id
        if feedback_type is not None:
            self.feedback_type = feedback_type
        if feedback is not None:
            self.feedback = feedback

    @property
    def anomaly_type(self):
        """Gets the anomaly_type of this XiqAnomaliesFeedbackRequest.  # noqa: E501


        :return: The anomaly_type of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :rtype: XiqAnomalyType
        """
        return self._anomaly_type

    @anomaly_type.setter
    def anomaly_type(self, anomaly_type):
        """Sets the anomaly_type of this XiqAnomaliesFeedbackRequest.


        :param anomaly_type: The anomaly_type of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :type: XiqAnomalyType
        """

        self._anomaly_type = anomaly_type

    @property
    def anomaly_id(self):
        """Gets the anomaly_id of this XiqAnomaliesFeedbackRequest.  # noqa: E501

        The anomaly Id  # noqa: E501

        :return: The anomaly_id of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._anomaly_id

    @anomaly_id.setter
    def anomaly_id(self, anomaly_id):
        """Sets the anomaly_id of this XiqAnomaliesFeedbackRequest.

        The anomaly Id  # noqa: E501

        :param anomaly_id: The anomaly_id of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :type: str
        """

        self._anomaly_id = anomaly_id

    @property
    def feedback_type(self):
        """Gets the feedback_type of this XiqAnomaliesFeedbackRequest.  # noqa: E501


        :return: The feedback_type of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :rtype: XiqFeedbackType
        """
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, feedback_type):
        """Sets the feedback_type of this XiqAnomaliesFeedbackRequest.


        :param feedback_type: The feedback_type of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :type: XiqFeedbackType
        """

        self._feedback_type = feedback_type

    @property
    def feedback(self):
        """Gets the feedback of this XiqAnomaliesFeedbackRequest.  # noqa: E501

        The feedback description  # noqa: E501

        :return: The feedback of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :rtype: str
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this XiqAnomaliesFeedbackRequest.

        The feedback description  # noqa: E501

        :param feedback: The feedback of this XiqAnomaliesFeedbackRequest.  # noqa: E501
        :type: str
        """

        self._feedback = feedback

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
        if not isinstance(other, XiqAnomaliesFeedbackRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAnomaliesFeedbackRequest):
            return True

        return self.to_dict() != other.to_dict()
