# extremecloudiq.model.xiq_auth_log.XiqAuthLog

ExtremeCloud IQ Auth Log

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Auth Log | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The auth log id | 
**auth_type** | str,  | str,  | The auth type | [optional] 
**sn** | str,  | str,  | The serial number | [optional] 
**vhm_id** | str,  | str,  | The vhm id | [optional] 
**username** | str,  | str,  | The username | [optional] 
**reply** | str,  | str,  | The reply | [optional] 
**called_station_id** | str,  | str,  | The called station id | [optional] 
**calling_station_id** | str,  | str,  | The calling station id | [optional] 
**auth_date** | decimal.Decimal, int,  | decimal.Decimal,  | The authentication date | [optional] value must be a 64 bit integer
**ssid** | str,  | str,  | The ssid | [optional] 
**identity** | str,  | str,  | The identity | [optional] 
**nas_port_type** | str,  | str,  | The nas port type | [optional] 
**reject_reason** | str,  | str,  | The reject reason | [optional] 
**nas_identifier** | str,  | str,  | The nas identifier | [optional] 
**mgmt_mac_address** | str,  | str,  | The management mac address | [optional] 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The org id | [optional] value must be a 64 bit integer
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The audit log timestamp | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

