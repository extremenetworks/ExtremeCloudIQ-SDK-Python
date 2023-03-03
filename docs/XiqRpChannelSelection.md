# XiqRpChannelSelection

The payload of config for the radio profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**enable_dynamic_channel_switching** | **bool** | Whether to dynamically select and switch channels based on the defined criteria. | [optional] 
**channel_width** | **str** | The channel frequency range | [optional] 
**enable_dynamic_frequency_selection** | **bool** | Whether dynamic frequency selection is enabled (a/n, a, ac mode) | [optional] 
**enable_static_channel** | **bool** | Whether static channel is enabled (manual channel selection return) | [optional] 
**enable_zero_wait_dfs** | **bool** | Whether ZeroWait DFS is enabled | [optional] 
**enable_use_last_selection** | **bool** | Whether to use the last known power and channel during the AP boot up process | [optional] 
**exclude_channels** | **str** | The comma-separated list of excluded channels not on the selected channel width. | [optional] 
**exclude_channels_width** | **str** | The comma-separated list of excluded channels on the selected channel width. | [optional] 
**channel** | **int** | The number of channel selections from 1 up to 165 or AUTO for default selection. | [optional] 
**enable_limit_channel_selection** | **bool** | Whether to allow for limiting the channel selection to non-overlapping channels. (b/g,g/n/, axes modes) | [optional] 
**channel_region** | **str** | The channel region -- \&quot;USA\&quot;, \&quot;Canada\&quot;, \&quot;Europe\&quot;, or \&quot;World\&quot; | [optional] 
**channel_model** | **int** | The number of channel models to limit. | [optional] 
**channels** | **str** | The comma separated list of channels allowed channel switching | [optional] 
**enable_channel_auto_selection** | **bool** | Whether to enable automatic channel switching during specified time interval. | [optional] 
**channel_selection_start_time** | **str** | The start time for channel switching in 24-hr time format of hh:mm | [optional] 
**channel_selection_end_time** | **str** | The end time for channel switching in 24-hr time format of hh:mm | [optional] 
**enable_avoid_switch_channel_if_clients_connected** | **bool** | Whether to avoid channel switching if there are already max connected clients | [optional] 
**channel_selection_max_clients** | **int** | The maximum number of connected clients from 0 up to 100 to avoid switching | [optional] 
**enable_switch_channel_if_exceed_threshold** | **bool** | Whether to enable channel switching when RF interference exceeds the threshold | [optional] 
**rf_interference_threshold** | **int** | The RF interference threshold from 10 up to 80 for channel switching. | [optional] 
**crc_error_threshold** | **int** | The CRC error threshold from 10 up to 80 for channel switching. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


