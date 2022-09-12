from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    name = models.CharField(_('name'), max_length=50)
    owner_id = models.PositiveIntegerField(_('owner id'))
    owner_name = models.CharField(_('owner name'), max_length=30)
    thumb_url = models.URLField(_('thumb url'), blank=True, null=True)
    cover_url = models.URLField(_('cover url'), blank=True, null=True)
    description = models.TextField(_('description'))
    last_activity = models.DateTimeField(
        _('last activity'), blank=True, null=True
    )
    total_score = models.PositiveIntegerField(_('total score'), default=0)
    total_tasks = models.PositiveIntegerField(_('total tasks'), default=0)
    unchangeable = models.BooleanField(_('unchangeable'))
    include_weekly_report = models.BooleanField(_('include weekly report'))
    content_type = models.PositiveIntegerField(_('content type'))
    is_netology = models.BooleanField(_('is netology'))
    bg_url = models.URLField(_('bg url'), blank=True, null=True)
    video_url = models.URLField(_('video url'), blank=True, null=True)
    demo = models.BooleanField(_('demo'))
    custom_author_names = models.CharField(
        _('custom author names'), max_length=30
    )
    custom_contents_link = models.URLField(
        _('custom contents link'), blank=True, null=True
    )
    hide_viewer_navigation = models.BooleanField(_('hide viewer navigation'))
    duration = models.PositiveIntegerField(_('duration'), blank=True, null=True)


class CourseType(BaseModel):
    course = models.ForeignKey(
        'Course', verbose_name=_('course'), on_delete=models.CASCADE,
        related_name='types'
    )
    name = models.CharField(_('name'), max_length=30)


class CourseAuthor(BaseModel):
    course = models.ForeignKey(
        'Course', verbose_name=_('course'), on_delete=models.CASCADE,
        related_name='authors'
    )
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('phone'), max_length=30)
    name = models.CharField(_('name'), max_length=30)
    last_name = models.CharField(_('name'), max_length=30)
    role_id = models.PositiveIntegerField(_('role'))
    auth_type = models.PositiveIntegerField(_('auth type'))
    last_activity_at = models.PositiveIntegerField(
        _('last activity at'), blank=True, null=True
    )
    is_active = models.BooleanField(_('is active'), default=True)
