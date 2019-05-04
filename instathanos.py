from InstagramAPI import InstagramAPI

def get_vampires(api, user_id, get_ids = False):
    vampires = []

    followers = api.getTotalFollowers(user_id)
    followers_list = []
    for follower in followers:
        if get_ids:
            followers_list.append(follower['pk'])
        else:
            followers_list.append(follower['username'])

    followings = api.getTotalFollowings(user_id)
    following_list = []
    for following in followings:
        if get_ids:
            following_list.append(following['pk'])
        else:
            following_list.append(following['username'])

    for following in following_list:
        if following not in followers_list:
            vampires.append(following)

    return vampires

def unfollow_vampires(api, user_id):
    for vampire_id in get_vampires(api, user_id, True):
        api.unfollow(vampire_id)

if __name__ == "__main__":
    api = InstagramAPI("username", "password")
    api.login()

    user_id = api.username_id

    vampires = get_vampires(api, user_id)

    unfollow_vampires(api, user_id)

    print('Unfollowed: ', vampires)
