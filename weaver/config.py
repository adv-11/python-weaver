import os
from pathlib import Path
import toml
from typing import Any, Dict

CONFIG_FILENAMES = ["weaver.toml", ".weaverrc"]

def _load_file_config() -> Dict[str, Any]:
    for name in CONFIG_FILENAMES:
        path = Path(name)
        if path.exists():
            data = toml.loads(path.read_text())
            creds = data.get("credentials", {})
            if "openai_api_key" in creds:
                return creds
    return {}

def get_openai_api_key(cli_key: str = None) -> str:
    """
    Resolution order:
      1) CLI-supplied key
      2) OPENAI_API_KEY env var
      3) weaver.toml / .weaverrc credentials.openai_api_key
    """
    if cli_key:
        return cli_key

    env_key = os.getenv("OPENAI_API_KEY")
    if env_key:
        return env_key

    file_cfg = _load_file_config()
    if file_cfg.get("openai_api_key"):
        return file_cfg["openai_api_key"]

    raise EnvironmentError(
        "Missing OpenAI API key: please supply via --api-key, "
        "set OPENAI_API_KEY, or add it to weaver.toml under [credentials]."
    )