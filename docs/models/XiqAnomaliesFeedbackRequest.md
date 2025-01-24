# extremecloudiq.model.xiq_anomalies_feedback_request.XiqAnomaliesFeedbackRequest

Copilot Anomalies Feedback Request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot Anomalies Feedback Request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**anomaly_type** | [**XiqAnomalyType**](XiqAnomalyType.md) | [**XiqAnomalyType**](XiqAnomalyType.md) |  | [optional] 
**anomaly_id** | str,  | str,  | The anomaly Id | [optional] 
**feedback_type** | [**XiqFeedbackType**](XiqFeedbackType.md) | [**XiqFeedbackType**](XiqFeedbackType.md) |  | [optional] 
**feedback** | str,  | str,  | The feedback description | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

