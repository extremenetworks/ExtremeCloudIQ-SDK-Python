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


class XiqAttachUPAssignmentRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class user_profile_assignment_rules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqAttachUPAssignmentEntry']:
                        return XiqAttachUPAssignmentEntry
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqAttachUPAssignmentEntry'], typing.List['XiqAttachUPAssignmentEntry']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'user_profile_assignment_rules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqAttachUPAssignmentEntry':
                    return super().__getitem__(i)
            enable_user_profile_assignment = schemas.BoolSchema
            enable_radius_attribute_user_profile_assignment = schemas.BoolSchema
        
            @staticmethod
            def attribute_type() -> typing.Type['XiqAttributeType']:
                return XiqAttributeType
            attribute_key = schemas.Int32Schema
            default_radius_client_object_id = schemas.Int64Schema
            __annotations__ = {
                "user_profile_assignment_rules": user_profile_assignment_rules,
                "enable_user_profile_assignment": enable_user_profile_assignment,
                "enable_radius_attribute_user_profile_assignment": enable_radius_attribute_user_profile_assignment,
                "attribute_type": attribute_type,
                "attribute_key": attribute_key,
                "default_radius_client_object_id": default_radius_client_object_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_profile_assignment_rules"]) -> MetaOapg.properties.user_profile_assignment_rules: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_user_profile_assignment"]) -> MetaOapg.properties.enable_user_profile_assignment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_radius_attribute_user_profile_assignment"]) -> MetaOapg.properties.enable_radius_attribute_user_profile_assignment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribute_type"]) -> 'XiqAttributeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attribute_key"]) -> MetaOapg.properties.attribute_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_radius_client_object_id"]) -> MetaOapg.properties.default_radius_client_object_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_profile_assignment_rules", "enable_user_profile_assignment", "enable_radius_attribute_user_profile_assignment", "attribute_type", "attribute_key", "default_radius_client_object_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_profile_assignment_rules"]) -> typing.Union[MetaOapg.properties.user_profile_assignment_rules, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_user_profile_assignment"]) -> typing.Union[MetaOapg.properties.enable_user_profile_assignment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_radius_attribute_user_profile_assignment"]) -> typing.Union[MetaOapg.properties.enable_radius_attribute_user_profile_assignment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribute_type"]) -> typing.Union['XiqAttributeType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attribute_key"]) -> typing.Union[MetaOapg.properties.attribute_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_radius_client_object_id"]) -> typing.Union[MetaOapg.properties.default_radius_client_object_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_profile_assignment_rules", "enable_user_profile_assignment", "enable_radius_attribute_user_profile_assignment", "attribute_type", "attribute_key", "default_radius_client_object_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        user_profile_assignment_rules: typing.Union[MetaOapg.properties.user_profile_assignment_rules, list, tuple, schemas.Unset] = schemas.unset,
        enable_user_profile_assignment: typing.Union[MetaOapg.properties.enable_user_profile_assignment, bool, schemas.Unset] = schemas.unset,
        enable_radius_attribute_user_profile_assignment: typing.Union[MetaOapg.properties.enable_radius_attribute_user_profile_assignment, bool, schemas.Unset] = schemas.unset,
        attribute_type: typing.Union['XiqAttributeType', schemas.Unset] = schemas.unset,
        attribute_key: typing.Union[MetaOapg.properties.attribute_key, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        default_radius_client_object_id: typing.Union[MetaOapg.properties.default_radius_client_object_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqAttachUPAssignmentRequest':
        return super().__new__(
            cls,
            *_args,
            user_profile_assignment_rules=user_profile_assignment_rules,
            enable_user_profile_assignment=enable_user_profile_assignment,
            enable_radius_attribute_user_profile_assignment=enable_radius_attribute_user_profile_assignment,
            attribute_type=attribute_type,
            attribute_key=attribute_key,
            default_radius_client_object_id=default_radius_client_object_id,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_attach_up_assignment_entry import XiqAttachUPAssignmentEntry
from extremecloudiq.model.xiq_attribute_type import XiqAttributeType
