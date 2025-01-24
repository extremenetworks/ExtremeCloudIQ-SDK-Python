# extremecloudiq.model.xiq_internal_radius_server.XiqInternalRadiusServer

The configuration of internal RADIUS server object

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration of internal RADIUS server object | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_check_user_for_tls_auth** | bool,  | BoolClass,  | Enable check user for TLS auth or not | 
**server_key_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Server key ID | value must be a 64 bit integer
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**authentication_method_group** | [**XiqInternalRadiusServerAuthenticationMethodGroup**](XiqInternalRadiusServerAuthenticationMethodGroup.md) | [**XiqInternalRadiusServerAuthenticationMethodGroup**](XiqInternalRadiusServerAuthenticationMethodGroup.md) |  | 
**default_authentication_method** | [**XiqInternalRadiusServerAuthenticationMethod**](XiqInternalRadiusServerAuthenticationMethod.md) | [**XiqInternalRadiusServerAuthenticationMethod**](XiqInternalRadiusServerAuthenticationMethod.md) |  | 
**ca_certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | The CA certificate ID | value must be a 64 bit integer
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**authentication_server_port** | decimal.Decimal, int,  | decimal.Decimal,  | Port for the authentication, must enable authentication. Max:65535, Min:1 | if omitted the server will use the default value of 1812value must be a 32 bit integer
**enable_verify_server_cert** | bool,  | BoolClass,  | Enable verify server cert or not | 
**name** | str,  | str,  | The internal RADIUS server name | 
**enable_radius_accounting_settings** | bool,  | BoolClass,  | Enable the RADIUS server as accounting or not, must enable authentication server if want to enable accounting settings | 
**server_certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Server certificate ID | value must be a 64 bit integer
**[device_ids](#device_ids)** | list, tuple,  | tuple,  | The list of device ID associated with the internal RADIUS server | 
**enable_check_cert_common_name** | bool,  | BoolClass,  | Enable check cert common name or not | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**enable_authentication_server** | bool,  | BoolClass,  | Enable the RADIUS server as authentication or not | 
**external_user_directory** | [**XiqExternalUserDirectory**](XiqExternalUserDirectory.md) | [**XiqExternalUserDirectory**](XiqExternalUserDirectory.md) |  | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The internal RADIUS server description | [optional] 
**server_key_password** | str,  | str,  | password for server key | [optional] 
**enable_check_user_for_peap_auth** | bool,  | BoolClass,  | Enable check user for PEAP auth or not, for Active Directory as the external user directory only | [optional] 
**enable_check_user_for_ttls_auth** | bool,  | BoolClass,  | Enable check user for TTLS auth or not, for Active Directory as the external user directory only | [optional] 
**active_session_limit** | decimal.Decimal, int,  | decimal.Decimal,  | Active session limit, must enable accounting setting. Max:15, Min:0 | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**active_session_age_timeout** | decimal.Decimal, int,  | decimal.Decimal,  | Active session age timeout in seconds, must enable accounting setting. Max:300000000, Min:0 | [optional] if omitted the server will use the default value of 30value must be a 32 bit integer
**[clients](#clients)** | list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# device_ids

The list of device ID associated with the internal RADIUS server

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of device ID associated with the internal RADIUS server | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The list of device ID associated with the internal RADIUS server | value must be a 64 bit integer

# clients

The RADIUS clients of RADIUS proxy

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The RADIUS clients of RADIUS proxy | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRadiusClient**](XiqRadiusClient.md) | [**XiqRadiusClient**](XiqRadiusClient.md) | [**XiqRadiusClient**](XiqRadiusClient.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

