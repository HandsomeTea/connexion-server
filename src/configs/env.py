import os
from typing import Dict, Optional, Literal

__env_type__ = Literal[
    'ENV'
]

__default_env__ = {
    'ENV': 'development'
}


def get_env(key: Optional[Dict[__env_type__, str]]):
    return os.getenv(key, __default_env__.get(key))
