# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.logs_audit_reports.post import AuditLogsReport
from extremecloudiq.paths.logs_audit_reports_id.get import DownloadAuditLogsReport
from extremecloudiq.paths.logs_audit_full_descriptions_id.get import GetAuditLogFullDescriptions
from extremecloudiq.paths.logs_accounting.get import ListAccountingLogs
from extremecloudiq.paths.logs_audit.get import ListAuditLogs
from extremecloudiq.paths.logs_auth.get import ListAuthLogs
from extremecloudiq.paths.logs_credential.get import ListCredentialLogs
from extremecloudiq.paths.logs_email.get import ListEmailLogs
from extremecloudiq.paths.logs_sms.get import ListSmsLogs


class LogApi(
    AuditLogsReport,
    DownloadAuditLogsReport,
    GetAuditLogFullDescriptions,
    ListAccountingLogs,
    ListAuditLogs,
    ListAuthLogs,
    ListCredentialLogs,
    ListEmailLogs,
    ListSmsLogs,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
