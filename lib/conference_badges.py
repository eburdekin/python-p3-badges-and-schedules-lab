def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    # badges = []
    # for name in names:
    #     badge = badge_maker(name)
    #     badges.append(badge)
    # return badges
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    # rooms = []
    # for index, name in enumerate(names):
    #     room_assignment = f"Hello, {name}! You'll be assigned to room {index+1}!"
    #     rooms.append(room_assignment)
    # return rooms
    return [
        f"Hello, {name}! You'll be assigned to room {index+1}!"
        for index, name in enumerate(names)
    ]


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    output = "\n".join(badges + rooms)
    print(output)
