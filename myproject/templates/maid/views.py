from django.conf import settings
from django.template.response import TemplateResponse
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.context_processors import csrf
from maid.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date, timedelta
from templated_email import send_templated_mail
from maid.forms import MaidInfoForm
from django.shortcuts import get_object_or_404

def agency_registration(request):
	"""
	Home Page
	"""
	maid = Maid.objects.all()
	if request.method == 'POST':
		email = request.POST['email']
		agency = Agency()
		agency.username = request.POST.get('username', '')
		agency.password = request.POST.get('password', '')

		agency.agency_name = request.POST.get('agency_name', '')
		agency.licence_no = request.POST.get('licence_no', '')
		if 'logo' in request.FILES:
			agency.logo = request.FILES['logo']
		agency.address = request.POST.get('address', '')
		agency.office_no = request.POST.get('licence_no', '')
		agency.fax = request.POST.get('fax', '')
		agency.contact_person = request.POST.get('contact_person', '')
		agency.mobile = request.POST.get('mobile', '')
		agency.second_contact_person = request.POST.get('second_contact_person', '')
		agency.second_mobile_no = request.POST.get('second_mobile_no', '')
		agency.second_Email = request.POST.get('second_Email', '')
		agency.website = request.POST.get('website', '')
		agency.office_hours = request.POST.get('office_hours', '')
		agency.description = request.POST.get('licence_no', '')
		agency.save()
		try:
			ag = User.objects.get(username=request.POST.get('username', ''))
			ag.set_password(request.POST.get('password', ''))
			ag.save()
		except User.DoesNotExist:
			ag = None

	return render_to_response('agencyregistration.html',{'maid':maid}, context_instance=RequestContext(request))

def home(request):
	"""
	Home Page
	"""
	home_content = Home.objects.first()
	return render_to_response('home.html',{'home_content':home_content}, context_instance=RequestContext(request))

def aboutus(request):
	"""
	About Us
	"""
	about_content = Aboutus.objects.first()
	return render_to_response('aboutus.html',{'about_content':about_content}, context_instance=RequestContext(request))

def maid_profile(request, pk):
	"""
	Home Page
	"""
	success_msg = None
	try:
		maids = Maid.objects.get(pk=pk)
	except Maid.DoesNotExist:
		maids = None
	if request.method == 'POST':

		from django.core.mail import EmailMultiAlternatives
		from django.template.loader import render_to_string
		from django.utils.html import strip_tags
		file_to_be_sent= download_maid_profile(request,pk).getvalue()
		subject = 'Share maid details'

		html_content = render_to_string('templated_email/share_friend.html', {'maids':maids, 'DOMAIN_URL': settings.DOMAIN_URL,}) # ...
		text_content = strip_tags(html_content) # this strips the html, so people will have the text as well.

		# create the email, and attach the HTML version as well.
		msg = EmailMultiAlternatives(subject, text_content, 'biodata@amaremployment.com.sg', [request.POST.get('email')])
		msg.attach_alternative(html_content, "text/html")
		msg.attach("Report.pdf", file_to_be_sent, "application/pdf")
		msg.send()

		success_msg = "Your request successfully sent to your Friend."

	return render_to_response('maid_profiile.html',{'maids':maids, 'success_msg':success_msg}, context_instance=RequestContext(request))

def print_maid_profile(request, pk):
	"""
	Print Maid Profile Page
	"""
	try:
		maids = Maid.objects.get(pk=pk)
	except Maid.DoesNotExist:
		maids = None
	return render_to_response('print_maid_profiile.html',{'maids':maids}, context_instance=RequestContext(request))

def services(request):
	"""
	Serivces
	"""
	service_content = Services.objects.first()
	return render_to_response('services.html',{'service_content':service_content}, context_instance=RequestContext(request))

def faq(request):
	"""
	FAQ
	"""
	faq_content = Faq.objects.first()
	return render_to_response('faq.html',{'faq_content':faq_content}, context_instance=RequestContext(request))

def contact(request):
	"""
	Contact us
	"""
	success_msg = None
	if request.POST:
		contact = ContactForm()
		contact.name = request.POST.get('name', '')
		contact.email = request.POST.get('email', '')
		contact.mobile = request.POST.get('phone', '')
		contact.message = request.POST.get('message', '')
		contact.save()
		try:
			send_templated_mail(
					template_name='contact',
					from_email='info@asmaid.comgmail.com',
					recipient_list=[request.POST.get('email')],
					context={
						'username':request.POST.get('name', 'Guest')
					},
			)
		except:
			email = None
		success_msg = "Your request successfully sent to Admin. We will revert back you soon"
	return render_to_response('contact_us.html',{'success_msg':success_msg}, context_instance=RequestContext(request))

@login_required(login_url='/')
def agency_profile(request):
	"""
	Agency Profile
	"""
	try:
		agency_details = Agency.objects.get(user=request.user)
		noofmaids = Maid.objects.filter(agency=agency_details).count()
	except Agency.DoesNotExist:
		agency_details = None
		noofmaids = 0
	return render_to_response('agencyprofile.html',{'agency_details':agency_details, 'noofmaids':noofmaids}, context_instance=RequestContext(request))

def maid_list(request):
	"""
	Maid List
	"""
	maid = Maid.objects.all()
	filter_args = {}
	if request.method == 'POST':
		created = request.POST.get('created_date', '')
		type = request.POST.get('maid_type', '')
		country = request.POST.get('country', '')
		maritial_status = request.POST.get('maritial_status', '')

		if created:
			filter_args['modified__gte'] = date.today()-timedelta(days=int(created))

		if type:
			filter_args['types'] = type

		if maritial_status:
			filter_args['mstatus'] = maritial_status

		if country:
			filter_args['nationality__contains'] = country

		maid = maid.filter(**filter_args)
	return render_to_response('maid_list.html', {'maid': maid}, context_instance=RequestContext(request))

@login_required(login_url='/')
def add_maid(request):
	"""
	Add Maid
	"""
	maid_form = MaidInfoForm()
	agency_init = Agency.objects.all()[:1]
	maid_form = MaidInfoForm(initial={'agency': agency_init})
	success_msg = None
	if request.method == 'POST':
		maid_form = MaidInfoForm(request.POST, request.FILES)
		if maid_form.is_valid():
			maid_form = maid_form.save()
			return HttpResponseRedirect("/agency_maid_list/")
	return render_to_response('addmaid.html',{'maid_form':maid_form,}, context_instance=RequestContext(request))

@login_required(login_url='/')
def agency_maid_list(request):
	"""
	Agency Maid List
	"""
	try:
		agency_name = Agency.objects.get(user=request.user)
	except Agency.DoesNotExist:
		agency_name = None
	maid_list = Maid.objects.filter(agency=agency_name)
	return render_to_response('maidlistings.html',{'maid_list':maid_list}, context_instance=RequestContext(request))

@login_required(login_url='/')
def agency_maid_delete(request):
	"""
	Agency Maid Delete
	"""
	try:
		agency_name = Agency.objects.get(user=request.user)
	except Agency.DoesNotExist:
		agency_name = None
	if request.method == 'POST':
		maid_id = request.POST.get('delete_id', None)
		if maid_id:
			try:
				maid = Maid.objects.get(agency=agency_name, pk=maid_id)
				maid.delete()
			except DoesNotExist:
				maid = None
	maid_list = Maid.objects.filter(agency=agency_name)
	return HttpResponseRedirect("/agency_maid_list/")

@login_required(login_url='/')
def agency_maid_edit(request, pk):
	"""
	Agency Maid Edit
	"""
	maid = get_object_or_404(Maid, id=pk)
	maid_form = MaidInfoForm(instance=maid)
	if request.method == 'POST':
		maid_form = MaidInfoForm(request.POST, request.FILES, instance=maid)
		if maid_form.is_valid():
			maid_form.save()
		return HttpResponseRedirect("/agency_maid_list/")
	return render_to_response('editmaid.html',{'maid_form':maid_form}, context_instance=RequestContext(request))

@login_required(login_url='/')
def edit_account(request):
	"""
	Edit Account
	"""
	success_msg = None
	try:
		edit_account = Agency.objects.get(user=request.user)
	except Agency.DoesNotExist:
		edit_account = None

	if request.POST:
		try:
			edit_account = Agency.objects.get(user=request.user)
			edit_account.username = request.POST.get('username', '')
			edit_account.agency_name = request.POST.get('agency_name', '')
			edit_account.licence_no = request.POST.get('licence_no', '')
			if 'logo' in request.FILES:
				edit_account.logo = request.FILES['logo']
			edit_account.address = request.POST.get('address', '')
			edit_account.office_no = request.POST.get('office_no', '')
			edit_account.fax = request.POST.get('fax', '')
			edit_account.email = request.POST['email']
			edit_account.contact_person = request.POST.get('contact_person', '')
			edit_account.mobile = request.POST.get('mobile', '')
			edit_account.second_contact_person = request.POST.get('second_contact_person', '')
			edit_account.second_mobile_no = request.POST.get('second_mobile_no', '')
			edit_account.second_Email = request.POST.get('second_Email', '')
			edit_account.website = request.POST.get('website', '')
			edit_account.office_hours = request.POST.get('office_hours', '')
			edit_account.description = request.POST.get('description', '')
			edit_account.save()
			return HttpResponseRedirect("/agency_profile/")
		except Agency.DoesNotExist:
			edit_account = None

	return render_to_response('editaccount.html',{'success_msg':success_msg, 'edit_account':edit_account}, context_instance=RequestContext(request))

def login_view(request):
    if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				if not request.user.is_superuser:
					try:
						agency = Agency.objects.get(user=request.user, is_active=True)
					except Agency.DoesNotExist:
						logout(request)
						return HttpResponseRedirect(request.POST['next'])
				return HttpResponseRedirect(request.POST['next'])
		else:
			return HttpResponseRedirect(request.POST['next']+'?q=1')
    return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def globals(request):
	maid = Maid.objects.all()
	logo = Logo.objects.first()
	banner = Banner_Image.objects.all()
	return {'maid':maid, 'logo':logo, 'banner':banner}

def search(request):
	"""
	Maid Search
	"""
	maid = Maid.objects.all()
	filter_args = {}
	if request.method == 'POST':
		created = request.POST.get('created_date', '')
		type = request.POST.get('maid_type', '')
		country = request.POST.get('country', '')
		religion = request.POST.get('religion', '')
		maritial_status = request.POST.get('maritial_status', '')
		home = request.POST.get('home', '')
		singapore = request.POST.get('singapore', '')
		malaysia = request.POST.get('malaysia', '')
		hongkong = request.POST.get('hongkong', '')
		taiwan = request.POST.get('taiwan', '')
		east = request.POST.get('east', '')
		other = request.POST.get('other', '')
		infant = request.POST.get('infant', '')
		young = request.POST.get('young', '')
		elder = request.POST.get('elder', '')
		cook = request.POST.get('cook', '')
		house = request.POST.get('house', '')
		agepre = request.POST.get('house', '')
		education = request.POST.get('edu', '')

		if education:
			filter_args['education__icontains'] = education

		if agepre:
			filter_args['agepre__icontains'] = agepre

		if house:
			filter_args['house__gt'] = 1

		if cook:
			filter_args['cook__gt'] = 1

		if elder:
			filter_args['elder__gt'] = 1

		if young:
			filter_args['young__gt'] = 1

		if infant:
			filter_args['infant__gt'] = 1

		if created:
			filter_args['modified__gte'] = date.today()-timedelta(days=int(created))

		if type:
			filter_args['types'] = type

		if maritial_status:
			filter_args['mstatus'] = maritial_status

		if country:
			filter_args['nationality__icontains'] = country

		if religion:
			filter_args['religion__icontains'] = country

		if home:
			filter_args['home__gt'] = 0

		if singapore:
			filter_args['singapore__gt'] = 0

		if malaysia:
			filter_args['malaysia__gt'] = 0

		if taiwan:
			filter_args['taiwan__gt'] = 0

		if east:
			filter_args['east__gt'] = 0

		if other:
			filter_args['other__gt'] = 0

		if hongkong:
			filter_args['hongkong__gt'] = 0

		maid = maid.filter(**filter_args)
		return render_to_response('maid_list.html', {'maid': maid}, context_instance=RequestContext(request))
	return render_to_response('search.html', {'maid': maid}, context_instance=RequestContext(request))



from django import http
from django.template.loader import get_template
from django.template import Context
#import ho.pisa as pisa
import xhtml2pdf.pisa as pisa
import cStringIO as StringIO
import cgi

def write_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(
        html.encode("UTF8")), result)
    if not pdf.err:
        response  = HttpResponse(result.getvalue(), mimetype='application/pdf')
        response['Content-Type'] = 'application/pdf'
        response['Content-disposition'] = 'attachment'

        return result

def download_maid_profile(request, pk=None):
    maids = Maid.objects.get(pk=pk)
    #pdf_image_path = settings.PDF_IMAGE_PATH
    return write_pdf('download.html',{
        'maids' : maids,})

def dm_monthly(request, year, month):
    html  = render_to_string('download.html', { 'pagesize' : 'A4', }, context_instance=RequestContext(request))
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), dest=result, link_callback=fetch_resources )
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Gremlins ate your pdf! %s' % cgi.escape(html))
