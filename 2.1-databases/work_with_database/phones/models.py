from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=60)

    @classmethod
    def create(cls, id, name, price, image, release_date, lte_exists, slug):
        phone = cls(id=id, name=name, price=price, image=image, release_date=release_date, lte_exists=lte_exists,
                    slug=slug)
        return phone
