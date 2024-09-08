#!/usr/bin/env python3
"""start a new authentication mechanism
"""
from api.v1.auth.auth import Auth
from flask import Flask, session
from uuid import uuid4


class SessionAuth(Auth):
    """ authentication mechanism starting
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a session id for user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ return User ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
