# extremecloudiq.model.xiq_anomaly_device_with_location.XiqAnomalyDeviceWithLocation

Copilot Anomaly details with Location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomaly details with Location | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**severity** | [**XiqAnomalySeverity**](XiqAnomalySeverity.md) | [**XiqAnomalySeverity**](XiqAnomalySeverity.md) |  | 
**building_id** | decimal.Decimal, int,  | decimal.Decimal,  | The building ID | value must be a 64 bit integer
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The device ID | value must be a 64 bit integer
**device_model** | str,  | str,  | The device model | 
**interface_name** | str,  | str,  | The interface name | 
**device_make** | str,  | str,  | The device make | 
**device_name** | str,  | str,  | The device name | 
**location_name** | str,  | str,  | The location name | 
**last_detected_time** | decimal.Decimal, int,  | decimal.Decimal,  | The last detected time of anomaly | value must be a 64 bit integer
**anomaly_type** | [**XiqAnomalyType**](XiqAnomalyType.md) | [**XiqAnomalyType**](XiqAnomalyType.md) |  | 
**category** | [**XiqDeviceCategory**](XiqDeviceCategory.md) | [**XiqDeviceCategory**](XiqDeviceCategory.md) |  | 
**switch_stack** | bool,  | BoolClass,  | The device model | 
**muted** | bool,  | BoolClass,  | To filter muted anomalies | 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location ID | [optional] value must be a 64 bit integer
**anomaly_id** | str,  | str,  | The anomaly ID | [optional] 
**frequency** | str,  | str,  | The frequency | [optional] 
**channel_number** | decimal.Decimal, int,  | decimal.Decimal,  | The channel number | [optional] value must be a 32 bit integer
**channel_mode** | str,  | str,  | The channel mode | [optional] 
**recommended_action** | str,  | str,  | The recommended action | [optional] 
**issue** | str,  | str,  | The issue | [optional] 
**current_poe_mode** | str,  | str,  | The current poe mode | [optional] 
**device_status** | bool,  | BoolClass,  | The device status | [optional] 
**anomaly_subtypes** | str,  | str,  | The Anomaly Subtypes | [optional] 
**missing_vlan_info** | [**XiqMissingVlanInfo**](XiqMissingVlanInfo.md) | [**XiqMissingVlanInfo**](XiqMissingVlanInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

