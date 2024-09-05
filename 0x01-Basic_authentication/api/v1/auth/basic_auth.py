#!/usr/bin/env python3
"""in this time the class empty
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """start class"""

    def extract_base64_authorization_header(self, authorization_header: str)
    -> str:
        """return the base64
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):]
