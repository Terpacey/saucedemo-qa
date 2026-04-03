import os

# FAST_MODE: zeros all artificial delays for a faster test run.
# Automatically True in CI (GitHub Actions sets CI=true).
# Override locally: FAST_MODE=true pytest, or change the fallback value below.
# Note: DELAY_SORT in InventoryPage keeps a minimum of 0.3 s even in FAST_MODE
# because sorting triggers a full DOM re-render; setting it to 0 causes
# stale-element failures.
_fast_env = os.environ.get("FAST_MODE")
FAST_MODE = (
    _fast_env.lower() in ("true", "1") if _fast_env
    else bool(os.environ.get("CI"))
)

# Browser to use for test runs.
# Override per-run: BROWSER=firefox pytest
# Supported values: "chrome", "firefox", "edge".
# Firefox requires geckodriver to be installed and on PATH.
# Edge requires msedgedriver to be installed and on PATH.
BROWSER = os.environ.get("BROWSER", "chrome")


def delay(value, minimum=0):
    """Return minimum when FAST_MODE is True, otherwise return value."""
    return minimum if FAST_MODE else value
