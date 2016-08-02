from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from django.db import models
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('photo', filename)

def get_file_paths(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('agencylogo', filename)

TYPE = (
	('1', 'No Preference'),
	('2', 'Fresh Maid'),
	('3', 'Experienced Maid'),
	('4', 'Transfer Maid'),
)

NATIONALITY = (
	('1', 'No Preference'),
	('2', 'Singapore'),
	('3', 'Malaysia'),
)

MSTATUS = (
	('1', 'No Preference'),
	('2', 'Single'),
	('3', 'Married'),
	('4', 'Divorced'),
	('5', 'Separated'),
)
CARING = (
	('1', 'No Preference'),
	('2', 'Canlearn'),
	('3', 'Poor'),
	('4', 'Average'),
	('5', 'Good'),
	('6', 'Very Good'),
	('7', 'Excellent'),
)

DIETRY = (
	('1', 'No Preference'),
	('2', 'Vegetarian'),
	('3', 'Non Vegetarian'),
	('4', 'Both'),
)

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class Agency(models.Model):
	"""
	A Model to store Agency.
	"""
	user = models.OneToOneField(User)
	agency_name = models.CharField(max_length=128, help_text="Agency Company Name")
	licence_no = models.CharField(max_length=128, help_text="Agency Licence Name")
	logo = models.ImageField(upload_to='agency_logos', null=True, blank=True)
	address = models.TextField(blank=True, null=True)
	office_no = models.CharField(max_length=16, help_text="Agency")
	fax = models.CharField(max_length=16, null=True, blank=True, help_text="Agency")
	contact_person = models.CharField(max_length=128, null=True, blank=True, help_text="Agency Contact Person Name")
	email = models.CharField(max_length=128, null=True, blank=True, help_text="Agency Contact E-mail Address")
	mobile = models.CharField(max_length=16, null=True, blank=True, help_text="Agency")
	second_contact_person = models.CharField(max_length=128, null=True, blank=True, help_text="Agency second Contact person Name")
	second_mobile_no = models.CharField(max_length=16, null=True, blank=True, help_text="Agency")
	second_Email = models.CharField(max_length=128, null=True, blank=True, help_text="Agency Contact E-mail Address")
	website = models.CharField(max_length=200, null=True, blank=True, help_text="Actor Website URL")
	office_hours = models.CharField(max_length=128, blank=True, help_text="Agency Company Name")
	description = models.TextField(blank=True, null=True)
	is_active = models.BooleanField(default=False, help_text="Agency profice active")
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.agency_name) if str(self.agency_name) else ''

	class Meta:
		db_table = "Agency"
		verbose_name = "Agency"
		verbose_name_plural = "Agency"


class MaidOld(models.Model):
	"""
	Maid Details
	"""
	agency = models.ForeignKey(Agency)
	name = models.CharField(max_length = 100, help_text="Maid Full Name")
	image = models.FileField(upload_to='maid_photo', null=True, blank=True)
	image1 = models.FileField(upload_to='maid_photo', null=True, blank=True)
	image2 = models.FileField(upload_to='maid_photo', null=True, blank=True)
	types = models.CharField(max_length=100, null=True, blank=True)
	nationality = models.CharField(max_length=150, null=True, blank=True)
	dob = models.DateField(blank=True, editable=True, null=True, help_text="For first-time applicants: Aged 23 years or above, and below 50 years old at the time of the Work Permit application.")
	birth_place = models.CharField(max_length = 200, help_text="Maid place of birth")
	height = models.CharField(max_length =30, null=True, blank=True, help_text="Height")
	weight = models.CharField(max_length =30, null=True, blank=True, help_text="Weight")
	religion = models.CharField(max_length = 50, help_text="Maid Religion")
	mstatus = models.CharField(default=1, max_length =10, choices=MSTATUS)
	no_of_child = models.CharField(max_length =10, null=True, blank=True, help_text="Number of child")
	no_of_siblings_sis = models.CharField(max_length =10, null=True, blank=True, help_text="Number of sister")
	no_of_siblings_bro = models.CharField(max_length =10, null=True, blank=True, help_text="Number of brothers")
	dietary_restrictions = models.CharField(default=1, max_length =10, choices=DIETRY)
	agepre = models.CharField(max_length =20, null=True, blank=True, help_text="Age preference")
	education = models.CharField(max_length = 50, null=True, blank=True, help_text="Have a minimum eight years of formal education and possesses")
	language1 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	language2 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	language3 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	language4 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	language5 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	expertise1 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	expertise2 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	expertise3 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	expertise4 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	expertise5 = models.CharField(max_length = 50, null=True, blank=True, help_text="Maid known languages")
	pork = models.CharField(max_length = 10, null=True, blank=True, help_text="Able to handle pork?")
	epork = models.CharField(max_length = 10, null=True, blank=True, help_text="Able to eat pork?")
	caredog = models.CharField(max_length = 10, null=True, blank=True, help_text="Able to handle dog?")
	sewing = models.CharField(max_length = 10, null=True, blank=True, help_text="Able to do simple sewing?")
	garden = models.CharField(max_length = 10, null=True, blank=True, help_text="Able to do gardening work?")
	car = models.CharField(max_length = 10, null=True, blank=True, help_text="Willing to wash car?")
	no_offday = models.CharField(max_length = 10, null=True, blank=True, help_text="Number of off-days per month:")
	house = models.CharField(default=1, max_length =30, choices=CARING, null=True, blank=True, help_text="General Housekeeping")
	young = models.CharField(default=1, max_length =30, choices=CARING, help_text="Care for Young Children")
	infant = models.CharField(default=1, max_length =30, choices=CARING, help_text="Care for Infant")
	cook = models.CharField(default=1, max_length =30, choices=CARING, help_text="Cooking")
	elder = models.CharField(default=1, max_length =30, choices=CARING, help_text="Care for Elderly/Disabled")
	home = models.CharField(max_length =50, null=True, default=0, blank=True, help_text="Work Experience in Home Country")
	singapore = models.CharField(max_length =50, null=True, default=0, blank=True, help_text="Work Experience in Singapore")
	malaysia = models.CharField(max_length =50, null=True, default=0, blank=True, help_text="Work Experience in Malaysia")
	hongkong = models.CharField(max_length =50, null=True, default=0, blank=True, help_text="Work Experience in HongKong")
	taiwan = models.CharField(max_length =50, null=True, default=0, blank=True, help_text="Work Experience in Taiwan")
	east = models.CharField(max_length =50, null=True, blank=True, help_text="Work Experience in Middle East")
	other = models.CharField(max_length =50, null=True, blank=True, help_text="Work Experience in Other Countries")
	about = models.TextField(null=True, blank=True, help_text="About Yourself")
	address = models.TextField(null=True, blank=True, help_text="Maid Address")
	age_of_child = models.CharField(max_length =50, null=True, blank=True, help_text="Work Experience in Other Countries")
	video = models.TextField(null=True, blank=True, help_text="You tube video link")
	is_active = models.BooleanField(default=True, help_text="Maid profice active")
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	base_salary = models.CharField(max_length =50, null=True, blank=True, help_text="S$580 with 4 rest days per month")


	def __unicode__(self):
		return str(self.name) if str(self.name) else ''

	class Meta:
		db_table = "Maid Old"
		verbose_name = "Maid Old"
		verbose_name_plural = "Maid Old"


from redactor.fields import RedactorField

class Aboutus(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')

    def __unicode__(self):
		return str(self.title) if str(self.title) else ''

    class Meta:
		db_table = "About Us"
		verbose_name = "About Us"
		verbose_name_plural = "About Us"

class Services(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')

    def __unicode__(self):
		return str(self.title) if str(self.title) else ''

    class Meta:
		db_table = "Services"
		verbose_name = "Services"
		verbose_name_plural = "Services"


class Faq(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')

    def __unicode__(self):
		return str(self.title) if str(self.title) else ''

    class Meta:
		db_table = "FAQ"
		verbose_name = "FAQ"
		verbose_name_plural = "FAQ"


class Home(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    short_text = RedactorField(verbose_name=u'Text')

    def __unicode__(self):
		return str(self.title) if str(self.title) else ''

    class Meta:
		db_table = "Home"
		verbose_name = "Home"
		verbose_name_plural = "Home"


class Logo(models.Model):
    logo = models.ImageField(upload_to='agency_logos', null=True, blank=True)

    class Meta:
		db_table = "Logo"
		verbose_name = "Logo"
		verbose_name_plural = "Logo"

class Banner_Image(models.Model):
    image = models.ImageField(upload_to='banner_images', null=True, blank=True)

    class Meta:
		db_table = "Banner_Image"
		verbose_name = "Banner_Image"
		verbose_name_plural = "Banner_Image"

class ContactForm(models.Model):
	"""
	Contact form from End User
	"""
	name = models.CharField(max_length = 100, help_text="Requester Full Name")
	email = models.CharField(max_length=128, help_text="Contact Person E-mail Address")
	mobile = models.CharField(max_length=16, help_text="Contact Person Phone Number")
	message = models.CharField(max_length=500, null=True, blank=True)

	def __unicode__(self):
		return str(self.name) if str(self.name) else ''



class Maid(models.Model):
    # personal details
    agency = models.ForeignKey(Agency)
    types = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=200, help_text="Maid Full Name")
    base_salary = models.CharField(max_length =300, null=True, blank=True)
    image = models.FileField(upload_to='maid_photo', null=True, blank=True)
    image1 = models.FileField(upload_to='maid_photo', null=True, blank=True)
    image2 = models.FileField(upload_to='maid_photo', null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    birth_place = models.CharField(max_length=200, null=True, blank=True)
    height = models.CharField(max_length =200, null=True, blank=True, help_text="cm")
    weight = models.CharField(max_length =200, null=True, blank=True, help_text="Kg")
    nationality = models.CharField(max_length=150, null=True, blank=True)
    resident = models.TextField(null=True, blank=True)
    repatriat = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    religion = models.CharField(max_length=200, null=True, blank=True)
    education = models.CharField(max_length= 200, null=True, blank=True)
    no_of_sibling = models.CharField(max_length =200, null=True, blank=True, help_text="Number of Sibling")
    mstatus = models.CharField(max_length=200, null=True, blank=True)
    no_of_child = models.CharField(max_length=200, null=True, blank=True, help_text="Number of child")
    age_of_child = models.CharField(max_length =200, null=True, blank=True, help_text="Work Experience in Other Countries")

    # medical details
    allergies = models.CharField(max_length=200, null=True, blank=True)
    illness = models.TextField(blank=True, null=True)
    disabilities = models.CharField(max_length=200, null=True, blank=True)
    dietary_restrictions = models.CharField(max_length=200, null=True, blank=True)
    food_handle = models.TextField(blank=True, null=True)
    food_other = models.CharField(max_length=200,blank=True, null=True)

    # other details
    off_days = models.CharField(max_length=100, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    # skill details
    no_eval = models.BooleanField(default=False)
    sg_eval = models.BooleanField(default=False)
    sg_interview_type = models.TextField(null=True, blank=True)
    sg_children = models.TextField(null=True, blank=True)
    sg_child_age = models.CharField(max_length=200, null=True, blank=True)
    sg_elderly = models.TextField(null=True, blank=True)
    sg_disabled = models.TextField(null=True, blank=True)
    sg_housework = models.TextField(null=True, blank=True)
    sg_cooking = models.TextField(null=True, blank=True)
    sg_cook_cusine = models.CharField(max_length=200, null=True, blank=True)
    sg_language = models.TextField(null=True, blank=True)
    sg_languages = models.CharField(max_length=200, null=True, blank=True)
    sg_other = models.TextField(null=True, blank=True)
    sg_others = models.CharField(max_length=200, null=True, blank=True)

    ov_eval = models.BooleanField(default=False)
    ov_ea_name = models.CharField(max_length=200, null=True, blank=True)
    ov_ea_certify = models.CharField(max_length=200, null=True, blank=True)
    ov_interview_type = models.TextField(null=True, blank=True)
    ov_children = models.TextField(null=True, blank=True)
    ov_child_age = models.CharField(max_length=200, null=True, blank=True)
    ov_elderly = models.TextField(null=True, blank=True)
    ov_disabled = models.TextField(null=True, blank=True)
    ov_housework = models.TextField(null=True, blank=True)
    ov_cooking = models.TextField(null=True, blank=True)
    ov_cook_cusine = models.CharField(max_length=200, null=True, blank=True)
    ov_language = models.TextField(null=True, blank=True)
    ov_languages = models.CharField(max_length=200, null=True, blank=True)
    ov_other = models.TextField(null=True, blank=True)
    ov_others = models.CharField(max_length=200, null=True, blank=True)

    # experience details
    ov_history1 = models.TextField(null=True, blank=True)
    ov_history2 = models.TextField(null=True, blank=True)
    singapore_history = models.BooleanField(default=False)
    feedback1 = models.TextField(null=True, blank=True)
    feedback2 = models.TextField(null=True, blank=True)
    fdw_availability = models.TextField(null=True, blank=True)
    other_remarks = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.name) if str(self.name) else ''

    class Meta:
        db_table = "Maid"
        verbose_name = "Maid"
        verbose_name_plural = "Maid"
