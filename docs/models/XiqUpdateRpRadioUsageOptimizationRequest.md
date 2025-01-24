# extremecloudiq.model.xiq_update_rp_radio_usage_optimization_request.XiqUpdateRpRadioUsageOptimizationRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**preamble** | str,  | str,  | The preamble data length -- \&quot;AUTO\&quot; or \&quot;LONG\&quot; | [optional] 
**beacon_period** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of time between beacons in the range from 40 to 3500. | [optional] value must be a 32 bit integer
**enable_frame_burst** | bool,  | BoolClass,  | Whether to enable Frame Burst | [optional] 
**enable_smart_antenna** | bool,  | BoolClass,  | Whether to enable Smart Antenna (Enabling this option will disable (Null) for MU-MIMO) | [optional] 
**enable_backhaul_failover** | bool,  | BoolClass,  | Whether to enable backhaul failover. Backhaul failover settings determine the thresholds at which the device switches from a wired to a wireless backhaul link, and the thresholds at which the device switches back | [optional] 
**wireless_backhaul_switch_trigger_time** | decimal.Decimal, int,  | decimal.Decimal,  | Switch to Wireless Backhaul after the number of seconds (1 to 5) after the wired link fails | [optional] value must be a 32 bit integer
**wired_backhaul_revert_hold_time** | decimal.Decimal, int,  | decimal.Decimal,  | Revert Back to Wired Backhaul after the number of seconds (1 to 300) after the wired link is established | [optional] value must be a 32 bit integer
**enable_band_steering** | bool,  | BoolClass,  | Whether to enable band steering. Enabling steers clients from 2.4 GHz to 5.0 GHz radio band | [optional] 
**band_steering_mode** | str,  | str,  | The band steering mode -- \&quot;BALANCE\&quot;, \&quot;URGE_5G\&quot;, or \&quot;ENFORCE_5G\&quot; | [optional] 
**ratio_for5g_clients** | decimal.Decimal, int,  | decimal.Decimal,  | The allowed percentage distribution of 2.4 and 5.0 GHz clients for \&quot;BALANCE\&quot; steering mode. | [optional] value must be a 32 bit integer
**ignore_initial_client_connection_number** | decimal.Decimal, int,  | decimal.Decimal,  | The number of connection attempts from 2.4 GHz clients to ignore before responding for URGE_5G steering mode. | [optional] value must be a 32 bit integer
**enable_client_load_balancing** | bool,  | BoolClass,  | Whether to enable client load balancing.  Enabling load-balances clients across neighboring Extreme Networks within the same hive. Set WiFi0 and WiFi1 radios to the same load balancing mode when it is based on the number of associated stations. | [optional] 
**load_balancing_mode** | str,  | str,  | The client load balancing mode -- \&quot;AIRTIME_BASED\&quot; or \&quot;CLIENT_NUMBER\&quot; | [optional] 
**crc_error_rate_per_device** | decimal.Decimal, int,  | decimal.Decimal,  | The CRC Error rate threshold value for \&quot;AIRTIME_BASED\&quot; load balancing. Ignore probe and association requests per device when CRC Error rate exceeds the threshold. | [optional] value must be a 32 bit integer
**rf_interference_per_device** | decimal.Decimal, int,  | decimal.Decimal,  | The RF Interference threshold value for \&quot;AIRTIME_BASED\&quot; load balancing. Ignore probe and association requests per device when RF Interference exceeds the threshold. | [optional] value must be a 32 bit integer
**average_airtime_per_client** | decimal.Decimal, int,  | decimal.Decimal,  | The Average Airtime Per Client threshold value for \&quot;AIRTIME_BASED\&quot; load balancing. Ignore probe and association requests per device when Average Airtime Per Client exceeds the threshold. | [optional] value must be a 32 bit integer
**anchor_period** | decimal.Decimal, int,  | decimal.Decimal,  | The Anchor Period value for both \&quot;AIRTIME_BASED\&quot; and \&quot;CLIENT_NUMBER\&quot; load balancing. Ignore probe and association requests from clients associated with other Extreme Networks devices until Anchor Period Eelapses in the range of 10 to 600 seconds | [optional] value must be a 32 bit integer
**neighbor_query_interval** | decimal.Decimal, int,  | decimal.Decimal,  | In both client load balancing modes, query neighbors about client load every in the range of 1 to 600 seconds | [optional] value must be a 32 bit integer
**enable_weak_signal_probe_request_suppression** | bool,  | BoolClass,  | Whether to enable Weak Signal Probe Request Suppression. Weak Signal Probe Request Suppression allows the configuration of signal-to-noise threshold beyond which the device does not respond to client probes. | [optional] 
**weak_snr_threshold** | decimal.Decimal, int,  | decimal.Decimal,  | The signal to noise threshold in the range of 1 to 100 for Weak Signal Probe Request Suppression. | [optional] value must be a 32 bit integer
**enable_safety_net** | bool,  | BoolClass,  | Whether to enable Safety Net. When a device is overloaded or is probed by clients with a low signal-to-noise ratio,  Safety Net allows the device to respond to association requests  after a certain time period lapses. | [optional] 
**safety_net_period** | decimal.Decimal, int,  | decimal.Decimal,  | The Safety Net Time Period in the range of 5 to 300 seconds. | [optional] value must be a 32 bit integer
**enable_high_density** | bool,  | BoolClass,  | Whether to enable High Density Configuration. Enabling optimizes performance in high density environments | [optional] 
**management_frame_basic_data_rate** | str,  | str,  | The data rates to support in high density environment -- \&quot;HIGH\&quot; or \&quot;LOW\&quot; | [optional] 
**enable_suppress_successive_probe_request** | bool,  | BoolClass,  | Whether to Reduce Response to Probe Requests. Enabling suppresses successive requests within the same beacon interval | [optional] 
**probe_response_reduction_option** | str,  | str,  | The suppress response to broadcast probes options --  \&quot;ONLY_ONE_SSID_RESPOND_AT_A_TIME\&quot; (allowed for only one SSID to respond at a time), \&quot;REDUCE_CERTAIN_CLIENTS_RESPONSE\&quot; (reducing responses to certain client devices). | [optional] 
**suppression_limit** | decimal.Decimal, int,  | decimal.Decimal,  | The Number of Connection Attempts in the range of 1 to 10 | [optional] value must be a 32 bit integer
**enable_radio_balance** | bool,  | BoolClass,  | Whether to enable Radio Load Balancing. Enabling distributes wireless clients that support 5 GHz band evenly across the two radios in Dual-5G mode when an SSID is available on both radios | [optional] 
**[mac_oui_ids](#mac_oui_ids)** | list, tuple,  | tuple,  | The MacOui Profile IDs for the \&quot;REDUCE_CERTAIN_CLIENTS_RESPONSE\&quot; probe response reduction option | [optional] 
**enable_ampdu** | bool,  | BoolClass,  | Enable Aggregate MAC Protocol Data Units to combine data frames into larger frames before transmission. | [optional] 
**enable_mu_mimo** | bool,  | BoolClass,  | Whether to enable Multiple-Input Multiple-Output (802.11ac &amp; 802.11ax) for multiple-user access by using different spatial streams. | [optional] 
**enable_ofdma_down_link** | bool,  | BoolClass,  | Whether to enable OFDMA for AP downlink communication. | [optional] 
**enable_ofdma_up_link** | bool,  | BoolClass,  | Whether to enable OFDMA for AP uplink communication. | [optional] 
**bss_coloring** | decimal.Decimal, int,  | decimal.Decimal,  | The numerical identifier of the basic service sets (802.11ax ) to identify overlapping basic service sets (OBSSs). | [optional] value must be a 32 bit integer
**enable_target_weak_time** | bool,  | BoolClass,  | Whether to enable Target Weak Time. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mac_oui_ids

The MacOui Profile IDs for the \"REDUCE_CERTAIN_CLIENTS_RESPONSE\" probe response reduction option

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The MacOui Profile IDs for the \&quot;REDUCE_CERTAIN_CLIENTS_RESPONSE\&quot; probe response reduction option | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | The MacOui Profile IDs for the \&quot;REDUCE_CERTAIN_CLIENTS_RESPONSE\&quot; probe response reduction option | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

