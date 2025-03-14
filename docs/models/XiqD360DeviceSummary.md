# extremecloudiq.model.xiq_d360_device_summary.XiqD360DeviceSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connected_status** | bool,  | BoolClass,  | The connected status of the device | [optional] 
**active_since** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**device_health_issues** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**usage_and_capacity_issues** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**client_health_issues** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**device_details** | [**XiqDeviceDetails**](XiqDeviceDetails.md) | [**XiqDeviceDetails**](XiqDeviceDetails.md) |  | [optional] 
**system_information** | [**XiqDeviceSystemInformation**](XiqDeviceSystemInformation.md) | [**XiqDeviceSystemInformation**](XiqDeviceSystemInformation.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

