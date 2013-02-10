import datetime
from flask import url_for
from fakelbst import db

class Mark(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    link = db.StringField(max_length=255, required=True)
    tag_id = db.IntField(required=True)

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': False,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

class MarkTag(db.Document):
    id = db.IntField(required=True)
    title = db.StringField(max_length=255, required=True)


'''
class BlogPost(Post):
    body = db.StringField(required=True)

class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(verbose_name="Comment", required=True)
    author = db.StringField(verbose_name="Name", max_length=255, required=True)
'''
