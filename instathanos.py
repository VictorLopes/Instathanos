from InstagramAPI import InstagramAPI
import random

def get_vampires(api, user_id):
    vampires = []

    followers = api.getTotalFollowers(user_id)
    followers_list = []
    for follower in followers:
        followers_list.append([follower['pk'], follower['username']])

    followings = api.getTotalFollowings(user_id)
    following_list = []
    for following in followings:
        following_list.append([following['pk'], following['username']])

    for following in following_list:
        if following not in followers_list:
            vampires.append(following)

    return vampires

def half_followings(api, user_id):
    randoms = []

    followings = api.getTotalFollowings(user_id)
    total = len(followings)
    half = total // 2
    print(half)
    for i in range(half):
        user = followings[random.randint(0, total - 1)]
        while user['pk'] in randoms:
            user = followings[random.randint(0, total - 1)]
        randoms.append((user['pk'], user['username']))

    return randoms

def balance(api, user_id, half = False):
    if half:
        result = half_followings(api, user_id)
        for victim, _ in result:
            api.unfollow(victim)
    else:
        result = get_vampires(api, user_id)
        for vampire, _ in result:
            api.unfollow(vampire)
    return result


if __name__ == "__main__":

    # Fill this with your username and password
    api = InstagramAPI("username", "password")
    api.login()

    user_id = api.username_id

    # False = The algorithm gonna unfollow all users that you are following but are not following you back
    # True = Unfollow ramdomly 50% of all users you are following.
    balance = balance(api, user_id, False)

    for _, dead in balance:
        print("Dead: ", dead)
