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


class XiqCliOutput(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The CLI output
    """


    class MetaOapg:
        required = {
            "cli",
            "response_code",
        }
        
        class properties:
            cli = schemas.StrSchema
        
            @staticmethod
            def response_code() -> typing.Type['XiqCliResponseCode']:
                return XiqCliResponseCode
            output = schemas.StrSchema
            __annotations__ = {
                "cli": cli,
                "response_code": response_code,
                "output": output,
            }
    
    cli: MetaOapg.properties.cli
    response_code: 'XiqCliResponseCode'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cli"]) -> MetaOapg.properties.cli: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["response_code"]) -> 'XiqCliResponseCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output"]) -> MetaOapg.properties.output: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cli", "response_code", "output", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cli"]) -> MetaOapg.properties.cli: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["response_code"]) -> 'XiqCliResponseCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output"]) -> typing.Union[MetaOapg.properties.output, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cli", "response_code", "output", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cli: typing.Union[MetaOapg.properties.cli, str, ],
        response_code: 'XiqCliResponseCode',
        output: typing.Union[MetaOapg.properties.output, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCliOutput':
        return super().__new__(
            cls,
            *_args,
            cli=cli,
            response_code=response_code,
            output=output,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_cli_response_code import XiqCliResponseCode
