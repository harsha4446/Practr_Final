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


def round_data(object, filename):
    return "%s/%s" %(object.student.email , filename)


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
    location = models.CharField(max_length=100, blank=True, choices=(('Bangalore', 'Bangalore'),
                                                                     ('Mysore', 'Mysore')),
                            default='')
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
    question1 = models.IntegerField(default=0)
    question2 = models.IntegerField(default=0, blank=True)
    question3 = models.IntegerField(default=0, blank=True)
    question4 = models.IntegerField(default=0, blank=True)
    question5 = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.username.email

    def __unicode__(self):
        return self.username.email


class student_detail(models.Model):
    email = models.OneToOneField(student, on_delete=models.CASCADE, primary_key=True)
    label = models.CharField(max_length=50,default='')
    degree = models.CharField(max_length=100, default='', choices=(('B.COM', 'B.COM'),
                                                        ('BBA', 'BBA')),)
    college = models.CharField(max_length=150, default='')
    year = models.CharField(max_length=10, choices=(('First', 'First'),
                                                    ('Second', 'Second'),
                                                    ('Third', 'Third')),
                            default='First')
    section = models.CharField(default='',max_length=10)

    def __str__(self):
        return self.label

    def __unicode__(self):
        return self.label

    def __college(self):
        return self.college


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
    college_name = models.CharField(max_length=200,choices=(('Christ University B.COM', 'Christ University B.COM'),
                                                    ('Christ University D.M.S', 'Christ University D.M.S'),
                                                    ('Christ University D.P.S', 'Christ University D.P.S'),
                                                    ('Jain University SCS', 'Jain University SCS'),
                                                    ('Jain University CMS', 'Jain University CMS'),
                                                    ('Mount Carmel B.COM', 'Mount Carmel B.COM'),
                                                    ('Mount Carmel BBA', 'Mount Carmel BBA'),
                                                    ('St.Josephs B.COM', 'St.Josephs B.COM')),

                            default='')
    phone = models.CharField(max_length=10, default='')
    logo = models.ImageField(upload_to=upload_loction,null=True,blank=True, default='default/new_logo.png')


    def __str__(self):
        return self.college_name

    def __unicode__(self):
        return self.college_name


class clubs(models.Model):
    email = models.ForeignKey(colleges, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=100,default='Dummy')
    college = models.CharField(max_length=150, default='')
    admin_name = models.CharField(max_length=100,default='')
    club_email = models.CharField(max_length=100,default='', unique=True)
    phone = models.CharField(max_length=10, default='')
    video = models.CharField(max_length=250, default='')
    website = models.CharField(max_length=250, default='')
    about = models.CharField(max_length=400, default='')
    logo = models.ImageField(upload_to=upload_loction,null=True,blank=True, default='default/club_default.jpg')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class events(models.Model):
    email = models.ForeignKey(clubs, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=150, default='')
    live = models.BooleanField(default=False)
    registration = models.BooleanField(default=False)
    about = models.CharField(max_length=400, default='')
    website = models.CharField(max_length=250, default='')
    logo = models.ImageField(upload_to=upload_loction,null=True,blank=True,default='default/club_default.jpg')
    inter_type = models.BooleanField(default=False)
    marketing = models.BooleanField(default=False)
    team_size1 = models.IntegerField(default=1)
    subhead1 = models.BooleanField(default=False)
    quota11 = models.IntegerField(default=400)
    quota12 = models.IntegerField(default=400)
    quota13 = models.IntegerField(default=400)
    registered11 = models.IntegerField(default=0)
    registered12 = models.IntegerField(default=0)
    registered13 = models.IntegerField(default=0)
    finance = models.BooleanField(default=False)
    subhead2 = models.BooleanField(default=False)
    team_size2 = models.IntegerField(default=1)
    quota21 = models.IntegerField(default=400)
    quota22 = models.IntegerField(default=400)
    quota23 = models.IntegerField(default=400)
    registered21 = models.IntegerField(default=0)
    registered22 = models.IntegerField(default=0)
    registered23 = models.IntegerField(default=0)
    public_relations = models.BooleanField(default=False)
    subhead3 = models.BooleanField(default=False)
    team_size3 = models.IntegerField(default=1)
    quota31 = models.IntegerField(default=400)
    quota32 = models.IntegerField(default=400)
    quota33 = models.IntegerField(default=400)
    registered31 = models.IntegerField(default=0)
    registered32 = models.IntegerField(default=0)
    registered33 = models.IntegerField(default=0)
    human_resources = models.BooleanField(default=False)
    subhead4 = models.BooleanField(default=False)
    team_size4 = models.IntegerField(default=1)
    quota41 = models.IntegerField(default=400)
    quota42 = models.IntegerField(default=400)
    quota43 = models.IntegerField(default=400)
    registered41 = models.IntegerField(default=0)
    registered42 = models.IntegerField(default=0)
    registered43 = models.IntegerField(default=0)
    ent_dev = models.BooleanField(default=False)
    subhead5 = models.BooleanField(default=False)
    team_size5 = models.IntegerField(default=1)
    quota51 = models.IntegerField(default=400)
    quota52 = models.IntegerField(default=400)
    quota53 = models.IntegerField(default=400)
    registered51 = models.IntegerField(default=0)
    registered52 = models.IntegerField(default=0)
    registered53 = models.IntegerField(default=0)
    best_manager = models.BooleanField(default=False)
    subhead6 = models.BooleanField(default=False)
    team_size6 = models.IntegerField(default=1)
    quota61 = models.IntegerField(default=400)
    quota62 = models.IntegerField(default=400)
    quota63 = models.IntegerField(default=400)
    registered61 = models.IntegerField(default=0)
    registered62 = models.IntegerField(default=0)
    registered63 = models.IntegerField(default=0)
    current = models.BooleanField(default=True)
    multiregistration = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class rounds(models.Model):
    email = models.ForeignKey(events, default='')
    club = models.ForeignKey(clubs, default='')
    ext_judge = models.BooleanField(default=False)
    title = models.CharField(max_length=150, default='')
    sub_title = models.CharField(max_length=150, default='')
    about = models.CharField(max_length=400, default='')
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
    core1 = models.IntegerField(choices=((1, 'Marketing'),(2, 'Finance'),(3, 'Public Relations'),
                                         (4,'Human Resources'),(5,'Entrpreneur and Development'),(6,'Best Manager')),default=8)
    question2 = models.CharField(max_length=150, default='', blank=True)
    core2 = models.IntegerField(choices=((1, 'Marketing'),(2, 'Finance'),(3, 'Public Relations'),
                                         (4,'Human Resources'),(5,'Entrpreneur and Development'),(6,'Best Manager')),default=8)
    question3 = models.CharField(max_length=150, default='', blank=True)
    core3 = models.IntegerField(choices=((1, 'Marketing'),(2, 'Finance'),(3, 'Public Relations'),
                                         (4,'Human Resources'),(5,'Entrpreneur and Development'),(6,'Best Manager')),default=8)
    question4 = models.CharField(max_length=150, default='', blank=True)
    core4 = models.IntegerField(choices=((1, 'Marketing'),(2, 'Finance'),(3, 'Public Relations'),
                                         (4,'Human Resources'),(5,'Entrpreneur and Development'),(6,'Best Manager')),default=8)
    question5 = models.CharField(max_length=150, default='', blank=True)
    core5 = models.IntegerField(choices=((1, 'Marketing'),(2, 'Finance'),(3, 'Public Relations'),
                                         (4,'Human Resources'),(5,'Entrpreneur and Development'),(6,'Best Manager')),default=8)
    type = models.IntegerField(default=0)
    created = models.DateField(default=datetime.date.today)
    published = models.BooleanField(default=False)
    team_size = models.IntegerField(default=1)
    deadline = models.DateField(default=None, null=True)
    creativityvalue = models.IntegerField(default=0)
    contentvalue = models.IntegerField(default=0)
    presentationvalue = models.IntegerField(default=0)
    rebuttalvalue = models.IntegerField(default=0)
    communicationvalue = models.IntegerField(default=0)
    feasibilityvalue = models.IntegerField(default=0)
    qualified = models.IntegerField(default=2)
    weight = models.FloatField(default=1.0)
    finished = models.BooleanField(default=False)
    enddate = models.DateField(default=None, null=True)
    author = models.CharField(max_length=100, default=0)
    offline = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

#student to student
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


#student to club
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


#student to event
class event_registered(models.Model):
    registered_to = models.ManyToManyField(events)
    current_user = models.ForeignKey(student, related_name='registered', null=True)

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
        return '%s' % self.registered_to.name


class event_registered_details(models.Model):
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    event = models.ForeignKey(events,on_delete=models.CASCADE)
    marketing = models.BooleanField(default=0)
    finance = models.BooleanField(default=0)
    public_relations = models.BooleanField(default=0)
    best_manager = models.BooleanField(default=0)
    ent_dev = models.BooleanField(default=0)
    human_resources = models.BooleanField(default=0)
    teammate1 = models.CharField(default='', blank=True, max_length=150)
    teammate2 = models.CharField(default='', blank=True, max_length=150)
    teammate3 = models.CharField(default='', blank=True, max_length=150)


    def __str__(self):
        return '%s' % self.student.email


    def __unicode__(self):
        return '%s' % self.student.email


#per round scores and data
class round_scores(models.Model):
    round = models.ForeignKey(rounds, related_name='round_score', on_delete=models.CASCADE)
    student = models.ForeignKey(student)
    question1 = models.IntegerField(default=0, blank=True, null=True)
    question2 = models.IntegerField(default=0, blank=True, null=True)
    question3 = models.IntegerField(default=0, blank=True, null=True)
    question4 = models.IntegerField(default=0, blank=True, null=True)
    question5 = models.IntegerField(default=0, blank=True, null=True)
    creativity = models.IntegerField(default=0, blank=True, null=True)
    content = models.IntegerField(default=0, blank=True, null=True)
    presentation = models.IntegerField(default=0, blank=True, null=True)
    rebuttal = models.IntegerField(default=0, blank=True, null=True)
    communication = models.IntegerField(default=0, blank=True, null=True)
    feasibility = models.IntegerField(default=0, blank=True, null=True)
    feedback = models.CharField(default='Not Available', max_length=600, null=True)
    submitted = models.BooleanField(default=False)
    judged = models.BooleanField(default=False)
    data1 = models.FileField(upload_to=round_data, null=True)
    data2 = models.FileField(upload_to=round_data, null=True)
    data3 = models.FileField(upload_to=round_data, null=True)
    total = models.IntegerField(default=0)
    qualified = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.student.email

    def __unicode__(self):
        return '%s' % self.student.email


class round_room(models.Model):
    round = models.ForeignKey(rounds,on_delete=models.CASCADE)
    room = models.SmallIntegerField(default=1)

    def __str__(self):
        return '%s' % self.round.title

    def __unicode__(self):
        return '%s' % self.round.title


class room_judge(models.Model):
    round = models.ForeignKey(rounds, on_delete=models.CASCADE, default='')
    room = models.ForeignKey(round_room, on_delete=models.CASCADE, default='')
    judge_email = models.CharField(max_length=100, default='')
    judge_password = models.CharField(max_length=25, default='')

    def __str__(self):
        return '%s' % self.judge_email

    def __unicode__(self):
        return '%s' % self.judge_email


class judge_detail(models.Model):
    email = models.OneToOneField(student, on_delete=models.CASCADE, primary_key=True)
    club = models.ForeignKey(clubs,default='')
    type = models.IntegerField(default=0)
    degree = models.CharField(max_length=100, default='')
    website = models.CharField(default='', max_length=500)
    designation = models.CharField(max_length=100,default='')
    industry_exp = models.IntegerField(default=0)
    college = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.email.email

    def __unicode__(self):
        return self.email.email


class sub_head(models.Model):
    student = models.OneToOneField(student)
    type = models.IntegerField(default=0)

    def __str__(self):
        return self.student.email

    def __unicode__(self):
        return self.student.email




