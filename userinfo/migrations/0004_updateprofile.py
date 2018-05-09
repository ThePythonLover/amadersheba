# Generated by Django 2.0.4 on 2018-05-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0003_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('date_of_birth', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=8)),
                ('address', models.CharField(max_length=100)),
                ('present_address', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=60)),
                ('user_bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_setting')),
            ],
        ),
    ]
