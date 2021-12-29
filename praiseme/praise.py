from random import getrandbits, choice


def create_praise(user_id, praises_pieces):
    adjective = choice(praises_pieces["adjectives"])
    include_adverb = getrandbits(1)

    if include_adverb:
        adverb = choice(praises_pieces["adverbs"])
        return f"<@{user_id}> is {adverb} {adjective}"
    else:
        return f"<@{user_id}> is {adjective}"

def formatted_id(user_id):
    return f"<@{user_id}>"

def praise_tagged_user(user_id, praises_full, praises_pieces):
    craft_praise = getrandbits(1)

    if craft_praise:
        return create_praise(user_id, praises_pieces)
    else:
        praise = choice(praises_full)
        formatted_praise = praise.format(user=formatted_id(user_id))
        return formatted_praise
