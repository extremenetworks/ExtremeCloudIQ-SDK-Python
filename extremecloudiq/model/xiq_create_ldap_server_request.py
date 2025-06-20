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


class XiqCreateLdapServerRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bind_dn",
            "protocol_type",
            "enable_tls",
            "base_dn",
            "enable_strip_realm_name",
            "l3_address_profile_id",
            "destination_port",
            "verification_mode",
            "name",
            "bind_dn_password",
        }
        
        class properties:
            name = schemas.StrSchema
            enable_tls = schemas.BoolSchema
            bind_dn = schemas.StrSchema
            bind_dn_password = schemas.StrSchema
            base_dn = schemas.StrSchema
            l3_address_profile_id = schemas.Int64Schema
        
            @staticmethod
            def protocol_type() -> typing.Type['XiqLdapProtocolType']:
                return XiqLdapProtocolType
            enable_strip_realm_name = schemas.BoolSchema
            
            
            class destination_port(
                schemas.Int32Schema
            ):
            
            
                class MetaOapg:
                    format = 'int32'
                    inclusive_minimum = 1
        
            @staticmethod
            def verification_mode() -> typing.Type['XiqLdapServerVerificationMode']:
                return XiqLdapServerVerificationMode
            description = schemas.StrSchema
            ca_certificate_id = schemas.Int64Schema
            client_certificate_id = schemas.Int64Schema
            client_key_id = schemas.Int64Schema
            client_key_password = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "enable_tls": enable_tls,
                "bind_dn": bind_dn,
                "bind_dn_password": bind_dn_password,
                "base_dn": base_dn,
                "l3_address_profile_id": l3_address_profile_id,
                "protocol_type": protocol_type,
                "enable_strip_realm_name": enable_strip_realm_name,
                "destination_port": destination_port,
                "verification_mode": verification_mode,
                "description": description,
                "ca_certificate_id": ca_certificate_id,
                "client_certificate_id": client_certificate_id,
                "client_key_id": client_key_id,
                "client_key_password": client_key_password,
            }
    
    bind_dn: MetaOapg.properties.bind_dn
    protocol_type: 'XiqLdapProtocolType'
    enable_tls: MetaOapg.properties.enable_tls
    base_dn: MetaOapg.properties.base_dn
    enable_strip_realm_name: MetaOapg.properties.enable_strip_realm_name
    l3_address_profile_id: MetaOapg.properties.l3_address_profile_id
    destination_port: MetaOapg.properties.destination_port
    verification_mode: 'XiqLdapServerVerificationMode'
    name: MetaOapg.properties.name
    bind_dn_password: MetaOapg.properties.bind_dn_password
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_tls"]) -> MetaOapg.properties.enable_tls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bind_dn"]) -> MetaOapg.properties.bind_dn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bind_dn_password"]) -> MetaOapg.properties.bind_dn_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_dn"]) -> MetaOapg.properties.base_dn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["l3_address_profile_id"]) -> MetaOapg.properties.l3_address_profile_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol_type"]) -> 'XiqLdapProtocolType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_strip_realm_name"]) -> MetaOapg.properties.enable_strip_realm_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination_port"]) -> MetaOapg.properties.destination_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_mode"]) -> 'XiqLdapServerVerificationMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ca_certificate_id"]) -> MetaOapg.properties.ca_certificate_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_certificate_id"]) -> MetaOapg.properties.client_certificate_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_key_id"]) -> MetaOapg.properties.client_key_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_key_password"]) -> MetaOapg.properties.client_key_password: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "enable_tls", "bind_dn", "bind_dn_password", "base_dn", "l3_address_profile_id", "protocol_type", "enable_strip_realm_name", "destination_port", "verification_mode", "description", "ca_certificate_id", "client_certificate_id", "client_key_id", "client_key_password", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_tls"]) -> MetaOapg.properties.enable_tls: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bind_dn"]) -> MetaOapg.properties.bind_dn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bind_dn_password"]) -> MetaOapg.properties.bind_dn_password: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_dn"]) -> MetaOapg.properties.base_dn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["l3_address_profile_id"]) -> MetaOapg.properties.l3_address_profile_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol_type"]) -> 'XiqLdapProtocolType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_strip_realm_name"]) -> MetaOapg.properties.enable_strip_realm_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination_port"]) -> MetaOapg.properties.destination_port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_mode"]) -> 'XiqLdapServerVerificationMode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ca_certificate_id"]) -> typing.Union[MetaOapg.properties.ca_certificate_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_certificate_id"]) -> typing.Union[MetaOapg.properties.client_certificate_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_key_id"]) -> typing.Union[MetaOapg.properties.client_key_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_key_password"]) -> typing.Union[MetaOapg.properties.client_key_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "enable_tls", "bind_dn", "bind_dn_password", "base_dn", "l3_address_profile_id", "protocol_type", "enable_strip_realm_name", "destination_port", "verification_mode", "description", "ca_certificate_id", "client_certificate_id", "client_key_id", "client_key_password", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bind_dn: typing.Union[MetaOapg.properties.bind_dn, str, ],
        protocol_type: 'XiqLdapProtocolType',
        enable_tls: typing.Union[MetaOapg.properties.enable_tls, bool, ],
        base_dn: typing.Union[MetaOapg.properties.base_dn, str, ],
        enable_strip_realm_name: typing.Union[MetaOapg.properties.enable_strip_realm_name, bool, ],
        l3_address_profile_id: typing.Union[MetaOapg.properties.l3_address_profile_id, decimal.Decimal, int, ],
        destination_port: typing.Union[MetaOapg.properties.destination_port, decimal.Decimal, int, ],
        verification_mode: 'XiqLdapServerVerificationMode',
        name: typing.Union[MetaOapg.properties.name, str, ],
        bind_dn_password: typing.Union[MetaOapg.properties.bind_dn_password, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        ca_certificate_id: typing.Union[MetaOapg.properties.ca_certificate_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        client_certificate_id: typing.Union[MetaOapg.properties.client_certificate_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        client_key_id: typing.Union[MetaOapg.properties.client_key_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        client_key_password: typing.Union[MetaOapg.properties.client_key_password, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqCreateLdapServerRequest':
        return super().__new__(
            cls,
            *_args,
            bind_dn=bind_dn,
            protocol_type=protocol_type,
            enable_tls=enable_tls,
            base_dn=base_dn,
            enable_strip_realm_name=enable_strip_realm_name,
            l3_address_profile_id=l3_address_profile_id,
            destination_port=destination_port,
            verification_mode=verification_mode,
            name=name,
            bind_dn_password=bind_dn_password,
            description=description,
            ca_certificate_id=ca_certificate_id,
            client_certificate_id=client_certificate_id,
            client_key_id=client_key_id,
            client_key_password=client_key_password,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_ldap_protocol_type import XiqLdapProtocolType
from extremecloudiq.model.xiq_ldap_server_verification_mode import XiqLdapServerVerificationMode
