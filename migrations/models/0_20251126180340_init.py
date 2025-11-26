from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "telegram_id" BIGINT UNIQUE,
    "vk_id" BIGINT UNIQUE,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255),
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS "idx_users_telegra_ab91e9" ON "users" ("telegram_id");
CREATE INDEX IF NOT EXISTS "idx_users_vk_id_cfcf6c" ON "users" ("vk_id");
CREATE TABLE IF NOT EXISTS "scores" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "subject" VARCHAR(50) NOT NULL,
    "score" INT NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_scores_user_id_04f4e8" UNIQUE ("user_id", "subject")
);
COMMENT ON COLUMN "scores"."subject" IS 'MATH_PROF: math_prof\nRUSSIAN: russian\nPHYSICS: physics\nINF: informatics';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmFtT4jAUgP9Kp0/ujOtoEWF9q4gr6woO4F68TCe0oWRt05qkKuPw3zdJW3qFFQZW3P"
    "WNnkt6zsfJyWmeVdezoEN3dEiQOVIPlWcVAxfyHznNtqIC30/kQsDAwJGmILEZUEaAybh0"
    "CBwKuciC1CTIZ8jDXIoDxxFCz+SGCNuJKMDoPoAG82zIRpBwxfUtFyNswSdI40f/zhgi6F"
    "iZUJEl3i3lBhv7UtbC7EQaircNDNNzAhcnxv6YjTw8tUaYCakNMSSAQbE8I4EIX0QX5Rln"
    "FEaamIQhpnwsOASBw1LpvpCB6WHBj0dDZYK2eMtHbW+/tl+vHOzXuYmMZCqpTcL0ktxDR0"
    "mg3VcnUg8YCC0kxoTbAyRUhFSA1xgBUk4v5ZJDyAPPI4yBzWMYCxKISeGsiKILngwHYpuJ"
    "Ateq1TnMvundxqne3eJWH0Q2Hi/msMbbkUoLdQJsAlJsjQUgRuZvE+De7u4LAHKrmQClLg"
    "uQv5HBcA9mIX7pddrlEFMuOZCXmCd4bSGTbSsOoux2M7HOoSiyFkG7lN47aXhb5/qPPNfG"
    "186RpOBRZhO5ilzgiDMWLXN4l9r8QjAA5t0jIJZR0HiaN8u2qHI1Ny8BGNiSlchY5BcdIj"
    "3TI7DsdAkVcw8XKkzo6g+XazWgUO44Ggx+Qb7s7ft5s97zJgZd2iqbOHAlwRaPCWATFkim"
    "3F+5darnev/UuOh2Tg4VF7CR4RNveIO7l71eS28fKiSgFAF8gy9Of/Zajd6h4o/GFJn0Br"
    "fa3AfhoUe4I5eoS7Tg6ks6cHV2A64W+i+N9+ELi3pq/+e63oxmu5rSToAFviXyM0BJNR9z"
    "DUMuLEeX9czxsyLXnfjHhtIkEFgd7IyjHjQHXb913uz19fOLzHl2rPebQqNJ6Tgn3TrIle"
    "50EeV7q3+qiEflqtNu5o+9qV3/ShUxgYB5BvYeDWCl2mUsTYJP/a/8TDAW6u8pj/9pMxQm"
    "iyzDIsAT3jGQjc/guNDlc9yi2eAyWmbz+E3iGoilSW0R8DgdGNKlwdPjSUEWHnd6r6EfN9"
    "XJ60xjEmzJMBYDnz2LiYTWMIq9z13rnbsYrzybALe0sR0heybDnONS/S1i9bdhftK0SqWm"
    "7VYO6tX9Wq1a351SLarm4T1qfRaEM+dRcR54uFsY7tTlHetMrENEKDPkU+lHQznZrNfbvG"
    "ZZyz2VA5agmXFaCma+Vv8JliafgZf7Ash6vn8BvOoXgASzyD1Z7qOZljT9yO/krAsdwMqv"
    "y/MXYJv3F8+aciern00nvwHT+Xb7"
)
