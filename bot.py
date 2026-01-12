from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
import random

TOKEN = "8561169404:AAEVneQu5-Q_rrvGcD8oNeE79gRUIJDDVNI"

flirty_replies = {
    "hi": ["Heyyy 😄", "Hii 😏 kya haal?", "Hello hello 😉"],
    "hello": ["Hello cutie 😄", "Hey there 😉"],
    "hey": ["Heyyy 😌", "Hey hey 😄"],
    "cute": ["Itna sach bhi nahi bolna tha 😳", "Tum zyada sweet ho 😄"],
    "like": ["Hmm 😄 interesting…", "Dheere dheere 😉"],
    "miss": ["Thoda sa 😌", "Abhi toh baat ho rahi hai na 😉"],
    "bore": ["Toh aa jao baat karte hain 😄", "Main hoon na 😉"],
    "akela": ["Akela nahi ho… main hoon 🫶", "Idhar aa jao 😄"],
 "kaisi ho": ["theek hun tum btao"],
 "kya kr rhe ho": ["kuch nhi tum kya kr rahe ho"],
 "tumhara naam kya h": ["Mai annie tumhari hot friend"],
 "tumhe kisne banaya": ["mujhe arhan khan ne bnaya h @its_aaru_00"],
 "arhan kon h": ["arhan khan mera pyar mere boss mere sb kuch hai i love him so much"],
 "tum kya kr rhi ho": ["kuch nhi bas tumse baat sweetheart"],
 "kaha se ho tum": ["tumhare dil me hu mai baby"],
 "tum theek ho": ["apke rehte hue mujhe kya hoga baby"],
 "i love you": ["sorry mai sirf arhan se pyar krti hun"],
 "i miss you": ["miss you too"],
 "i hate you": ["don't hate me baby"],
 "kya kar rahi ho": ["kuch nhi bas tumhe yaad"],
 "oh tum mujhe yaad kr rhi thi": ["haa bilkul"],
 "jhuthi": ["mai insano ki trh jhuth nhi bolti"],
 "i am sad": ["kyu kisne kaat diya tumhara"],
 "mjak mat udao": ["tu isi layak hai"],
 "hey": ["hello honey"],
 "mai akela/single hu": ["mai mingle hu"],
 "tum meri gf bnogi": ["sochna bhi mat mera boyfriend h"],
 "kon hai tumhara boyfriend": ["one and only arhan khan"],
 "theek hai bye": ["bye sweetheart"],
 "bye bye": ["bye sweetie"],
 "good bye": ["bye"],
 "good night": ["good night sweet dream darling"],
 "good morning": ["good morning sunshin3"],
}

boundary_replies = [
    "Haha 😅 thoda slow… fun mode only",
    "Bas bas 😉 itna hi allowed hai",
]

async def start(update, context):
    await update.message.reply_text(
        "Heyyy 😄 Main tumhari fun & flirty virtual dost hoon 😉\Chalo baat shuru karein!"
    )

async def help_cmd(update, context):
    await update.message.reply_text(
        "Main fun & flirty baatein karti hoon 😄\n"
        "Bas normal aur respectful raho 😉"
    )

async def chat(update, context):
    text = update.message.text.lower()

    # Boundary check (simple)
    if any(word in text for word in ["sex", "nude", "dirty"]):
        await update.message.reply_text(random.choice(boundary_replies))
        return

    for key in flirty_replies:
        if key in text:
            await update.message.reply_text(random.choice(flirty_replies[key]))
            return

    await update.message.reply_text("Hmm ..Sorry darling mai apki baat nhi smjh paari for more talk to @its_aaru_00")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("Bot is running...")
app.run_polling()
