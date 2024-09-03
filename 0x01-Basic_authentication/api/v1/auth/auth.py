#!/usr/bin/env python3
"""create a class authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks if a path is in th eexcluded_path
        """
        if path not in excluded_paths:
            return True
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """get the authorization header from the request
        """
        if request is not None:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user from the request
        """
        return None
