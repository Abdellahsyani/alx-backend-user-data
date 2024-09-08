#!/usr/bin/env python3
"""create a class authentication
"""
import re
import os
from flask import request, cookies
from typing import List, TypeVar


class Auth:
    """API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication.
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """get the authorization header from the request
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """get the current user from the request
        """
        return None

    def session_cookie(self, request=None):
        """ return a cookie value
        """
        if request is None:
            return None

        cookie_value = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(cookie_value)
