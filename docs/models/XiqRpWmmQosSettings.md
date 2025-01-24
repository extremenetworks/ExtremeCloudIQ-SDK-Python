# extremecloudiq.model.xiq_rp_wmm_qos_settings.XiqRpWmmQosSettings

The payload of config for the radio profile

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The payload of config for the radio profile | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**access_category** | str,  | str,  | The media categories, including \&quot;VOICE\&quot;, \&quot;VIDEO\&quot;, \&quot;BEST_EFFORT\&quot;, and \&quot;BACKGROUND\&quot; | [optional] 
**arbitration_interframe_space** | decimal.Decimal, int,  | decimal.Decimal,  | The Arbitration Interframe space from 1 up to 15. | [optional] value must be a 32 bit integer
**min_contention_window** | decimal.Decimal, int,  | decimal.Decimal,  | The Minimum Contention window from 1 up to 15. | [optional] value must be a 32 bit integer
**max_contention_window** | decimal.Decimal, int,  | decimal.Decimal,  | The Maximum Contention window from 1 up to 15. | [optional] value must be a 32 bit integer
**transmission_opportunity_limit** | decimal.Decimal, int,  | decimal.Decimal,  | The Transmission Opportunity limit from 0 up to 8192. | [optional] value must be a 32 bit integer
**enable_no_ack** | bool,  | BoolClass,  | Whether to enable No Acknowledgment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

