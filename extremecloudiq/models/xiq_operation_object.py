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


class XiqOperationObject(object):
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
        'id': 'str',
        'metadata': 'XiqOperationMetadata',
        'done': 'bool',
        'response': 'object',
        'error': 'XiqError'
    }

    attribute_map = {
        'id': 'id',
        'metadata': 'metadata',
        'done': 'done',
        'response': 'response',
        'error': 'error'
    }

    def __init__(self, id=None, metadata=None, done=None, response=None, error=None, local_vars_configuration=None):  # noqa: E501
        """XiqOperationObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._metadata = None
        self._done = None
        self._response = None
        self._error = None
        self.discriminator = None

        self.id = id
        self.metadata = metadata
        self.done = done
        if response is not None:
            self.response = response
        if error is not None:
            self.error = error

    @property
    def id(self):
        """Gets the id of this XiqOperationObject.  # noqa: E501

        The unique identifier of the operation  # noqa: E501

        :return: The id of this XiqOperationObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XiqOperationObject.

        The unique identifier of the operation  # noqa: E501

        :param id: The id of this XiqOperationObject.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this XiqOperationObject.  # noqa: E501


        :return: The metadata of this XiqOperationObject.  # noqa: E501
        :rtype: XiqOperationMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this XiqOperationObject.


        :param metadata: The metadata of this XiqOperationObject.  # noqa: E501
        :type: XiqOperationMetadata
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def done(self):
        """Gets the done of this XiqOperationObject.  # noqa: E501

        Whether the operation is done  # noqa: E501

        :return: The done of this XiqOperationObject.  # noqa: E501
        :rtype: bool
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this XiqOperationObject.

        Whether the operation is done  # noqa: E501

        :param done: The done of this XiqOperationObject.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and done is None:  # noqa: E501
            raise ValueError("Invalid value for `done`, must not be `None`")  # noqa: E501

        self._done = done

    @property
    def response(self):
        """Gets the response of this XiqOperationObject.  # noqa: E501

        The API response of the operation if the status is SUCCEEDED  # noqa: E501

        :return: The response of this XiqOperationObject.  # noqa: E501
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this XiqOperationObject.

        The API response of the operation if the status is SUCCEEDED  # noqa: E501

        :param response: The response of this XiqOperationObject.  # noqa: E501
        :type: object
        """

        self._response = response

    @property
    def error(self):
        """Gets the error of this XiqOperationObject.  # noqa: E501


        :return: The error of this XiqOperationObject.  # noqa: E501
        :rtype: XiqError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this XiqOperationObject.


        :param error: The error of this XiqOperationObject.  # noqa: E501
        :type: XiqError
        """

        self._error = error

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
        if not isinstance(other, XiqOperationObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XiqOperationObject):
            return True

        return self.to_dict() != other.to_dict()
