# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.5.0.41
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from extremecloudiq.configuration import Configuration


class XiqUser(object):
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
        'login_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'display_name': 'str',
        'phone': 'str',
        'job_title': 'str',
        'locale': 'str',
        'user_role': 'XiqUserRole',
        'idle_timeout': 'int',
        'last_login_time': 'datetime',
        'org_id': 'int',
        'location_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'login_name': 'login_name',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'display_name': 'display_name',
        'phone': 'phone',
        'job_title': 'job_title',
        'locale': 'locale',
        'user_role': 'user_role',
        'idle_timeout': 'idle_timeout',
        'last_login_time': 'last_login_time',
        'org_id': 'org_id',
        'location_ids': 'location_ids'
    }

    def __init__(self, id=None, create_time=None, update_time=None, login_name=None, first_name=None, last_name=None, display_name=None, phone=None, job_title=None, locale=None, user_role=None, idle_timeout=None, last_login_time=None, org_id=None, location_ids=None, local_vars_configuration=None):  # noqa: E501
        """XiqUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._login_name = None
        self._first_name = None
        self._last_name = None
        self._display_name = None
        self._phone = None
        self._job_title = None
        self._locale = None
        self._user_role = None
        self._idle_timeout = None
        self._last_login_time = None
        self._org_id = None
        self._location_ids = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.login_name = login_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if display_name is not None:
            self.display_name = display_name
        if phone is not None:
            self.phone = phone
        if job_title is not None:
            self.job_title = job_title
        if locale is not None:
            self.locale = locale
        if user_role is not None:
            self.user_role = user_role
        if idle_timeout is not None:
            self.idle_timeout = idle_timeout
        if last_login_time is not None:
            self.last_login_time = last_login_time
        if org_id is not None:
            self.org_id = org_id
        if location_ids is not None:
            self.location_ids = location_ids

    @property
    def id(self):
        """Gets the id of this XiqUser.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqUser.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqUser.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqUser.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqUser.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqUser.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqUser.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqUser.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqUser.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqUser.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqUser.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def login_name(self):
        """Gets the login_name of this XiqUser.  # noqa: E501

        Login name, i.e. username or login Email  # noqa: E501

        :return: The login_name of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this XiqUser.

        Login name, i.e. username or login Email  # noqa: E501

        :param login_name: The login_name of this XiqUser.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and login_name is None:  # noqa: E501
            raise ValueError("Invalid value for `login_name`, must not be `None`")  # noqa: E501

        self._login_name = login_name

    @property
    def first_name(self):
        """Gets the first_name of this XiqUser.  # noqa: E501

        The first name  # noqa: E501

        :return: The first_name of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this XiqUser.

        The first name  # noqa: E501

        :param first_name: The first_name of this XiqUser.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this XiqUser.  # noqa: E501

        The last name, i.e. family name  # noqa: E501

        :return: The last_name of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this XiqUser.

        The last name, i.e. family name  # noqa: E501

        :param last_name: The last_name of this XiqUser.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def display_name(self):
        """Gets the display_name of this XiqUser.  # noqa: E501

        The name to display  # noqa: E501

        :return: The display_name of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this XiqUser.

        The name to display  # noqa: E501

        :param display_name: The display_name of this XiqUser.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def phone(self):
        """Gets the phone of this XiqUser.  # noqa: E501

        The Phone Number  # noqa: E501

        :return: The phone of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this XiqUser.

        The Phone Number  # noqa: E501

        :param phone: The phone of this XiqUser.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def job_title(self):
        """Gets the job_title of this XiqUser.  # noqa: E501

        The job title  # noqa: E501

        :return: The job_title of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this XiqUser.

        The job title  # noqa: E501

        :param job_title: The job_title of this XiqUser.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def locale(self):
        """Gets the locale of this XiqUser.  # noqa: E501

        The locale  # noqa: E501

        :return: The locale of this XiqUser.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this XiqUser.

        The locale  # noqa: E501

        :param locale: The locale of this XiqUser.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def user_role(self):
        """Gets the user_role of this XiqUser.  # noqa: E501


        :return: The user_role of this XiqUser.  # noqa: E501
        :rtype: XiqUserRole
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this XiqUser.


        :param user_role: The user_role of this XiqUser.  # noqa: E501
        :type: XiqUserRole
        """

        self._user_role = user_role

    @property
    def idle_timeout(self):
        """Gets the idle_timeout of this XiqUser.  # noqa: E501

        The idle timeout in minutes, the minimum value is 5 minutes and the maximum value is 4 hours  # noqa: E501

        :return: The idle_timeout of this XiqUser.  # noqa: E501
        :rtype: int
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """Sets the idle_timeout of this XiqUser.

        The idle timeout in minutes, the minimum value is 5 minutes and the maximum value is 4 hours  # noqa: E501

        :param idle_timeout: The idle_timeout of this XiqUser.  # noqa: E501
        :type: int
        """

        self._idle_timeout = idle_timeout

    @property
    def last_login_time(self):
        """Gets the last_login_time of this XiqUser.  # noqa: E501

        The last login time  # noqa: E501

        :return: The last_login_time of this XiqUser.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login_time

    @last_login_time.setter
    def last_login_time(self, last_login_time):
        """Sets the last_login_time of this XiqUser.

        The last login time  # noqa: E501

        :param last_login_time: The last_login_time of this XiqUser.  # noqa: E501
        :type: datetime
        """

        self._last_login_time = last_login_time

    @property
    def org_id(self):
        """Gets the org_id of this XiqUser.  # noqa: E501

        The HIQ organization ID if it is HIQ user  # noqa: E501

        :return: The org_id of this XiqUser.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this XiqUser.

        The HIQ organization ID if it is HIQ user  # noqa: E501

        :param org_id: The org_id of this XiqUser.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def location_ids(self):
        """Gets the location_ids of this XiqUser.  # noqa: E501

        The assigned location IDs.  # noqa: E501

        :return: The location_ids of this XiqUser.  # noqa: E501
        :rtype: list[int]
        """
        return self._location_ids

    @location_ids.setter
    def location_ids(self, location_ids):
        """Sets the location_ids of this XiqUser.

        The assigned location IDs.  # noqa: E501

        :param location_ids: The location_ids of this XiqUser.  # noqa: E501
        :type: list[int]
        """

        self._location_ids = location_ids

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
        if not isinstance(other, XiqUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqUser):
            return True

        return self.to_dict() != other.to_dict()
