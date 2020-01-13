from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(EngineerTitle)
admin.site.register(ProcessKind)
admin.site.register(StageKind)
admin.site.register(Engineer)
admin.site.register(Reviewer)
admin.site.register(Process)
admin.site.register(ProcessReview)
admin.site.register(Comment)
admin.site.register(ProcessComments)

