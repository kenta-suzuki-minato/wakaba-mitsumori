"""見積金額の計算。"""

TAX_RATE = 0.10


def zeikomi(price: int) -> int:
    """税抜金額 price から税込金額を返す（1円未満は切り捨て）。"""
    return round(price * (1 + TAX_RATE))
