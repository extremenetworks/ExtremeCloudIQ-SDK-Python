# extremecloudiq.model.xiq_usage_and_capacity_dashboard.XiqUsageAndCapacityDashboard

The usage and capacity diagnostic data for total devices, wired devices like AP, and wireless devices like switch.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The usage and capacity diagnostic data for total devices, wired devices like AP, and wireless devices like switch. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**total_usage_and_capacity_issues** | decimal.Decimal, int,  | decimal.Decimal,  | Total count of usage and capacity issues | [optional] value must be a 64 bit integer
**wired_usage_and_capacity_issues** | decimal.Decimal, int,  | decimal.Decimal,  | Count of wired devices like switch with usage and capacity issues | [optional] value must be a 64 bit integer
**wireless_usage_and_capacity_issues** | decimal.Decimal, int,  | decimal.Decimal,  | Count of wireless devices like APs with usage and capacity issues | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

