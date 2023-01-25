# Twitter Search Mockup
# Kyle Simmons
# Requires Elevated Developer Access on Twitter to run.

import tweepy


BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAANgkgEAAAAAUX79Ycp3rd8lcY%2BhyVfJletTKVE%3D2BqVg4JOAuQUfoTvOBPDU3TNYZ3g7970sOUkJHTjMYv1OsZVTw"
#Fake_Amazon_Token = "BsnFNoUoKPrfRgWP4Eh2W8nT9pI3v5hGUcwYA3q"

def search_username(keyword, results_master_list, results_usernames):
    auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)  # Authorizes user to API
    api = tweepy.API(auth)
    # Search for users with the keyword in their username, name, or description
    users = tweepy.Cursor(api.search_users, q=keyword).items(200)  # 500 is maximum
    # Print the screen names of the found users
    for user in users:
        userinfo = [user.screen_name, user.id_str, user.name]  # output the handle, the ID, and the
        # chosen name of the user into a list
        results_master_list.append(userinfo)  # add the list to a master list
        results_usernames.append(user.screen_name)  # add usernames into username list
    return results_master_list, results_usernames
def main():
    input_keywords = input("Enter keywords separated by comma: ")
    keyword_list = input_keywords.split(",")
    results_master_list = []  # all data related to user
    results_usernames = []  # screen names of users
    for keyword in keyword_list:
        results_master_list, results_usernames = search_username(keyword, results_master_list, results_usernames)
    deduplicated_list = []  # deduplicates list of user data for writing into output
    for user_data in results_master_list:
        if user_data not in deduplicated_list:
            deduplicated_list.append(user_data)

if __name__ == '__main__':
    main()
    
