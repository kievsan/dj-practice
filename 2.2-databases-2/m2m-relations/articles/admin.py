from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Scope, Tag, Article


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self, main_count=0):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными формы,
            # которые можно проверить
            if form.cleaned_data:
                main_count += int(form.cleaned_data['is_main'])

        # исключение ValidationError покажет админке наличие ошибки,
        # объект не будет сохранен, а пользователь получит сообщение об ошибке
        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 2
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]


@admin.register(Tag)
class ArticleTag(admin.ModelAdmin):
    list_display = ['name']

