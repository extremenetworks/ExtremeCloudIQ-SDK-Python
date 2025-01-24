# extremecloudiq.model.xiq_anomaly_device_entity.XiqAnomalyDeviceEntity

Copilot Anomaly Device data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomaly Device data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | the device id | [optional] value must be a 64 bit integer
**device_name** | str,  | str,  | the device name | [optional] 
**pinned** | bool,  | BoolClass,  | is device pinned | [optional] 
**wired** | bool,  | BoolClass,  | is device wired | [optional] 
**anomaly_id** | str,  | str,  | the anomaly id | [optional] 
**severity** | [**XiqAnomalySeverity**](XiqAnomalySeverity.md) | [**XiqAnomalySeverity**](XiqAnomalySeverity.md) |  | [optional] 
**summary** | str,  | str,  | the anomaly summary | [optional] 
**last_detected_time** | decimal.Decimal, int,  | decimal.Decimal,  | the last detected time | [optional] value must be a 64 bit integer
**recommended_action** | str,  | str,  | the recommended action | [optional] 
**anomaly_subtypes** | str,  | str,  | the anomaly sub-type | [optional] 
**interface_name** | str,  | str,  | the interface name | [optional] 
**channel_mode** | str,  | str,  | the channel mode : tx or rx | [optional] 
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | the channel number | [optional] value must be a 32 bit integer
**frequency** | str,  | str,  | the frequency | [optional] 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | the location id | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

