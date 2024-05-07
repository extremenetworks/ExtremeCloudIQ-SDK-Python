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


class XiqOperationMetadata(object):
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
        'status': 'XiqOperationStatus',
        'cancelable': 'bool',
        'percentage': 'int',
        'step': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'expires_in': 'int'
    }

    attribute_map = {
        'status': 'status',
        'cancelable': 'cancelable',
        'percentage': 'percentage',
        'step': 'step',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'expires_in': 'expires_in'
    }

    def __init__(self, status=None, cancelable=None, percentage=None, step=None, create_time=None, update_time=None, start_time=None, end_time=None, expires_in=None, local_vars_configuration=None):  # noqa: E501
        """XiqOperationMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._cancelable = None
        self._percentage = None
        self._step = None
        self._create_time = None
        self._update_time = None
        self._start_time = None
        self._end_time = None
        self._expires_in = None
        self.discriminator = None

        self.status = status
        self.cancelable = cancelable
        if percentage is not None:
            self.percentage = percentage
        if step is not None:
            self.step = step
        self.create_time = create_time
        self.update_time = update_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        self.expires_in = expires_in

    @property
    def status(self):
        """Gets the status of this XiqOperationMetadata.  # noqa: E501


        :return: The status of this XiqOperationMetadata.  # noqa: E501
        :rtype: XiqOperationStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XiqOperationMetadata.


        :param status: The status of this XiqOperationMetadata.  # noqa: E501
        :type: XiqOperationStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def cancelable(self):
        """Gets the cancelable of this XiqOperationMetadata.  # noqa: E501

        Indicates if the operation can be canceled in the current status  # noqa: E501

        :return: The cancelable of this XiqOperationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._cancelable

    @cancelable.setter
    def cancelable(self, cancelable):
        """Sets the cancelable of this XiqOperationMetadata.

        Indicates if the operation can be canceled in the current status  # noqa: E501

        :param cancelable: The cancelable of this XiqOperationMetadata.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and cancelable is None:  # noqa: E501
            raise ValueError("Invalid value for `cancelable`, must not be `None`")  # noqa: E501

        self._cancelable = cancelable

    @property
    def percentage(self):
        """Gets the percentage of this XiqOperationMetadata.  # noqa: E501

        The progress in percentage ranges from 0 to 100 (it's not guaranteed to be accurate)  # noqa: E501

        :return: The percentage of this XiqOperationMetadata.  # noqa: E501
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this XiqOperationMetadata.

        The progress in percentage ranges from 0 to 100 (it's not guaranteed to be accurate)  # noqa: E501

        :param percentage: The percentage of this XiqOperationMetadata.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                percentage is not None and percentage > 100):  # noqa: E501
            raise ValueError("Invalid value for `percentage`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                percentage is not None and percentage < 0):  # noqa: E501
            raise ValueError("Invalid value for `percentage`, must be a value greater than or equal to `0`")  # noqa: E501

        self._percentage = percentage

    @property
    def step(self):
        """Gets the step of this XiqOperationMetadata.  # noqa: E501

        The optional step name for multiple steps operations when the operation is running  # noqa: E501

        :return: The step of this XiqOperationMetadata.  # noqa: E501
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this XiqOperationMetadata.

        The optional step name for multiple steps operations when the operation is running  # noqa: E501

        :param step: The step of this XiqOperationMetadata.  # noqa: E501
        :type: str
        """

        self._step = step

    @property
    def create_time(self):
        """Gets the create_time of this XiqOperationMetadata.  # noqa: E501

        The operation's create time, which is the time when the operation is in PENDING status  # noqa: E501

        :return: The create_time of this XiqOperationMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqOperationMetadata.

        The operation's create time, which is the time when the operation is in PENDING status  # noqa: E501

        :param create_time: The create_time of this XiqOperationMetadata.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqOperationMetadata.  # noqa: E501

        The operation's last update time  # noqa: E501

        :return: The update_time of this XiqOperationMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqOperationMetadata.

        The operation's last update time  # noqa: E501

        :param update_time: The update_time of this XiqOperationMetadata.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def start_time(self):
        """Gets the start_time of this XiqOperationMetadata.  # noqa: E501

        The operation's start time, which is the time when the operation is in RUNNING status  # noqa: E501

        :return: The start_time of this XiqOperationMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this XiqOperationMetadata.

        The operation's start time, which is the time when the operation is in RUNNING status  # noqa: E501

        :param start_time: The start_time of this XiqOperationMetadata.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this XiqOperationMetadata.  # noqa: E501

        The operation's end time, which is the time when the operation is done  # noqa: E501

        :return: The end_time of this XiqOperationMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this XiqOperationMetadata.

        The operation's end time, which is the time when the operation is done  # noqa: E501

        :param end_time: The end_time of this XiqOperationMetadata.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def expires_in(self):
        """Gets the expires_in of this XiqOperationMetadata.  # noqa: E501

        The number of seconds remaining until the operation expires and is to be deleted.  # noqa: E501

        :return: The expires_in of this XiqOperationMetadata.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this XiqOperationMetadata.

        The number of seconds remaining until the operation expires and is to be deleted.  # noqa: E501

        :param expires_in: The expires_in of this XiqOperationMetadata.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

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
        if not isinstance(other, XiqOperationMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqOperationMetadata):
            return True

        return self.to_dict() != other.to_dict()
