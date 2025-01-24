# extremecloudiq.model.xiq_anomaly_location_entity.XiqAnomalyLocationEntity

Copilot Anomaly Locations data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomaly Locations data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**location_type** | [**XiqLocationType**](XiqLocationType.md) | [**XiqLocationType**](XiqLocationType.md) |  | [optional] 
**[location_ids](#location_ids)** | list, tuple,  | tuple,  | the location id | [optional] 
**building_id** | decimal.Decimal, int,  | decimal.Decimal,  | the building id | [optional] value must be a 64 bit integer
**location_name** | str,  | str,  | the location name | [optional] 
**pinned** | bool,  | BoolClass,  | is location pinned | [optional] 
**muted** | bool,  | BoolClass,  | the location muted | [optional] 
**severity** | [**XiqAnomalySeverity**](XiqAnomalySeverity.md) | [**XiqAnomalySeverity**](XiqAnomalySeverity.md) |  | [optional] 
**severity_id** | decimal.Decimal, int,  | decimal.Decimal,  | the severity id | [optional] value must be a 32 bit integer
**summary** | str,  | str,  | the anomaly summary | [optional] 
**affected_device_count** | decimal.Decimal, int,  | decimal.Decimal,  | the affected number of devices | [optional] value must be a 32 bit integer
**last_detected_time** | decimal.Decimal, int,  | decimal.Decimal,  | the last detected time | [optional] value must be a 64 bit integer
**anomaly_type** | [**XiqAnomalyType**](XiqAnomalyType.md) | [**XiqAnomalyType**](XiqAnomalyType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location_ids

the location id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the location id | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | the location id | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

