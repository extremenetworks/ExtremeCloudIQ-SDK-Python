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


class XiqApplication(object):
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
        'category_id': 'int',
        'category_name': 'str',
        'detection_rules': 'list[XiqApplicationDetectionRule]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'org_id': 'org_id',
        'name': 'name',
        'description': 'description',
        'predefined': 'predefined',
        'category_id': 'category_id',
        'category_name': 'category_name',
        'detection_rules': 'detection_rules'
    }

    def __init__(self, id=None, create_time=None, update_time=None, org_id=None, name=None, description=None, predefined=None, category_id=None, category_name=None, detection_rules=None, local_vars_configuration=None):  # noqa: E501
        """XiqApplication - a model defined in OpenAPI"""  # noqa: E501
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
        self._category_id = None
        self._category_name = None
        self._detection_rules = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        if org_id is not None:
            self.org_id = org_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if predefined is not None:
            self.predefined = predefined
        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if detection_rules is not None:
            self.detection_rules = detection_rules

    @property
    def id(self):
        """Gets the id of this XiqApplication.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqApplication.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqApplication.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqApplication.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqApplication.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqApplication.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqApplication.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqApplication.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqApplication.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqApplication.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqApplication.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqApplication.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqApplication.  # noqa: E501

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :return: The org_id of this XiqApplication.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqApplication.

        The organization identifier, valid when enabling HIQ feature  # noqa: E501

        :param org_id: The org_id of this XiqApplication.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def name(self):
        """Gets the name of this XiqApplication.  # noqa: E501

        The application name  # noqa: E501

        :return: The name of this XiqApplication.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqApplication.

        The application name  # noqa: E501

        :param name: The name of this XiqApplication.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this XiqApplication.  # noqa: E501

        The application description  # noqa: E501

        :return: The description of this XiqApplication.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XiqApplication.

        The application description  # noqa: E501

        :param description: The description of this XiqApplication.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def predefined(self):
        """Gets the predefined of this XiqApplication.  # noqa: E501

        Flag to describle whether the application is predefined or customized  # noqa: E501

        :return: The predefined of this XiqApplication.  # noqa: E501
        :rtype: bool
        """
        return self._predefined

    @predefined.setter
    def predefined(self, predefined):
        """Sets the predefined of this XiqApplication.

        Flag to describle whether the application is predefined or customized  # noqa: E501

        :param predefined: The predefined of this XiqApplication.  # noqa: E501
        :type: bool
        """

        self._predefined = predefined

    @property
    def category_id(self):
        """Gets the category_id of this XiqApplication.  # noqa: E501

        The category ID of application  # noqa: E501

        :return: The category_id of this XiqApplication.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this XiqApplication.

        The category ID of application  # noqa: E501

        :param category_id: The category_id of this XiqApplication.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def category_name(self):
        """Gets the category_name of this XiqApplication.  # noqa: E501

        The category name of application  # noqa: E501

        :return: The category_name of this XiqApplication.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this XiqApplication.

        The category name of application  # noqa: E501

        :param category_name: The category_name of this XiqApplication.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def detection_rules(self):
        """Gets the detection_rules of this XiqApplication.  # noqa: E501

        The application detection rules  # noqa: E501

        :return: The detection_rules of this XiqApplication.  # noqa: E501
        :rtype: list[XiqApplicationDetectionRule]
        """
        return self._detection_rules

    @detection_rules.setter
    def detection_rules(self, detection_rules):
        """Sets the detection_rules of this XiqApplication.

        The application detection rules  # noqa: E501

        :param detection_rules: The detection_rules of this XiqApplication.  # noqa: E501
        :type: list[XiqApplicationDetectionRule]
        """

        self._detection_rules = detection_rules

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
        if not isinstance(other, XiqApplication):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqApplication):
            return True

        return self.to_dict() != other.to_dict()
