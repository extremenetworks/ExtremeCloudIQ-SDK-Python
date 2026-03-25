# extremecloudiq.model.xiq_rate_limit_policy.XiqRateLimitPolicy

The rate limit policy for the API token

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The rate limit policy for the API token | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hour** | decimal.Decimal, int,  | decimal.Decimal,  | The sustained request quota per hour. Defines the baseline traffic capacity. | value must be a 64 bit integer
**second** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum burst allowance per second. If omitted, no short-term throttling is applied. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

