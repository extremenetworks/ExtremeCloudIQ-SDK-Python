# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.7.0.64
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.operation_api import OperationApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestOperationApi(unittest.TestCase):
    """OperationApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.operation_api.OperationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_operation(self):
        """Test case for cancel_operation

        Cancel Long-Running Operation (LRO)  # noqa: E501
        """
        pass

    def test_delete_operation(self):
        """Test case for delete_operation

        Delete Long-Running Operation (LRO)  # noqa: E501
        """
        pass

    def test_get_operation(self):
        """Test case for get_operation

        Get Long-Running Operation (LRO) status and result  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
