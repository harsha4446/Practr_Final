from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
import datetime

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, phoneno):
        if not email:
            raise ValueError("No username entered")
        email = self.normalize_email(email)
        new_user = self.model(email=email,name=name, phoneno=phoneno)
        new_user.set_password(password)
        new_user.is_staff=False
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email, password, name, phoneno):
        if not email:
            raise ValueError("No username entered")
        email = self.normalize_email(email)
        new_user = self.model(email=email,name=name, phoneno=phoneno)
        new_user.set_password(password)
        new_user.is_staff = True
        new_user.is_superuser = True
        new_user.save(using=self._db)
        return new_user


def upload_loction(object, filename):
    return "%s/%s" %(object.email , filename)


class student(AbstractBaseUser):
    email = models.EmailField(max_length=100,unique=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    judge = models.BooleanField(default=False)
    college = models.BooleanField(default=False)
    club = models.BooleanField(default=False)
    about = models.CharField(max_length=500,default='', blank=True)
    dob = models.DateField(default=datetime.date.today)
    experience = models.PositiveSmallIntegerField(default=0)
    location = models.CharField(max_length=100, default='', blank=True)
    profile_picture = models.ImageField(upload_to=upload_loction,null=True,blank=True, default='default/new_logo.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phoneno']
    objects=CustomUserManager()

    def get_absolute_url(self):
        return "/user/%s/" %self.email

    def get_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_phoneno(self):
        return self.phoneno

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def email_user(self,subject,message,from_mail=None):
        send_mail(subject,message,from_mail,[self.email])


class student_scores(models.Model):
    username=models.OneToOneField(student,on_delete=models.CASCADE)
    creativity = models.IntegerField(default=0)
    content = models.IntegerField(default=0)
    presentation = models.IntegerField(default=0)
    rebuttal = models.IntegerField(default=0)
    communication = models.IntegerField(default=0)
    feasibility = models.IntegerField(default=0)
    feedback = models.CharField(max_length=1000, default='')
    question1 = models.IntegerField(default=0)
    question2 = models.IntegerField(default=0, blank=True)
    question3 = models.IntegerField(default=0, blank=True)
    question4 = models.IntegerField(default=0, blank=True)
    question5 = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class student_detail(models.Model):
    email = models.OneToOneField(student, on_delete=models.CASCADE, primary_key=True)
    label = models.CharField(max_length=50,default='')
    degree = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=150, default='')
    year = models.CharField(max_length=10, choices=(('First', 'First'),
                                                    ('Second', 'Second'),
                                                    ('Third', 'Third')),
                            default='First')
    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label

    def __college(self):
        return self.college


class judge_detail(models.Model):
    email = models.OneToOneField(student, on_delete=models.CASCADE, primary_key=True)
    label = models.CharField(max_length=50, default='')
    degree = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    designation = models.CharField(max_length=100,default='')
    industry_exp = models.PositiveSmallIntegerField(default=0)
    college = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label


class interests(models.Model):
    email = models.OneToOneField(student, on_delete=models.CASCADE, primary_key= True)
    label = models.CharField(max_length=50, default='')
    marketing = models.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    public_relations = models.BooleanField(default=False)
    human_resources = models.BooleanField(default=False)
    ent_dev = models.BooleanField(default=False)
    business_quiz = models.BooleanField(default=False)


    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label


class colleges(models.Model):
    email = models.OneToOneField(student,on_delete=models.CASCADE, primary_key=True,default='')
    address = models.CharField(max_length=350, default='')
    college_name = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=10, default='')


    def __str__(self):
        return self.college_name

    def __unicode__(self):
        return self.college_name


class clubs(models.Model):
    email = models.ForeignKey(colleges, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=100,default='')
    admin_name = models.CharField(max_length=100,default='')
    club_email = models.CharField(max_length=100,default='', unique=True)
    phone = models.CharField(max_length=10, default='')
    video = models.CharField(max_length=250, default='')
    website = models.CharField(max_length=250, default='')
    about = models.CharField(max_length=1000, default='')
    logo = models.ImageField(upload_to=upload_loction,null=True,blank=True, default='default/club_default.jpg')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class events(models.Model):
    email = models.ForeignKey(clubs, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=150, default='')
    registration = models.BooleanField(default=False)
    about = models.CharField(max_length=1000, default='')
    website = models.CharField(max_length=250, default='')
    logo = models.ImageField(upload_to=upload_loction,null=True,blank=True,default='default/club_default.jpg')
    inter_type = models.BooleanField(default=False)
    team_size = models.IntegerField(default=1)
    marketing = models.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    public_relations = models.BooleanField(default=False)
    human_resources = models.BooleanField(default=False)
    ent_dev = models.BooleanField(default=False)
    business_quiz = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class rounds(models.Model):
    email = models.ForeignKey(events, on_delete=models.CASCADE, default='')
    ext_judge = models.BooleanField(default=False)
    title = models.CharField(max_length=150, default='')
    sub_title = models.CharField(max_length=150, default='')
    about = models.CharField(max_length=1000, default='')
    task1 = models.CharField(max_length=150, default='')
    task2 = models.CharField(max_length=150, default='', blank=True)
    tast3 = models.CharField(max_length=150, default='', blank=True)
    task4 = models.CharField(max_length=150, default='', blank=True)
    task5 = models.CharField(max_length=150, default='', blank=True)
    resource1 = models.CharField(max_length=150, default='')
    resource2 = models.CharField(max_length=150, default='', blank=True)
    resource3 = models.CharField(max_length=150, default='', blank=True)
    resource4 = models.CharField(max_length=150, default='', blank=True)
    resource5 = models.CharField(max_length=150, default='', blank=True)
    creativity = models.BooleanField(default=False)
    content = models.BooleanField(default=False)
    presentation = models.BooleanField(default=False)
    rebuttal = models.BooleanField(default=False)
    communication = models.BooleanField(default=False)
    feasibility = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    question1 = models.CharField(max_length=150, default='')
    question2 = models.CharField(max_length=150, default='', blank=True)
    question3 = models.CharField(max_length=150, default='', blank=True)
    question4 = models.CharField(max_length=150, default='', blank=True)
    question5 = models.CharField(max_length=150, default='', blank=True)
    type = models.IntegerField(default=0)
    created = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class follow_table(models.Model):
    connected_to = models.ManyToManyField(student)
    current_user = models.ForeignKey(student, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        follow, created = cls.objects.get_or_create(current_user=current_user)
        follow.connected_to.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        follow, created = cls.objects.get_or_create(current_user=current_user)
        follow.connected_to.remove(new_friend)

    def __str__(self):
        return '%s' % self.current_user.email

    def __unicode__(self):
        return '%s' % self.current_user.email


class register_table(models.Model):
    registered_to = models.ManyToManyField(clubs)
    current_user = models.ForeignKey(student, related_name='following', null=True)

    @classmethod
    def register(cls, current_user, registered_to):
        follow, created = cls.objects.get_or_create(current_user=current_user)
        follow.registered_to.add(registered_to)

    @classmethod
    def rmregister(cls, current_user, registered_to):
        follow, created = cls.objects.get_or_create(current_user=current_user)
        follow.registered_to.remove(registered_to)

    def __str__(self):
        return '%s' % self.current_user.email

    def __unicode__(self):
        return '%s' % self.current_user.email