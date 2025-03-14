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


class XiqExternalRadiusServer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The configuration of external RADIUS server object
    """


    class MetaOapg:
        required = {
            "authentication_port",
            "update_time",
            "create_time",
            "accounting_port",
            "enable_a3",
            "name",
            "id",
            "ip_address",
            "server_type",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            name = schemas.StrSchema
            authentication_port = schemas.Int32Schema
            accounting_port = schemas.Int32Schema
        
            @staticmethod
            def server_type() -> typing.Type['XiqRadiusServerType']:
                return XiqRadiusServerType
            ip_address = schemas.StrSchema
            enable_a3 = schemas.BoolSchema
            org_id = schemas.Int64Schema
            shared_secret = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "name": name,
                "authentication_port": authentication_port,
                "accounting_port": accounting_port,
                "server_type": server_type,
                "ip_address": ip_address,
                "enable_a3": enable_a3,
                "org_id": org_id,
                "shared_secret": shared_secret,
            }
    
    authentication_port: MetaOapg.properties.authentication_port
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    accounting_port: MetaOapg.properties.accounting_port
    enable_a3: MetaOapg.properties.enable_a3
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    ip_address: MetaOapg.properties.ip_address
    server_type: 'XiqRadiusServerType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication_port"]) -> MetaOapg.properties.authentication_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounting_port"]) -> MetaOapg.properties.accounting_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_type"]) -> 'XiqRadiusServerType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip_address"]) -> MetaOapg.properties.ip_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_a3"]) -> MetaOapg.properties.enable_a3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shared_secret"]) -> MetaOapg.properties.shared_secret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "authentication_port", "accounting_port", "server_type", "ip_address", "enable_a3", "org_id", "shared_secret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication_port"]) -> MetaOapg.properties.authentication_port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounting_port"]) -> MetaOapg.properties.accounting_port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_type"]) -> 'XiqRadiusServerType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip_address"]) -> MetaOapg.properties.ip_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_a3"]) -> MetaOapg.properties.enable_a3: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shared_secret"]) -> typing.Union[MetaOapg.properties.shared_secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "authentication_port", "accounting_port", "server_type", "ip_address", "enable_a3", "org_id", "shared_secret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        authentication_port: typing.Union[MetaOapg.properties.authentication_port, decimal.Decimal, int, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        accounting_port: typing.Union[MetaOapg.properties.accounting_port, decimal.Decimal, int, ],
        enable_a3: typing.Union[MetaOapg.properties.enable_a3, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        ip_address: typing.Union[MetaOapg.properties.ip_address, str, ],
        server_type: 'XiqRadiusServerType',
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        shared_secret: typing.Union[MetaOapg.properties.shared_secret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqExternalRadiusServer':
        return super().__new__(
            cls,
            *_args,
            authentication_port=authentication_port,
            update_time=update_time,
            create_time=create_time,
            accounting_port=accounting_port,
            enable_a3=enable_a3,
            name=name,
            id=id,
            ip_address=ip_address,
            server_type=server_type,
            org_id=org_id,
            shared_secret=shared_secret,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_radius_server_type import XiqRadiusServerType
