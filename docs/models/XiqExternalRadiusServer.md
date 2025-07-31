# extremecloudiq.model.xiq_external_radius_server.XiqExternalRadiusServer

The configuration of external RADIUS server object

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The configuration of external RADIUS server object | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**authentication_port** | decimal.Decimal, int,  | decimal.Decimal,  | The authentication port for the external RADIUS server (1 ~ 65535) | value must be a 32 bit integer
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**accounting_port** | decimal.Decimal, int,  | decimal.Decimal,  | The accounting port for the external RADIUS server (1 ~ 65535) | value must be a 32 bit integer
**enable_a3** | bool,  | BoolClass,  | Indicates whether this is an Extreme A3 RADIUS server or not, cannot be updated after creation. Please set it to false if it is not an Extreme A3 RADIUS server. | 
**name** | str,  | str,  | The external RADIUS server name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**server_type** | [**XiqRadiusServerType**](XiqRadiusServerType.md) | [**XiqRadiusServerType**](XiqRadiusServerType.md) |  | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**shared_secret** | str,  | str,  | The shared secret for the external RADIUS server (optional) | [optional] 
**ip_address** | str,  | str,  | The ip address or hostname of the RADIUS server | [optional] 
**enable_peer_discovery** | bool,  | BoolClass,  | Indicates whether the RADIUS server allows devices to connect automatically without manually defining their IP address or hostname. | [optional] 
**access_type** | [**XiqRadiusAccessType**](XiqRadiusAccessType.md) | [**XiqRadiusAccessType**](XiqRadiusAccessType.md) |  | [optional] 
**trust_pilot** | [**XiqCertificateBundle**](XiqCertificateBundle.md) | [**XiqCertificateBundle**](XiqCertificateBundle.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

