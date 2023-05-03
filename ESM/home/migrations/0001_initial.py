# Generated by Django 4.2 on 2023-05-02 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TInput',
            fields=[
                ('i_id', models.IntegerField(primary_key=True, serialize=False)),
                ('in_fname', models.CharField(max_length=30)),
                ('in_ftype', models.CharField(max_length=4)),
                ('in_contents', models.TextField()),
                ('in_words', models.TextField()),
                ('in_date', models.DateField()),
            ],
            options={
                'db_table': 'tinput',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('us_id', models.CharField(max_length=20)),
                ('us_pw', models.CharField(max_length=20)),
                ('us_api', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'tuser',
            },
        ),
        migrations.CreateModel(
            name='TWord',
            fields=[
                ('w_id', models.IntegerField(primary_key=True, serialize=False)),
                ('w_name', models.TextField()),
                ('w_contents', models.TextField()),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tinput')),
            ],
            options={
                'db_table': 'tword',
            },
        ),
        migrations.CreateModel(
            name='TSummary',
            fields=[
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('su_impwords', models.TextField()),
                ('su_contents', models.TextField()),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tinput')),
            ],
            options={
                'db_table': 'tsummary',
            },
        ),
        migrations.AddField(
            model_name='tinput',
            name='p_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tuser'),
        ),
        migrations.CreateModel(
            name='TExtent',
            fields=[
                ('e_id', models.IntegerField(primary_key=True, serialize=False)),
                ('ex_contents', models.TextField()),
                ('i_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.tinput')),
            ],
            options={
                'db_table': 'textent',
            },
        ),
    ]