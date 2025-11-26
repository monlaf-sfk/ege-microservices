from tortoise import fields, models

from ege_shared.consts import SubjectEnum


class User(models.Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True, null=True, index=True)
    vk_id = fields.BigIntField(unique=True, null=True, index=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    scores: fields.ReverseRelation["Score"]

    class Meta:
        table = "users"

class Score(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="scores")
    subject = fields.CharEnumField(SubjectEnum, max_length=50)
    score = fields.IntField() # Балл (0-100)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "scores"
        unique_together = ("user", "subject")