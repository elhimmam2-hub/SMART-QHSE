"""Internationalization (i18n) Module"""
import json
from typing import Dict, Any
from pathlib import Path

# Supported languages
SUPPORTED_LANGUAGES = ["ar", "en", "fr"]
DEFAULT_LANGUAGE = "ar"

# Load translations
TRANSLATIONS: Dict[str, Dict[str, Any]] = {}

def load_translations():
    """Load all translation files"""
    global TRANSLATIONS
    translations_dir = Path(__file__).parent / "locales"
    
    for lang in SUPPORTED_LANGUAGES:
        lang_file = translations_dir / f"{lang}.json"
        if lang_file.exists():
            with open(lang_file, 'r', encoding='utf-8') as f:
                TRANSLATIONS[lang] = json.load(f)
        else:
            TRANSLATIONS[lang] = {}

def get_translation(key: str, language: str = DEFAULT_LANGUAGE, **kwargs) -> str:
    """Get translation for a key in a specific language"""
    if language not in SUPPORTED_LANGUAGES:
        language = DEFAULT_LANGUAGE
    
    if not TRANSLATIONS:
        load_translations()
    
    translation = TRANSLATIONS.get(language, {}).get(key, key)
    
    # Format with kwargs if provided
    if kwargs:
        try:
            return translation.format(**kwargs)
        except KeyError:
            return translation
    
    return translation

def t(key: str, language: str = DEFAULT_LANGUAGE, **kwargs) -> str:
    """Shorthand for get_translation"""
    return get_translation(key, language, **kwargs)

# Load translations on module import
load_translations()
