#!/usr/bin/env python3
"""Small, dependency-free connectivity check used by Crip Welcome."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


CONNECTIVITY_URL = "https://connectivitycheck.gstatic.com/generate_204"


class Response(Protocol):
    status: int | None

    def getcode(self) -> int | None: ...

    def close(self) -> None: ...


@dataclass(frozen=True)
class InternetStatus:
    connected: bool
    detail: str


def check_internet(
    timeout: float = 2.0,
    opener: Callable[..., Response] | None = None,
) -> InternetStatus:
    """Probe a lightweight endpoint and return a display-safe status.

    The caller should invoke this from a worker thread.  Any reachable HTTP
    server is enough to establish connectivity, including an HTTP error page.
    """
    request = Request(
        CONNECTIVITY_URL,
        headers={"User-Agent": "CripWelcome/0.1"},
        method="HEAD",
    )
    open_request = opener or urlopen

    try:
        response = open_request(request, timeout=max(float(timeout), 0.1))
        try:
            status_code = getattr(response, "status", None)
            if status_code is None:
                status_code = response.getcode()
        finally:
            response.close()
    except HTTPError:
        return InternetStatus(True, "Connected")
    except (OSError, URLError, ValueError):
        return InternetStatus(False, "Offline")

    if status_code is None or 200 <= status_code < 400:
        return InternetStatus(True, "Connected")
    return InternetStatus(False, "Offline")
