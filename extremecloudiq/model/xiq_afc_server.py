# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.2.0.123
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


class XiqAfcServer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def state() -> typing.Type['XiqAfcServerState']:
                return XiqAfcServerState
            server_url = schemas.StrSchema
            region = schemas.StrSchema
            server_id = schemas.Int64Schema
            __annotations__ = {
                "state": state,
                "server_url": server_url,
                "region": region,
                "server_id": server_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'XiqAfcServerState': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_url"]) -> MetaOapg.properties.server_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_id"]) -> MetaOapg.properties.server_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["state", "server_url", "region", "server_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union['XiqAfcServerState', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_url"]) -> typing.Union[MetaOapg.properties.server_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_id"]) -> typing.Union[MetaOapg.properties.server_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["state", "server_url", "region", "server_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        state: typing.Union['XiqAfcServerState', schemas.Unset] = schemas.unset,
        server_url: typing.Union[MetaOapg.properties.server_url, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        server_id: typing.Union[MetaOapg.properties.server_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAfcServer':
        return super().__new__(
            cls,
            *_args,
            state=state,
            server_url=server_url,
            region=region,
            server_id=server_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_afc_server_state import XiqAfcServerState
