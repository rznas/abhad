# Generated by Django 4.2 on 2023-05-21 13:33

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
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'هیچ'), (1, 'خیلی کم'), (2, 'کم'), (3, 'متوسط'), (4, 'زیاد'), (5, 'خیلی زیاد')], default=3)),
            ],
        ),
        migrations.CreateModel(
            name='SoldierRelevant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relevance', models.CharField(choices=[('F', 'پدر'), ('M', 'مادر'), ('B', 'برادر'), ('S', 'خواهر'), ('W', 'همسر'), ('D', 'فرزند')], max_length=1)),
                ('age', models.PositiveSmallIntegerField()),
                ('education_level', models.IntegerField(choices=[(0, 'ابتدایی'), (1, 'ششم متوسطه'), (2, 'هفتم متوسطه'), (3, 'هشتم متوسطه'), (4, 'نهم متوسطه'), (5, 'دهم متوسطه'), (6, 'یازدهم متوسطه'), (7, 'دوازدهم متوسطه')])),
                ('job', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='نام')),
                ('last_name', models.CharField(max_length=64, verbose_name='نشان')),
                ('rank', models.IntegerField(choices=[(0, 'سرباز'), (1, 'سرباز ۲'), (2, 'سرباز ۱'), (3, 'سر جوخه'), (4, 'گروهبانسوم'), (5, 'گروهباندوم'), (6, 'گروهبانیکم'), (7, 'ستوانسوم'), (8, 'ستواندوم'), (9, 'ستوانیکم')], verbose_name='درجه')),
                ('guild', models.IntegerField(choices=[(0, 'پیاده'), (1, 'بهداشت و درمان')], default=1, verbose_name='رسته')),
                ('military_id', models.CharField(max_length=10, verbose_name='شماره پرسنلی')),
                ('father_name', models.CharField(max_length=64, verbose_name='نام پدر')),
                ('birth_date', models.DateField(verbose_name='تاریخ تولد')),
                ('birth_location', models.CharField(max_length=64, verbose_name='محل تولد')),
                ('national_id', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('education_level', models.IntegerField(choices=[(0, 'ابتدایی'), (1, 'ششم متوسطه'), (2, 'هفتم متوسطه'), (3, 'هشتم متوسطه'), (4, 'نهم متوسطه'), (5, 'دهم متوسطه'), (6, 'یازدهم متوسطه'), (7, 'دوازدهم متوسطه')], verbose_name='میزان تحصیلات')),
                ('education_field', models.CharField(blank=True, max_length=64, null=True, verbose_name='رشته تحصیلی / گرایش')),
                ('is_married', models.BooleanField(default=False, verbose_name='آیا متأهل است؟')),
                ('religion', models.IntegerField(choices=[(0, 'اسلام شیعه'), (1, 'اسلام سنی'), (2, 'یهودی'), (3, 'مسیحی'), (4, 'آتئیسم (بی دین)')], verbose_name='دین / مذهب')),
                ('dispatch_date', models.DateField(verbose_name='تاریخ اعزام')),
                ('dispatch_territory', models.CharField(max_length=64, verbose_name='حوزه اعزام')),
                ('living_location_before_dispatch', models.CharField(max_length=64, verbose_name='محل زندگی قبل از خدمت')),
                ('former_job', models.CharField(blank=True, max_length=64, null=True, verbose_name='شغل قبلی')),
                ('attendance_date', models.DateField(verbose_name='تاریخ حضور')),
                ('living_address', models.CharField(max_length=256, verbose_name='آدرس محل سکونت')),
                ('home_phone_number', models.CharField(max_length=13, verbose_name='تلفن ثابت')),
                ('cell_number', models.CharField(max_length=13, verbose_name='تلفن همراه')),
                ('financial_status', models.PositiveSmallIntegerField(choices=[(0, 'هیچ'), (1, 'خیلی کم'), (2, 'کم'), (3, 'متوسط'), (4, 'زیاد'), (5, 'خیلی زیاد')], default=3, verbose_name='وضعیت اقتصادی - مالی')),
                ('belief_status', models.PositiveSmallIntegerField(choices=[(0, 'هیچ'), (1, 'خیلی کم'), (2, 'کم'), (3, 'متوسط'), (4, 'زیاد'), (5, 'خیلی زیاد')], default=3, verbose_name='وضعیت مذهبی - اعتقادی')),
                ('social_status', models.PositiveSmallIntegerField(choices=[(0, 'هیچ'), (1, 'خیلی کم'), (2, 'کم'), (3, 'متوسط'), (4, 'زیاد'), (5, 'خیلی زیاد')], default=3, verbose_name='وضعیت اجتماعی')),
                ('relevants', models.ManyToManyField(to='cognitive.soldierrelevant', verbose_name='بستگان')),
                ('skills', models.ManyToManyField(to='cognitive.skill', verbose_name='مهارت ها')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soldier_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'سرباز',
                'verbose_name_plural': 'سربازان',
            },
        ),
    ]