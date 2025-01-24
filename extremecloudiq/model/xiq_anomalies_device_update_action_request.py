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


class XiqAnomaliesDeviceUpdateActionRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Anomalies Devices Update Action Request
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def anomaly_type() -> typing.Type['XiqAnomalyType']:
                return XiqAnomalyType
        
            @staticmethod
            def action_type() -> typing.Type['XiqActionType']:
                return XiqActionType
            location_id = schemas.Int64Schema
            anomaly_id = schemas.StrSchema
            __annotations__ = {
                "anomaly_type": anomaly_type,
                "action_type": action_type,
                "location_id": location_id,
                "anomaly_id": anomaly_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomaly_type"]) -> 'XiqAnomalyType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action_type"]) -> 'XiqActionType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_id"]) -> MetaOapg.properties.location_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["anomaly_id"]) -> MetaOapg.properties.anomaly_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["anomaly_type", "action_type", "location_id", "anomaly_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomaly_type"]) -> typing.Union['XiqAnomalyType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action_type"]) -> typing.Union['XiqActionType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_id"]) -> typing.Union[MetaOapg.properties.location_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["anomaly_id"]) -> typing.Union[MetaOapg.properties.anomaly_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["anomaly_type", "action_type", "location_id", "anomaly_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        anomaly_type: typing.Union['XiqAnomalyType', schemas.Unset] = schemas.unset,
        action_type: typing.Union['XiqActionType', schemas.Unset] = schemas.unset,
        location_id: typing.Union[MetaOapg.properties.location_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        anomaly_id: typing.Union[MetaOapg.properties.anomaly_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAnomaliesDeviceUpdateActionRequest':
        return super().__new__(
            cls,
            *_args,
            anomaly_type=anomaly_type,
            action_type=action_type,
            location_id=location_id,
            anomaly_id=anomaly_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_action_type import XiqActionType
from extremecloudiq.model.xiq_anomaly_type import XiqAnomalyType
