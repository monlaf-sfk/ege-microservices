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
    "value" INT NOT NULL,
    "updated_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "user_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_scores_user_id_04f4e8" UNIQUE ("user_id", "subject")
);
COMMENT ON COLUMN "scores"."subject" IS 'MATH_PROF: math_prof\nRUSSIAN: russian\nPHYSICS: physics\nINF: informatics';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmOtT2kAQwP+VTD7ZGetoFLF+i4iVWsEB7MPHZI7kCFeTS7y7qIzD/967y/sBFQYqtn"
    "4j+0h2f2x2N/esup4FHbqlQ4LMkXqoPKsYuJD/KGg2FRX4fioXAgYGjjQFqc2AMgJMxqVD"
    "4FDIRRakJkE+Qx7mUhw4jhB6JjdE2E5FAUb3ATSYZ0M2goQrrm+5GGELPkEaX/p3xhBBx8"
    "qFiizxbCk32NiXshZmJ9JQPG1gmJ4TuDg19sds5OHEGmEmpDbEkAAGxe0ZCUT4Iroozzij"
    "MNLUJAwx42PBIQgclkn3hQxMDwt+PBoqE7TFUz5qO3v1vYPd/b0DbiIjSST1SZhemnvoKA"
    "m0++pE6gEDoYXEmHJ7gISKkErwGiNAqullXAoIeeBFhDGwWQxjQQoxLZwlUXTBk+FAbDNR"
    "4FqtNoPZN73bONW7G9zqg8jG48Uc1ng7UmmhToBNQYpXYw6IkfnbBLizvf0CgNxqKkCpyw"
    "PkT2QwfAfzEL/0Ou1qiBmXAshLzBO8tpDJNhUHUXa7nlhnUBRZi6BdSu+dLLyNc/1HkWvj"
    "a+dIUvAos4m8i7zBEWcsWubwLvPyC8EAmHePgFhGSeNp3jTbssrV3KIEYGBLViJjkV80RH"
    "qmR2DVdAkVM4cLFSZ0+cPlWg0olG8cDQa/IL/t7fu8We28iUFXtsomDlxJsMVjAtiEJZIZ"
    "91duneq53j81Lrqdk0PFBWxk+MQb3uDuZa/X0tuHCgkoRQDf4IvTn71Wo3eo+KMxRSa9wa"
    "0290F46BHuyCXqAi249pIOXJvegGul/vsAnADOUdSJ/Z/rej2a7XJKOwUW+JbIzwAV1XzM"
    "NQy5sBpd3rPAz4pct+Ifa0qTQGB1sDOOetAMdP3WebPX188vcvPsWO83hUaT0nFBurFfKN"
    "3kJsr3Vv9UEZfKVafdLI69xK5/pYqYQMA8A3uPBrAy7TKWpsFn/lc+E4y5+nvG4396GUqb"
    "RZ5hGeAJH+PIxmdwXOryBW7RbnAZ3Wb9+E3iGoilaW0R8JgsDNnS4OnxpCALx53ea+jHTX"
    "XyOtuYBFuxjMXAp+9iIqEVrGLve9dq9y7GK88mwK1sbEfInsqw4LhQf4tY/W2YnzRtd7eu"
    "be/uH9T26vXawXZCtayahfeo9VkQzs2j8j7wcDc33MTlHetUrENEKDPkVeVHQzXZvNfbPG"
    "ZZyTmVAxagmXNaCGaxVv8JlibfgRf7Ash7vn8BvOoXgAQzzzlZ5jgjOZkqNP3I7+SsCx3A"
    "qo/Liwdg6/cXT9tyJ8vfTSe/AfTHdv0="
)
