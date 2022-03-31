# Generated by Django 3.2.3 on 2021-05-25 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='uploaded_images/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('basicfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.basicfields')),
            ],
            options={
                'verbose_name': 'Thread',
                'verbose_name_plural': 'Threads',
            },
            bases=('board.basicfields',),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('basicfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.basicfields')),
                ('belonging_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.thread')),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
            bases=('board.basicfields',),
        ),
    ]
