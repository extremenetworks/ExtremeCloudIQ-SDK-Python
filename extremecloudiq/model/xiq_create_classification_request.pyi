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


class XiqCreateClassificationRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The details of rule assignments
    """


    class MetaOapg:
        required = {
            "match",
            "classification_type",
            "classification_type_id",
        }
        
        class properties:
            
            
            class classification_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CLASSIFICATION_TYPE_UNSPECIFIED(cls):
                    return cls("CLASSIFICATION_TYPE_UNSPECIFIED")
                
                @schemas.classproperty
                def CLASSIFICATION_TYPE_LOCATION(cls):
                    return cls("CLASSIFICATION_TYPE_LOCATION")
                
                @schemas.classproperty
                def CLASSIFICATION_TYPE_CLOUD_CONFIG_GROUP(cls):
                    return cls("CLASSIFICATION_TYPE_CLOUD_CONFIG_GROUP")
                
                @schemas.classproperty
                def CLASSIFICATION_TYPE_IP_ADDRESS(cls):
                    return cls("CLASSIFICATION_TYPE_IP_ADDRESS")
                
                @schemas.classproperty
                def CLASSIFICATION_TYPE_IP_SUBNET(cls):
                    return cls("CLASSIFICATION_TYPE_IP_SUBNET")
                
                @schemas.classproperty
                def CLASSIFICATION_TYPE_IP_RANGE(cls):
                    return cls("CLASSIFICATION_TYPE_IP_RANGE")
                
                @schemas.classproperty
                def UNRECOGNIZED(cls):
                    return cls("UNRECOGNIZED")
            match = schemas.BoolSchema
            classification_type_id = schemas.Int64Schema
            __annotations__ = {
                "classification_type": classification_type,
                "match": match,
                "classification_type_id": classification_type_id,
            }
    
    match: MetaOapg.properties.match
    classification_type: MetaOapg.properties.classification_type
    classification_type_id: MetaOapg.properties.classification_type_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification_type"]) -> MetaOapg.properties.classification_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["match"]) -> MetaOapg.properties.match: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification_type_id"]) -> MetaOapg.properties.classification_type_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["classification_type", "match", "classification_type_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification_type"]) -> MetaOapg.properties.classification_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["match"]) -> MetaOapg.properties.match: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification_type_id"]) -> MetaOapg.properties.classification_type_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["classification_type", "match", "classification_type_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        match: typing.Union[MetaOapg.properties.match, bool, ],
        classification_type: typing.Union[MetaOapg.properties.classification_type, str, ],
        classification_type_id: typing.Union[MetaOapg.properties.classification_type_id, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCreateClassificationRequest':
        return super().__new__(
            cls,
            *_args,
            match=match,
            classification_type=classification_type,
            classification_type_id=classification_type_id,
            _configuration=_configuration,
            **kwargs,
        )
