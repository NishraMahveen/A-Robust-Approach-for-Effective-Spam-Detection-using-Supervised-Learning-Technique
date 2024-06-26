from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Remote_User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientPosts_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tdesc', models.CharField(max_length=300)),
                ('uname', models.CharField(max_length=300)),
                ('topics', models.CharField(max_length=300)),
                ('sanalysis', models.CharField(max_length=300)),
                ('senderstatus', models.CharField(default='process', max_length=300)),
                ('ratings', models.IntegerField(default=0)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Remote_User.ClientRegister_Model')),
            ],
        ),
    ]
