cat_type = input()
cat_gender = input()

if cat_type == "British Shorthair":
    if cat_gender == "m":
        human_months = 13 * 12
        cat_months = human_months / 6
    else:
        human_months = 14 * 12
        cat_months = human_months / 6
    print(f"{cat_months:.0f} cat months")

elif cat_type == "Siamese":
    if cat_gender == "m":
        human_months = 15 * 12
        cat_months = human_months / 6
    else:
        human_months = 16 * 12
        cat_months = human_months / 6
    print(f"{cat_months:.0f} cat months")
elif cat_type == "Persian":
    if cat_gender == "m":
        human_months = 14 * 12
        cat_months = human_months / 6
    else:
        human_months = 15 * 12
        cat_months = human_months / 6
    print(f"{cat_months:.0f} cat months")
elif cat_type == "Ragdoll":
    if cat_gender == "m":
        human_months = 16 * 12
        cat_months = human_months / 6
    else:
        human_months = 17 * 12
        cat_months = human_months / 6
    print(f"{cat_months:.0f} cat months")
elif cat_type == "American Shorthair":
    if cat_gender == "m":
        human_months = 12 * 12
        cat_months = human_months / 6
    else:
        human_months = 13 * 12
        cat_months = human_months / 6
    print(f"{cat_months:.0f} cat months")
elif cat_type == "Siberian":
    if cat_gender == "m":
        human_months = 11 * 12
        cat_months = human_months / 6
    else:
        human_months = 12 * 12
        cat_months = human_months / 6
    print(f"{cat_months:.0f} cat months")
else:
    print(f"{cat_type} is invalid cat!")

