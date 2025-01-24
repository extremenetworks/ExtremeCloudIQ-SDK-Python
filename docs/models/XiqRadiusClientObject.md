# extremecloudiq.model.xiq_radius_client_object.XiqRadiusClientObject

The RADIUS client object configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The RADIUS client object configuration | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_permit_dynamic_authorization_message_change** | bool,  | BoolClass,  | The flag for enable permit dynamic authorization message change | 
**[entries](#entries)** | list, tuple,  | tuple,  | The list of RADIUS client object entries | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**enable_inject_operator_name_attribute** | bool,  | BoolClass,  | The flag for enable inject operator name attribute. | 
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**accounting_interim_update_interval** | decimal.Decimal, int,  | decimal.Decimal,  | The accounting interim update interval, 60 - 100000000 seconds | value must be a 32 bit integer
**enable_message_authenticator_attribute** | bool,  | BoolClass,  | The flag for enable message authenticator attribute | 
**name** | str,  | str,  | The RADIUS client object name. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**retry_interval** | decimal.Decimal, int,  | decimal.Decimal,  | The retry interval, 60 - 100000000 seconds | value must be a 32 bit integer
**description** | str,  | str,  | The RADIUS client object description. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# entries

The list of RADIUS client object entries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of RADIUS client object entries | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqRadiusClientObjectEntry**](XiqRadiusClientObjectEntry.md) | [**XiqRadiusClientObjectEntry**](XiqRadiusClientObjectEntry.md) | [**XiqRadiusClientObjectEntry**](XiqRadiusClientObjectEntry.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

