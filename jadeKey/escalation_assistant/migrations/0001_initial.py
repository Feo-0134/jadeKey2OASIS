# Generated by Django 3.0 on 2019-12-18 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('OG', 'On-going'), ('PS', 'Pass'), ('NP', 'No Pass')], max_length=2)),
                ('comment_text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('title', models.CharField(choices=[('SE', 'Support Engineer'), ('SEE', 'Support Escalation Engineer'), ('EE', 'Escalation Engineer')], max_length=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('E1', 'Escalation to SEE'), ('E2', 'Escalat\x08ion to EE')], max_length=2)),
                ('status', models.CharField(choices=[('S0', 'Stage1'), ('S1', 'Stage1'), ('S2', 'Stage1'), ('S3', 'Stage1'), ('PS', 'Pass'), ('NP', 'No Pass')], max_length=2)),
                ('engineer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalation_assistant.Engineer')),
            ],
            options={
                'ordering': ['engineer'],
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('S1', 'Stage1'), ('S2', 'Stage2'), ('S3', 'Stage3'), ('S4', 'Stage4'), ('S0', 'BackUp')], max_length=2)),
                ('status', models.CharField(choices=[('OG', 'On-going'), ('PS', 'Pass'), ('NP', 'No Pass')], max_length=2)),
                ('commitee_num', models.IntegerField()),
            ],
            options={
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='StageLinkComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalation_assistant.Comment')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalation_assistant.Stage')),
            ],
        ),
        migrations.AddField(
            model_name='stage',
            name='comment',
            field=models.ManyToManyField(through='escalation_assistant.StageLinkComment', to='escalation_assistant.Comment'),
        ),
        migrations.CreateModel(
            name='ProcessLinkStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalation_assistant.Process')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalation_assistant.Stage')),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='stage',
            field=models.ManyToManyField(through='escalation_assistant.ProcessLinkStage', to='escalation_assistant.Stage'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escalation_assistant.Engineer'),
        ),
    ]
