# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from extremecloudiq.paths.applications_id_clients_topn.get import ListApplicationTopClientsUsage
from extremecloudiq.paths.applications.get import ListApplications
from extremecloudiq.paths.applications_topn.get import ListTopApplicationsUsage


class ApplicationApi(
    ListApplicationTopClientsUsage,
    ListApplications,
    ListTopApplicationsUsage,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
