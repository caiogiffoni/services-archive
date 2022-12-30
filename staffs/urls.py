from django.urls import path

from staffs.views import StaffDetailView, StaffView

urlpatterns = [
    path("staffs/", StaffView.as_view()),
    path("staffs/<uuid:staff_id>/", StaffDetailView.as_view()),
]
