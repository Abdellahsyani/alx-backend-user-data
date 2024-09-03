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
        if path in excluded_paths:
            return False
        return True


    def authorization_header(self, request=None) -> str:
        """return
        """
        head = request.headers.get('Authorization')
        return head


    def current_user(self, request=None) -> TypeVar('User'):
        """return
        """
         authorization_header = request.headers.get('Authorization')
        if authorization_header:
            token = authorization_header.split(' ')[1]
            # Validate the token and extract user information
            user_data = validate_token(token)
            if user_data:
                return User(**user_data)  # Assuming User class has appropriate fields

        return None
