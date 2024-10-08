from _typeshed import Incomplete
from typing import Any

log: Any

class ValidatorsContainer:
    pre_auth: Any
    post_auth: Any
    pre_token: Any
    post_token: Any
    def __init__(self, post_auth, post_token, pre_auth, pre_token) -> None: ...
    @property
    def all_pre(self): ...
    @property
    def all_post(self): ...

class GrantTypeBase:
    error_uri: Any
    request_validator: Any
    default_response_mode: str
    refresh_token: bool
    response_types: Any
    def __init__(self, request_validator: Incomplete | None = None, **kwargs) -> None: ...
    def register_response_type(self, response_type) -> None: ...
    def register_code_modifier(self, modifier) -> None: ...
    def register_token_modifier(self, modifier) -> None: ...
    def create_authorization_response(self, request, token_handler) -> None: ...
    def create_token_response(self, request, token_handler) -> None: ...
    def add_token(self, token, token_handler, request): ...
    def validate_grant_type(self, request) -> None: ...
    def validate_scopes(self, request) -> None: ...
    def prepare_authorization_response(self, request, token, headers, body, status): ...
