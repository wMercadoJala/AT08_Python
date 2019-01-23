def age_identifier(age):
    if 13 <= age <= 17:
        return "You are a teenager"
    if 18 <= age <= 29:
        return "You are young"
    if age >= 30:
        return "Your are adult"
    return "You are a child"
