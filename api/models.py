from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

class Member(models.Model):
    user_name = models.CharField(max_length=100 ,  primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    admission_id = models.CharField(max_length=8)
    grade = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone =  models.CharField(max_length=12)
    profile = models.ImageField(upload_to='profiles/', blank=True , default='profiles/default_user.png')
    address = models.CharField(max_length=500)
    birthday = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=10)
    parent_name = models.CharField(max_length=255,default="n")
    parent_phone = models.CharField(max_length=12,default="n")
    parent_adress = models.CharField(max_length=255,default="n")

    def __str__(self):
        return '{}'.format(self.user_name)


class Post(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    just_member = models.BooleanField(default=False);
    president_in_chief = models.BooleanField(default=False)
    vice_president_in_chief = models.BooleanField(default=False)
    Photography_president = models.BooleanField(default=False)
    Photography_vice_president = models.BooleanField(default=False)
    videography_president = models.BooleanField(default=False)
    videography_vice_president = models.BooleanField(default=False)
    technical_president = models.BooleanField(default=False)
    technical_vice_president = models.BooleanField(default=False)
    announcing_president = models.BooleanField(default=False)
    announcing_vice_president = models.BooleanField(default=False)
    reporting_president = models.BooleanField(default=False)
    reporting_vice_president = models.BooleanField(default=False)
    photo_and_video_editing_president = models.BooleanField(default=False)
    photo_and_video_editing_vice_president = models.BooleanField(default=False)
    graphic_designing_president = models.BooleanField(default=False)
    graphic_designing_vice_president = models.BooleanField(default=False)
    web_designing_president = models.BooleanField(default=False)
    web_designing_vice_president = models.BooleanField(default=False)
    promoted = models.DateTimeField()  

    class Meta:
            verbose_name_plural = "Post"

    def __str__(self):
        return '{}'.format(self.user_name)


class Authentication_Info(models.Model):
    member = models.ForeignKey(Member , on_delete=models.CASCADE)
    token = models.CharField(max_length=100)
    is_registered = models.BooleanField(default=False)
    is_verrified = models.BooleanField(default=False)

    class Meta:
            verbose_name_plural = "Authentication_Info"


    def __str__(self):
        return '{}'.format(self.member.user_name)


class DSLR_MirrorLess(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    type_of_cam = models.CharField(max_length=100 , blank=True)
    type_of_lense = models.CharField(max_length=100 , blank=True)
    has_trypod = models.BooleanField(default=False)
    has_flashgun = models.BooleanField(default=False)
    has_ndfilter = models.BooleanField(default=False)
    has_triger = models.BooleanField(default=False)
    has_softbox = models.BooleanField(default=False)
    skil_exp = models.CharField(max_length=3000 , blank=True)

    class Meta:
        verbose_name_plural = "DSLR_MirrorLess"


    def __str__(self):
        return '{}'.format(self.member)

class Arial(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    type_of_drons = models.CharField(max_length=200 , blank=True)
    is_registered = models.BooleanField(default=False)
    skil_exp = models.CharField(max_length=3000 , blank=True)

    class Meta:
            verbose_name_plural = "Arial"

    def __str__(self):
        return '{}'.format(self.member)

        

class Mobile(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    type_of_device = models.CharField(max_length=100 , blank=True)
    skil_exp = models.CharField(max_length=1000 , blank=True)


    def __str__(self):
        return '{}'.format(self.member)


class Photographer(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    is_dslr_mirrorless_photographer = models.BooleanField(default=False)
    is_arial_photographer = models.BooleanField(default=False)
    is_mobile_photographer =models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.member)


class Videographer(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    is_dslr_mirrorless_videographer =  models.BooleanField(default=False)
    is_arial_videographer =  models.BooleanField(default=False)
    is_mobile_videographer = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.member)


class Technician(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    skil_exp = models.CharField(max_length=2000 , blank=True)
    course = models.CharField(max_length=300 , blank=True)

    def __str__(self):
        return '{}'.format(self.member)


class Announcer(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    skil_exp = models.CharField(max_length=2000)
    sinhala_lan = models.BooleanField(default=False)
    english_lan = models.BooleanField(default=False)
    tamil_lan = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.member)


class Reporter(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    skil_exp = models.CharField(max_length=2000)
    sinhala_lan = models.BooleanField(default=False)
    english_lan = models.BooleanField(default=False)
    tamil_lan = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.member)


class Photo_Editor(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    exp_lumina = models.BooleanField(default=False)
    exp_photoshop = models.BooleanField(default=False)
    exp_illustrator = models.BooleanField(default=False)
    exp_bridge = models.BooleanField(default=False)
    other_softwares = models.CharField(max_length=200   , blank=True)
    skil_exp = models.CharField(max_length=3000   , blank=True)

    def __str__(self):
        return '{}'.format(self.member)




class Video_Editor(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    exp_premire = models.BooleanField(default=False)
    exp_after = models.BooleanField(default=False)
    exp_filmora = models.BooleanField(default=False)
    other_softwares = models.CharField(max_length=200  , blank=True)
    skil_exp = models.CharField(max_length=3000  , blank=True)

    def __str__(self):
        return '{}'.format(self.member)


class Graphic_Designer(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    exp_photoshop = models.BooleanField(default=False)
    exp_illustrator = models.BooleanField(default=False)
    exp_coreldraw = models.BooleanField(default=False)
    other_softwares = models.CharField(max_length=200  , blank=True)
    skil_exp = models.CharField(max_length=3000  , blank=True)

    def __str__(self):
        return '{}'.format(self.member)


class Web_Designer(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    skil_exp = models.CharField(max_length=1000  , blank=True)


class Fields(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    photoghaphy = models.BooleanField(default=False)
    videography = models.BooleanField(default=False)
    technical = models.BooleanField(default=False)
    announcing = models.BooleanField(default=False)
    reporting = models.BooleanField(default=False)
    photo_editing = models.BooleanField(default=False)
    video_editing = models.BooleanField(default=False)
    graphic_design = models.BooleanField(default=False)
    web_design = models.BooleanField(default=False)

    class Meta:
            verbose_name_plural = "Fields"

    def __str__(self):
        return '{}'.format(self.member)


class Accessory(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    filed = models.ForeignKey(Fields,on_delete=models.CASCADE)
    accessory = models.ImageField(upload_to='accessories/', blank=True)

    class Meta:
            verbose_name_plural = "Accessories"

    def __str__(self):
        return '{}'.format(self.member)


class Behaviour(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    behaviour_data = models.CharField(max_length=1000)
    is_good = models.BooleanField(default=False)

    class Meta:
            verbose_name_plural = "Behaviour"

    def __str__(self):
        return '{}'.format(self.member)

