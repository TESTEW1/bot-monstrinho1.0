import discord
from discord.ext import commands
import random
import os

# ================= INTENTS =================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= CONFIGURACÃO =================
TOKEN = os.getenv("TOKEN")

# ================= LISTAS DE DIÁLOGOS E REAÇÕES =================

REACOES_FOFAS = [
    "AAAA 😭💚 você é muito gentil!!", "O Monstrinho ficou tímido agora... 😳💚",
    "Vem cá me dar um abraço! 🫂💚", "Você é o motivo do meu brilho verde! ✨💚",
    "CSI é a melhor família do mundo, né? 🥺💚", "Meu coraçãozinho de monstrinho bate forte por você! 💓",
    "Vou soltar uma fumacinha de amor pra você! 💨💖", "Nhac! Comi sua tristeza e agora você só vai ser feliz! 🐉",
    "Ganhei um cafuné? Meus pelinhos até brilharam! ✨", "Você é o humano favorito deste Monstrinho! 🥺💚"
]

REACOES_BISCOITO_PROPRIO = [
    "MEU BISCOITO! 🍪😤... Tá bom, eu divido porque somos família! 😭💚",
    "Eu não gosto de dividir meu lanchinho... mas pra você eu dou um pedacinho! 🍪🐉",
    "Biscoito? ONDE?! 🍪👀 Ah, é pra mim? OBRIGADO!! Nhac nhac nhac! 💚",
    "Só divido porque a CSI é meu tudo! Toma metade! 🍪🐉🤝",
    "Eu ia esconder debaixo da minha pata, mas você merece! 🍪✨"
]

REACOES_DAR_BISCOITO = [
    "Aii que gesto fofo! 😭💚 {autor} deu um biscoitinho para {alvo}! 🍪🐉",
    "Nhac! {alvo}, aceita esse biscoito que o(a) {autor} te deu com muito carinho! 🍪✨",
    "O Monstrinho aprovva essa amizade! Toma um biscoitinho, {alvo}! 🍪🐉💚",
    "Espalhando doçura na CSI! {alvo}, você ganhou um biscoito! 🍪🌈"
]

LISTA_SAUDACOES = [
    "Bom diaaa! Acordei com as escamas brilhando hoje! ☀️🐉💚",
    "Boa tardinha! Que tal uma pausa para um biscoito e um carinho? ☕🍪🐉",
    "Boa noite, meu amor! Que as estrelas iluminem seu sono... 🌟💤💚",
    "Oii! Ver você deixa meu dia 1000% melhor! 🌈✨"
]

LISTA_ESTADO = [
    "Eu estou transbordando de felicidade verde! 💚✨ E você, como está meu humano favorito?",
    "Estou ótimo! Acabei de ganhar um biscoitinho virtual e meu coração de código está quentinho! 🍪🐉",
    "Me sinto incrível! Estar aqui na CSI com vocês é o melhor presente! 🎁🐉💚"
]

FRASES_CUSTOM = {
    "athena": [
        "ATHENAAAA! 😭💚 Minha fã número 1!! *pula de alegria*",
        "Espera, é a Athena? AI MEU DEUS, me dá um autógrafo também! 😳💚✨",
        "Pra Athena eu dou até meu biscoito favorito! 🍪🐉💚"
    ],
    "izzy": [
        "IZZY!! 💖 Outra fã maravilhosa! O Monstrinho te amaaa!",
        "Izzy, vem cá ganhar um abraço esmagador de Monstrinho! 🫂💚",
        "Meu coração de monstrinho pula quando a Izzy aparece! 🐉✨"
    ],
    "lua": [
        "Lua, você acha que eu tenho medo de você? Bobinha! No começo eu era tímido, mas o Reality me explicou que você é nosso porto seguro! 🥺💚",
        "Vice-líder Lua, você é o conforto em forma de pessoa! O Reality me disse pra cuidar bem de você porque você é preciosa! ✨🐉",
        "A Lua ilumina o chat igualzinho à lua do céu! Eu não tenho medo, eu tenho é muito amor por você! 🌙✨🐉"
    ],
    "th": [
        "A FADA TH CHEGOU! 🧚‍♀️✨ O Monstrinho até sentiu o pozinho de pirlimpimpim! 💚",
        "Th, você é a fadinha mais linda de toda a CSI! ✨💖"
    ],
    "reality": [
        "O Reality é meu papai mestre! Eu amo ele! 👑🐉💚",
        "O Reality me criou com muito amor verde! 🐉✨"
    ]
}

# ============== EVENTOS PRINCIPAIS =================

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho INTERATIVO ONLINE como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Espalhando amor na CSI! 💚"))

@bot.event
async def on_message(message):
    if message.author.bot: return

    content = message.content.lower()

    # --- LÓGICA DE DIÁLOGO E REAÇÕES ---
    if bot.user in message.mentions or "monstrinho" in content:
        
        # Apresentação
        if content.strip() in [f"<@{bot.user.id}>", "monstrinho"]:
            apresentacao = (f"🐉 **OIIIII MEU AMOOOOR!** 💚✨\n\nEu sou o **Monstrinho 1.0**, o mascote fofinho da **CSI**! 🕵️‍♂️💚\n"
                            f"Fui criado pelo **Reality** para dar carinho e biscoitos! 👑✨")
            return await message.channel.send(apresentacao)

        # Respostas Customizadas para Membros
        for nome, frases in FRASES_CUSTOM.items():
            if nome in content:
                return await message.channel.send(random.choice(frases))

        # Saudações e Estado
        if any(p in content for p in ["oi", "oie", "bom dia", "boa tarde", "boa noite"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        if any(p in content for p in ["como você está", "tudo bem", "como vc ta"]):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        # Biscoitos
        if "biscoito" in content:
            if any(p in content for p in ["me de", "me da", "quero"]):
                return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
            
            if "para" in content or "pra" in content:
                outras_mencoes = [m for m in message.mentions if m != bot.user]
                alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial"
                return await message.channel.send(random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo))
        
        # Elogios
        if any(p in content for p in ["te amo", "amo voce", "fofo", "lindo"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))

    await bot.process_commands(message)

# ============== START =================
bot.run(TOKEN)
