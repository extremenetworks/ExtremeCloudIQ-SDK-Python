# extremecloudiq.model.xiq_connectivity_experience.XiqConnectivityExperience

Get connectivity experience

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Get connectivity experience | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**start_timestamp** | decimal.Decimal, int,  | decimal.Decimal,  | Client Start trial in epoch format (milliseconds) | [optional] value must be a 64 bit integer
**device_name** | str,  | str,  | The Ap name | [optional] 
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | The Ap ID | [optional] value must be a 64 bit integer
**ssid** | str,  | str,  | The SSID | [optional] 
**association_duration** | decimal.Decimal, int,  | decimal.Decimal,  | The association duration in epoch format (milliseconds) | [optional] value must be a 64 bit integer
**auth_method** | str,  | str,  | Authentication Protocol | [optional] 
**authentication_response_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the response in epoch format (milliseconds) | [optional] value must be a 32 bit integer
**authentication_status** | str,  | str,  | authentication status in default PASS | [optional] 
**dhcp_server_ip** | str,  | str,  | Dhcp server address | [optional] 
**dhcp_server_response_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the response in epoch format (milliseconds) | [optional] value must be a 32 bit integer
**dhcp_ip_address_obtained** | str,  | str,  | Dhcp address ip obtained (in old api clientIp) | [optional] 
**default_gateway_ip** | str,  | str,  | Default gateway server address | [optional] 
**default_gateway_round_trip_delay_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the delay trip in epoch format (milliseconds) | [optional] value must be a 32 bit integer
**dns_server_ip** | str,  | str,  | Dns server address | [optional] 
**dns_server_response_time** | decimal.Decimal, int,  | decimal.Decimal,  | Time of the response in epoch format (milliseconds) | [optional] value must be a 32 bit integer
**association_circle_status** | str,  | str,  | The circle Association status (Available status  SUCCESS, INVALID, DISABLED, ERROR) | [optional] must be one of ["SUCCESS", "INVALID", "DISABLED", "ERROR", ] 
**auth_circle_status** | str,  | str,  | The circle Authentication status (Available status  SUCCESS, INVALID, DISABLED, ERROR) | [optional] must be one of ["SUCCESS", "INVALID", "DISABLED", "ERROR", ] 
**dhcp_circle_status** | str,  | str,  | The circle Dhcp Status (Available status  SUCCESS, INVALID, DISABLED, ERROR) | [optional] must be one of ["SUCCESS", "INVALID", "DISABLED", "ERROR", ] 
**dns_circle_status** | str,  | str,  | The circle Dns Status (Available status  SUCCESS, INVALID, DISABLED, ERROR) | [optional] must be one of ["SUCCESS", "INVALID", "DISABLED", "ERROR", ] 
**gateway_circle_status** | str,  | str,  | The circle Gateway ARP Status (Available status  SUCCESS, INVALID, DISABLED, ERROR) | [optional] must be one of ["SUCCESS", "INVALID", "DISABLED", "ERROR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

