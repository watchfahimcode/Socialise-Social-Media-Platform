

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorites',
        ),
    ]
