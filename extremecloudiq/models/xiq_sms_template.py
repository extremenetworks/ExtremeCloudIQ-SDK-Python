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


class XiqSmsTemplate(object):
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
        'org_id': 'int',
        'name': 'str',
        'description': 'str',
        'predefined': 'bool',
        'content': 'str',
        'password_type': 'XiqPasswordType'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'predefined': 'predefined',
        'content': 'content',
        'password_type': 'password_type'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, predefined=None, content=None, password_type=None, local_vars_configuration=None):  # noqa: E501
        """XiqSmsTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._org_id = None
        self._name = None
        self._description = None
        self._predefined = None
        self._content = None
        self._password_type = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        self.name = name
        if description is not None:
            self.description = description
        self.predefined = predefined
        if content is not None:
            self.content = content
        self.password_type = password_type

    @property
    def id(self):
        """Gets the id of this XiqSmsTemplate.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqSmsTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqSmsTemplate.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqSmsTemplate.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqSmsTemplate.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqSmsTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqSmsTemplate.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqSmsTemplate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqSmsTemplate.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqSmsTemplate.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqSmsTemplate.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqSmsTemplate.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqSmsTemplate.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqSmsTemplate.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqSmsTemplate.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqSmsTemplate.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqSmsTemplate.  # noqa: E501

        The SMS template name  # noqa: E501

        :return: The name of this XiqSmsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqSmsTemplate.

        The SMS template name  # noqa: E501

        :param name: The name of this XiqSmsTemplate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqSmsTemplate.  # noqa: E501

        The SMS template description  # noqa: E501

        :return: The description of this XiqSmsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqSmsTemplate.

        The SMS template description  # noqa: E501

        :param description: The description of this XiqSmsTemplate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def predefined(self):
        """Gets the predefined of this XiqSmsTemplate.  # noqa: E501

        Wheter or not it is a system prefined template  # noqa: E501

        :return: The predefined of this XiqSmsTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqSmsTemplate.

        Wheter or not it is a system prefined template  # noqa: E501

        :param predefined: The predefined of this XiqSmsTemplate.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and predefined is None:  # noqa: E501
            raise ValueError("Invalid value for `predefined`, must not be `None`")  # noqa: E501

        self._predefined = predefined

    @property
    def content(self):
        """Gets the content of this XiqSmsTemplate.  # noqa: E501

        The SMS template content  # noqa: E501

        :return: The content of this XiqSmsTemplate.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this XiqSmsTemplate.

        The SMS template content  # noqa: E501

        :param content: The content of this XiqSmsTemplate.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def password_type(self):
        """Gets the password_type of this XiqSmsTemplate.  # noqa: E501


        :return: The password_type of this XiqSmsTemplate.  # noqa: E501
        :rtype: XiqPasswordType
        """
        return self._password_type

    @password_type.setter
    def password_type(self, password_type):
        """Sets the password_type of this XiqSmsTemplate.


        :param password_type: The password_type of this XiqSmsTemplate.  # noqa: E501
        :type: XiqPasswordType
        """
        if self.local_vars_configuration.client_side_validation and password_type is None:  # noqa: E501
            raise ValueError("Invalid value for `password_type`, must not be `None`")  # noqa: E501

        self._password_type = password_type

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
        if not isinstance(other, XiqSmsTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqSmsTemplate):
            return True

        return self.to_dict() != other.to_dict()
