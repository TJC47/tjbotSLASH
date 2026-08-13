class Styles:
    blue = {
        " ": "⬛",
        "0": "0️⃣",
        "1": "1️⃣",
        "2": "2️⃣",
        "3": "3️⃣",
        "4": "4️⃣",
        "5": "5️⃣",
        "6": "6️⃣",
        "7": "7️⃣",
        "8": "8️⃣",
        "9": "9️⃣",
        "a": "🇦",
        "b": "🇧",
        "c": "🇨",
        "d": "🇩",
        "e": "🇪",
        "f": "🇫",
        "g": "🇬",
        "h": "🇭",
        "i": "🇮",
        "j": "🇯",
        "k": "🇰",
        "l": "🇱",
        "m": "🇲",
        "n": "🇳",
        "o": "🇴",
        "p": "🇵",
        "q": "🇶",
        "r": "🇷",
        "s": "🇸",
        "t": "🇹",
        "u": "🇺",
        "v": "🇻",
        "w": "🇼",
        "x": "🇽",
        "y": "🇾",
        "z": "🇿"
    }
    discord = {
        " ": "⬛",
        "0": "0️⃣",
        "1": "1️⃣",
        "2": "2️⃣",
        "3": "3️⃣",
        "4": "4️⃣",
        "5": "5️⃣",
        "6": "6️⃣",
        "7": "7️⃣",
        "8": "8️⃣",
        "9": "9️⃣",
        "a": ":regional_indicator_a:",
        "b": ":regional_indicator_b:",
        "c": ":regional_indicator_c:",
        "d": ":regional_indicator_d:",
        "e": ":regional_indicator_e:",
        "f": ":regional_indicator_f:",
        "g": ":regional_indicator_g:",
        "h": ":regional_indicator_h:",
        "i": ":regional_indicator_i:",
        "j": ":regional_indicator_j:",
        "k": ":regional_indicator_k:",
        "l": ":regional_indicator_l:",
        "m": ":regional_indicator_m:",
        "n": ":regional_indicator_n:",
        "o": ":regional_indicator_o:",
        "p": ":regional_indicator_p:",
        "q": ":regional_indicator_q:",
        "r": ":regional_indicator_r:",
        "s": ":regional_indicator_s:",
        "t": ":regional_indicator_t:",
        "u": ":regional_indicator_u:",
        "v": ":regional_indicator_v:",
        "w": ":regional_indicator_w:",
        "x": ":regional_indicator_x:",
        "y": ":regional_indicator_y:",
        "z": ":regional_indicator_z:"
    }
    """The default style as you know and love it!"""

class StylizedString:
    def __init__(self, string: str):
        self.unformatted = string
    def __str__(self) -> str:
        return self.unformatted
    
    def format(self, style: dict[str, str] = Styles.blue) -> str:
        stylized = ""
        for char in self.unformatted:
            stylized += style.get(char.lower(), char)

        return stylized
    

def quickstyle(string: str, style: dict[str, str] = Styles.blue) -> str:
    """A quick way to stylize a string without creating an instance of StylizedString."""
    return StylizedString(string).format(style)