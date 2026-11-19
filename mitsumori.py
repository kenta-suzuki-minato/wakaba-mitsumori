"""見積金額の計算。"""

# 消費税率（%）。浮動小数点の誤差を避けるため整数で持つ。
TAX_RATE_PERCENT = 10


def zeikomi(price: int) -> int:
    """税抜金額 price から税込金額を返す（1円未満は切り捨て）。"""
    return price * (100 + TAX_RATE_PERCENT) // 100
