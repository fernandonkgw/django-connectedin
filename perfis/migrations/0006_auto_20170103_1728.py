# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_perfil_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nome_empresa',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
