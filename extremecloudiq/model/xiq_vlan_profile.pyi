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


class XiqVlanProfile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The payload of common object - VLAN profile
    """


    class MetaOapg:
        required = {
            "update_time",
            "create_time",
            "enable_classification",
            "name",
            "default_vlan_id",
            "id",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            name = schemas.StrSchema
            
            
            class default_vlan_id(
                schemas.Int32Schema
            ):
                pass
            enable_classification = schemas.BoolSchema
            org_id = schemas.Int64Schema
            
            
            class classified_entries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqVlanObjectClassifiedEntry']:
                        return XiqVlanObjectClassifiedEntry
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqVlanObjectClassifiedEntry'], typing.List['XiqVlanObjectClassifiedEntry']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'classified_entries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqVlanObjectClassifiedEntry':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "name": name,
                "default_vlan_id": default_vlan_id,
                "enable_classification": enable_classification,
                "org_id": org_id,
                "classified_entries": classified_entries,
            }
    
    update_time: MetaOapg.properties.update_time
    create_time: MetaOapg.properties.create_time
    enable_classification: MetaOapg.properties.enable_classification
    name: MetaOapg.properties.name
    default_vlan_id: MetaOapg.properties.default_vlan_id
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_vlan_id"]) -> MetaOapg.properties.default_vlan_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_classification"]) -> MetaOapg.properties.enable_classification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classified_entries"]) -> MetaOapg.properties.classified_entries: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "default_vlan_id", "enable_classification", "org_id", "classified_entries", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["default_vlan_id"]) -> MetaOapg.properties.default_vlan_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_classification"]) -> MetaOapg.properties.enable_classification: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classified_entries"]) -> typing.Union[MetaOapg.properties.classified_entries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "default_vlan_id", "enable_classification", "org_id", "classified_entries", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        enable_classification: typing.Union[MetaOapg.properties.enable_classification, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        default_vlan_id: typing.Union[MetaOapg.properties.default_vlan_id, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        classified_entries: typing.Union[MetaOapg.properties.classified_entries, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqVlanProfile':
        return super().__new__(
            cls,
            *_args,
            update_time=update_time,
            create_time=create_time,
            enable_classification=enable_classification,
            name=name,
            default_vlan_id=default_vlan_id,
            id=id,
            org_id=org_id,
            classified_entries=classified_entries,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_vlan_object_classified_entry import XiqVlanObjectClassifiedEntry
