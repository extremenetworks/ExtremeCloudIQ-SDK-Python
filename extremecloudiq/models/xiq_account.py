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


class XiqAccount(object):
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
        'account_type': 'XiqAccountType',
        'account_mode': 'XiqAccountMode',
        'quota': 'str',
        'data_center': 'str',
        'industry': 'str',
        'country': 'str',
        'state': 'str',
        'city': 'str',
        'address': 'str',
        'zipcode': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'name': 'name',
        'account_type': 'account_type',
        'account_mode': 'account_mode',
        'quota': 'quota',
        'data_center': 'data_center',
        'industry': 'industry',
        'country': 'country',
        'state': 'state',
        'city': 'city',
        'address': 'address',
        'zipcode': 'zipcode'
    }

    def __init__(self, id=None, create_time=None, update_time=None, name=None, account_type=None, account_mode=None, quota=None, data_center=None, industry=None, country=None, state=None, city=None, address=None, zipcode=None, local_vars_configuration=None):  # noqa: E501
        """XiqAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._create_time = None
        self._update_time = None
        self._name = None
        self._account_type = None
        self._account_mode = None
        self._quota = None
        self._data_center = None
        self._industry = None
        self._country = None
        self._state = None
        self._city = None
        self._address = None
        self._zipcode = None
        self.discriminator = None

        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.name = name
        self.account_type = account_type
        self.account_mode = account_mode
        self.quota = quota
        self.data_center = data_center
        if industry is not None:
            self.industry = industry
        if country is not None:
            self.country = country
        if state is not None:
            self.state = state
        if city is not None:
            self.city = city
        if address is not None:
            self.address = address
        if zipcode is not None:
            self.zipcode = zipcode

    @property
    def id(self):
        """Gets the id of this XiqAccount.  # noqa: E501

        The unique identifier  # noqa: E501

        :return: The id of this XiqAccount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqAccount.

        The unique identifier  # noqa: E501

        :param id: The id of this XiqAccount.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this XiqAccount.  # noqa: E501

        The create time  # noqa: E501

        :return: The create_time of this XiqAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this XiqAccount.

        The create time  # noqa: E501

        :param create_time: The create_time of this XiqAccount.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and create_time is None:  # noqa: E501
            raise ValueError("Invalid value for `create_time`, must not be `None`")  # noqa: E501

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this XiqAccount.  # noqa: E501

        The last update time  # noqa: E501

        :return: The update_time of this XiqAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this XiqAccount.

        The last update time  # noqa: E501

        :param update_time: The update_time of this XiqAccount.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and update_time is None:  # noqa: E501
            raise ValueError("Invalid value for `update_time`, must not be `None`")  # noqa: E501

        self._update_time = update_time

    @property
    def name(self):
        """Gets the name of this XiqAccount.  # noqa: E501

        Account name  # noqa: E501

        :return: The name of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XiqAccount.

        Account name  # noqa: E501

        :param name: The name of this XiqAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def account_type(self):
        """Gets the account_type of this XiqAccount.  # noqa: E501


        :return: The account_type of this XiqAccount.  # noqa: E501
        :rtype: XiqAccountType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this XiqAccount.


        :param account_type: The account_type of this XiqAccount.  # noqa: E501
        :type: XiqAccountType
        """
        if self.local_vars_configuration.client_side_validation and account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

    @property
    def account_mode(self):
        """Gets the account_mode of this XiqAccount.  # noqa: E501


        :return: The account_mode of this XiqAccount.  # noqa: E501
        :rtype: XiqAccountMode
        """
        return self._account_mode

    @account_mode.setter
    def account_mode(self, account_mode):
        """Sets the account_mode of this XiqAccount.


        :param account_mode: The account_mode of this XiqAccount.  # noqa: E501
        :type: XiqAccountMode
        """
        if self.local_vars_configuration.client_side_validation and account_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `account_mode`, must not be `None`")  # noqa: E501

        self._account_mode = account_mode

    @property
    def quota(self):
        """Gets the quota of this XiqAccount.  # noqa: E501

        The API quota policy  # noqa: E501

        :return: The quota of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this XiqAccount.

        The API quota policy  # noqa: E501

        :param quota: The quota of this XiqAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and quota is None:  # noqa: E501
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def data_center(self):
        """Gets the data_center of this XiqAccount.  # noqa: E501

        The default Regional Data Center (RDC) to hold data from customer network  # noqa: E501

        :return: The data_center of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this XiqAccount.

        The default Regional Data Center (RDC) to hold data from customer network  # noqa: E501

        :param data_center: The data_center of this XiqAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and data_center is None:  # noqa: E501
            raise ValueError("Invalid value for `data_center`, must not be `None`")  # noqa: E501

        self._data_center = data_center

    @property
    def industry(self):
        """Gets the industry of this XiqAccount.  # noqa: E501

        The industry of the account belongs to  # noqa: E501

        :return: The industry of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """Sets the industry of this XiqAccount.

        The industry of the account belongs to  # noqa: E501

        :param industry: The industry of this XiqAccount.  # noqa: E501
        :type: str
        """

        self._industry = industry

    @property
    def country(self):
        """Gets the country of this XiqAccount.  # noqa: E501

        The country for the account  # noqa: E501

        :return: The country of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this XiqAccount.

        The country for the account  # noqa: E501

        :param country: The country of this XiqAccount.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def state(self):
        """Gets the state of this XiqAccount.  # noqa: E501

        The state for the account (if any)  # noqa: E501

        :return: The state of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this XiqAccount.

        The state for the account (if any)  # noqa: E501

        :param state: The state of this XiqAccount.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def city(self):
        """Gets the city of this XiqAccount.  # noqa: E501

        The city for the account  # noqa: E501

        :return: The city of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this XiqAccount.

        The city for the account  # noqa: E501

        :param city: The city of this XiqAccount.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def address(self):
        """Gets the address of this XiqAccount.  # noqa: E501

        The address for the account  # noqa: E501

        :return: The address of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this XiqAccount.

        The address for the account  # noqa: E501

        :param address: The address of this XiqAccount.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def zipcode(self):
        """Gets the zipcode of this XiqAccount.  # noqa: E501

        The zipcode of the address  # noqa: E501

        :return: The zipcode of this XiqAccount.  # noqa: E501
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this XiqAccount.

        The zipcode of the address  # noqa: E501

        :param zipcode: The zipcode of this XiqAccount.  # noqa: E501
        :type: str
        """

        self._zipcode = zipcode

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
        if not isinstance(other, XiqAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqAccount):
            return True

        return self.to_dict() != other.to_dict()
