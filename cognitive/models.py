from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class RANK_CHOISES(models.IntegerChoices):
    SARBAZ = 0, 'سرباز'
    SARBAZ_2 = 1, 'سرباز ۲'
    SARBAZ_1 = 2, 'سرباز ۱'
    SAR_JOOKHE = 3, 'سر جوخه'
    GORUHBAN_3 = 4, 'گروهبانسوم'
    GORUHBAN_2 = 5, 'گروهباندوم'
    GORUHBAN_1 = 6, 'گروهبانیکم'
    OSTOVAR_3 = 7, 'ستوانسوم'
    OSTOVAR_2 = 8, 'ستواندوم'
    OSTOVAR_1 = 9, 'ستوانیکم'


class GUILD_CHOISES(models.IntegerChoices):
    PIADE = 0, 'پیاده'
    BEHDASHT = 1, 'بهداشت و درمان'


class EDUCATION_LEVEL_CHOICES(models.IntegerChoices):
    EBTEDAEI = 0, 'ابتدایی'
    MOTEVASETE_6 = 1, 'ششم متوسطه'
    MOTEVASETE_7 = 2, 'هفتم متوسطه'
    MOTEVASETE_8 = 3, 'هشتم متوسطه'
    MOTEVASETE_9 = 4, 'نهم متوسطه'
    MOTEVASETE_10 = 5, 'دهم متوسطه'
    MOTEVASETE_11 = 6, 'یازدهم متوسطه'
    MOTEVASETE_12 = 7, 'دوازدهم متوسطه'


class LEVEL_CHOICES(models.IntegerChoices):
    NONE = 0, 'هیچ'
    VERY_LOW = 1, 'خیلی کم'
    LOW = 2, 'کم'
    MODERATE = 3, 'متوسط'
    HIGH = 4, 'زیاد'
    VERY_HIGH = 5, 'خیلی زیاد'


class RELIGION_CHOICES(models.IntegerChoices):
    ISLAM_SHIA = 0, 'اسلام شیعه'
    ISLAM_SUNNI = 1, 'اسلام سنی'
    JUDAISM = 2, 'یهودی'
    CHRISTIANITY = 3, 'مسیحی'
    ATHEISM = 4, 'آتئیسم (بی دین)'


class FAMILY_RELEVANCE_CHOICES(models.TextChoices):
    FATHER = 'F', 'پدر'
    MOTHER = 'M', 'مادر'
    BROTHER = 'B', 'برادر'
    SISTER = 'S', 'خواهر'
    WIFE = 'W', 'همسر'
    SON_DAUGHTER = 'D', 'فرزند'


class Skill(models.Model):
    name = models.CharField(max_length=64, verbose_name='نام')
    level = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='سطح')
    
    def __str__(self) -> str:
        return f'{self.name} | {self.level}'
    
    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'


class SoldierRelevant(models.Model):
    relevance = models.CharField(
        max_length=1, choices=FAMILY_RELEVANCE_CHOICES.choices, verbose_name='نسبت')
    name = models.CharField(max_length=64, verbose_name='نام')
    age = models.PositiveSmallIntegerField(verbose_name='سن')
    education_level = models.IntegerField(
        choices=EDUCATION_LEVEL_CHOICES.choices, verbose_name='سطح تحصیلات')
    job = models.CharField(max_length=64, null=True, blank=True, verbose_name='شغل')
    is_alive = models.BooleanField(default=True, verbose_name='آیا در قید حیات هستند؟')

    def __str__(self) -> str:
        rel = self.get_relevance_display()
        return f'{rel} | {self.name} ({self.age})'
    
    class Meta:
        verbose_name = 'فرد نزدیک سرباز'
        verbose_name_plural = 'نزدیکان سرباز'


class Soldier(models.Model):
    # user = models.ForeignKey(to=User, on_delete=models.CASCADE,
    #                          related_name='soldier_profile', null=True, blank=True)
    first_name = models.CharField(max_length=64, verbose_name='نام')
    last_name = models.CharField(max_length=64, verbose_name='نشان')
    rank = models.IntegerField(
        choices=RANK_CHOISES.choices, verbose_name='درجه')
    guild = models.IntegerField(choices=GUILD_CHOISES.choices,
                                default=GUILD_CHOISES.BEHDASHT.value, verbose_name='رسته')
    military_id = models.CharField(max_length=10, verbose_name='شماره پرسنلی')
    father_name = models.CharField(max_length=64, verbose_name='نام پدر')
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    birth_location = models.CharField(max_length=64, verbose_name='محل تولد')
    national_id = models.CharField(max_length=10, verbose_name='کد ملی')
    education_level = models.IntegerField(
        choices=EDUCATION_LEVEL_CHOICES.choices, verbose_name='میزان تحصیلات')
    education_field = models.CharField(max_length=64, null=True, blank=True, verbose_name='رشته تحصیلی / گرایش')
    skills = models.ManyToManyField(to=Skill, verbose_name='مهارت ها')
    is_married = models.BooleanField(default=False, verbose_name='آیا متأهل است؟')
    religion = models.IntegerField(choices=RELIGION_CHOICES.choices, verbose_name='دین / مذهب')
    dispatch_date = models.DateField(verbose_name='تاریخ اعزام')
    dispatch_territory = models.CharField(max_length=64, verbose_name='حوزه اعزام')
    living_location_before_dispatch = models.CharField(max_length=64, verbose_name='محل زندگی قبل از خدمت')
    former_job = models.CharField(max_length=64, null=True, blank=True, verbose_name='شغل قبلی')
    attendance_date = models.DateField(verbose_name='تاریخ حضور')
    living_address = models.CharField(max_length=256, verbose_name='آدرس محل سکونت')
    home_phone_number = models.CharField(max_length=13, verbose_name='تلفن ثابت')
    cell_number = models.CharField(max_length=13, verbose_name='تلفن همراه')
    relevants = models.ManyToManyField(to=SoldierRelevant, verbose_name='بستگان')
    financial_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='وضعیت اقتصادی - مالی')
    belief_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='وضعیت مذهبی - اعتقادی')
    social_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='وضعیت اجتماعی')
    social_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='وضعیت اجتماعی')
    currently_disease = models.BooleanField(default=False, verbose_name='آیا اکنون بیماری خاصی دارید؟')
    former_disease = models.BooleanField(default=False, verbose_name='آیا سابقه بیماری خاصی داشته اید؟')
    head_accident_history = models.BooleanField(default=False, verbose_name='سابقه ضربه به سر و یا تصادف؟')
    surgery_history = models.BooleanField(default=False, verbose_name='سابقه عمل جراحی؟')
    drug_consumption_history = models.BooleanField(default=False, verbose_name='سابقه سو مصرف مواد مخدر؟')
    being_poisoned_history = models.BooleanField(default=False, verbose_name='سابقه مسمومیت؟')
    psycho_desease_history = models.BooleanField(default=False, verbose_name='سابقه اختلالات روانی؟')
    medicine_treatment_history = models.BooleanField(default=False, verbose_name='سابقه درمان های دارویی اختلالات روانی؟')
    psychotrapy_consultant_history = models.BooleanField(default=False, verbose_name='سابقه مشاوره و روان درمانی؟')
    hospitalization_history = models.BooleanField(default=False, verbose_name='سابقه بستری شدن؟')
    family_relation_with_parents_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='میزان روابط با والدین؟')
    family_relation_with_siblings_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='میزان روابط با خواهر  برادر؟')
    family_relation_with_each_other_status = models.PositiveSmallIntegerField(
        choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.MODERATE.value, verbose_name='میزان روابط اعضای خانواده با یکدیگر؟')
    divorce_history = models.BooleanField(default=False, verbose_name='سابقه جدایی والدین؟')
    family_suicide_history = models.BooleanField(default=False, verbose_name='سابقه خودکشی در خانواده؟')
    family_psychological_problems_history = models.BooleanField(default=False, verbose_name='سابقه بیماری های روانی در خانواده؟')
    family_drug_consumption_history = models.BooleanField(default=False, verbose_name='سابقه سو مصرف مواد در خانواده؟')

    interviewer_opinions = models.TextField(verbose_name='نظرات مصاحبه کننده', default='')

    class Meta:
        verbose_name = 'سرباز'
        verbose_name_plural = 'سربازان'

    def __str__(self):
        rank = self.get_rank_display()
        return f'{rank} وظیفه {self.first_name} {self.last_name}'

