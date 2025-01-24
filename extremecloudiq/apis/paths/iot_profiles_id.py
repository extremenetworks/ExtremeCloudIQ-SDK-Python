from extremecloudiq.paths.iot_profiles_id.get import ApiForget
from extremecloudiq.paths.iot_profiles_id.put import ApiForput
from extremecloudiq.paths.iot_profiles_id.delete import ApiFordelete


class IotProfilesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
