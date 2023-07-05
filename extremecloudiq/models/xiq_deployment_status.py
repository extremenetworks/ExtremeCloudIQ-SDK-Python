# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.4.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqDeploymentStatus(object):
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
        'current_progress': 'int',
        'current_step_code': 'str',
        'current_step_message': 'str',
        'is_finished_successful': 'bool',
        'last_deploy_time': 'int',
        'finished': 'bool'
    }

    attribute_map = {
        'current_progress': 'current_progress',
        'current_step_code': 'current_step_code',
        'current_step_message': 'current_step_message',
        'is_finished_successful': 'is_finished_successful',
        'last_deploy_time': 'last_deploy_time',
        'finished': 'finished'
    }

    def __init__(self, current_progress=None, current_step_code=None, current_step_message=None, is_finished_successful=None, last_deploy_time=None, finished=None, local_vars_configuration=None):  # noqa: E501
        """XiqDeploymentStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._current_progress = None
        self._current_step_code = None
        self._current_step_message = None
        self._is_finished_successful = None
        self._last_deploy_time = None
        self._finished = None
        self.discriminator = None

        if current_progress is not None:
            self.current_progress = current_progress
        if current_step_code is not None:
            self.current_step_code = current_step_code
        if current_step_message is not None:
            self.current_step_message = current_step_message
        if is_finished_successful is not None:
            self.is_finished_successful = is_finished_successful
        if last_deploy_time is not None:
            self.last_deploy_time = last_deploy_time
        if finished is not None:
            self.finished = finished

    @property
    def current_progress(self):
        """Gets the current_progress of this XiqDeploymentStatus.  # noqa: E501

        The current deploy progress if not finished, range from 0 to 100  # noqa: E501

        :return: The current_progress of this XiqDeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_progress

    @current_progress.setter
    def current_progress(self, current_progress):
        """Sets the current_progress of this XiqDeploymentStatus.

        The current deploy progress if not finished, range from 0 to 100  # noqa: E501

        :param current_progress: The current_progress of this XiqDeploymentStatus.  # noqa: E501
        :type: int
        """

        self._current_progress = current_progress

    @property
    def current_step_code(self):
        """Gets the current_step_code of this XiqDeploymentStatus.  # noqa: E501

        The code of the current deploy step if not finished  # noqa: E501

        :return: The current_step_code of this XiqDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_step_code

    @current_step_code.setter
    def current_step_code(self, current_step_code):
        """Sets the current_step_code of this XiqDeploymentStatus.

        The code of the current deploy step if not finished  # noqa: E501

        :param current_step_code: The current_step_code of this XiqDeploymentStatus.  # noqa: E501
        :type: str
        """

        self._current_step_code = current_step_code

    @property
    def current_step_message(self):
        """Gets the current_step_message of this XiqDeploymentStatus.  # noqa: E501

        The readable message of the current deploy step if not finished  # noqa: E501

        :return: The current_step_message of this XiqDeploymentStatus.  # noqa: E501
        :rtype: str
        """
        return self._current_step_message

    @current_step_message.setter
    def current_step_message(self, current_step_message):
        """Sets the current_step_message of this XiqDeploymentStatus.

        The readable message of the current deploy step if not finished  # noqa: E501

        :param current_step_message: The current_step_message of this XiqDeploymentStatus.  # noqa: E501
        :type: str
        """

        self._current_step_message = current_step_message

    @property
    def is_finished_successful(self):
        """Gets the is_finished_successful of this XiqDeploymentStatus.  # noqa: E501

        Indicates whether the last deployment is successful if finished  # noqa: E501

        :return: The is_finished_successful of this XiqDeploymentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._is_finished_successful

    @is_finished_successful.setter
    def is_finished_successful(self, is_finished_successful):
        """Sets the is_finished_successful of this XiqDeploymentStatus.

        Indicates whether the last deployment is successful if finished  # noqa: E501

        :param is_finished_successful: The is_finished_successful of this XiqDeploymentStatus.  # noqa: E501
        :type: bool
        """

        self._is_finished_successful = is_finished_successful

    @property
    def last_deploy_time(self):
        """Gets the last_deploy_time of this XiqDeploymentStatus.  # noqa: E501

        The last deployed time (Only valid when in_progress = false)  # noqa: E501

        :return: The last_deploy_time of this XiqDeploymentStatus.  # noqa: E501
        :rtype: int
        """
        return self._last_deploy_time

    @last_deploy_time.setter
    def last_deploy_time(self, last_deploy_time):
        """Sets the last_deploy_time of this XiqDeploymentStatus.

        The last deployed time (Only valid when in_progress = false)  # noqa: E501

        :param last_deploy_time: The last_deploy_time of this XiqDeploymentStatus.  # noqa: E501
        :type: int
        """

        self._last_deploy_time = last_deploy_time

    @property
    def finished(self):
        """Gets the finished of this XiqDeploymentStatus.  # noqa: E501


        :return: The finished of this XiqDeploymentStatus.  # noqa: E501
        :rtype: bool
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this XiqDeploymentStatus.


        :param finished: The finished of this XiqDeploymentStatus.  # noqa: E501
        :type: bool
        """

        self._finished = finished

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
        if not isinstance(other, XiqDeploymentStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqDeploymentStatus):
            return True

        return self.to_dict() != other.to_dict()
