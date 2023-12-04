
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExampleForm

#def checklistform(request):
#    return HttpResponse("Welcome to CIDM 6395 Project for Megan Moore!")

def checklistform(request):
  template = loader.get_template('welcome.html')
  return HttpResponse(template.render())

from django.shortcuts import render
def welcome_view (request):
    return render(request, 'welcome.html')

from django.template import loader

def checklistform(request):
    for name in request.POST:
        print("{}: {}".format(name,
        request.POST.getlist(name)))
    return render(request, "studentform2.html", {"method":
request.method})

def welcome_view(request):
       message = f"<html><h1>Welcome to CIDM 6325 landing page!</h1></html>"
       return HttpResponse(message)

from .forms import PublisherForm, SearchForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Professor, WTStaff
from django.contrib import messages

def publisher_edit(request, pk=None):
    if pk is not None:
        WTStaff = get_object_or_404(WTStaff,
        pk=pk)
    else:
        WTStaff = None
    if request.method == "POST":
        form = PublisherForm(request.POST,
        instance=WTStaff)
        if form.is_valid():
            updated_publisher = form.save()
            if WTStaff is None:
                messages.success(request, "WTStaff
                "{}" was created."
                .format(updated_publisher))
            else:
                messages.success(request, "WTStaff
                "{}" was updated."
                .format(updated_publisher))
            return redirect("publisher_edit",
            updated_publisher.pk)
    else:
        form = PublisherForm(instance=WTStaff)
        return render(request, "form-example.html",
    {"method": request.method, "form": form})

    
# 9.03.2
def is_staff_user(user):
    return user.is_staff


# @permission_required('edit_publisher')  # 9.03.1
@user_passes_test(is_staff_user)  # 9.03.2
def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(
                    request, 'Publisher "{}" was created.'.format(updated_publisher)
                )
            else:
                messages.success(
                    request, 'Publisher "{}" was updated.'.format(updated_publisher)
                )

            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    return render(
        request,
        "reviews/instance-form.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Publisher",
            "instance": publisher,
        },
    )


@login_required  # 9.03.3
def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Course, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
        user = request.user
        if not user.is_staff and review.creator.id != user.id:
            raise PermissionDenied
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                messages.success(request, 'Review for "{}" created.'.format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, 'Review for "{}" updated.'.format(book))

            updated_review.save()
            return redirect("book_detail", book.pk)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "reviews/instance-form.html",
        {
            "form": form,
            "instance": review,
            "model_type": "Review",
            "related_instance": book,
            "related_model_type": "Book",
        },
    )
