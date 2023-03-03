# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 23.1.0.40
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import extremecloudiq
from extremecloudiq.models.xiq_operation_object import XiqOperationObject  # noqa: E501
from extremecloudiq.rest import ApiException

class TestXiqOperationObject(unittest.TestCase):
    """XiqOperationObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XiqOperationObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = extremecloudiq.models.xiq_operation_object.XiqOperationObject()  # noqa: E501
        if include_optional :
            return XiqOperationObject(
                id = '0', 
                metadata = extremecloudiq.models.xiq_operation_metadata.XiqOperationMetadata(
                    status = 'PENDING', 
                    cancelable = True, 
                    percentage = 0, 
                    step = '0', 
                    create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expires_in = 56, ), 
                done = True, 
                response = None, 
                error = extremecloudiq.models.xiq_error.XiqError(
                    error_code = '0', 
                    error_id = '0', 
                    error_message = '0', )
            )
        else :
            return XiqOperationObject(
                id = '0',
                metadata = extremecloudiq.models.xiq_operation_metadata.XiqOperationMetadata(
                    status = 'PENDING', 
                    cancelable = True, 
                    percentage = 0, 
                    step = '0', 
                    create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    expires_in = 56, ),
                done = True,
        )

    def testXiqOperationObject(self):
        """Test XiqOperationObject"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
