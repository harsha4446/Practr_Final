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
    return "%s/%s" %(object.name , filename)


def upload_loction_college(object, filename):
    return "%s/%s" %(object.college_name , filename)


def round_data(object, filename):
    return "%s/%s" %(object.student.name , filename)


def case_data(object, filename):
    return "%s/%s" %(object.title , filename)


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
    about = models.CharField(max_length=1000,default='', blank=True)
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
    creativity = models.IntegerField(default=1)
    content = models.IntegerField(default=1)
    presentation = models.IntegerField(default=1)
    rebuttal = models.IntegerField(default=1)
    communication = models.IntegerField(default=1)
    feasibility = models.IntegerField(default=1)
    question1 = models.IntegerField(default=0, blank=True)
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
                                                        ('BBA', 'BBA'),
                                                        ('BMS', 'BMS'),
                                                        ('Other','Other')),)
    college = models.CharField(max_length=150, default='')
    year = models.CharField(max_length=10, choices=(('First', 'First'),
                                                    ('Second', 'Second'),
                                                    ('Third', 'Third')),
                            default='First')
    section = models.CharField(default='',max_length=10)

    def __str__(self):
        return '%s-%s' % (self.email.email, self.college)

    def __unicode__(self):
        return self.email.email

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
    best_manager = models.BooleanField(default=False)

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
                                                    ('Christ University, Bannerghatta', 'Christ University, Bannerghatta'),
                                                    ('Presidency College','Presidency College'),
                                                    ('Jain University SCS', 'Jain University SCS'),
                                                    ('Jain University CMS', 'Jain University CMS'),
                                                    ('Mount Carmel B.COM', 'Mount Carmel B.COM'),
                                                    ('Mount Carmel BBA', 'Mount Carmel BBA'),
                                                    ('St.Josephs B.COM', 'St.Josephs B.COM'),
                                                    ('Kristu Jayanti College B.COM', 'Kristu Jayanti College  B.COM'),
                                                    ('Kristu Jayanti College BBA','Kristu Jayanti College BBA'),
                                                    ('KLE CBALC Belgaum', 'KLE CBALC Belgaum'),
                                                    ('Bishop Cotton Womens College', 'Bishop Cotton Womens College'),
                                                    ('Garden City College', 'Garden City College'),
                                                    ('Trinity College of Commerce', 'Trinity College of Commerce'),
                                                    ('Manipal University DOC', 'Manipal University DOC'),
                                                    ('Vidhyaashram FGC', 'Vidhyaashram FGC')),
                                                    default='')
    phone = models.CharField(max_length=10, default='')
    logo = models.ImageField(upload_to=upload_loction_college,null=True,blank=True, default='default/new_logo.png')


    def __str__(self):
        return self.college_name

    def __unicode__(self):
        return self.college_name


class clubs(models.Model):
    email = models.ForeignKey(colleges, on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=100,default='')
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
    about = models.CharField(max_length=1000, default='')
    website = models.CharField(max_length=250, default='')
    logo = models.ImageField(upload_to=upload_loction,null=True,blank=True,default='default/club_default.jpg')
    inter_type = models.BooleanField(default=False)
    marketing = models.BooleanField(default=False)
    mktlabel = models.CharField(default="Marketing",max_length=20)
    team_size1 = models.IntegerField(default=1)
    subhead1 = models.BooleanField(default=False)
    quota11 = models.IntegerField(default=100)
    quota12 = models.IntegerField(default=100)
    quota13 = models.IntegerField(default=100)
    registered11 = models.IntegerField(default=0)
    registered12 = models.IntegerField(default=0)
    registered13 = models.IntegerField(default=0)
    finance = models.BooleanField(default=False)
    finlabel = models.CharField(default="Finance",max_length=20)
    subhead2 = models.BooleanField(default=False)
    team_size2 = models.IntegerField(default=1)
    quota21 = models.IntegerField(default=100)
    quota22 = models.IntegerField(default=100)
    quota23 = models.IntegerField(default=100)
    registered21 = models.IntegerField(default=0)
    registered22 = models.IntegerField(default=0)
    registered23 = models.IntegerField(default=0)
    public_relations = models.BooleanField(default=False)
    prlabel = models.CharField(default="Public Relations",max_length=20)
    subhead3 = models.BooleanField(default=False)
    team_size3 = models.IntegerField(default=1)
    quota31 = models.IntegerField(default=100)
    quota32 = models.IntegerField(default=100)
    quota33 = models.IntegerField(default=100)
    registered31 = models.IntegerField(default=0)
    registered32 = models.IntegerField(default=0)
    registered33 = models.IntegerField(default=0)
    human_resources = models.BooleanField(default=False)
    hrlabel = models.CharField(default="Human Resource",max_length=20)
    subhead4 = models.BooleanField(default=False)
    team_size4 = models.IntegerField(default=1)
    quota41 = models.IntegerField(default=100)
    quota42 = models.IntegerField(default=100)
    quota43 = models.IntegerField(default=100)
    registered41 = models.IntegerField(default=0)
    registered42 = models.IntegerField(default=0)
    registered43 = models.IntegerField(default=0)
    ent_dev = models.BooleanField(default=False)
    edlabel = models.CharField(default="Entrepreneurship Development",max_length=20)
    subhead5 = models.BooleanField(default=False)
    team_size5 = models.IntegerField(default=1)
    quota51 = models.IntegerField(default=100)
    quota52 = models.IntegerField(default=100)
    quota53 = models.IntegerField(default=100)
    registered51 = models.IntegerField(default=0)
    registered52 = models.IntegerField(default=0)
    registered53 = models.IntegerField(default=0)
    best_manager = models.BooleanField(default=False)
    bmlabel = models.CharField(default="Best Manager",max_length=20)
    subhead6 = models.BooleanField(default=False)
    team_size6 = models.IntegerField(default=1)
    quota61 = models.IntegerField(default=100)
    quota62 = models.IntegerField(default=100)
    quota63 = models.IntegerField(default=100)
    registered61 = models.IntegerField(default=0)
    registered62 = models.IntegerField(default=0)
    registered63 = models.IntegerField(default=0)
    corp_strg = models.BooleanField(default=False)
    cslabel = models.CharField(default="Corporate Strategy",max_length=20)
    subhead7 = models.BooleanField(default=False)
    team_size7 = models.IntegerField(default=1)
    quota71 = models.IntegerField(default=100)
    quota72 = models.IntegerField(default=100)
    quota73 = models.IntegerField(default=100)
    registered71 = models.IntegerField(default=0)
    registered72 = models.IntegerField(default=0)
    registered73 = models.IntegerField(default=0)
    quiz = models.BooleanField(default=False)
    qulabel = models.CharField(default="Quiz", max_length=20)
    subhead8 = models.BooleanField(default=False)
    team_size8 = models.IntegerField(default=1)
    quota81 = models.IntegerField(default=100)
    quota82 = models.IntegerField(default=100)
    quota83 = models.IntegerField(default=100)
    registered81 = models.IntegerField(default=0)
    registered82 = models.IntegerField(default=0)
    registered83 = models.IntegerField(default=0)
    team = models.BooleanField(default=False)
    telabel = models.CharField(default="Team",max_length=20)
    subhead9 = models.BooleanField(default=False)
    team_size9 = models.IntegerField(default=1)
    quota91 = models.IntegerField(default=100)
    quota92 = models.IntegerField(default=100)
    quota93 = models.IntegerField(default=100)
    registered91 = models.IntegerField(default=0)
    registered92 = models.IntegerField(default=0)
    registered93 = models.IntegerField(default=0)
    current = models.BooleanField(default=True)
    multiregistration = models.BooleanField(default=False)
    firstyear = models.BooleanField(default=True)
    secondyear = models.BooleanField(default=True)
    thirdyear = models.BooleanField(default=True)
    prefix = models.CharField(max_length=4,default='',null=True,blank=True)
    tprefix = models.CharField(max_length=4,default='',null=True,blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class rounds(models.Model):
    email = models.ForeignKey(events, default='')
    club = models.ForeignKey(clubs, default='')
    ext_judge = models.BooleanField(default=False)
    title = models.CharField(max_length=150, default='')
    sub_title = models.CharField(max_length=150, default='',blank=True)
    about = models.CharField(max_length=60000, default='', blank=True)
    task1 = models.CharField(max_length=500, default='',blank=True)
    task2 = models.CharField(max_length=500, default='', blank=True)
    tast3 = models.CharField(max_length=500, default='', blank=True)
    task4 = models.CharField(max_length=500, default='', blank=True)
    task5 = models.CharField(max_length=500, default='', blank=True)
    resource1 = models.CharField(max_length=200, default='',blank=True)
    resource2 = models.CharField(max_length=200, default='', blank=True)
    resource3 = models.CharField(max_length=200, default='', blank=True)
    resource4 = models.CharField(max_length=200, default='', blank=True)
    resource5 = models.CharField(max_length=200, default='', blank=True)
    resource1data = models.FileField(upload_to=case_data, null=True, blank=True)
    resource2data = models.FileField(upload_to=case_data, null=True, blank=True)
    resource3data = models.FileField(upload_to=case_data, null=True, blank=True)
    resource4data = models.FileField(upload_to=case_data, null=True, blank=True)
    resource5data = models.FileField(upload_to=case_data, null=True, blank=True)
    creativity = models.BooleanField(default=False)
    content = models.BooleanField(default=False)
    presentation = models.BooleanField(default=False)
    rebuttal = models.BooleanField(default=False)
    communication = models.BooleanField(default=False)
    feasibility = models.BooleanField(default=False)
    feedback = models.BooleanField(default=False)
    question1 = models.CharField(max_length=500, default='',blank=True,null=True)
    core1 = models.IntegerField(default=0,blank=True,null=True)
    question2 = models.CharField(max_length=500, default='', blank=True,null=True)
    core2 = models.IntegerField(default=0,blank=True,null=True)
    question3 = models.CharField(max_length=500, default='', blank=True,null=True)
    core3 = models.IntegerField(default=0,blank=True,null=True)
    question4 = models.CharField(max_length=500, default='', blank=True,null=True)
    core4 = models.IntegerField(default=0,blank=True,null=True)
    question5 = models.CharField(max_length=500, default='', blank=True,null=True)
    core5 = models.IntegerField(default=0,blank=True,null=True)
    # core1 = models.IntegerField(choices=((1, 'Marketing'), (2, 'Finance'), (3, 'Public Relations'),
    #                                         (4,'Human Resources'),(5,'Entrpreneur and Development'),(6,'Best Manager')),default=1,null=True)
    type = models.IntegerField(default=0)
    created = models.DateField(default=datetime.date.today)
    published = models.BooleanField(default=False)
    team_size = models.IntegerField(default=1)
    deadline = models.DateTimeField(default=None, null=True,)
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
    offline = models.CharField(default='0',max_length=1)
    max_score = models.IntegerField(default=100)

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
    student = models.ForeignKey(student)
    event = models.ForeignKey(events,on_delete=models.CASCADE)
    regmarketing = models.BooleanField(default=0)
    regfinance = models.BooleanField(default=0)
    regpublic_relations = models.BooleanField(default=0)
    regbest_manager = models.BooleanField(default=0)
    regent_dev = models.BooleanField(default=0)
    reghuman_resources = models.BooleanField(default=0)
    regcorp_strg = models.BooleanField(default=0)
    regquiz = models.BooleanField(default=0)
    regteam = models.BooleanField(default=0)
    marketing = models.BooleanField(default=0)
    finance = models.BooleanField(default=0)
    public_relations = models.BooleanField(default=0)
    best_manager = models.BooleanField(default=0)
    ent_dev = models.BooleanField(default=0)
    human_resources = models.BooleanField(default=0)
    corp_strg = models.BooleanField(default=0)
    quiz = models.BooleanField(default=0)
    team = models.BooleanField(default=0)
    rcode = models.CharField(default='',max_length=10)
    mkttotal = models.FloatField(default=0)
    fintotal = models.FloatField(default=0)
    prtotal = models.FloatField(default=0)
    hrtotal = models.FloatField(default=0)
    edtotal = models.FloatField(default=0)
    bmtotal = models.FloatField(default=0)
    cstotal = models.FloatField(default=0)
    qutotal = models.FloatField(default=0)
    tetotal = models.FloatField(default=0)

    def __str__(self):
        college = student_detail.objects.get(email=self.student)
        return '%s-%s' % (self.student.email,college.college)


    def __unicode__(self):
        return '%s' % self.student.email


class teams(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)
    club = models.ForeignKey(clubs,default=None, null=True)
    student = models.ForeignKey(student,default=None, null=True)
    tcode = models.CharField(default='', max_length=10)


    def __str__(self):
        return '%s-%s' % (self.event.name, self.club.name)


    def __unicode__(self):
        return '%s' % self.event.name

#per round scores and data
class round_scores(models.Model):
    round = models.ForeignKey(rounds, related_name='round_score', on_delete=models.CASCADE)
    student = models.ForeignKey(student)
    question1 = models.FloatField(default=0, blank=True, null=True)
    question2 = models.FloatField(default=0, blank=True, null=True)
    question3 = models.FloatField(default=0, blank=True, null=True)
    question4 = models.FloatField(default=0, blank=True, null=True)
    question5 = models.FloatField(default=0, blank=True, null=True)
    creativity = models.FloatField(default=0, blank=True, null=True)
    content = models.FloatField(default=0, blank=True, null=True)
    presentation = models.FloatField(default=0, blank=True, null=True)
    rebuttal = models.FloatField(default=0, blank=True, null=True)
    communication = models.FloatField(default=0, blank=True, null=True)
    feasibility = models.FloatField(default=0, blank=True, null=True)
    feedback = models.CharField(default='No Feedback Available', max_length=2000, null=True)
    submitted = models.BooleanField(default=False)
    judged = models.BooleanField(default=False)
    judged_value = models.IntegerField(default=0)
    data1 = models.FileField(upload_to=round_data, null=True, blank=True)
    data2 = models.FileField(upload_to=round_data, null=True, blank=True)
    data3 = models.FileField(upload_to=round_data, null=True, blank=True)
    total = models.FloatField(default=0)
    qualified = models.BooleanField(default=True)
    late = models.BooleanField(default=False)
    submission_time = models.DateTimeField(blank=True,null=True)
    rcode = models.CharField(default='',max_length=10)

    def __str__(self):
        return '%s-%s' % (self.student.email, self.round.title)

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
    degree = models.CharField(max_length=100, default='',blank=True,null=True)
    website = models.CharField(default='', max_length=500,blank=True,null=True)
    designation = models.CharField(max_length=100,default='',blank=True,null=True)
    industry_exp = models.IntegerField(default=0)
    college = models.CharField(max_length=150, default='',blank=True,null=True)

    def __str__(self):
        return self.email.email

    def __unicode__(self):
        return self.email.email


class sub_head(models.Model):
    student = models.OneToOneField(student)
    event = models.ForeignKey(events,on_delete=models.CASCADE)
    type = models.IntegerField(default=0)

    def __str__(self):
        return self.student.email

    def __unicode__(self):
        return self.student.email




