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


class XiqWiredHardwareResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Copilot Wired Hardware Response
    """


    class MetaOapg:
        
        class properties:
            
            
            class quality_index_graph(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqWiredHardwareEntity']:
                        return XiqWiredHardwareEntity
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqWiredHardwareEntity'], typing.List['XiqWiredHardwareEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'quality_index_graph':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqWiredHardwareEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "quality_index_graph": quality_index_graph,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quality_index_graph"]) -> MetaOapg.properties.quality_index_graph: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["quality_index_graph", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quality_index_graph"]) -> typing.Union[MetaOapg.properties.quality_index_graph, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["quality_index_graph", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        quality_index_graph: typing.Union[MetaOapg.properties.quality_index_graph, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqWiredHardwareResponse':
        return super().__new__(
            cls,
            *_args,
            quality_index_graph=quality_index_graph,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_wired_hardware_entity import XiqWiredHardwareEntity
