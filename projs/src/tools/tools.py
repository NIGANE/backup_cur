
from functools import lru_cache
from src.models.Prompt import Prompt


def in_string(sub: str, sen: str) -> bool:
    """Determine whether a string is contained within another string.

    The comparison is case-insensitive.

    Args:
        sub: The substring to search for.
        sen: The string to search within.

    Returns:
        ``True`` if ``sub`` occurs within ``sen``; otherwise ``False``.
    """
    if sub is None or sen is None:
        return False
    i = 0
    j = 0
    sub = sub.lower()
    sen = sen.lower()
    while i < len(sen):
        if sub[j] == sen[i]:
            while j < len(sub) and i + j < len(sen):
                if sub[j] != sen[i + j]:
                    break
                j += 1
            if (j == len(sub)):
                return True
            j = 0
        i += 1
    return False


@lru_cache()
def _cache(prompt: str) -> Prompt:
    """Return a cached ``Prompt`` instance.

    Reuses previously created ``Prompt`` objects for identical prompt
    strings, avoiding repeated instantiation.

    Args:
        prompt: The prompt text.

    Returns:
        A cached ``Prompt`` instance corresponding to the given prompt.
    """
    return Prompt(prompt)
