# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.hiq_organizations.post import CreateOrganization
from extremecloudiq.paths.hiq_organizations_id.delete import DeleteOrganization
from extremecloudiq.paths.hiq_context_creating.get import GetCreatingOrgId
from extremecloudiq.paths.hiq_context.get import GetHiqContext
from extremecloudiq.paths.hiq_status.get import GetHiqStatus
from extremecloudiq.paths.hiq_context_reading.get import GetReadingOrgIds
from extremecloudiq.paths.hiq_organizations.get import ListOrganizations
from extremecloudiq.paths.hiq_organizations_id_rename.post import RenameOrganization
from extremecloudiq.paths.hiq_context_creating.put import SetCreatingOrgId
from extremecloudiq.paths.hiq_context.put import SetHiqContext
from extremecloudiq.paths.hiq_context_reading.put import SetReadingOrgIds


class HIQApi(
    CreateOrganization,
    DeleteOrganization,
    GetCreatingOrgId,
    GetHiqContext,
    GetHiqStatus,
    GetReadingOrgIds,
    ListOrganizations,
    RenameOrganization,
    SetCreatingOrgId,
    SetHiqContext,
    SetReadingOrgIds,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
