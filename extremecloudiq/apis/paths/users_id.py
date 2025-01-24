from extremecloudiq.paths.users_id.get import ApiForget
from extremecloudiq.paths.users_id.delete import ApiFordelete
from extremecloudiq.paths.users_id.patch import ApiForpatch


class UsersId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
