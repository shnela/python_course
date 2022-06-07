# SQLAlchemy

## New model `Post` (blog post)
`Post` should have
* `id`
* `content`
* `creation_date` (default now)

What type should we use for blog post?  
[Available SQLAlchemy field types](https://docs.sqlalchemy.org/en/13/core/type_basics.html?highlight=datetime#generic-types)

```python
from datetime import datetime, timezone
datetime.now()
datetime.now(tz=timezone.utc)
```

**Always use utc timezone in backend code**

But remember, [datetime handling is mess](https://zachholman.com/talk/utc-is-enough-for-everyone-right)
> So you’ve got a bunch of scientist types around 1960 who are like, hey, time is all screwy we should totes make a standard. And some of them spoke English, and some of them spoke French, which, of course, is the cause of so much conflict over so many generations. (In hindsight, maybe we should have split all those troublemakers up from the start.)

> The English-speaking folk were like yo, this definitely sounds like Coordinated Universal Time, boom, ship it. And the French speakers were like yeah that makes total sense! Temps Universel Coordonné DOES work out well in our language, too, ship it! Then they both looked up and realized cool, they’ve created both CUT and TUC for acronyms. Shit.

> When your standard — that is expressly meant to standardize time — doesn’t even standardize on a standard acronym, well, damn, that probably doesn’t bode well for your standard.

Let's see `default` datetime for `creation_date` `Column`: `datetime.now`

# `User` has written the `Post` - one to many

## Look at our `User` and `Post` models in dBeaver
```
test.db -> Tables -> ER Diagram
```

And compare with [this](https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help/one-to-many-relationships.html)
explanation.

## One to many in `Flask-SQLAlchemy`

[One to many](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#one-to-many)

```python
class User:
    ...
    posts = relationship('Post', backref='user', lazy=True)

class Post:
    ...
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
```

We edited only `post` **database table** - we've added `user_id` column.
