from django.contrib import admin
from .models import Doctor, Specialization, Appointment
from django.contrib.admin import StackedInline, TabularInline

# Register your models here.


class DoctorInline(TabularInline):
    model = Doctor
    extra = 1


class AppointmentInline(StackedInline):
    model = Appointment
    extra = 1


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)

    inlines = [DoctorInline]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "specialization", "likes")
    list_filter = ("specialization", "available_days")
    search_fields = ("name", "email", "phone")
    readonly_fields = ("likes",)

    fieldsets = (
        (None, {"fields": ("name", "email", "phone", "address", "specialization")}),
        ("Location", {"fields": ("latitude", "longitude")}),
        ("Availability", {"fields": ("available_days", "available_times")}),
        ("Statistics", {"fields": ("likes",)}),
    )

    inlines = [AppointmentInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ("likes",)
        return self.readonly_fields
