# extremecloudiq.model.xiq_anomaly_devices_by_location_response.XiqAnomalyDevicesByLocationResponse

Copilot Anomaly Devices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomaly Devices | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**location_entity** | [**XiqAnomalyLocationEntity**](XiqAnomalyLocationEntity.md) | [**XiqAnomalyLocationEntity**](XiqAnomalyLocationEntity.md) |  | [optional] 
**[devices](#devices)** | list, tuple,  | tuple,  | the anomaly devices data | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# devices

the anomaly devices data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly devices data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAnomalyDeviceEntity**](XiqAnomalyDeviceEntity.md) | [**XiqAnomalyDeviceEntity**](XiqAnomalyDeviceEntity.md) | [**XiqAnomalyDeviceEntity**](XiqAnomalyDeviceEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

