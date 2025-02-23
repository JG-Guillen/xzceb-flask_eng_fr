import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

"""Translator file"""

load_dotenv()
APIKEY = os.environ["apikey"]
URL = os.environ["url"]

AUTHENTICATOR = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=AUTHENTICATOR
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """write the code here"""
    if english_text == "" or english_text is None or english_text == "null":
        return ""
    else:
        translation = language_translator.translate(
            text=english_text, model_id="en-fr"
        ).get_result()
        french_text = translation["translations"][0]["translation"]
        return french_text


def french_to_english(french_text):
    """write the code here"""
    if french_text == "" or french_text is None or french_text == "null":
        return ""
    else:
        translation = language_translator.translate(
            text=french_text, model_id="fr-en"
        ).get_result()
        english_text = translation["translations"][0]["translation"]
        return english_text
