# extremecloudiq.model.xiq_rp_neighborhood_analysis.XiqRpNeighborhoodAnalysis

The payload of neighborhood analysis config for the radio profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of neighborhood analysis config for the radio profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**enable_background_scan** | bool,  | BoolClass,  | Whether to enable background scanning of neighboring devices | [optional] 
**background_scan_interval** | decimal.Decimal, int,  | decimal.Decimal,  | The background scan interval from 1 up to 1440 minutes | [optional] value must be a 32 bit integer
**enable_skip_scan_when_clients_connected** | bool,  | BoolClass,  | Whether to enable skipping of background scan when devices have client connections | [optional] 
**enable_skip_scan_when_clients_in_power_save_mode** | bool,  | BoolClass,  | Whether to skipping of background scan when connected devices are in power save mode | [optional] 
**enable_skip_scan_when_process_voice_traffic** | bool,  | BoolClass,  | Whether to enable skipping of background scan when devices have network traffic with voice priority | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

