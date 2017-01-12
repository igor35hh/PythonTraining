from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
	
    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

class MaleAutor(models.Manager):
    def get_query_set(self):
        return super(MaleAutor, self).get_query_set().filter(sex='M')

class FemaleAutor(models.Manager):
    def get_query_set(self):
        return super(FemaleAutor, self).get_query_set().filter(sex='F')    

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    sex = models.CharField(max_length=1, null=True, choices=(('M','Male'),('F','Female')))
    male_objects = MaleAutor()
    female_objects = FemaleAutor()
                           
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()

class Book(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
	
    def __unicode__(self):
        return self.title
