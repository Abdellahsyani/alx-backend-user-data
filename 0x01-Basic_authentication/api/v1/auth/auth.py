#!/usr/bin/env python3
"""create a class authentication
"""
from flask import request


class Auth:
    """API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return
        """
        pass


    def authorization_header(self, request=None) -> str:
        """return
        """
        pass


    def current_user(self, request=None) -> TypeVar('User'):
        """return
        """
        pass
