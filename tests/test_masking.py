import pytest
from src.core.masker import LLMMasker

def test_mask_email():
    masker = LLMMasker()
    text = "Contact me at user@example.com"
    result = masker.mask(text)
    assert "user@example.com" not in result["masked_text"]
    assert "EMAIL_ADDRESS" in result["entities"]

def test_mask_phone():
    masker = LLMMasker()
    text = "Call me at 555-0101"
    result = masker.mask(text)
    assert "555-0101" not in result["masked_text"]
    assert "PHONE_NUMBER" in result["entities"]

def test_mask_no_pii():
    masker = LLMMasker()
    text = "Hello world, what's up?"
    result = masker.mask(text)
    assert result["masked_text"] == text
    assert len(result["entities"]) == 0
