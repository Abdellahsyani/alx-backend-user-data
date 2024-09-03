#!/usr/bin/env python3
"""create a class authentication
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """return
        """
        if path in excluded_paths:
            return False
        return True


    def authorization_header(self, request=None) -> str:
        """return
        """
        if request is not None:
            return request.headers.get('Authorization')
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user from the request
        """
        return None
