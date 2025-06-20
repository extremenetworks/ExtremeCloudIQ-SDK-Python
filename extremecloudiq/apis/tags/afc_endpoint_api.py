# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.site_afc_schedule.post import CreateSiteAfcSchedule
from extremecloudiq.paths.afcserver_server_id.get import GetAfcServer
from extremecloudiq.paths.afcserver_statistics_server_id.get import GetAfcServerStatistics
from extremecloudiq.paths.ap_spectrum_.post import GetAfcSpectrumPerAp
from extremecloudiq.paths.site_spectrum_.post import GetAfcSpectrumPerSite
from extremecloudiq.paths.ap_afc_diagnostics_id.get import GetApsAfcDiagnostics
from extremecloudiq.paths.ap_afc_interface_details_sn.get import GetApsAfcInfo
from extremecloudiq.paths.aps_afc_query_.get import GetApsAfcSummaryInfo
from extremecloudiq.paths.site_afc_schedule.get import GetSiteAfcSchedule
from extremecloudiq.paths.afcserver.get import ListAfcServers
from extremecloudiq.paths.aps_afc_update.post import PostApsManualAfcSpectrum
from extremecloudiq.paths.site_afc_schedule.put import UpdateSiteAfcSchedule


class AfcEndpointApi(
    CreateSiteAfcSchedule,
    GetAfcServer,
    GetAfcServerStatistics,
    GetAfcSpectrumPerAp,
    GetAfcSpectrumPerSite,
    GetApsAfcDiagnostics,
    GetApsAfcInfo,
    GetApsAfcSummaryInfo,
    GetSiteAfcSchedule,
    ListAfcServers,
    PostApsManualAfcSpectrum,
    UpdateSiteAfcSchedule,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
