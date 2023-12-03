from django.contrib import auth
from django.db import models


class WTStaff(models.Model):
    """A member of WTAMU Staff."""
    name = models.CharField(max_length=50,
                            help_text="The name of the WT Staff indiviual.")
    website = models.URLField(help_text="The WT Staff's website.")
    email = models.EmailField(help_text="The WT Staff's email address.")

    def __str__(self):
        return self.name


class Course(models.Model):
    """A WT course."""
    title = models.CharField(max_length=70,
                             help_text="The title of the course.")
    coursedate = models.DateField(
        verbose_name="Date the course is to take place.")
    coursenumber = models.CharField(max_length=20,
                            verbose_name="Course number ex CIDM6325.")
    publisher = models.ForeignKey(WTStaff,
                                  on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Student',
                                          through='Professor')

    def __str__(self):
        return "{} ({})".format(self.title, self.isbn)

    def isbn13(self):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format(self.isbn[0:3], self.isbn[3:4],
                                       self.isbn[4:6], self.isbn[6:12],
                                       self.isbn[12:13])


class Student(models.Model):
    """A Student of WT."""
    first_names = models.CharField(max_length=50,
                                   help_text="The student's first name or names.")
    last_names = models.CharField(max_length=50,
                                  help_text="The student's last name or names.")
    email = models.EmailField(help_text="The contact email for the student.")

    def initialled_name(self):
        """ self.first_names='Jerome David', self.last_names='Salinger'
            => 'Salinger, JD' """
        initials = ''.join([name[0] for name
                            in self.first_names.split(' ')])
        return "{}, {}".format(self.last_names, initials)

    def __str__(self):
        return self.initialled_name()


class Professor(models.Model):
    class ContributionRole(models.TextChoices):
        Professor = "PROFESSOR", "Professor"
        ProfAide = "PROFAIDE", "Prof-Aide"
        REVIEWER = "REVIEWER", "Reviewer"
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Student, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this professor had in the course.",
                            choices=ContributionRole.choices, max_length=20)


class Reviewer(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(null=True,
                                       help_text='''The date and time the review was last edited.'''
                                       )
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                             help_text="The Course that this review is for.")