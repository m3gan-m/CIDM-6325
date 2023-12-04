from django import forms

PROGRAM_YEAR_CHOICES = (
    ("Value One", "Year 2022-2023"),
    ("Value Two", "Year 2023-2024"),
    ("Value Three", "Year 2024-2025"),
)

CIRRICULUM_CHOICES = (
    ("BBA Core Cirriculum - Communication: 6 Hours",
        (("1", "ENGL 1301 - Introduction to Academic Writing and Argumentation"), 
         ("2", "OR ENGL 1311 - Writing About Ideas"),
         ("3","AND"),
         ("4","COMM 1315 - Basic Speech Communication"),
         ("5","OR COMM 1318 - Interpersonal Communication"),
         ("6","OR COMM 1321 - Business and Professional Communication")),
    ),
    ("BBA Core Cirriculum - Math: 3 Hours",
        (("7", "MATH 1324 - Mathematics for Business and Economics I")),
    ),
    ("BBA Core Cirriculum - Social and Behavioral Sciences: 3 Hours",
        (("8", "COMM 1321 - ECON 2301 - Principles of Macroeconomics")),
    ),
    ("BBA Core Cirriculum - Component Area Option: 3 Hours",
        (("9", "BUSI 1301 - Business Principles"), 
         ("10", "BUSI 1304 - Business Communication"),
         ("11","CIDM 1301 - Introduction to Information Science"),
         ("12","CIDM 1315 - Programming Fundamentals"),
         ("13","ECON 2331 - Economics and Society")),
    ),
    ("BBA Major Requirements - 21 Hours required",
        (("14", "CIDM 1315 - Programming Fundamentals"), 
         ("15", "CIDM 3312 - Advanced Business Programming"),
         ("16","CIDM 4360 - Object-Oriented Analysis and Design"),
         ("17","CS 3340 - Software Engineering"),
         ("18","CIDM 4390 - Software Systems Development"),
         ("19","CIDM 3312 - Advanced Business Programming"),
         ("20","AND"),
         ("21","CIDM 2315 - Programming Business Applications"),
         ("22","OR CS 1337 - Programming Principles I")),
    ),
    ("BBA Major Electives - 9 Hours required", 
        (("23", "CIDM 3310 - Spreadsheet Applications in Business"), 
         ("24", "CIDM 3342 - Business Statistics"), 
         ("25", "CIDM 3372 - Front-End Web Application Development"), 
         ("26", "CIDM 3380 - Information Security"),
         ("27", "CIDM 3390 - Project Management"))
    ),
      
)


class ExampleForm(forms.Form):
    studentfirstname = forms.CharField(max_length=3)
    studentlastname = forms.CharField(max_length=3)
    password_input = forms.CharField(min_length=8, widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=PROGRAM_YEAR_CHOICES, widget=forms.RadioSelect)
    cirriculum = forms.ChoiceField(choices=CIRRICULUM_CHOICES)
    cirriculum_completed = forms.MultipleChoiceField(required=False, choices=CIRRICULUM_CHOICES)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    email_input = forms.EmailField()
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")

elective_count = forms.IntegerField(
    min_value=0,
    max_value=80,
    widget=forms.NumberInput(attrs={"placeholder":
    "Number of Electives"}),
)

course_count = forms.IntegerField(
    min_value=0,
    max_value=50,
    widget=forms.NumberInput(attrs={"placeholder":
    "Number of Courses"}),
)

email = forms.EmailField(
    required=False,
    validators=[validate_email_domain],
    widget=forms.EmailInput(attrs={"placeholder":
    "Your email address"}),
)

from .models import WTStaff
class PublisherForm(forms.ModelForm):
    class Meta:
        model = WTStaff
        fields = "__all__"

from django.core.exceptions import ValidationError


def validate_email_domain(value):
    if value.split("@")[-1].lower() != "example.com":
        raise ValidationError("The email address must be on the domain example.com.")


class OrderForm(forms.Form):
    elective_count = forms.IntegerField(min_value=0, max_value=80)
    course_count = forms.IntegerField(min_value=0, max_value=50)
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(required=False ,validators=[validate_email_domain])

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["send_confirmation"] and not cleaned_data.get("email"):
            self.add_error("email", "Please enter an email address to receive the confirmation message.")
        elif cleaned_data.get("email") and not cleaned_data["send_confirmation"]:
            self.add_error("send_confirmation", "Please check this if you want to receive a confirmation email.")

        item_total = cleaned_data.get("elective_count", 0) + cleaned_data.get("course_count", 0)

        if item_total > 100:
            self.add_error(None, "The total number of items must be 100 or less.")