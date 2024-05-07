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


class XiqIotProfile(object):
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
        'name': 'str',
        'app_id': 'XiqIotApplicationId',
        'thread_gateway': 'XiqIotProfileThreadGateway'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'app_id': 'app_id',
        'thread_gateway': 'thread_gateway'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, app_id=None, thread_gateway=None, local_vars_configuration=None):  # noqa: E501
        """XiqIotProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._app_id = None
        self._thread_gateway = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.name = name
        self.app_id = app_id
        if thread_gateway is not None:
            self.thread_gateway = thread_gateway

    @property
    def id(self):
        """Gets the id of this XiqIotProfile.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqIotProfile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqIotProfile.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqIotProfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqIotProfile.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqIotProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqIotProfile.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqIotProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqIotProfile.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqIotProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqIotProfile.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqIotProfile.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqIotProfile.  # noqa: E501

        The IoT profile name  # noqa: E501

        :return: The name of this XiqIotProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqIotProfile.

        The IoT profile name  # noqa: E501

        :param name: The name of this XiqIotProfile.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this XiqIotProfile.  # noqa: E501


        :return: The app_id of this XiqIotProfile.  # noqa: E501
        :rtype: XiqIotApplicationId
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this XiqIotProfile.


        :param app_id: The app_id of this XiqIotProfile.  # noqa: E501
        :type: XiqIotApplicationId
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def thread_gateway(self):
        """Gets the thread_gateway of this XiqIotProfile.  # noqa: E501


        :return: The thread_gateway of this XiqIotProfile.  # noqa: E501
        :rtype: XiqIotProfileThreadGateway
        """
        return self._thread_gateway

    @thread_gateway.setter
    def thread_gateway(self, thread_gateway):
        """Sets the thread_gateway of this XiqIotProfile.


        :param thread_gateway: The thread_gateway of this XiqIotProfile.  # noqa: E501
        :type: XiqIotProfileThreadGateway
        """

        self._thread_gateway = thread_gateway

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
        if not isinstance(other, XiqIotProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqIotProfile):
            return True

        return self.to_dict() != other.to_dict()
