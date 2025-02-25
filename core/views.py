from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.forms import OrderchangeForm


# Create your views here.
@login_required
def edit_order(request):
    if request.method == "POST":
        form = OrderchangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")  # Redirect back to profile after editing
    else:
        form = OrderchangeForm(instance=request.user)

    return render(request, "accounts/edit_profile.html", {"form": form})