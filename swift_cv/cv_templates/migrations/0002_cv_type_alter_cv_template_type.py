# Generated by Django 4.1.3 on 2023-03-18 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv_templates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV_type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='cv_template',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv_templates.cv_type'),
        ),
    ]