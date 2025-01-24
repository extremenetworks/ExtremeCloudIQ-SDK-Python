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


class XiqRadiusClientObject(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The RADIUS client object configuration
    """


    class MetaOapg:
        required = {
            "enable_permit_dynamic_authorization_message_change",
            "entries",
            "update_time",
            "enable_inject_operator_name_attribute",
            "create_time",
            "accounting_interim_update_interval",
            "enable_message_authenticator_attribute",
            "name",
            "id",
            "retry_interval",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            name = schemas.StrSchema
            enable_inject_operator_name_attribute = schemas.BoolSchema
            enable_message_authenticator_attribute = schemas.BoolSchema
            enable_permit_dynamic_authorization_message_change = schemas.BoolSchema
            
            
            class retry_interval(
                schemas.Int32Schema
            ):
                pass
            
            
            class accounting_interim_update_interval(
                schemas.Int32Schema
            ):
                pass
            
            
            class entries(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqRadiusClientObjectEntry']:
                        return XiqRadiusClientObjectEntry
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqRadiusClientObjectEntry'], typing.List['XiqRadiusClientObjectEntry']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqRadiusClientObjectEntry':
                    return super().__getitem__(i)
            description = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "name": name,
                "enable_inject_operator_name_attribute": enable_inject_operator_name_attribute,
                "enable_message_authenticator_attribute": enable_message_authenticator_attribute,
                "enable_permit_dynamic_authorization_message_change": enable_permit_dynamic_authorization_message_change,
                "retry_interval": retry_interval,
                "accounting_interim_update_interval": accounting_interim_update_interval,
                "entries": entries,
                "description": description,
            }
    
    enable_permit_dynamic_authorization_message_change: MetaOapg.properties.enable_permit_dynamic_authorization_message_change
    entries: MetaOapg.properties.entries
    update_time: MetaOapg.properties.update_time
    enable_inject_operator_name_attribute: MetaOapg.properties.enable_inject_operator_name_attribute
    create_time: MetaOapg.properties.create_time
    accounting_interim_update_interval: MetaOapg.properties.accounting_interim_update_interval
    enable_message_authenticator_attribute: MetaOapg.properties.enable_message_authenticator_attribute
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    retry_interval: MetaOapg.properties.retry_interval
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_inject_operator_name_attribute"]) -> MetaOapg.properties.enable_inject_operator_name_attribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_message_authenticator_attribute"]) -> MetaOapg.properties.enable_message_authenticator_attribute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_permit_dynamic_authorization_message_change"]) -> MetaOapg.properties.enable_permit_dynamic_authorization_message_change: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["retry_interval"]) -> MetaOapg.properties.retry_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounting_interim_update_interval"]) -> MetaOapg.properties.accounting_interim_update_interval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "enable_inject_operator_name_attribute", "enable_message_authenticator_attribute", "enable_permit_dynamic_authorization_message_change", "retry_interval", "accounting_interim_update_interval", "entries", "description", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["enable_inject_operator_name_attribute"]) -> MetaOapg.properties.enable_inject_operator_name_attribute: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_message_authenticator_attribute"]) -> MetaOapg.properties.enable_message_authenticator_attribute: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_permit_dynamic_authorization_message_change"]) -> MetaOapg.properties.enable_permit_dynamic_authorization_message_change: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["retry_interval"]) -> MetaOapg.properties.retry_interval: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounting_interim_update_interval"]) -> MetaOapg.properties.accounting_interim_update_interval: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entries"]) -> MetaOapg.properties.entries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "enable_inject_operator_name_attribute", "enable_message_authenticator_attribute", "enable_permit_dynamic_authorization_message_change", "retry_interval", "accounting_interim_update_interval", "entries", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_permit_dynamic_authorization_message_change: typing.Union[MetaOapg.properties.enable_permit_dynamic_authorization_message_change, bool, ],
        entries: typing.Union[MetaOapg.properties.entries, list, tuple, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        enable_inject_operator_name_attribute: typing.Union[MetaOapg.properties.enable_inject_operator_name_attribute, bool, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        accounting_interim_update_interval: typing.Union[MetaOapg.properties.accounting_interim_update_interval, decimal.Decimal, int, ],
        enable_message_authenticator_attribute: typing.Union[MetaOapg.properties.enable_message_authenticator_attribute, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        retry_interval: typing.Union[MetaOapg.properties.retry_interval, decimal.Decimal, int, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqRadiusClientObject':
        return super().__new__(
            cls,
            *_args,
            enable_permit_dynamic_authorization_message_change=enable_permit_dynamic_authorization_message_change,
            entries=entries,
            update_time=update_time,
            enable_inject_operator_name_attribute=enable_inject_operator_name_attribute,
            create_time=create_time,
            accounting_interim_update_interval=accounting_interim_update_interval,
            enable_message_authenticator_attribute=enable_message_authenticator_attribute,
            name=name,
            id=id,
            retry_interval=retry_interval,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_radius_client_object_entry import XiqRadiusClientObjectEntry
