"""Unit testi app.py faila funkcijai."""

import pytest

from app import calculate_vat


def test_calculate_vat_for_positive_price():
    """Pārbauda PVN aprēķinu pozitīvai cenai."""
    assert calculate_vat(100) == 21.0


def test_calculate_vat_for_zero_price():
    """Pārbauda, ka PVN no 0 EUR ir 0 EUR."""
    assert calculate_vat(0) == 0.0


def test_calculate_vat_for_negative_price():
    """Pārbauda, ka negatīva cena nav atļauta."""
    with pytest.raises(ValueError):
        calculate_vat(-10)


def test_calculate_vat_for_invalid_type():
    """Pārbauda, ka teksts cenas vietā nav atļauts."""
    with pytest.raises(TypeError):
        calculate_vat("100")