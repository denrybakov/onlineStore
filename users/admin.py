from django.contrib import admin
from users.models import User, EmailVerification

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'image')
  
  
@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
  list_display = ('code', 'user', 'expiration')
  fields = ('code', 'user', 'expiration', 'created')
  readonly_fields = ('created',)