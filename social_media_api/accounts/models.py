from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # """
    # Our custom user model extends Django's built-in AbstractUser, so we inherit
    # username, password, email, first_name, last_name, etc., then add fields
    # useful for social features.
    # """

    bio = models.TextField(blank=True, help_text="Short description about the user")


# ImageField stores the path to an uploaded image. Requires Pillow.
# Files will be saved under MEDIA_ROOT/profiles/...
profile_picture = models.ImageField(
    upload_to="profiles/",
    blank=True,
    null=True,
    help_text="User's avatar/profile picture",
)


# Self-referential ManyToMany: a user can follow many other users.
# symmetrical=False makes the relationship directional: if A follows B,
# it does NOT imply B follows A.
followers = models.ManyToManyField(
    "self",
    symmetrical=False,
    related_name="following",  # reverse accessor: user.following -> who I follow
    blank=True,
    help_text="Users who follow this user",
)


def followers_count(self) -> int:
    return self.followers.count()


def following_count(self) -> int:
    return self.following.count()


def __str__(self):
    return self.username
