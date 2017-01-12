# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_num_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.CharField(max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
