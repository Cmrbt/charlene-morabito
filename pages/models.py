from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, default="CHARLÈNE MORABITO")
    slogan = models.CharField(max_length=255, blank=True, default="SAVOIR-FAIRE ITALIEN, ALLURE PARISIENNE")
    call_to_action = models.CharField(max_length=100, blank=True, default="DÉCOUVRIR LA COLLECTION")
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.name



class FirstHomeSection(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    link_text = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='home/first_section/', blank=True, null=True)

    def __str__(self):
        return self.title or "Première section"


class SecondHomeSection(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    link_text = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='home/second_section/', blank=True, null=True)

    def __str__(self):
        return self.title or "Deuxième section"


class ReadyToWearSection(models.Model):
    subtitle = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200, blank=True)
    link_text = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    background = models.ImageField(upload_to='home/ready_section/', blank=True, null=True)

    def __str__(self):
        return self.title or "Section Ready-to-Wear"
    



class LookbookSection(models.Model):
    subtitle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.subtitle or "Lookbook"
    

class LookbookImage(models.Model):
    section = models.ForeignKey(LookbookSection, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home/lookbook/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image {self.pk} - {self.section.subtitle}"




class HeritageIntro(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title or "Introduction Héritage"


class HeritageBlockOne(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='home/heritage_block_one/', blank=True, null=True)

    def __str__(self):
        return self.title or "Bloc 1 – Calabre"


class HeritageBlockTwo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='home/heritage_block_two/', blank=True, null=True)

    def __str__(self):
        return self.title or "Bloc 2 – Cannes"


class HeritageBlockThree(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='home/heritage_block_three/', blank=True, null=True)

    def __str__(self):
        return self.title or "Bloc 3 – Paris"
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to='products/main/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/extra/')

    def __str__(self):
        return f"Image pour {self.product.name}"


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"Détail pour {self.product.name}"


class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=20)

    def __str__(self):
        return f"Taille {self.size} pour {self.product.name}"