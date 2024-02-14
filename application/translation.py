from modeltranslation.translator import register, TranslationOptions
from application.models import Application, Package, PackageType

@register(Package)
class PackageTranslationOptions(TranslationOptions):
	fields = ('name',)

@register(PackageType)
class PackageTypeTranslationOptions(TranslationOptions):
	fields = ('description', 'package_type')


