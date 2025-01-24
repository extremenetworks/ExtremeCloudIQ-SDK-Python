# extremecloudiq.model.xiq_wireless_performance_entity.XiqWirelessPerformanceEntity

ExtremeCloud IQ Connectivity Experience Performance data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ExtremeCloud IQ Connectivity Experience Performance data | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp | value must be a 64 bit integer
**quality_index** | decimal.Decimal, int,  | decimal.Decimal,  | The quality index | [optional] value must be a 32 bit integer
**total_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The total clients | [optional] value must be a 32 bit integer
**time_to_connect_score** | decimal.Decimal, int,  | decimal.Decimal,  | The time to connect score | [optional] value must be a 32 bit integer
**performance_score** | decimal.Decimal, int,  | decimal.Decimal,  | The performance score | [optional] value must be a 32 bit integer
**snr** | decimal.Decimal, int,  | decimal.Decimal,  | The average snr | [optional] value must be a 32 bit integer
**retries_data** | [**XiqWirelessPerformanceRetriesEntity**](XiqWirelessPerformanceRetriesEntity.md) | [**XiqWirelessPerformanceRetriesEntity**](XiqWirelessPerformanceRetriesEntity.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

