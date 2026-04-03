# Set FAST_MODE = True to zero all artificial delays for a faster test run.
# Note: DELAY_SORT in InventoryPage keeps a minimum of 0.3 s even in FAST_MODE
# because sorting triggers a full DOM re-render; setting it to 0 causes
# stale-element failures.

FAST_MODE = False

# Browser to use for test runs. Supported values: "chrome", "firefox", "edge".
# Firefox requires geckodriver to be installed and on PATH.
# Edge requires msedgedriver to be installed and on PATH.

BROWSER = "chrome"


def delay(value, minimum=0):
    """Return minimum when FAST_MODE is True, otherwise return value."""
    return minimum if FAST_MODE else value
