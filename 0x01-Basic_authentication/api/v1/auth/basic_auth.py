#!/usr/bin/env python3
"""in this time the class empty
"""
from api.v1.auth.auth import Auth
from typing import Tuple
import base64
import binascii


class BasicAuth(Auth):
    """start class"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """return the base64
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ return the decoded value of base64
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # convert the decode part to byte
            code_byte = base64.b64decode(
                    base64_authorization_header,
                    validate=True)

            # convert byte to utf-8
            base64_str = code_byte.decode('utf-8')
            return base64_str
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        extract_user = decoded_base64_authorization_header.split(':', 1)
        if len(extract_user) == 2:
            return (extract_user[0], extract_user[1])
        return (None, None)
