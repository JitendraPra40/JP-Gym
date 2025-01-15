from django.contrib import admin
from authapp.models import Contact, MembershipPlan, Enrollment,Trainer, Gallery,CustAttendance, Workout, GymImage, GymContact, Facility,GymAddress, Services, Review
# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(Gallery)
admin.site.register(CustAttendance)
admin.site.register(Workout)
admin.site.register(GymImage)
admin.site.register(GymContact)
admin.site.register(Facility)
admin.site.register(GymAddress)
admin.site.register(Services)
admin.site.register(Review)