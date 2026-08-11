"""Vienkārša Python lietotne PB1_PD20 praktiskajam darbam."""


def calculate_vat(price: float) -> float:
    """Aprēķina 21% PVN summu no norādītās cenas.

    Args:
        price: Cena EUR bez PVN.

    Returns:
        PVN summa EUR.

    Raises:
        ValueError: Ja cena ir negatīva.
        TypeError: Ja cena nav skaitlis.
    """
    if not isinstance(price, (int, float)):
        raise TypeError("Cenai jābūt skaitlim.")

    if price < 0:
        raise ValueError("Cena nevar būt negatīva.")

    return round(price * 0.25, 2)


if __name__ == "__main__":
    price = 100
    vat = calculate_vat(price)
    print(f"PVN no {price} EUR ir {vat} EUR")