# Generated by Django 4.2.1 on 2023-05-30 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='Flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='hello.airport'),
        ),
        migrations.AlterField(
            model_name='Flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='hello.airport'),
        ),
    ]
