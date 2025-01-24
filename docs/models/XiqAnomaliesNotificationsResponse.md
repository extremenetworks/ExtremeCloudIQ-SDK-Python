# extremecloudiq.model.xiq_anomalies_notifications_response.XiqAnomaliesNotificationsResponse

Copilot Anomalies Notification Response

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomalies Notification Response | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_anomaly_count** | decimal.Decimal, int,  | decimal.Decimal,  | The total anomaly count | [optional] value must be a 64 bit integer
**[location_entity](#location_entity)** | list, tuple,  | tuple,  | the anomaly location | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# location_entity

the anomaly location

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the anomaly location | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqAnomalyLocationEntity**](XiqAnomalyLocationEntity.md) | [**XiqAnomalyLocationEntity**](XiqAnomalyLocationEntity.md) | [**XiqAnomalyLocationEntity**](XiqAnomalyLocationEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

