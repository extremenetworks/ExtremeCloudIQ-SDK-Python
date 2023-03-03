# XiqRpNeighborhoodAnalysis

The payload of neighborhood analysis config for the radio profile
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier | 
**create_time** | **datetime** | The create time | 
**update_time** | **datetime** | The last update time | 
**enable_background_scan** | **bool** | Whether to enable background scanning of neighboring devices | [optional] 
**background_scan_interval** | **int** | The background scan interval from 1 up to 1440 minutes | [optional] 
**enable_skip_scan_when_clients_connected** | **bool** | Whether to enable skipping of background scan when devices have client connections | [optional] 
**enable_skip_scan_when_clients_in_power_save_mode** | **bool** | Whether to skipping of background scan when connected devices are in power save mode | [optional] 
**enable_skip_scan_when_process_voice_traffic** | **bool** | Whether to enable skipping of background scan when devices have network traffic with voice priority | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


