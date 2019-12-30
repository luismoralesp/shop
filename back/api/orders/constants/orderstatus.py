
class OrderStatus:
    """
    This is the aviable values for order status
    """

    CREATED = 'CREATED'
    PAYED = 'PAYED'
    REJECTED = 'REJECTED'

    choices = (
        (CREATED, CREATED),
        (PAYED, PAYED),
        (REJECTED, REJECTED)
    )