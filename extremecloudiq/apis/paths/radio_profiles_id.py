from extremecloudiq.paths.radio_profiles_id.get import ApiForget
from extremecloudiq.paths.radio_profiles_id.put import ApiForput
from extremecloudiq.paths.radio_profiles_id.delete import ApiFordelete


class RadioProfilesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
