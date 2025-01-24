from extremecloudiq.paths.user_profiles_id.get import ApiForget
from extremecloudiq.paths.user_profiles_id.put import ApiForput
from extremecloudiq.paths.user_profiles_id.delete import ApiFordelete


class UserProfilesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
