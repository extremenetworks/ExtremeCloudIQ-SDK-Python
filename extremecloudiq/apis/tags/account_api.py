# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.1.0.147
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.account_viq_backup.post import BackupViq
from extremecloudiq.paths.account_viq_download.get import DownloadViqReport
from extremecloudiq.paths.account_viq_export_import_status.get import ExportImportStatus
from extremecloudiq.paths.account_viq_export.post import ExportViq
from extremecloudiq.paths.account_viq_default_device_password.get import GetDefaultDevicePassword
from extremecloudiq.paths.account_home.get import GetHomeAccount
from extremecloudiq.paths.account_viq.get import GetViqInfo
from extremecloudiq.paths.account_viq_import.post import ImportViq
from extremecloudiq.paths.account_external.get import ListExternalAccounts
from extremecloudiq.paths.account_switch.post import SwitchAccount
from extremecloudiq.paths.account_viq_default_device_password.put import UpdateDefaultDevicePassword


class AccountApi(
    BackupViq,
    DownloadViqReport,
    ExportImportStatus,
    ExportViq,
    GetDefaultDevicePassword,
    GetHomeAccount,
    GetViqInfo,
    ImportViq,
    ListExternalAccounts,
    SwitchAccount,
    UpdateDefaultDevicePassword,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
