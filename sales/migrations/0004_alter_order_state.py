# Generated by Django 4.1 on 2022-09-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_order_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('Failed', 'failed'), ('Success', 'success'), ('Pending', 'pending')], default=('pending', 'Pending'), max_length=100),
        ),
    ]
