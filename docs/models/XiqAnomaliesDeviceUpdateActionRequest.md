# extremecloudiq.model.xiq_anomalies_device_update_action_request.XiqAnomaliesDeviceUpdateActionRequest

Copilot Anomalies Devices Update Action Request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomalies Devices Update Action Request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anomaly_type** | [**XiqAnomalyType**](XiqAnomalyType.md) | [**XiqAnomalyType**](XiqAnomalyType.md) |  | [optional] 
**action_type** | [**XiqActionType**](XiqActionType.md) | [**XiqActionType**](XiqActionType.md) |  | [optional] 
**location_id** | decimal.Decimal, int,  | decimal.Decimal,  | The location id | [optional] value must be a 64 bit integer
**anomaly_id** | str,  | str,  | The anomaly Id | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

