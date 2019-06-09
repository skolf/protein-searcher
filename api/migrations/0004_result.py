# Generated by Django 2.2 on 2019-06-09 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_load_proteins'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Protein')),
                ('search', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Search')),
            ],
        ),
    ]