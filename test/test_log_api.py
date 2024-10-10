# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 24.6.0.74
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import extremecloudiq
from extremecloudiq.api.log_api import LogApi  # noqa: E501
from extremecloudiq.rest import ApiException


class TestLogApi(unittest.TestCase):
    """LogApi unit test stubs"""

    def setUp(self):
        self.api = extremecloudiq.api.log_api.LogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_audit_logs_report(self):
        """Test case for audit_logs_report

        [LRO] Create audit logs report  # noqa: E501
        """
        pass

    def test_download_audit_logs_report(self):
        """Test case for download_audit_logs_report

        Download audit logs  # noqa: E501
        """
        pass

    def test_get_audit_log_full_descriptions(self):
        """Test case for get_audit_log_full_descriptions

        Get audit log full descriptions  # noqa: E501
        """
        pass

    def test_list_accounting_logs(self):
        """Test case for list_accounting_logs

        List accounting logs  # noqa: E501
        """
        pass

    def test_list_audit_logs(self):
        """Test case for list_audit_logs

        List audit logs  # noqa: E501
        """
        pass

    def test_list_auth_logs(self):
        """Test case for list_auth_logs

        List auth logs  # noqa: E501
        """
        pass

    def test_list_credential_logs(self):
        """Test case for list_credential_logs

        List credential logs  # noqa: E501
        """
        pass

    def test_list_email_logs(self):
        """Test case for list_email_logs

        List Email logs  # noqa: E501
        """
        pass

    def test_list_sms_logs(self):
        """Test case for list_sms_logs

        List SMS logs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
