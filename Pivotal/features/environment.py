def before_all(context):
        print("****************** PIVOTAL TRACKER API TESTING **************")


def before_feature(context, feature):
    if 'smoke' in feature.tags:
        print("****************** SMOKE TESTS **************")

    elif 'acceptance' in feature.tags:
        print("****************** ACCEPTANCE TESTS **************")
