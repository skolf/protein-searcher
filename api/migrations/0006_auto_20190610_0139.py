# Generated by Django 2.2 on 2019-06-10 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_update_NC_016072_sequence_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='protein',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Protein'),
        ),
    ]
