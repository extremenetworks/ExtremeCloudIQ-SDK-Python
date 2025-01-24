# extremecloudiq.model.xiq_update_rp_neighborhood_analysis_request.XiqUpdateRpNeighborhoodAnalysisRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enable_background_scan** | bool,  | BoolClass,  | Whether background scan of neighboring devices is enabled | [optional] 
**background_scan_interval** | decimal.Decimal, int,  | decimal.Decimal,  | The background scan interval in the range of 1 to 1440 minutes | [optional] if omitted the server will use the default value of 3value must be a 32 bit integer
**enable_skip_scan_when_clients_connected** | bool,  | BoolClass,  | Whether to skip background scan when devices have client connections | [optional] 
**enable_skip_scan_when_clients_in_power_save_mode** | bool,  | BoolClass,  | Whether to skip background scan when connected devices are in power save mode | [optional] 
**enable_skip_scan_when_process_voice_traffic** | bool,  | BoolClass,  | Whether to skip background scan when devices have network traffic with voice priority | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

