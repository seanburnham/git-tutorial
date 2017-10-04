from django.contrib import admin

import vote.models

admin.site.register(vote.models.Candidate)
