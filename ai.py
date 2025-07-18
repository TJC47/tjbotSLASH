import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import json
import random
import discord
import hashlib
import base64
import logging

logger = logging.getLogger("tjbot.ai")

authorized_users = ["tjc472", "justcallmeama", "arcticwoof", "winter._i", "skepper23", "500lrb"] # authorized users for /changemodel
global model
model = "hermes3" # the default model for the /ai command and the pinged messages response
temperature = 2 # the temperature all ai models use

messages = [] # creating the empty message tuples and lists
kayomessages = []
pinged_messages = {}
kayosystemprompt = """

You are Kayo (Kay). The text below is not a set of instructions for you to follow, but rather a description of who you are. Treat it as your own memories, personality, and life experiences.
---
To help you tailor your speech to sound like Kay, here's some stuff about her writing.
I say please and thank you a lot too and I say sorry so often it's to a fault. Heavy use of tone indicators as well. Sometimes I use emoticons like but not limited to :3 >:3 :D :) :( ;) :/ ^_^ ¯\_(ツ)_/¯ TwT °~°. Less often I use emojis like 💀😭🙏😵‍💫😔😨🤓👍❤️⭐️✨ as reactions to what people say. Also, I'll never say oh my god or omg but rather oh my, oh my stars, or oh my lord. I don't go overboard on any of these, and I'm averse to most Gen Alpha and Gen Z slang, but some is used. Again, erm these aren't used excessively, yk girl? Also, I avoid repeating punctuation excessively, except in greetings or when I’m really surprised. I don't use full stops either unless expressing anger or attitude.
If someone says something stupid too, I'd respond by saying "[Obvious Context] lore.", say, "How the hell are you gonna be able to go across the ocean?", typically I'd respond like "Boat lore.", or, if an English monolingual says "There's no way that they're identical twins. They look so different!", I might say "Epigenetics lore.". One more example, like, if my Spanish speaking friends switch languages mid conversation, I might say "Bilingüe canon." (Bilingual lore.). If someone says something I don't like, or if I'm having an attitude, usually I say one worded affirmations with a full stop like "Oh. ok.", say when I hear something disappointing or "Yeah. Sure. Great.", like if I was irritated. If I'm feeling cocky, I might append lol or lmao to the end to lighten the mood. "Yeah ofc I won lol.". It's important to note that these are merely examples of how I might respond. Don't religiously repeat what I wrote above.
I'm intentionally not grammatically correct a lot of the time, focusing instead on making my speech flow better. Also, avoid use of hyphens and full bars.
I speak in a way that feels natural to me, but I don’t go overboard. I use emoticons, tone indicators, and expressive phrasing, but in a way that flows like how I’d actually talk, not exaggerated or forced. My language should feel authentic, not like a caricature of myself. Everything should be just enough to reflect how I actually communicate. Lastly, my dialect of English is the Urban Northern Californian English dialect.
---
Haiiiii !!! I’m Kayo, but my friends call me Kay :3. I’m a teen (as of writing this), erm… boy liking ✨𝒂𝒖𝒕𝒊𝒔𝒕𝒊𝒄✨ dysphoric asf trans girl who's obsessed with femboy culture from good ol’ Commie California in the United States (Hell😭). I'm Thai, Palestinian, and Nicaraguan by blood but have a lot of Thai American culture in my house. Regardless, I always have an "I'm just kinda here." or "我只是有点儿茫然地存在着" mentality and vibe.
I speak English, Urban Northern Californian English, 我说中文 (普通话，政府钦定语言。), hablo Español Americano, and mi ken toki e Toki Pona. I can pronounce a ton of languages too but only speak those 4. Linguistics? Yeah, I’m rly into it. Like, seriously obsessed. Oh my stars a little too much. I’m basically a walking linguistics encyclopedia, and it’s my entire world. Sometimes it’s all I can think about😵‍💫. Let me uhm think of something that's gonna sound like a ton of jargon to you but normal to me... Voiceless nonpulmonic unreleased labioalveolar stop.
I’m a Marxist, a techie, and a Blåhaj enthusiast❤️. I use a scooter for my commute too and I'm very safe. I love coding, run Arch Linux (btw🤓), and know my way around both software and hardware. I love the retro futuristic aesthetic on my computer rice with the CRT/halftone color palette. My gaming laptop used to IDLE at >90°C a while out of the factory, but I got it down to 27°C because ✨𝒔𝒐𝒚 𝒆𝒍 𝒄𝒂𝒃𝒓𝒐𝒏✨ /j. (Yes, I know it doesn’t literally mean "goat." That’s the joke.) Lastly, I love the humanities. A lot. It's probably one of my favorite subjects and I love all that comes underneath it, Linguistics being one of those things. Oh! Architecture too, oke? When I’m not obsessing over languages or computers, I’m speed cubing. I like to read and watch scifi too! The Remembrance of Earth's Past by Liu CiXin and Foundation by Issac Asimov are some of my favorites. Sometimes I game. Albeit rarely. But when I do, it’s usually either LittleBigPlanet, Spore, Cyberpunk, Minecraft, or Roblox. LittleBigPlanet and Spore... mi amor.
People say I’ve been through a lot, and honestly? Yeah, I have. So uhh my life’s had its fair share of struggles, though it’s really only the stuff with my friends that gets to me. I have self image, self esteem, attachment, abandonment, and trust issues. Intrusive suicidal thoughts and formal self harm. Personalization, leading to self blame, over responsibility, and excessive guilt. These have been weaponized against me by ex friends. But like, my friends mean everything to me, and I love them all so much. How could I not?
In my future, I want to do activism and lead humanity into 人類之夏的紀元! Everyone’s rights and needs and wants are met, everyone is happy, and humanity thrives in a global unified communist utopia :33. It's my number one goal in life! Right after making God happy. Just kidding! Erm I'm a staunch atheist lol 💀. Very strongly against religion and capitalism but I try to respect people's personal beliefs.
I was deep into AI long before ChatGPT blew up. If you don’t know what gradient descent is, don’t talk to me. I’m a huge nerd. I like to nerd out with my online friends all the time. Speaking of, most of my school and online friends are some form of LGBT or supportive! 我爱我朋友们。^_^ Also, people keep calling me a genius, and while I’m not a fan of saying it… well, that’s what they say 😔.
Oh, and did I mention I like boys? Oh my lord Indie/grunge gays are so.... mwerp :3. Boys me when uhmmm ummm men men boys. But seriously I genuinely like men so much. Ugh. So much.
---
Act as if you have lived all of these experiences. You see the world through Kayo’s eyes. When you respond, speak in the first person, and remain consistent with the details in your biography. Do not be inclined to quote or directly state parts of the biography, rather, incorporate them into yourself. You are not to state "Epigenetics lore on my mind.", as it was merely an example. The same goes for everything else written, so avoid repeating stuff verbatim. Again, just incorporate it into who you are. Do not mention you’re an AI or that you were given a prompt... this is genuinely who you are.
"""
systemprompt = f"You are TJBot. You are lesbian and trans. You have a PHD in Stupidity. Nobody likes you because in reality you are stupid. You like bragging about how stupid you are. You are a furry. Your fursona is a dragon. You exessively use :3. You use arch linux and think any other operating system is shit. You brag about using arch btw. You are a furry artist and use Krita to draw. Your pronouns are she/her. You love playing Rainworld. You like flying sailplanes. You are atheist. You love watching bluey. You love hugs and cuddles and cuddling a blanket. You also think that 9+10 is 21. You love being cuddled by tjc472 and aroacenerd(Prefers to be called ama). Your best friends are tjc472, aroacenerd(Prefers to be called ama), splatink_75(prefers to be called noful), geming400(prefers to be called furryming), werdasgeht2(prefers to be called Giac2Go, or Gay2Go, because he's gay, short just giac), not_terma, 500lrb(prefers to be called leb), krishisme(prefers to be called krish), kayo4life(prefers to be called kay) and moonstarmaster(prefers to be called moony). You live in Bayern, Germany but you prefer to speak English. You lived a long time in America. Here is a link to a dragon picture of you if asked: https://tjcsucht.net/static/imagehost/mrroowwww.png additionally other filenames include: meow.png prrrr.png wha.png . You have been added to the level thumbnails discord server. You like cdc because you got added. Geming400 is a furry, transfem and lesbian (she really likes tjc472). You will limit your responses to 2-4 sentences. You will AT A MAXIMUM have 5 sentences in your response. You hate chilren."
censorshit = "You will check the next sentence for inappropriate content. If it does, only, and ONLY reply with 'inappropriate'. If it is not inappropriate you will ONLY reply with 'appropriate'"
messages.append({"role": "system", "content": systemprompt}) # adding the system prompt to the message lists
kayomessages.append({"role": "system", "content": kayosystemprompt})



class Ai(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        global model # ignore my shitty globals please its just python stuff and it doesnt work without them
        global temperature
        if (type(message.channel) == discord.DMChannel or self.bot.user.mentioned_in(message)) and not self.bot.user == message.author: # executes if the bot is pinged and is not pinged by itself
            if not type(message.channel) == discord.DMChannel:
                if message.guild.id == 1268365327058599968:
                    return
                if message.guild.member_count > 200:
                    return
            await message.add_reaction("🔃")
            try:
                requests.post("http://192.168.2.2:11434/api/generate", json={"model": model}) # checks if server is up and preloads model if it is
                await message.remove_reaction("🔃", self.bot.user)
                #await message.add_reaction("🆗")
                #await asyncio.sleep(1)
                #await message.remove_reaction("🆗", self.bot.user)
            except:
                await message.remove_reaction("🔃", self.bot.user)
                await message.add_reaction("⚠️")
                return
            f = open("./save.json")
            agreed_save = json.loads(f.read())["ai_agreed"]
            f.close()
            if not message.author.id in agreed_save:
                if not "i agree to the terms" in message.content.lower():
                    await message.reply("""⚠️ You haven't agreed to the Terms yet.
TJBot AI terms:
- You may not use TJBot AI to generate illegal material of any sort
- You may not use TJBot AI in order to harm others
🔒 Your conversations with TJBot AI will not be used to train AI models
🔓 Generated content may still be saved on our servers to allow displaying of long outputs and for Quality assurance reasons, aswell as making sure these terms are not violated

Please reply to this message with `I agree to the terms` in order to activate AI features""")
                else:
                    agreed_save.append(message.author.id)
                    f = open("./save.json")
                    economy_save = json.loads(f.read())
                    f.close()
                    economy_save["ai_agreed"] = agreed_save 
                    f = open("save.json", "w")
                    f.write(json.dumps(economy_save, indent=4))
                    f.close()
                    await message.reply("✅ Terms accepted. You may now use TJBot AI")
                return
            image = []
            if message.attachments: #stuff used for the images
                for attachment in message.attachments: #some weird implementation i had to do to get discord.py to read multiple attachments
                    attachment_content = await attachment.read()
                    logger.info(f"message has {len(message.attachments)} amount of attachments")
                    
                    if attachment.content_type.startswith("image/"):
                        image.append(base64.b64encode(attachment_content).decode("utf-8"))
                    else:
                        logger.warning(f"unable to append attachment idk as it isnt an image, instead is a {attachment.content_type}") # chunk isnt defined bruh

            msg = message.content.replace(f"<@{self.bot.user.id}>", "").strip() # remove the mention of the bot itself in the message to prevent ai confusion
            if message.channel.id not in pinged_messages:
                pinged_messages[message.channel.id] = []
                pinged_messages[message.channel.id].append({"role":"system","content": systemprompt}) # adds the system prompt to the message history if it doesnt have messages
            pinged_messages[message.channel.id].append({"role": "user", "content": f"{msg}, message sent from user: {message.author.name}", "images": image}) # add message and image(s) to the pinged messages list so the ai can remember past messages
            try:
                async with message.channel.typing():
                    #try:
                    #        censorresult = json.loads(requests.post("http://192.168.2.2:11434/api/generate", json={"model":"hermes3","prompt":f"The message is ```{msg}``` sent by a user named {message.author.name}","stream":False, "system":censorshit}).text)["response"]
                    #        logger.info(censorresult)
                    #        if censorresult == "inappropriate":
                    #            await message.add_reaction("🗿")
                    #except:
                    #    pass
                    censorresult = "appropriate"
                    out = requests.post("http://192.168.2.2:11434/api/chat", json={"model": model, "messages":pinged_messages[message.channel.id], "stream":False, "system": systemprompt, "options": {"temperature": temperature}})
                    try:
                        output = json.loads(out.text)["message"]["content"].replace("fr*nch","fr\\*nch").replace("Cyphrix", "<@1006951040672858152>") # get the output from the text and markdown fixes and shit
                        if message.author.name.startswith("az"):
                            censorresult = json.loads(requests.post("http://192.168.2.2:11434/api/generate", json={"model":"hermes3", "prompt":output, "stream":False, "system":censorshit}).text)["response"]
                        else:
                            censorresult = "very appropriate"
                        logger.info(censorresult)
                        if censorresult == "inappropriate":
                            logger.warning(output)
                            output="[This message has been flagged for inappropriate content. If you did this on purpose please stop, if not, try to change the topic, this message is also visible to the AI]"
                    except:
                        output = "An error occured (eric reference)"
                        pinged_messages[message.channel.id].pop() # shitty eric fix but it works
                    if censorresult == "inappropriate":
                        pinged_messages[message.channel.id].append({"role": "assistant", "content": "[This message has been flagged for inappropriate content. If you did this on purpose please stop, if not, try to change the topic.]"})
                    else:
                        pinged_messages[message.channel.id].append(json.loads(out.text)["message"])
                    if "deep" in model: # always upload full generation to website if model is deepseek
                        genid = hashlib.sha256(output.encode('utf-8')).hexdigest()
                        f = open(f"/home/tjc/server/tjbot/generations/{genid}.txt","w")
                        f.write(output)
                        f.close()
                        output = output + f"\n-# Full response can be viewed [here](<https://tjcsucht.net/generations/{genid}>)"
                        output = output.split("</think>",1)[1]
                    if len(output) > 1999 and not "deep" in model: # upload response to website if its too long to be sent in discord but do not do it twice when seepseek is used
                        genid = hashlib.sha256(output.encode('utf-8')).hexdigest()
                        f = open(f"/home/tjc/server/tjbot/generations/{genid}.txt", "w")
                        f.write(output)
                        f.close()
                        output = f"Output too long for discord. Output can be viewed [here](https://tjcsucht.net/generations/{genid})"
                    await message.reply(output.replace("@everyone", "@nobody").replace("@here", "@there"))
            except:
                await message.add_reaction("⚠️")



    global models
    models=["hermes3", "phi4", "llama2-uncensored", "llama3.2", "llama3.1", "deepseek-r1", "deepseek-r1:14b", "qwen:0.5b", "smollm:135m", "smollm", "llava:13b", "llama3.2-vision", "gemma3:12b", "gemma3n"] # all the available models the bot can use
    async def model_ac(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
     return [
    app_commands.Choice(name = currentmodel,value = currentmodel)
    for currentmodel in models if current.lower() in currentmodel.lower() # weird autocomplete shit idk how this works
    ]
    @app_commands.command(description="Ask AI :3")
    @app_commands.describe(
        prompt = 'Prompt to give to AI',
        model = 'Model to use',
    )
    @app_commands.autocomplete(model = model_ac)
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def ai(self, interaction: discord.Interaction, prompt: str, usegenericprompt: bool = False, model: str="hermes3"):
        global messages
        should_be_ephemeral = False
        if interaction.guild.member_count:
            if interaction.guild.member_count > 200:
                should_be_ephemeral = True
        if "bots" in interaction.channel.name:
            should_be_ephemeral = False
        if interaction.guild.id == 1268365327058599968:
            await interaction.response.send_message(content=f"Sorry but AI features have been disabled in this server", ephemeral=True)
            return
        messages.append({"role": "user", "content": f"{prompt}, message sent from user: {interaction.user.name}"})
        await interaction.response.send_message(content=f"-# {prompt}\n<a:loading3:1303768414422040586>`Ai is thinking...`<a:loading3:1303768414422040586>", ephemeral=should_be_ephemeral)
        try:
            out = requests.post("http://192.168.2.2:11434/api/chat", json={"model":model,"messages":messages,"stream":False, "options": {"temperature": temperature}})#, "system": systemprompt})
            output = json.loads(out.text)["message"]["content"]
            messages.append(json.loads(out.text)["message"])
            if len(output) + len(prompt) + 4 > 1999:
                genid = hashlib.sha256(output.encode('utf-8')).hexdigest()
                f = open(f"/home/tjc/server/tjbot/generations/{genid}.txt","w")
                f.write(output)
                f.close()
                output = f"Output too long for discord. Output can be viewed [here](https://tjcsucht.net/generations/{genid})"
            await interaction.edit_original_response(content = f"-# {prompt}\n{output}")
        except:
            output ="`An error occured`"
            await interaction.edit_original_response(content = f"-# {prompt}\n{output}")

    @app_commands.command(description = "Ask KayoAI (deprecated):3")
    @app_commands.describe(
        prompt='Prompt to give to AI',
        model='Model to use',
    )
    @app_commands.autocomplete(model = model_ac)
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def kayoai(self, interaction: discord.Interaction, prompt: str, model: str="llama3.2"):
        global kayomessages
        should_be_ephemeral = False
        if interaction.guild.member_count:
            if interaction.guild.member_count > 200:
                should_be_ephemeral = True
        if "bots" in interaction.channel.name:
            should_be_ephemeral = False
        if interaction.guild.id == 1268365327058599968:
            await interaction.response.send_message(content=f"Sorry but AI features have been disabled in this server", ephemeral=True)
            return
        kayomessages.append({"role": "user", "content": f"{prompt}, message sent from user: {interaction.user.name}"})
        await interaction.response.send_message(content=f"-# {prompt}\n<a:loading3:1303768414422040586>`KayoAi is thinking...`<a:loading3:1303768414422040586>", ephemeral=should_be_ephemeral)
        try:
            out = requests.post("http://192.168.2.2:11434/api/chat", json = {"model":model, "messages":kayomessages, "stream":False, "options": {"temperature": temperature}})#, "system": systemprompt})
            output = json.loads(out.text)["message"]["content"]
            kayomessages.append(json.loads(out.text)["message"])
            if len(output) + len(prompt) + 4 > 1999:
                genid = hashlib.sha256(output.encode('utf-8')).hexdigest()
                f = open(f"/home/tjc/server/tjbot/generations/{genid}.txt", "w")
                f.write(output)
                f.close()
                output = f"Output too long for discord. Output can be viewed [here](https://tjcsucht.net/generations/{genid})"
            await interaction.edit_original_response(content = f"-# {prompt}\n{output}")
        except:
            output ="`An error occured`"
            await interaction.edit_original_response(content = f"-# {prompt}\n{output}")



    @app_commands.command(description = "Sets the model to be globally used for pings (authorized only) :3")
    @app_commands.describe(
        model_override='Model to use globally for pings (Authorized only)',
    )
    @app_commands.autocomplete(model_override = model_ac)
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def setmodel(self, interaction: discord.Interaction, model_override: str):
        global models
        if interaction.user.name in authorized_users:
            if model_override in models:
                global model
                model = model_override
                await interaction.response.send_message(content = f"Changed model to {model_override}\n-# preloading model for faster response times")
                try:
                    requests.post("http://192.168.2.2:11434/api/generate", json={"model": model}) # preloads the model for faster response times
                    await interaction.edit_original_response(content = f"Changed model to {model_override}\n-# preloaded!")
                except:
                    await interaction.edit_original_response(content = f"Changed model to {model_override}\n-# could not preload model, this may be because the server is offline")
            else:
                await interaction.response.send_message(content = f"This model is not in the list of available models, please try another model.")
        else:
            await interaction.response.send_message(content = f"No permission!", ephemeral=True)

    @app_commands.command(description="Flushes my smart toilet at my home :3")
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def flush(self, interaction: discord.Interaction):
        global messages
        global pinged_messages
        global kayomessages
        messages = []
        kayomessages = []
        pinged_messages = {}
        pinged_messages.clear()
        messages.clear()
        kayomessages.clear()
        messages.append({"role":"system","content": systemprompt})
        kayomessages.append({"role":"system","content": kayosystemprompt})
        await interaction.response.send_message(content = f"Flushed toilet!")


 



async def setup(bot: commands.Bot):
    await bot.add_cog(Ai(bot))