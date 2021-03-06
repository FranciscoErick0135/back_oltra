# Generated by Django 3.1.2 on 2020-10-09 00:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarreraModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EventsModel',
            },
        ),
        migrations.CreateModel(
            name='SchoolCycleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('start', models.CharField(max_length=20, null=True)),
                ('end', models.CharField(max_length=20, null=True)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'SchoolCycleModel',
            },
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(max_length=255, null=True)),
                ('fullName', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('ap_pat', models.CharField(max_length=255, null=True)),
                ('ap_mat', models.CharField(max_length=255, null=True)),
                ('birthplace', models.CharField(max_length=255, null=True)),
                ('dadsName', models.CharField(max_length=255, null=True)),
                ('dadsOcupation', models.CharField(max_length=255, null=True)),
                ('dadsEmail', models.CharField(max_length=255, null=True)),
                ('dadsPhone', models.CharField(max_length=255, null=True)),
                ('momName', models.CharField(max_length=255, null=True)),
                ('momOcupation', models.CharField(max_length=255, null=True)),
                ('momEmail', models.CharField(max_length=255, null=True)),
                ('momPhone', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('birthDate', models.CharField(max_length=255, null=True)),
                ('civilStatus', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('economically', models.IntegerField(default=0)),
                ('work', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('other', models.CharField(max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'StudentModel',
            },
        ),
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('matricula', models.CharField(max_length=255)),
                ('nombreEquipo', models.CharField(max_length=255)),
                ('nombreCarrerar', models.CharField(max_length=255)),
                ('lider', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('carrera', models.ForeignKey(on_delete=models.SET(-1), to='Dashboard.carreramodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('phone', models.CharField(max_length=255)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncidenceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255)),
                ('commitment', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=models.SET(-1), to='Dashboard.studentmodel')),
                ('typeEvent', models.ForeignKey(on_delete=models.SET(-1), to='Dashboard.eventsmodel')),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'IncidenceModel',
            },
        ),
        migrations.CreateModel(
            name='GroupsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gruop', models.CharField(max_length=255)),
                ('matter', models.CharField(max_length=255)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('SchoolCycle', models.ForeignKey(on_delete=models.SET(-1), to='Dashboard.schoolcyclemodel')),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'GroupsModel',
            },
        ),
        migrations.CreateModel(
            name='GroupCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGroup', models.CharField(max_length=255)),
                ('codeGroup', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'GroupCode',
            },
        ),
        migrations.CreateModel(
            name='FilesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('incidence', models.ForeignKey(on_delete=models.SET(-1), to='Dashboard.incidencemodel')),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'FilesModel',
            },
        ),
        migrations.CreateModel(
            name='EconomicallyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'EconomicallyModel',
            },
        ),
        migrations.CreateModel(
            name='ChatIncidenceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('incidence', models.ForeignKey(on_delete=models.SET(-1), to='Dashboard.incidencemodel')),
                ('user', models.ForeignKey(on_delete=models.SET(-1), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ChatIncidenceModel',
            },
        ),
    ]
