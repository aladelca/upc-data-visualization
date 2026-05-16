from __future__ import annotations

import ssl
import urllib.error
import urllib.request
import warnings
from typing import cast

import certifi


def read_url_bytes(url: str, *, timeout: int = 120) -> bytes:
    context = ssl.create_default_context(cafile=certifi.where())
    try:
        return _read_url_bytes(url, timeout=timeout, context=context)
    except urllib.error.URLError as error:
        if isinstance(error.reason, ssl.SSLCertVerificationError):
            warnings.warn(
                "SSL certificate validation failed for "
                f"{url}; retrying with verification disabled.",
                stacklevel=2,
            )
            return _read_url_bytes(
                url,
                timeout=timeout,
                context=ssl._create_unverified_context(),  # noqa: SLF001
            )
        raise


def _read_url_bytes(url: str, *, timeout: int, context: ssl.SSLContext) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=timeout, context=context) as response:
        return cast(bytes, response.read())
