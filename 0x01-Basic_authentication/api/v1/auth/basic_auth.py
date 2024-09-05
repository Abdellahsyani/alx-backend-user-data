#!/usr/bin/env python3
"""in this time the class empty
"""
from api.v1.auth.auth import Auth
import base64


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
        if type(base64_authorization_header) is not str:
            return None

        try:
            # convert the decode part to byte
            code_byte = base64.b64decode(base64_authorization_header)

            # convert byte to utf-8
            base64_value = code_byte.decode('utf-8')
            return base64_value
        except Exception as error:
            print("Error decoding base64: {}".format(error))
            return None
