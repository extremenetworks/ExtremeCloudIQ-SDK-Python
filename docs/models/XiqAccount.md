# extremecloudiq.model.xiq_account.XiqAccount

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_type** | [**XiqAccountType**](XiqAccountType.md) | [**XiqAccountType**](XiqAccountType.md) |  | 
**update_time** | str, datetime,  | str,  | The last update time | value must conform to RFC-3339 date-time
**create_time** | str, datetime,  | str,  | The create time | value must conform to RFC-3339 date-time
**quota** | str,  | str,  | The API quota policy | 
**name** | str,  | str,  | Account name | 
**data_center** | str,  | str,  | The default Regional Data Center (RDC) to hold data from customer network | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier | value must be a 64 bit integer
**account_mode** | [**XiqAccountMode**](XiqAccountMode.md) | [**XiqAccountMode**](XiqAccountMode.md) |  | 
**industry** | str,  | str,  | The industry of the account belongs to | [optional] 
**country** | str,  | str,  | The country for the account | [optional] 
**state** | str,  | str,  | The state for the account (if any) | [optional] 
**city** | str,  | str,  | The city for the account | [optional] 
**address** | str,  | str,  | The address for the account | [optional] 
**zipcode** | str,  | str,  | The zipcode of the address | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

