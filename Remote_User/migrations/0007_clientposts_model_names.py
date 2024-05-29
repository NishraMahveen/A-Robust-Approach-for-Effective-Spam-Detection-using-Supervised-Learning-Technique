from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remote_User', '0006_review_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientposts_model',
            name='uname',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
