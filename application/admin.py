from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from application.models import Application, Package, PackageType, PackagePhoto

class PackagePhotoAdmin(admin.StackedInline):
	model = PackagePhoto

@admin.register(Package)
class Package(TranslationAdmin):
	class Meta:
		model = Package

@admin.register(PackageType)
class PackageTypeAdmin(TranslationAdmin):
	inlines = [PackagePhotoAdmin]

	class Meta:
		model = PackageType


admin.site.register(Application)

