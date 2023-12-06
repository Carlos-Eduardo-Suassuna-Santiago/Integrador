# Generated by Django 3.0.5 on 2023-12-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20231127_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Educação', 'Educação'), ('Entretenimento', 'Entretenimento'), ('Quadrinho', 'Quadrinho'), ('Biografia', 'Biografia'), ('História', 'História'), ('Narrativa', 'Narrativa'), ('Fantasia', 'Fantasia'), ('Suspense', 'Suspense'), ('Romance', 'Romance'), ('Ficção Científica', 'Ficção Científica')], default='education', max_length=30),
        ),
    ]