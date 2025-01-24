# extremecloudiq.model.xiq_update_rp_wmm_qos_settings_request.XiqUpdateRpWmmQosSettingsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**arbitration_interframe_space** | decimal.Decimal, int,  | decimal.Decimal,  | The Arbitration Interframe space, in the range of 1 to 15. | [optional] value must be a 32 bit integer
**min_contention_window** | decimal.Decimal, int,  | decimal.Decimal,  | The Minimum Contention window, in the range of 1 to 15. | [optional] value must be a 32 bit integer
**max_contention_window** | decimal.Decimal, int,  | decimal.Decimal,  | The Maximum Contention window, in the range of 1 to 15. | [optional] value must be a 32 bit integer
**transmission_opportunity_limit** | decimal.Decimal, int,  | decimal.Decimal,  | The Transmission Opportunity limit, in the range of 0 to 8192. | [optional] value must be a 32 bit integer
**enable_no_ack** | bool,  | BoolClass,  | Whether to enable No Acknowledgment | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

