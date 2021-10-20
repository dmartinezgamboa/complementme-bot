from random import randrange


def roast_tagged_user(user_id, insults_data):
    random_index = randrange(0, len(insults_data["adjectives"]))
    adjective = insults_data["adjectives"][random_index]
    include_adverb = bool(randrange(0, 2))

    if include_adverb:
        random_index = randrange(0, len(insults_data["adverbs"]))
        adverb = insults_data["adverbs"][random_index]
        return f"<@{user_id}> is {adverb} {adjective}"
    else:
        return f"<@{user_id}> is {adjective}"
