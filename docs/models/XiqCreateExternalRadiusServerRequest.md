# extremecloudiq.model.xiq_create_external_radius_server_request.XiqCreateExternalRadiusServerRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**authentication_port** | decimal.Decimal, int,  | decimal.Decimal,  | The authentication port for the external RADIUS server (1 ~ 65535) | if omitted the server will use the default value of 1812value must be a 32 bit integer
**accounting_port** | decimal.Decimal, int,  | decimal.Decimal,  | The accounting port for the external RADIUS server (1 ~ 65535) | if omitted the server will use the default value of 1813value must be a 32 bit integer
**enable_a3** | bool,  | BoolClass,  | Indicates whether this is an Extreme A3 RADIUS server or not, cannot be updated after creation. Please set it to false if it is not an Extreme A3 RADIUS server. | 
**name** | str,  | str,  | The external RADIUS server name | 
**ip_addr** | str,  | str,  | The IP address or hostname of the RADIUS server | 
**server_type** | [**XiqRadiusServerType**](XiqRadiusServerType.md) | [**XiqRadiusServerType**](XiqRadiusServerType.md) |  | 
**shared_secret** | str,  | str,  | The shared secret for the external RADIUS server (optional) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

