# extremecloudiq.model.xiq_alert_dashboard.XiqAlertDashboard

The diagnostic alert counts for critical, warning, information, and unacknowledged alerts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The diagnostic alert counts for critical, warning, information, and unacknowledged alerts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**critical** | decimal.Decimal, int,  | decimal.Decimal,  | Count of critical alerts | [optional] value must be a 64 bit integer
**warning** | decimal.Decimal, int,  | decimal.Decimal,  | Count of warning alerts | [optional] value must be a 64 bit integer
**information** | decimal.Decimal, int,  | decimal.Decimal,  | Count of informational alerts | [optional] value must be a 64 bit integer
**total_unacknowledged** | decimal.Decimal, int,  | decimal.Decimal,  | Total count of unacknowledged alerts | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

