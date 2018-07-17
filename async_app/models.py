from django.db import models

# Create your models here.

class AsyncMember(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class AsyncOrder(models.Model):
    order_id = models.CharField(max_length=128)
    name = models.CharField(max_length=128)

class PaymentMethod(models.Model):
    DEFAULT = 1
    WALLET = 2
    AMEX = 3
    PAYMENT_GATEWAY = 4
    FOOD_WALLET = 5
    PAYMENT_TYPE_COD = 'cod'
    PAYMENT_TYPES = (
        (DEFAULT, "Default"),
        (WALLET, "Wallet"),
        (AMEX, "Amex"),
        (PAYMENT_GATEWAY, "Payment Gateway"),
        (PAYMENT_TYPE_COD, "Cash On Delivery"),
        (FOOD_WALLET, "Food Wallet"),
    )
    NORMAL = ""
    BANK = "bank_voucher"
    VOUCHER_TYPES = (
        (NORMAL, ""),
        (BANK, "Bank Voucher")
    )

    CHECKOUT, PAY_NOW, FUND_WALLET = range(3)

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, help_text='Displayed on website')
    slug = models.SlugField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'cart_paymentmethod'


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    payment_method = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'order_invoice'


class Order(models.Model):
    """
    Orders contain the transaction details of a particular order.
    It will be closed automatically at the order closure time for the delivery.
    """

    order_id = models.CharField(max_length=50, blank=True, null=True, unique=True)
    invoice = models.ForeignKey(Invoice, blank=True, null=True)

    class Meta:
        db_table = 'order_order'

class PrepaidOrders(models.Model):

    MOBILE_ANDROID = 'MOBILE_ANDROID'
    MOBILE_IOS = 'MOBILE_IOS'
    MOBILE_WEB = 'MOBILE_WEB'
    TABLET_WEB = 'TABLET_WEB'
    WEB = 'WEB'

    CHANNEL_LIST = (
        (MOBILE_ANDROID, 'Mobile Android'),
        (MOBILE_IOS, 'Mobile iOS'),
        (MOBILE_WEB, 'Mobile Web'),
        (TABLET_WEB, 'Tablet Web'),
        (WEB, 'Web')
    )

    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=True)
    txn_id = models.IntegerField(null=True, blank=True, db_index=True)
    txn_status = models.CharField(max_length=200, null=True, blank=True)
    payment_source = models.CharField(max_length=200, null=True, blank=True)
    txn_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order = models.ForeignKey(Order, null=True, blank=True)

    class Meta:
        db_table = 'order_prepaidorders'

