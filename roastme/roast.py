from random import getrandbits, choice


def create_roast(user_id, roasts_pieces):
    adjective = choice(roasts_pieces["adjectives"])
    include_adverb = getrandbits(1)

    if include_adverb:
        adverb = choice(roasts_pieces["adverbs"])
        return f"<@{user_id}> is {adverb} {adjective}"
    else:
        return f"<@{user_id}> is {adjective}"

def formatted_id(user_id):
    return f"<@{user_id}>"

def roast_tagged_user(user_id, roasts_full, roasts_pieces):
    craft_roast = getrandbits(1)

    if craft_roast:
        return create_roast(user_id, roasts_pieces)
    else:
        roast = choice(roasts_full)
        formatted_roast = roast.format(user=formatted_id(user_id))
        return formatted_roast
