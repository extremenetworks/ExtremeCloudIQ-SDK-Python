# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.1.0.147
    Contact: support@extremenetworks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from extremecloudiq import schemas  # noqa: F401


class XiqMissingVlanAnomaliesCountResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Missing vlan anomalies count details
    """


    class MetaOapg:
        
        class properties:
            total_anomalies_count = schemas.Int32Schema
            
            
            class anomalies_count_by_site(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqMissingVlanSiteAnomalyCountDetails']:
                        return XiqMissingVlanSiteAnomalyCountDetails
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqMissingVlanSiteAnomalyCountDetails'], typing.List['XiqMissingVlanSiteAnomalyCountDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'anomalies_count_by_site':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqMissingVlanSiteAnomalyCountDetails':
                    return super().__getitem__(i)
            __annotations__ = {
                "total_anomalies_count": total_anomalies_count,
                "anomalies_count_by_site": anomalies_count_by_site,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_anomalies_count"]) -> MetaOapg.properties.total_anomalies_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomalies_count_by_site"]) -> MetaOapg.properties.anomalies_count_by_site: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total_anomalies_count", "anomalies_count_by_site", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_anomalies_count"]) -> typing.Union[MetaOapg.properties.total_anomalies_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomalies_count_by_site"]) -> typing.Union[MetaOapg.properties.anomalies_count_by_site, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total_anomalies_count", "anomalies_count_by_site", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        total_anomalies_count: typing.Union[MetaOapg.properties.total_anomalies_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        anomalies_count_by_site: typing.Union[MetaOapg.properties.anomalies_count_by_site, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqMissingVlanAnomaliesCountResponse':
        return super().__new__(
            cls,
            *_args,
            total_anomalies_count=total_anomalies_count,
            anomalies_count_by_site=anomalies_count_by_site,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_missing_vlan_site_anomaly_count_details import XiqMissingVlanSiteAnomalyCountDetails
