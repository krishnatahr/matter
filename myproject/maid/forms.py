from maid.models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple, MultiWidget
import pickle
import json

ILL_CHOICES = (
    ('1', 'Mental illness'),
    ('2', 'Epilepsy'),
    ('3', 'Asthma'),
    ('4', 'Diabetes'),
    ('5', 'Hypertension'),
    ('6', 'Tuberculosis'),
    ('7', 'Heart disease'),
    ('8', 'Malaria'),
    ('9', 'Operations'),
    ('10', 'Other')
)

FOOD_CHOICES = (
    ('1', 'No pork'),
    ('2', 'No beef'),
    ('3', 'Other')
)

INTERVIEW_CHOICES = (
    ('1', 'Interviewed via telephone/teleconference'),
    ('2', 'Interviewed via videoconference'),
    ('3', 'Interviewed in person'),
    ('4', 'Interviewed in person and also made observation of FDW in the areas of work listed in table')
)

FDW_CHOICES = (
    ('1', 'FDW is not available for interview'),
    ('2', 'FDW can be interviewed by phone'),
    ('3', 'FDW can be interviewed by video-conference'),
    ('4', 'FDW can be interviewed in person')
)

TYPE = (
	('Fresh Maid', 'Fresh Maid'),
	('Experienced Maid', 'Experienced Maid'),
	('Transfer Maid', 'Transfer Maid'),
)

COUNTRY = (
    ('Bangladesh', 'Bangladesh'),
    ('Cambodia', 'Cambodia'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Malaysia', 'Malaysia'),
    ('Myanmar', 'Myanmar'),
    ('Philippines', 'Philippines'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Thailand', 'Thailand'),
    ('Viet Nam', 'Viet Nam'),
)

MSTATUS = (
	('Single', 'Single'),
	('Married', 'Married'),
	('Divorced', 'Divorced'),
	('Separated', 'Separated'),
)

class EvalWidget(MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(),
                   forms.TextInput(),
                   forms.TextInput()]
        super(EvalWidget, self).__init__(widgets, attrs)

    def __iter__(self):
        return iter(self.widgets)

    def decompress(self, value):
        if value:
            return json.loads(value)
        else:
            return ['', '', '']

class EvalField(forms.fields.MultiValueField):
    widget = EvalWidget

    def __init__(self, *args, **kwargs):
        list_fields = [forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=31)]
        super(EvalField, self).__init__(list_fields, *args, **kwargs)



    def compress(self, values):
        return json.dumps(values)

class ExpWidget(MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(),
                   forms.TextInput(),
                   forms.TextInput(),
                   forms.TextInput(),
                   forms.TextInput(),
                   forms.TextInput()]
        super(ExpWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return json.loads(value)
        else:
            return ['', '', '', '', '', '']

class ExpField(forms.fields.MultiValueField):
    widget = ExpWidget

    def __init__(self, *args, **kwargs):
        list_fields = [forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=60),
                       forms.fields.CharField(max_length=80),
                       forms.fields.CharField(max_length=100),
                       forms.fields.CharField(max_length=150)]
        super(ExpField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        return json.dumps(values)

class MaidInfoForm(forms.ModelForm):
    types = forms.ChoiceField(choices=TYPE)
    name = forms.CharField(label="Maid Name:")
    dob = forms.CharField(label="Date of birth:", required=False)
    age = forms.IntegerField(required=False)
    birth_place = forms.CharField(label="Place of birth:", required=False)
    height = forms.CharField(required=False, help_text="cm")
    weight = forms.CharField(required=False, help_text="kg")
    nationality = forms.ChoiceField(choices=COUNTRY)
    resident = forms.CharField(widget=forms.Textarea, label="Residential address in home country:", required=False)
    repatriat = forms.CharField(widget=forms.Textarea, label="Name of port / airport to be repatriated to:", required=False)
    phone = forms.CharField(label="Contact number in home country:", required=False)
    religion = forms.CharField(required=False)
    education = forms.CharField(label="Education level:", required=False)
    no_of_sibling = forms.CharField(required=False, label="Number of Sibling:")
    mstatus = forms.ChoiceField(choices=MSTATUS, label="Marital status:")
    no_of_child = forms.CharField(required=False, label="Number of children:")
    age_of_child = forms.CharField(required=False, label="Age(s) of children (if any):")

    # medical details
    allergies = forms.CharField(required=False, label="Allergies (if any):")
    illness = forms.MultipleChoiceField(
        label="Past and existing illnesses (including chronic ailments and illnesses requiring medication):",
        required=False, widget=CheckboxSelectMultiple(), choices=ILL_CHOICES)
    disabilities = forms.CharField(required=False, label="Physical disabilities:")
    dietary_restrictions = forms.CharField(required=False, label="Dietary restrictions:")
    food_handle = forms.MultipleChoiceField(
        required=False, label="Food handling preferences:",
        widget=CheckboxSelectMultiple(), choices=FOOD_CHOICES)
    food_other = forms.CharField(required=False)

    # other details
    off_days = forms.CharField(required=False, label="Preference for rest day:")
    remarks = forms.CharField(widget=forms.Textarea, required=False, label="Any other remarks:")

    # skill details
    no_eval = forms.BooleanField(required=False, label="Based on FDW's declaration, no evaluation/observation by Singapore EA or overseas training centre/EA")
    sg_eval = forms.BooleanField(required=False, label="Interviewed by Singapore EA")
    sg_interview_type = ov_interview_type = forms.MultipleChoiceField(required=False, label="Interview Type:", widget=CheckboxSelectMultiple(), choices=INTERVIEW_CHOICES)
    sg_children = ov_children = EvalField(required=False, label="Care of infants/children")
    sg_child_age = ov_child_age = forms.CharField(required=False, label="Please specify age range:")
    sg_elderly = ov_elderly = EvalField(required=False, label="Care of elderly")
    sg_disabled = ov_disabled = EvalField(required=False, label="Care of disabled")
    sg_housework = ov_housework = EvalField(required=False, label="General housework")
    sg_cooking = ov_cooking = EvalField(required=False, label="Cooking")
    sg_cook_cusine = ov_cook_cusine = forms.CharField(required=False, label="Please specify cuisines:")
    sg_language = ov_language = EvalField(required=False, label="Language abilities (spoken)")
    sg_languages = ov_languages = forms.CharField(required=False, label="Please specify:")
    sg_other = ov_other = EvalField(required=False, label="Other skills, if any")
    sg_others = ov_others = forms.CharField(required=False, label="Please specify:")

    ov_eval = forms.BooleanField(required=False, label="nterviewed by overseas training centre / EA")
    ov_ea_name = forms.CharField(required=False, label="Please state name of foreign training centre / EA:")
    ov_ea_certify = forms.CharField(required=False, label="State if the third party is certified (e.g. ISO9001) or audited periodically by the EA:")

    # experience details
    ov_history1 = ExpField(required=False, label='1.')
    ov_history2 = ExpField(required=False, label='2.')
    singapore_history = forms.TypedChoiceField(
        choices=((True, 'Yes'), (False, 'No')), widget=forms.RadioSelect, required=False,  coerce=bool)
    feedback1 = forms.CharField(widget=forms.Textarea, required=False, label="Feedback of Employer 1.")
    feedback2 = forms.CharField(widget=forms.Textarea, required=False, label="Feedback of Employer 2.")
    fdw_availability = forms.MultipleChoiceField(required=False, label="AVAILABILITY OF FDW", widget=CheckboxSelectMultiple(), choices=FDW_CHOICES)
    other_remarks = forms.CharField(widget=forms.Textarea, required=False, label="")

    class Meta:
        model = Maid
