# extremecloudiq.model.xiq_client_monitor_profile.XiqClientMonitorProfile

The payload of client monitor profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of client monitor profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**name** | str,  | str,  | The client monitor profile name | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**predefined** | bool,  | BoolClass,  | Whether the client monitor profile is predefined or user-customized. | 
**org_id** | decimal.Decimal, int,  | decimal.Decimal,  | The organization identifier, valid when enabling HIQ feature | [optional] value must be a 64 bit integer
**description** | str,  | str,  | The client monitor profile description | [optional] 
**association** | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) |  | [optional] 
**authentication** | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) |  | [optional] 
**networking** | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) | [**XiqClientMonitorParameters**](XiqClientMonitorParameters.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

