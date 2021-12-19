from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Membership


class MembershipInlineFormSet(BaseInlineFormSet):
    def clean(self):

        count_is_main = 0

        for form in self.forms:
            try:
                if form.cleaned_data['is_main']:
                    count_is_main += 1
            except KeyError:
                continue

        if count_is_main > 1:
            raise ValidationError('Выбрано слишком много основных тэгов!')
        elif count_is_main == 0:
            raise ValidationError('Не выбран основной тэг!')

        return super().clean()


class TopicInLine(admin.TabularInline):
    model = Membership
    formset = MembershipInlineFormSet
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TopicInLine]


@admin.register(Scope)
class TopicAdmin(admin.ModelAdmin):
    pass
