# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
"""Utilities for the shop application."""

import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadHashedTo():
    """Return a function giving a name for a file in the given path."""

    def __init__(self, path):
        """Create object specifying the path."""
        self.path = path

    def __call__(self, instance, filename):
        """Function giving a nawe for a file in a given path."""
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)
