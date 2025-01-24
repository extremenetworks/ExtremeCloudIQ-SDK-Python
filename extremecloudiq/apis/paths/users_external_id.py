from extremecloudiq.paths.users_external_id.get import ApiForget
from extremecloudiq.paths.users_external_id.delete import ApiFordelete
from extremecloudiq.paths.users_external_id.patch import ApiForpatch


class UsersExternalId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
