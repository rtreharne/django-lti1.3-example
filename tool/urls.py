from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),

    # LTI Core
    path("login/", views.lti_login, name="lti_login"),
    path("launch/", views.lti_launch, name="lti_launch"),
    path("landing/", views.landing, name="lti_landing"),
    path("jwks/", views.jwks),

    # Deep Linking (for creating assignments only)
    path("deeplink/", views.deeplink, name="deeplink"),
    path("deeplink/submit/", views.deeplink_submit, name="deeplink_submit"),

    # Assignment main view (students + instructors)
    path("assignment/", views.assignment_view, name="assignment_view"),

    # NEW — Internal Assignment Editing (no deep linking)
    path("assignment/edit/", views.assignment_edit, name="assignment_edit"),
    path("assignment/edit/save/", views.assignment_edit_save, name="assignment_edit_save"),

    # Student Submission
    path("submit_text/", views.submit_text, name="submit_text"),
    path("submit_file/", views.submit_file, name="submit_file"),
    path("submission/<int:submission_id>/", views.submission_status, name="submission_status"),

    # nprs
    path("nrps/test/", views.nrps_test, name="nrps_test"),


    # # Debug helpers
    # path("test_set/", views.test_set_cookie),
    # path("test_read/", views.test_read_cookie),
]
