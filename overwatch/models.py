from django.db import models
from django.urls import reverse


from .calculatePrice import calculate_price

# Create your models here.
TYPE = (
    ('B','boost'),
    ('Q','qualification'),
    ('C', 'custom')
)


class Booster(models.Model):
    name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Pack(models.Model):
    name = models.CharField(max_length=16)
    type = models.CharField(max_length=1, choices=TYPE)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пакет услуг'
        verbose_name_plural = 'Пакеты услуг'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    type = models.CharField(max_length=1, choices=TYPE)
    pack = models.CharField(max_length=32, blank=True, null=True)
    oldScore = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    newScore = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    email = models.EmailField(max_length=30, default='', blank=True, null=True)
    discord = models.CharField(max_length=30, default='', blank=True, null=True)
    skype = models.CharField(max_length=30, default='', blank=True, null=True)
    name = models.CharField(max_length=30, default='', blank=True, null=True)
    contact = models.CharField(max_length=150, default='', blank=True, null=True)
    price = models.FloatField(max_length=3, blank=True, null=True)
    paid = models.BooleanField(default=True)
    booster = models.ForeignKey(Booster, default=1)
    done = models.BooleanField(default=False)

    def __str__(self):
        return '%f' % (self.newScore)

    class Meta:
        verbose_name = 'Заказ на буст'
        verbose_name_plural = 'Заказы на буст'

    def save(self):
        self.contact = 'discord: ' + str(self.discord) + ' || skype: ' + str(self.skype) + ' || name: ' + str(self.name)
        if self.newScore > self.oldScore:
            self.price = calculate_price(self.oldScore, self.newScore)
        elif self.newScore < self.oldScore:
            self.price = 150

        super(Order, self).save()


