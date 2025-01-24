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


class XiqHotspotNaiRealm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List of Network Access Identification (NAI) realms. A NAI realm is a FQDN of a service provider.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            description = schemas.StrSchema
            
            
            class eap_methods(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqHotspotEapMethod']:
                        return XiqHotspotEapMethod
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqHotspotEapMethod'], typing.List['XiqHotspotEapMethod']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'eap_methods':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqHotspotEapMethod':
                    return super().__getitem__(i)
        
            @staticmethod
            def encoding_type() -> typing.Type['XiqHotspotNaiEncodingType']:
                return XiqHotspotNaiEncodingType
            __annotations__ = {
                "name": name,
                "description": description,
                "eap_methods": eap_methods,
                "encoding_type": encoding_type,
            }
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eap_methods"]) -> MetaOapg.properties.eap_methods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encoding_type"]) -> 'XiqHotspotNaiEncodingType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "description", "eap_methods", "encoding_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eap_methods"]) -> typing.Union[MetaOapg.properties.eap_methods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encoding_type"]) -> typing.Union['XiqHotspotNaiEncodingType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "description", "eap_methods", "encoding_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        eap_methods: typing.Union[MetaOapg.properties.eap_methods, list, tuple, schemas.Unset] = schemas.unset,
        encoding_type: typing.Union['XiqHotspotNaiEncodingType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqHotspotNaiRealm':
        return super().__new__(
            cls,
            *_args,
            name=name,
            description=description,
            eap_methods=eap_methods,
            encoding_type=encoding_type,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_hotspot_eap_method import XiqHotspotEapMethod
from extremecloudiq.model.xiq_hotspot_nai_encoding_type import XiqHotspotNaiEncodingType
