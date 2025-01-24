# extremecloudiq.model.xiq_hh_client_stats_entity.XiqHhClientStatsEntity

ExtremeCloud IQ Hardware Health Client List Stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Hardware Health Client List Stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**client_mac** | str,  | str,  | The client mac | [optional] 
**client_name** | str,  | str,  | The client name | [optional] 
**client_host_os** | str,  | str,  | The client host os | [optional] 
**avg_snr** | decimal.Decimal, int,  | decimal.Decimal,  | The average SNR | [optional] value must be a 32 bit integer
**client_id** | decimal.Decimal, int,  | decimal.Decimal,  | The client id | [optional] value must be a 64 bit integer
**health_score** | [**XiqAnomalyHealthType**](XiqAnomalyHealthType.md) | [**XiqAnomalyHealthType**](XiqAnomalyHealthType.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

