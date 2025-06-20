# coding: utf-8

"""
    ExtremeCloud IQ API

    ExtremeCloud IQ RESTful API for external and internal applications.  # noqa: E501

    The version of the OpenAPI document: 25.3.0.140
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


class XiqCreateVlanProfileRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "enable_classification",
            "name",
            "default_vlan_id",
        }
        
        class properties:
            name = schemas.StrSchema
            default_vlan_id = schemas.Int32Schema
            enable_classification = schemas.BoolSchema
            
            
            class classified_entries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqCreateVlanObjectClassifiedEntryRequest']:
                        return XiqCreateVlanObjectClassifiedEntryRequest
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqCreateVlanObjectClassifiedEntryRequest'], typing.List['XiqCreateVlanObjectClassifiedEntryRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'classified_entries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqCreateVlanObjectClassifiedEntryRequest':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "default_vlan_id": default_vlan_id,
                "enable_classification": enable_classification,
                "classified_entries": classified_entries,
            }
    
    enable_classification: MetaOapg.properties.enable_classification
    name: MetaOapg.properties.name
    default_vlan_id: MetaOapg.properties.default_vlan_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_vlan_id"]) -> MetaOapg.properties.default_vlan_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_classification"]) -> MetaOapg.properties.enable_classification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classified_entries"]) -> MetaOapg.properties.classified_entries: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "default_vlan_id", "enable_classification", "classified_entries", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_vlan_id"]) -> MetaOapg.properties.default_vlan_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_classification"]) -> MetaOapg.properties.enable_classification: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classified_entries"]) -> typing.Union[MetaOapg.properties.classified_entries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "default_vlan_id", "enable_classification", "classified_entries", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_classification: typing.Union[MetaOapg.properties.enable_classification, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        default_vlan_id: typing.Union[MetaOapg.properties.default_vlan_id, decimal.Decimal, int, ],
        classified_entries: typing.Union[MetaOapg.properties.classified_entries, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCreateVlanProfileRequest':
        return super().__new__(
            cls,
            *_args,
            enable_classification=enable_classification,
            name=name,
            default_vlan_id=default_vlan_id,
            classified_entries=classified_entries,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_create_vlan_object_classified_entry_request import XiqCreateVlanObjectClassifiedEntryRequest
