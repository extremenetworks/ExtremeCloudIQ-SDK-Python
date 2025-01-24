# extremecloudiq.model.xiq_dfs_recurence_channel_stats_response.XiqDfsRecurenceChannelStatsResponse

Copilot DfsRecurrence Channel Stats

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copilot DfsRecurrence Channel Stats | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[dfs_channel_stats_entities](#dfs_channel_stats_entities)** | list, tuple,  | tuple,  | the channel stats data | [optional] 
**min_channel** | decimal.Decimal, int,  | decimal.Decimal,  | The min channel | [optional] value must be a 32 bit integer
**max_channel** | decimal.Decimal, int,  | decimal.Decimal,  | The max channel | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dfs_channel_stats_entities

the channel stats data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | the channel stats data | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**XiqDfsChannelStatsEntity**](XiqDfsChannelStatsEntity.md) | [**XiqDfsChannelStatsEntity**](XiqDfsChannelStatsEntity.md) | [**XiqDfsChannelStatsEntity**](XiqDfsChannelStatsEntity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

