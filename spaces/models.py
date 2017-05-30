from django.db import models
import uuid
from profiles.models import Profile


class Tag(models.Model):
    word = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

    def __unicode__(self):
        return self.word

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Space(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4,
            editable=False)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    # Join Policy: 0 - Required Invitation(default) -> 1 - Free Join
    POLICY = (
        ('0', 'Invitation'),
        ('1', 'Free'),
    )
    join_policy = models.CharField(max_length=1, choices=POLICY)
    visibility = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    #updated_by =
    color = models.CharField(max_length=20)
    url = models.SlugField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Space"
        verbose_name_plural = "Spaces"
        ordering = ['-created_at']
