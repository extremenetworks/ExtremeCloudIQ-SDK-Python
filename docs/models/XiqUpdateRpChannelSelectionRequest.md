# extremecloudiq.model.xiq_update_rp_channel_selection_request.XiqUpdateRpChannelSelectionRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_dynamic_channel_switching** | bool,  | BoolClass,  | Whether to dynamically select and switch channels based on the defined criteria. | [optional] 
**channel_width** | str,  | str,  | The channel frequency range | [optional] 
**enable_dynamic_frequency_selection** | bool,  | BoolClass,  | Whether dynamic frequency selection is enabled (a/n, a, ac mode) | [optional] 
**enable_static_channel** | bool,  | BoolClass,  | Whether static channel is enabled (manual channel selection return) | [optional] 
**enable_zero_wait_dfs** | bool,  | BoolClass,  | Whether ZeroWait DFS is enabled | [optional] 
**enable_use_last_selection** | bool,  | BoolClass,  | Whether to use the last known power and channel during the AP boot up process | [optional] 
**exclude_channels** | str,  | str,  | The comma-separated list of excluded channels not on the selected channel width. | [optional] 
**exclude_channels_width** | str,  | str,  | The comma-separated list of excluded channels on the selected channel width. | [optional] 
**channel** | decimal.Decimal, int,  | decimal.Decimal,  | The number of channel selections or AUTO for default selection. | [optional] value must be a 32 bit integer
**enable_limit_channel_selection** | bool,  | BoolClass,  | Whether to allow for limiting the channel selection to non-overlapping channels. (b/g,g/n/, axes modes) | [optional] 
**channel_region** | str,  | str,  | The channel region -- \&quot;USA\&quot;, \&quot;Canada\&quot;, \&quot;Europe\&quot;, or \&quot;World\&quot; | [optional] 
**channel_model** | decimal.Decimal, int,  | decimal.Decimal,  | The number of channel models to limit. | [optional] value must be a 32 bit integer
**channels** | str,  | str,  | The comma separated list of channels allowed channel switching | [optional] 
**enable_channel_auto_selection** | bool,  | BoolClass,  | Whether to enable automatic channel switching during specified time interval. | [optional] 
**channel_selection_start_time** | str,  | str,  | The start time for channel switching in 24-hr time format of hh:mm | [optional] 
**channel_selection_end_time** | str,  | str,  | The end time for channel switching in 24-hr time format of hh:mm | [optional] 
**enable_avoid_switch_channel_if_clients_connected** | bool,  | BoolClass,  | Whether to avoid channel switching if there are already max connected clients | [optional] 
**channel_selection_max_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of connected clients to avoid switching | [optional] value must be a 32 bit integer
**enable_switch_channel_if_exceed_threshold** | bool,  | BoolClass,  | Whether to enable channel switching when RF interference exceeds the threshold | [optional] 
**rf_interference_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | The RF interference threshold for channel switching. | [optional] value must be a 32 bit integer
**crc_error_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | The CRC error threshold for channel switching. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

