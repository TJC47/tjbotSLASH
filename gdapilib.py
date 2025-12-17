import requests
import base64

class LevelComment:
    def __init__(self, level_id: int, comment: str, author_player_id: int, author_name: str, likes: int, message_id: int, spam: bool, author_account_id: int, age: str, percent: int = 0, mod_badge: int = 0, moderator_chat_color: str = ""):
        self.level_id = level_id
        self.comment = comment
        self.author_player_id = author_player_id
        self.author_name = author_name
        self.likes = likes
        self.message_id = message_id
        self.spam = spam
        self.author_account_id = author_account_id
        self.age = age
        self.percent = percent
        self.mod_badge = mod_badge
        self.moderator_chat_color = moderator_chat_color

    def get_as_dict(self):
        return {
            "level_id": self.level_id,
            "comment": self.comment,
            "author_player_id": self.author_player_id,
            "author_name": self.author_name,
            "likes": self.likes,
            "message_id": self.message_id,
            "spam": self.spam,
            "author_account_id": self.author_account_id,
            "age": self.age,
            "percent": self.percent,
            "mod_badge": self.mod_badge,
            "moderator_chat_color": self.moderator_chat_color
        }

    def __str__(self):
        return self.comment

class Level:
    def __init__(self, level_id: int):
        self.level_id = level_id

    def get_comments(self, api_handler):
        return api_handler.get_level_comments(self.level_id)

class ApiHandler:
    def __init__(self, api_url: str = "https://www.boomlings.com/database"):
        self.api_url = api_url

    def keyed_to_dict(self, string: str, key_character: str = ":"):
        """
        Turns a keyed string into an easy to use dict (Robtop encoding is bad)
        """
        listed_keys = string.split(key_character)
        finaldict = {}
        for key_number in range(len(listed_keys[::2])):
            finaldict[listed_keys[::2][key_number]] = listed_keys[1::2][key_number]
        return finaldict

    def get_level_comments(self, level_id: int, page: int = 0):
        """
        Returns a list of comment objects for the specified level ID
        """
        data = {
            "levelID": level_id,
            "page": page,
            "secret": "Wmfd2893gb7"
        }
        headers = {
            "User-Agent": ""
        }
        req = requests.post(f"{self.api_url}/getGJComments21.php", data=data, headers=headers)

        all_comment_objects = []
        all_comments, page_info = req.text.split("#", 1)[0].split("|"), req.text.split("#", 1)[1]

        for comment in all_comments:
            if comment == "":
                continue
            comment_string, user_string = comment.split(":", 1)
            comment_data = self.keyed_to_dict(comment_string, key_character="~")
            user_data = self.keyed_to_dict(user_string, key_character="~")
            comment_obj = LevelComment(
                level_id=level_id,
                comment = base64.b64decode(comment_data["2"], altchars="_-").decode("utf-8") if "2" in comment_data else "",
                author_player_id=int(comment_data["3"]),
                author_name=user_data["1"],
                likes=int(comment_data["4"]),
                message_id=int(comment_data["6"]),
                spam=comment_data["7"] == "1",
                author_account_id=int(user_data["16"]),
                age=comment_data["9"],
                percent=int(comment_data["10"]),
                mod_badge=int(comment_data["11"]) if "11" in comment_data else 0,
                moderator_chat_color=comment_data["12"] if "12" in comment_data else ""
            )
            all_comment_objects.append(comment_obj)
        return all_comment_objects

    def get_level(self, level_id: int):
        """
        Returns a Level Object for the Specified level ID
        """
        data = {
            "levelID": level_id,
            "secret": "Wmfd2893gb7"
        }
        headers = {
            "User-Agent": ""
        }
        req = requests.post(f"{self.api_url}/downloadGJLevel22.php", data=data, headers=headers)