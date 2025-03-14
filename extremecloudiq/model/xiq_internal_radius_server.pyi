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


class XiqInternalRadiusServer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The configuration of internal RADIUS server object
    """


    class MetaOapg:
        required = {
            "enable_check_user_for_tls_auth",
            "server_key_id",
            "create_time",
            "authentication_method_group",
            "default_authentication_method",
            "ca_certificate_id",
            "update_time",
            "authentication_server_port",
            "enable_verify_server_cert",
            "name",
            "enable_radius_accounting_settings",
            "server_certificate_id",
            "device_ids",
            "enable_check_cert_common_name",
            "id",
            "enable_authentication_server",
            "external_user_directory",
        }
        
        class properties:
            id = schemas.Int64Schema
            create_time = schemas.DateTimeSchema
            update_time = schemas.DateTimeSchema
            name = schemas.StrSchema
        
            @staticmethod
            def authentication_method_group() -> typing.Type['XiqInternalRadiusServerAuthenticationMethodGroup']:
                return XiqInternalRadiusServerAuthenticationMethodGroup
        
            @staticmethod
            def default_authentication_method() -> typing.Type['XiqInternalRadiusServerAuthenticationMethod']:
                return XiqInternalRadiusServerAuthenticationMethod
            enable_verify_server_cert = schemas.BoolSchema
            enable_check_cert_common_name = schemas.BoolSchema
            enable_check_user_for_tls_auth = schemas.BoolSchema
            enable_authentication_server = schemas.BoolSchema
            enable_radius_accounting_settings = schemas.BoolSchema
            
            
            class authentication_server_port(
                schemas.Int32Schema
            ):
                pass
        
            @staticmethod
            def external_user_directory() -> typing.Type['XiqExternalUserDirectory']:
                return XiqExternalUserDirectory
            ca_certificate_id = schemas.Int64Schema
            server_certificate_id = schemas.Int64Schema
            server_key_id = schemas.Int64Schema
            
            
            class device_ids(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int64Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'device_ids':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            org_id = schemas.Int64Schema
            description = schemas.StrSchema
            server_key_password = schemas.StrSchema
            enable_check_user_for_peap_auth = schemas.BoolSchema
            enable_check_user_for_ttls_auth = schemas.BoolSchema
            
            
            class active_session_limit(
                schemas.Int32Schema
            ):
                pass
            
            
            class active_session_age_timeout(
                schemas.Int32Schema
            ):
                pass
            
            
            class clients(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['XiqRadiusClient']:
                        return XiqRadiusClient
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['XiqRadiusClient'], typing.List['XiqRadiusClient']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'clients':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'XiqRadiusClient':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "create_time": create_time,
                "update_time": update_time,
                "name": name,
                "authentication_method_group": authentication_method_group,
                "default_authentication_method": default_authentication_method,
                "enable_verify_server_cert": enable_verify_server_cert,
                "enable_check_cert_common_name": enable_check_cert_common_name,
                "enable_check_user_for_tls_auth": enable_check_user_for_tls_auth,
                "enable_authentication_server": enable_authentication_server,
                "enable_radius_accounting_settings": enable_radius_accounting_settings,
                "authentication_server_port": authentication_server_port,
                "external_user_directory": external_user_directory,
                "ca_certificate_id": ca_certificate_id,
                "server_certificate_id": server_certificate_id,
                "server_key_id": server_key_id,
                "device_ids": device_ids,
                "org_id": org_id,
                "description": description,
                "server_key_password": server_key_password,
                "enable_check_user_for_peap_auth": enable_check_user_for_peap_auth,
                "enable_check_user_for_ttls_auth": enable_check_user_for_ttls_auth,
                "active_session_limit": active_session_limit,
                "active_session_age_timeout": active_session_age_timeout,
                "clients": clients,
            }
    
    enable_check_user_for_tls_auth: MetaOapg.properties.enable_check_user_for_tls_auth
    server_key_id: MetaOapg.properties.server_key_id
    create_time: MetaOapg.properties.create_time
    authentication_method_group: 'XiqInternalRadiusServerAuthenticationMethodGroup'
    default_authentication_method: 'XiqInternalRadiusServerAuthenticationMethod'
    ca_certificate_id: MetaOapg.properties.ca_certificate_id
    update_time: MetaOapg.properties.update_time
    authentication_server_port: MetaOapg.properties.authentication_server_port
    enable_verify_server_cert: MetaOapg.properties.enable_verify_server_cert
    name: MetaOapg.properties.name
    enable_radius_accounting_settings: MetaOapg.properties.enable_radius_accounting_settings
    server_certificate_id: MetaOapg.properties.server_certificate_id
    device_ids: MetaOapg.properties.device_ids
    enable_check_cert_common_name: MetaOapg.properties.enable_check_cert_common_name
    id: MetaOapg.properties.id
    enable_authentication_server: MetaOapg.properties.enable_authentication_server
    external_user_directory: 'XiqExternalUserDirectory'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["create_time"]) -> MetaOapg.properties.create_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["update_time"]) -> MetaOapg.properties.update_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication_method_group"]) -> 'XiqInternalRadiusServerAuthenticationMethodGroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_authentication_method"]) -> 'XiqInternalRadiusServerAuthenticationMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_verify_server_cert"]) -> MetaOapg.properties.enable_verify_server_cert: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_check_cert_common_name"]) -> MetaOapg.properties.enable_check_cert_common_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_check_user_for_tls_auth"]) -> MetaOapg.properties.enable_check_user_for_tls_auth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_authentication_server"]) -> MetaOapg.properties.enable_authentication_server: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_radius_accounting_settings"]) -> MetaOapg.properties.enable_radius_accounting_settings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authentication_server_port"]) -> MetaOapg.properties.authentication_server_port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_user_directory"]) -> 'XiqExternalUserDirectory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ca_certificate_id"]) -> MetaOapg.properties.ca_certificate_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_certificate_id"]) -> MetaOapg.properties.server_certificate_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_key_id"]) -> MetaOapg.properties.server_key_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device_ids"]) -> MetaOapg.properties.device_ids: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_key_password"]) -> MetaOapg.properties.server_key_password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_check_user_for_peap_auth"]) -> MetaOapg.properties.enable_check_user_for_peap_auth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enable_check_user_for_ttls_auth"]) -> MetaOapg.properties.enable_check_user_for_ttls_auth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_session_limit"]) -> MetaOapg.properties.active_session_limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active_session_age_timeout"]) -> MetaOapg.properties.active_session_age_timeout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clients"]) -> MetaOapg.properties.clients: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "authentication_method_group", "default_authentication_method", "enable_verify_server_cert", "enable_check_cert_common_name", "enable_check_user_for_tls_auth", "enable_authentication_server", "enable_radius_accounting_settings", "authentication_server_port", "external_user_directory", "ca_certificate_id", "server_certificate_id", "server_key_id", "device_ids", "org_id", "description", "server_key_password", "enable_check_user_for_peap_auth", "enable_check_user_for_ttls_auth", "active_session_limit", "active_session_age_timeout", "clients", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["authentication_method_group"]) -> 'XiqInternalRadiusServerAuthenticationMethodGroup': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_authentication_method"]) -> 'XiqInternalRadiusServerAuthenticationMethod': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_verify_server_cert"]) -> MetaOapg.properties.enable_verify_server_cert: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_check_cert_common_name"]) -> MetaOapg.properties.enable_check_cert_common_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_check_user_for_tls_auth"]) -> MetaOapg.properties.enable_check_user_for_tls_auth: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_authentication_server"]) -> MetaOapg.properties.enable_authentication_server: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_radius_accounting_settings"]) -> MetaOapg.properties.enable_radius_accounting_settings: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authentication_server_port"]) -> MetaOapg.properties.authentication_server_port: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_user_directory"]) -> 'XiqExternalUserDirectory': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ca_certificate_id"]) -> MetaOapg.properties.ca_certificate_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_certificate_id"]) -> MetaOapg.properties.server_certificate_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_key_id"]) -> MetaOapg.properties.server_key_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device_ids"]) -> MetaOapg.properties.device_ids: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_key_password"]) -> typing.Union[MetaOapg.properties.server_key_password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_check_user_for_peap_auth"]) -> typing.Union[MetaOapg.properties.enable_check_user_for_peap_auth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enable_check_user_for_ttls_auth"]) -> typing.Union[MetaOapg.properties.enable_check_user_for_ttls_auth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_session_limit"]) -> typing.Union[MetaOapg.properties.active_session_limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active_session_age_timeout"]) -> typing.Union[MetaOapg.properties.active_session_age_timeout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clients"]) -> typing.Union[MetaOapg.properties.clients, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "create_time", "update_time", "name", "authentication_method_group", "default_authentication_method", "enable_verify_server_cert", "enable_check_cert_common_name", "enable_check_user_for_tls_auth", "enable_authentication_server", "enable_radius_accounting_settings", "authentication_server_port", "external_user_directory", "ca_certificate_id", "server_certificate_id", "server_key_id", "device_ids", "org_id", "description", "server_key_password", "enable_check_user_for_peap_auth", "enable_check_user_for_ttls_auth", "active_session_limit", "active_session_age_timeout", "clients", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enable_check_user_for_tls_auth: typing.Union[MetaOapg.properties.enable_check_user_for_tls_auth, bool, ],
        server_key_id: typing.Union[MetaOapg.properties.server_key_id, decimal.Decimal, int, ],
        create_time: typing.Union[MetaOapg.properties.create_time, str, datetime, ],
        authentication_method_group: 'XiqInternalRadiusServerAuthenticationMethodGroup',
        default_authentication_method: 'XiqInternalRadiusServerAuthenticationMethod',
        ca_certificate_id: typing.Union[MetaOapg.properties.ca_certificate_id, decimal.Decimal, int, ],
        update_time: typing.Union[MetaOapg.properties.update_time, str, datetime, ],
        authentication_server_port: typing.Union[MetaOapg.properties.authentication_server_port, decimal.Decimal, int, ],
        enable_verify_server_cert: typing.Union[MetaOapg.properties.enable_verify_server_cert, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        enable_radius_accounting_settings: typing.Union[MetaOapg.properties.enable_radius_accounting_settings, bool, ],
        server_certificate_id: typing.Union[MetaOapg.properties.server_certificate_id, decimal.Decimal, int, ],
        device_ids: typing.Union[MetaOapg.properties.device_ids, list, tuple, ],
        enable_check_cert_common_name: typing.Union[MetaOapg.properties.enable_check_cert_common_name, bool, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        enable_authentication_server: typing.Union[MetaOapg.properties.enable_authentication_server, bool, ],
        external_user_directory: 'XiqExternalUserDirectory',
        org_id: typing.Union[MetaOapg.properties.org_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        server_key_password: typing.Union[MetaOapg.properties.server_key_password, str, schemas.Unset] = schemas.unset,
        enable_check_user_for_peap_auth: typing.Union[MetaOapg.properties.enable_check_user_for_peap_auth, bool, schemas.Unset] = schemas.unset,
        enable_check_user_for_ttls_auth: typing.Union[MetaOapg.properties.enable_check_user_for_ttls_auth, bool, schemas.Unset] = schemas.unset,
        active_session_limit: typing.Union[MetaOapg.properties.active_session_limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active_session_age_timeout: typing.Union[MetaOapg.properties.active_session_age_timeout, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        clients: typing.Union[MetaOapg.properties.clients, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'XiqInternalRadiusServer':
        return super().__new__(
            cls,
            *_args,
            enable_check_user_for_tls_auth=enable_check_user_for_tls_auth,
            server_key_id=server_key_id,
            create_time=create_time,
            authentication_method_group=authentication_method_group,
            default_authentication_method=default_authentication_method,
            ca_certificate_id=ca_certificate_id,
            update_time=update_time,
            authentication_server_port=authentication_server_port,
            enable_verify_server_cert=enable_verify_server_cert,
            name=name,
            enable_radius_accounting_settings=enable_radius_accounting_settings,
            server_certificate_id=server_certificate_id,
            device_ids=device_ids,
            enable_check_cert_common_name=enable_check_cert_common_name,
            id=id,
            enable_authentication_server=enable_authentication_server,
            external_user_directory=external_user_directory,
            org_id=org_id,
            description=description,
            server_key_password=server_key_password,
            enable_check_user_for_peap_auth=enable_check_user_for_peap_auth,
            enable_check_user_for_ttls_auth=enable_check_user_for_ttls_auth,
            active_session_limit=active_session_limit,
            active_session_age_timeout=active_session_age_timeout,
            clients=clients,
            _configuration=_configuration,
            **kwargs,
        )

from extremecloudiq.model.xiq_external_user_directory import XiqExternalUserDirectory
from extremecloudiq.model.xiq_internal_radius_server_authentication_method import XiqInternalRadiusServerAuthenticationMethod
from extremecloudiq.model.xiq_internal_radius_server_authentication_method_group import XiqInternalRadiusServerAuthenticationMethodGroup
from extremecloudiq.model.xiq_radius_client import XiqRadiusClient
