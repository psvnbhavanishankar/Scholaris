# Generated by Django 2.1.3 on 2018-12-10 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Result_Analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('option1', models.CharField(max_length=200, verbose_name='option1')),
                ('option2', models.CharField(max_length=200, verbose_name='option2')),
                ('option3', models.CharField(max_length=200, verbose_name='option3')),
                ('option4', models.CharField(max_length=200, verbose_name='option4')),
                ('answer', models.CharField(choices=[('1', 'option1'), ('2', 'option2'), ('3', 'option3'), ('4', 'option4')], max_length=200)),
                ('mark', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_ans', models.IntegerField(default=0)),
                ('wrong_ans', models.IntegerField(default=0)),
                ('marks', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Result_Analysis.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('time', models.DateTimeField()),
                ('duration', models.IntegerField(default=0)),
                ('total_marks', models.IntegerField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_Analysis.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='studentresult',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Test_Designing.Test'),
        ),
        migrations.AddField(
            model_name='questionset',
            name='question_list',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Test_Designing.Test'),
        ),
        migrations.AddField(
            model_name='question',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test_Designing.QuestionSet'),
        ),
    ]
