# extremecloudiq.model.wifi_health.WifiHealth

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**overall_score** | decimal.Decimal, int,  | decimal.Decimal,  | The overall health score | [optional] value must be a 32 bit integer
**snr_score** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of snr | [optional] value must be a 32 bit integer
**channel_utilization_score** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of utilization | [optional] value must be a 32 bit integer
**association_per_radio_score** | decimal.Decimal, int,  | decimal.Decimal,  | The health score of association | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

