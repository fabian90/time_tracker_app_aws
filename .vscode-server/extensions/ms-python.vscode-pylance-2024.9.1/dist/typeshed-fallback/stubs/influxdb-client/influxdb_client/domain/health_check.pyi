from _typeshed import Incomplete

class HealthCheck:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        name: Incomplete | None = None,
        message: Incomplete | None = None,
        checks: Incomplete | None = None,
        status: Incomplete | None = None,
        version: Incomplete | None = None,
        commit: Incomplete | None = None,
    ) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def message(self): ...
    @message.setter
    def message(self, message) -> None: ...
    @property
    def checks(self): ...
    @checks.setter
    def checks(self, checks) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def version(self): ...
    @version.setter
    def version(self, version) -> None: ...
    @property
    def commit(self): ...
    @commit.setter
    def commit(self, commit) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
