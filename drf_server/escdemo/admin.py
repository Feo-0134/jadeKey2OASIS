from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Engineer)
admin.site.register(Comment)
admin.site.register(Stage)
admin.site.register(Process)
admin.site.register(HighLvl)

admin.site.register(ProcessLinkStage)
admin.site.register(StageLinkComment)
admin.site.register(MakeCommentOn)
