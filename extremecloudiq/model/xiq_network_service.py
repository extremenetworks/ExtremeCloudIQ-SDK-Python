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


class XiqNetworkService(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The IP Firewall Action.
    """


    class MetaOapg:
        required = {
            "service_type",
            "update_time",
            "create_time",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            
            
            class service_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NETWORK": "NETWORK",
                        "APPLICATION": "APPLICATION",
                    }
                
                @schemas.classproperty
                def NETWORK(cls):
                    return cls("NETWORK")
                
                @schemas.classproperty
                def APPLICATION(cls):
                    return cls("APPLICATION")
            org_id = schemas.Int64Schema
            name = schemas.StrSchema
            description = schemas.StrSchema
        
            @staticmethod
            def ip_protocol() -> typing.Type['XiqNetworkIpProtocol']:
                return XiqNetworkIpProtocol
            protocol_number = schemas.Int32Schema
            port_number = schemas.Int32Schema
        
            @staticmethod
            def alg_type() -> typing.Type['XiqNetworkAlgType']:
                return XiqNetworkAlgType
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "service_type": service_type,
                "org_id": org_id,
                "name": name,
                "description": description,
                "ip_protocol": ip_protocol,
                "protocol_number": protocol_number,
                "port_number": port_number,
                "alg_type": alg_type,
            }
    
    service_type: MetaOapg.properties.service_type
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service_type"]) -> MetaOapg.properties.service_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ip_protocol"]) -> 'XiqNetworkIpProtocol': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol_number"]) -> MetaOapg.properties.protocol_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port_number"]) -> MetaOapg.properties.port_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alg_type"]) -> 'XiqNetworkAlgType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "service_type", "org_id", "name", "description", "ip_protocol", "protocol_number", "port_number", "alg_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service_type"]) -> MetaOapg.properties.service_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ip_protocol"]) -> typing.Union['XiqNetworkIpProtocol', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol_number"]) -> typing.Union[MetaOapg.properties.protocol_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port_number"]) -> typing.Union[MetaOapg.properties.port_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alg_type"]) -> typing.Union['XiqNetworkAlgType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "service_type", "org_id", "name", "description", "ip_protocol", "protocol_number", "port_number", "alg_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        service_type: typing.Union[MetaOapg.properties.service_type, str, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        ip_protocol: typing.Union['XiqNetworkIpProtocol', schemas.Unset] = schemas.unset,
        protocol_number: typing.Union[MetaOapg.properties.protocol_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        port_number: typing.Union[MetaOapg.properties.port_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        alg_type: typing.Union['XiqNetworkAlgType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqNetworkService':
        return super().__new__(
            cls,
            *_args,
            service_type=service_type,
            update_time=update_time,
            create_time=create_time,
            id=id,
            org_id=org_id,
            name=name,
            description=description,
            ip_protocol=ip_protocol,
            protocol_number=protocol_number,
            port_number=port_number,
            alg_type=alg_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_network_alg_type import XiqNetworkAlgType
from extremecloudiq.model.xiq_network_ip_protocol import XiqNetworkIpProtocol
