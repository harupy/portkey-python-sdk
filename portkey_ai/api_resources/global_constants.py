MISSING_API_KEY_ERROR_MESSAGE = """Portkey API Key Not Found \

Resolution: \

1. Get your Portkey API key from https://app.portkey.ai/api-keys
2. Pass it while instantiating the Portkey client with api_key param,\
 or set it as an environment variable with export PORTKEY_API_KEY=YOUR_API_KEY
"""

MISSING_BASE_URL = """No Base url provided. Please provide a valid base url.
For example: https://api.portkey.ai
"""

MISSING_CONFIG_MESSAGE = (
    """The 'config' parameter is not set. Please provide a valid Config object."""
)
MISSING_MODE_MESSAGE = (
    """The 'mode' parameter is not set. Please provide a valid mode literal."""
)

INVALID_PORTKEY_MODE = """
Argument of type '{}' cannot be assigned to parameter "mode" of \
    type "ModesLiteral | Modes | None"
"""

DEFAULT_MAX_RETRIES = 2
VERSION = "0.1.0"
DEFAULT_TIMEOUT = 60
PORTKEY_HEADER_PREFIX = "x-portkey-"
PORTKEY_BASE_URL = "https://api.portkey.ai/v1"
PORTKEY_GATEWAY_URL = PORTKEY_BASE_URL
PORTKEY_API_KEY_ENV = "PORTKEY_API_KEY"
PORTKEY_PROXY_ENV = "PORTKEY_PROXY"
OPEN_AI_API_KEY = "DUMMY-KEY"
