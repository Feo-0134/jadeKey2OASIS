# Generated by Django 3.0 on 2019-12-18 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.AlterModelOptions(
            name='process',
            options={'ordering': ['engineer']},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'ordering': ['status']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='stage',
        ),
        migrations.RemoveField(
            model_name='process',
            name='created',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='created',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='process',
        ),
        migrations.AddField(
            model_name='engineer',
            name='user',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='commitee_num',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='result',
            field=models.CharField(choices=[('OG', 'On-going'), ('PS', 'Pass'), ('NP', 'No Pass')], max_length=2),
        ),
        migrations.AlterField(
            model_name='process',
            name='status',
            field=models.CharField(choices=[('S0', 'Stage1'), ('S1', 'Stage1'), ('S2', 'Stage1'), ('S3', 'Stage1'), ('PS', 'Pass'), ('NP', 'No Pass')], max_length=2),
        ),
        migrations.AlterField(
            model_name='process',
            name='title',
            field=models.CharField(choices=[('E1', 'Escalation to SEE'), ('E2', 'Escalat\x08ion to EE')], max_length=2),
        ),
        migrations.AlterField(
            model_name='stage',
            name='status',
            field=models.CharField(choices=[('OG', 'On-going'), ('PS', 'Pass'), ('NP', 'No Pass')], max_length=2),
        ),
        migrations.AlterField(
            model_name='stage',
            name='title',
            field=models.CharField(choices=[('S1', 'Stage1'), ('S2', 'Stage2'), ('S3', 'Stage3'), ('S4', 'Stage4'), ('S0', 'BackUp')], max_length=2),
        ),
        migrations.CreateModel(
            name='StageLinkComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escapp.Comment')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escapp.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessLinkStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escapp.Process')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escapp.Stage')),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='stage',
            field=models.ManyToManyField(through='escapp.ProcessLinkStage', to='escapp.Stage'),
        ),
        migrations.AddField(
            model_name='stage',
            name='comment',
            field=models.ManyToManyField(through='escapp.StageLinkComment', to='escapp.Comment'),
        ),
    ]
