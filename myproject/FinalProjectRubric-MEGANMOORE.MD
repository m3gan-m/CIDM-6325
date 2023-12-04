# MEGAN MOORE CIDM 6325 PROJECT - README
Guide for Final Project details. I will say through this course and working with the Django text, I preferred using VS Code in place of PyCharm. It's simply more familiar to me as I've used it much more. But for the steps I did use PyCharm, I found this quick step list to be handy.<br>
<kbd>
<img src="https://github.com/m3gan-m/CIDM-6325/blob/a57615705338d481a6b5e6294ff8d48c77bb5c73/myproject/checklistform/pycharmsteps.png" width="450">
</kbd>
<br><br>

Main admin page: (http://127.0.0.1:8000/)<br>
Launch html welcome page here: [Welcome to my Project](http://127.0.0.1:8000/members/)

Checklist Form built to Computer Information Systems B.B.A.<br>
Link to degree program checklist: (https://catalog.wtamu.edu/preview_program.php?catoid=29&poid=4565&returnto=2546)<br>

Checklist Form Screenshot<br>
<kbd>
<img src="https://github.com/m3gan-m/CIDM-6325/blob/9968741323197617df73a6d0f6cf6f39dbba37ce/myproject/checklistform/checklistform.png" width="450">
</kbd>
<br><br>

Django Admin Screenshot<br>
<kbd>
<img src="https://github.com/m3gan-m/CIDM-6325/blob/5af2eee6249f6ca88e7eddd47628d99da43e393d/myproject/checklistform/superuser5.png" width="450">
</kbd>
<br><br>

Working Static File Screenshot<br>
<kbd>
<img src="https://github.com/m3gan-m/CIDM-6325/blob/948e1d9c575e7c15bcd90ec0ab6fcdeeb642ef07/myproject/checklistform/staticsnip.png" width="450">
</kbd>
<br><br>

File finding Screenshot<br>
<kbd>
<img src="https://github.com/m3gan-m/CIDM-6325/blob/948e1d9c575e7c15bcd90ec0ab6fcdeeb642ef07/myproject/checklistform/filefinder.png" width="450">
</kbd>
<br><br>

RUBRIC OUTLINE BELOW:
* All **Baseline** components - Gets you to 70% of the value
* Six **Good** components - Gets you to 80% of the vaue
* Two **Better** components - Gets you to 85% of the value
* Two **Best** components - Gets you to 90% of the value

Topic                                   | Baseline  | Good  | Better  | Best  | LINK TO CODE PROOF  
---                                     | ---       | ---   | ---     | ---   | ---
***Chapter 3***                         |           |       |         |       | 
Templates                               | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/tree/main/myproject/checklistform/templates)
Template Inheritance                    | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/tree/main/myproject/checklistform/templates)
Views                                   | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/views.py)
Class-Based Views                       | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/urls.py)
URLs                                    | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/myproject/urls.py)
Routing                                 | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/urls.py)
***Chapter 4***                         |           |       |         |       |
Model Classes                           | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/models.py)
Django Admin configuration              | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/admin.py)
Tests                                   |           | x     |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/tests.py)
***Chapter 5***                         |           |       |         |       |
Static Files                            | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/f7c981ed5b13f0d56eb7c2af68d8c6a6be9c869a/myproject/landing/static/landing/logo.png) (https://github.com/m3gan-m/CIDM-6325/blob/bb1d11551b50c5e02052e09f35ebc11bbe80d694/myproject/landing/static/landing/cis_bba_2324.pdf) (https://github.com/m3gan-m/CIDM-6325/tree/main/myproject/static_production_test)
Queries                                 | x         |       |         |       | File Finding at end of (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/myproject/settings.py)
***Chapter 6***                         |           |       |         |       |
Class-Based Forms                       | x         |       |         |       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/templates/studentform2.html)  which loads to (http://127.0.0.1:8000/studentform2/)
***Chapter 7***                         |           |       |         |       |
Authentication                          | x         |       |         |       |
Social auth integration                 |           | x     |         |       |
Postgres                                |           | x     |         |       |
***Chapter 8***                         |           |       |         |       |
Custom user models                      |           | x     |         |       |
Ad hoc forms                            |           | x     |         |       |
***Chapter 10***                        |           |       |         |       |
Bootstrap                               | x         |       |         |       |
***Chapter 11***                        |           |       |         |       |
Custom templates                        |           | x     |         |       |
Account management                      |           | x     |         |       |
***Chapter12***                         |           |       |         |       |
Email                                   |           | x     |         |       |
***Chapter 13***                        |           |       |         |       |
django_crispy_forms                     |           | x     |         |       |
***Chapter 14***                        |           |       |         |       | 
authorization                           |           | x     |         |       |
CBV mixins                              |           | x     |         |       |
***Chapter15***                         |           |       |         |       |
ManytoMany relationships                |           | x     |         |       |
***Chapter16***                         |           |       |         |       |
heroku deployment                       |           |       | x       |       |
vps deployment (nginx, gunicorn)        |           |       | x       |       |
Static assets with nginx and whitenoise |           | x     |         |       |
Securing with SSL                       | x         |       |         |       |
Custom middlewre                        |           |       | x       |       |
Task scheduling with cron               |           | x     | x       |       |
CI/CD with Github                       |           |       |         | x       |
***3rd Party***                         |           |       |         |       |
[Django admin](https://github.com/wsvincent/awesome-django#admin) | | | | x       |
[APIs](https://github.com/wsvincent/awesome-django#apis) | |  |         | x       |
[Async](https://github.com/wsvincent/awesome-django#async) |           |       |         | x       |
[ECommerce](https://github.com/wsvincent/awesome-django#ecommerce) |    |   |   | x       |
[Files and Images](https://github.com/wsvincent/awesome-django#filesimages) |    |   |   | x       | (https://github.com/m3gan-m/CIDM-6325/blob/main/myproject/checklistform/checklistform.png)
[Model enhancements](https://github.com/wsvincent/awesome-django#models) |   |   |   | x       |
[Search](https://github.com/wsvincent/awesome-django#search) |   |   |   | x       |
[Tasks and Job Scheduling](https://github.com/wsvincent/awesome-django#task-queues) |   |   |   | x       |
[Users and SSO](https://github.com/wsvincent/awesome-django#users) |   |   |   | x       |
[Views](https://github.com/wsvincent/awesome-django#views) |   |   |   | x       |
