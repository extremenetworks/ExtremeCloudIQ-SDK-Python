# XiqRpRadioUsageOptimization

The payload of config for the radio profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**preamble** | **str** | The preamble data length -- \&quot;AUTO\&quot; or \&quot;LONG\&quot; | [optional] 
**beacon_period** | **int** | The amount of time between beacons from 40 up to 3500. | [optional] 
**enable_frame_burst** | **bool** | Whether to enable Frame Burst | [optional] 
**enable_smart_antenna** | **bool** | Whether to enable Smart Antenna (Enabling this option will disable (Null) for MU-MIMO) | [optional] 
**enable_backhaul_failover** | **bool** | Whether to enable backhaul failover. Backhaul failover settings determine the thresholds at which the device switches from a wired to a wireless backhaul link, and the thresholds at which the device switches back | [optional] 
**wireless_backhaul_switch_trigger_time** | **int** | Switch to Wireless Backhaul after 1 up to 5 seconds after the wired link fails | [optional] 
**wired_backhaul_revert_hold_time** | **int** | Revert Back to Wired Backhaul after 1 up to 300 seconds after the wired link is established | [optional] 
**enable_band_steering** | **bool** | Whether to enable band steering. Enabling steers clients from 2.4 GHz to 5.0 GHz radio band | [optional] 
**band_steering_mode** | **str** | The band steering mode -- \&quot;BALANCE\&quot;, \&quot;URGE_5G\&quot;, or \&quot;ENFORCE_5G\&quot; | [optional] 
**ignore_initial_client_connection_number** | **int** | The number of connection attempts from 1 to 100 for 2.4 GHz clients to ignore before responding for URGE_5G steering mode. | [optional] 
**enable_client_load_balancing** | **bool** | Whether to enable client load balancing.  Enabling load-balances clients across neighboring Extreme Networks within the same hive. Set WiFi0 and WiFi1 radios to the same load balancing mode when it is based on the number of associated stations. | [optional] 
**load_balancing_mode** | **str** | The client load balancing mode -- \&quot;AIRTIME_BASED\&quot; or \&quot;CLIENT_NUMBER\&quot; | [optional] 
**crc_error_rate_per_device** | **int** | The CRC Error rate threshold from 1 up to 99 for \&quot;AIRTIME_BASED\&quot; load balancing. Ignore probe and association requests per device when CRC Error rate exceeds the threshold. | [optional] 
**rf_interference_per_device** | **int** | The RF Interference threshold from 1 up to 99 for \&quot;AIRTIME_BASED\&quot; load balancing. Ignore probe and association requests per device when RF Interference exceeds the threshold. | [optional] 
**average_airtime_per_client** | **int** | The Average Airtime Per Client threshold from 1 up to 5 for \&quot;AIRTIME_BASED\&quot; load balancing. Ignore probe and association requests per device when Average Airtime Per Client exceeds the threshold. | [optional] 
**anchor_period** | **int** | The Anchor Period from 10 up to 600 for both \&quot;AIRTIME_BASED\&quot; and \&quot;CLIENT_NUMBER\&quot; load balancing. Ignore probe and association requests from clients associated with other Extreme Networks devices until Anchor Period Eelapses in the range of 10 to 600 seconds | [optional] 
**neighbor_query_interval** | **int** | In both client load balancing modes, query neighbors about client load every 1 up to 600 seconds | [optional] 
**enable_weak_signal_probe_request_suppression** | **bool** | Whether to enable Weak Signal Probe Request Suppression. Weak Signal Probe Request Suppression allows the configuration of signal-to-noise threshold beyond which the device does not respond to client probes. | [optional] 
**weak_snr_threshold** | **int** | The signal to noise threshold from 1 up to 100 for Weak Signal Probe Request Suppression. | [optional] 
**enable_safety_net** | **bool** | Whether to enable Safety Net. When a device is overloaded or is probed by clients with a low signal-to-noise ratio,  Safety Net allows the device to respond to association requests  after a certain time period lapses. | [optional] 
**safety_net_period** | **int** | The Safety Net Time Period from 5 up to 300 seconds. | [optional] 
**enable_high_density** | **bool** | Whether to enable High Density Configuration. Enabling optimizes performance in high density environments | [optional] 
**management_frame_basic_data_rate** | **str** | The data rates to support in high density environment -- \&quot;HIGH\&quot; or \&quot;LOW\&quot; | [optional] 
**enable_suppress_successive_probe_request** | **bool** | Whether to Reduce Response to Probe Requests. Enabling suppresses successive requests within the same beacon interval | [optional] 
**probe_response_reduction_option** | **str** | The suppress response to broadcast probes options --  \&quot;ONLY_ONE_SSID_RESPOND_AT_A_TIME\&quot; (allowed for only one SSID to respond at a time), \&quot;REDUCE_CERTAIN_CLIENTS_RESPONSE\&quot; (reducing responses to certain client devices). | [optional] 
**suppression_limit** | **int** | The Number of Connection Attempts from 1 up to 10 | [optional] 
**enable_radio_balance** | **bool** | Whether to enable Radio Load Balancing. Enabling distributes wireless clients that support 5 GHz band evenly across the two radios in Dual-5G mode when an SSID is available on both radios | [optional] 
**enable_ampdu** | **bool** | Enable Aggregate MAC Protocol Data Units to combine data frames into larger frames before transmission. | [optional] 
**enable_mu_mimo** | **bool** | Whether to enable Multiple-Input Multiple-Output (802.11ac &amp; 802.11ax) for multiple-user access by using different spatial streams. | [optional] 
**enable_ofdma_down_link** | **bool** | Whether to enable OFDMA for AP downlink communication. | [optional] 
**enable_ofdma_up_link** | **bool** | Whether to enable OFDMA for AP uplink communication. | [optional] 
**bss_coloring** | **int** | Whether to enable BSS Coloring (802.11ax ) to identify overlapping basic service sets (OBSSs). | [optional] 
**enable_target_weak_time** | **bool** | Whether to enable Target Weak Time. | [optional] 
**mac_ouis** | [**list[XiqRpMacOuiProfile]**](XiqRpMacOuiProfile.md) | The device vendor identifiers for the \&quot;REDUCE_CERTAIN_CLIENTS_RESPONSE\&quot; for the probe response reduction option | [optional] 
**ratio_for_5g_clients** | **int** | The percentage distribution from 1 up to 100 for 2.4 and 5.0 GHz clients for \&quot;BALANCE\&quot; steering mode. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


