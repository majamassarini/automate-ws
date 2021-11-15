from aiohttp_security.abc import AbstractAuthorizationPolicy


class Policy(AbstractAuthorizationPolicy):
    ADMIN_ROLE = "admin"
    USER_ROLE = "user"
    ANONYMOUS_ROLE = "anonymous"

    VIEW_PERMISSION = "view"
    EDIT_PERMISSION = "edit"
    CONFIGURE_PERMISSION = "configure"

    def __init__(self, credentials: dict = None, roles: dict = None):
        super().__init__()
        if credentials:
            self._credentials = credentials
        else:
            self._credentials = {"admin": "admin", "user": "user", "anonymous": ""}
        if roles:
            self._roles = roles
        else:
            self._roles = {
                "admin": self.ADMIN_ROLE,
                "user": self.USER_ROLE,
                "anonymous": self.ANONYMOUS_ROLE,
            }
        self._permissions = {
            self.ADMIN_ROLE: (
                self.VIEW_PERMISSION,
                self.EDIT_PERMISSION,
                self.CONFIGURE_PERMISSION,
            ),
            self.USER_ROLE: (self.VIEW_PERMISSION, self.EDIT_PERMISSION),
            self.ANONYMOUS_ROLE: (self.VIEW_PERMISSION,),
        }

    @property
    def credentials(self):
        return self._credentials

    async def authorized_userid(self, identity):
        if identity in self._credentials:
            return identity

    async def permits(self, identity, permission, context=None):
        try:
            role = self._roles[identity]
        except KeyError:
            return False
        return permission in self._permissions[role]


async def check_credentials(credentials, username, password):
    if username not in credentials:
        return False
    return credentials[username] == password
