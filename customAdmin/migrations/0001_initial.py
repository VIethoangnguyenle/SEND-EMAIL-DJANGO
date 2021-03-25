# Generated by Django 3.1.7 on 2021-03-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=1, max_length=3)),
                ('level', models.CharField(choices=[('ST', 'Student'), ('FR', 'Fresher'), ('JU', 'Junior'), ('PR', 'Professor')], default='ST', max_length=2)),
            ],
        ),
    ]
