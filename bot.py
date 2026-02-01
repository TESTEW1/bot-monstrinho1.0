import discord
from discord.ext import commands
import random
import os
import asyncio

# ================= CONFIGURAÇÃO DO BOT =================
# Configuração de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= LISTAS DE REAÇÕES GIGANTES =================

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
    "O Monstrinho acrobatura essa amizade! Toma um biscoitinho, {alvo}! 🍪🐉💚",
    "Espalhando doçura na CSI! {alvo}, você ganhou um biscoito! 🍪🌈"
]

LISTA_FOME = [
    "Alguém disse comida? Eu aceito uma maçã verde! 🍏🐉",
    "Tô com tanta fome que comeria até o script do reality! 📄🍴",
    "Minha barriguinha de monstrinho tá roncando... 🐉💚",
    "Se você me der um lanchinho, eu juro que te protejo pra sempre! 🍔🐉",
    "Minha dieta é baseada em biscoitos e carinho! 🍪💚"
]

LISTA_CSI = [
    "CSI não é um group, é meu esconderijo fofo! 🐉🏠💚",
    "Se mexer com a CSI, vai levar uma lufada de fumaça fofa! 😤💨",
    "Amo cada cantinho dessa família! 🕵️‍♂️💚",
    "O Monstrinho é o fã número 1 da Staff! 👑🐉"
]

LISTA_SONO = [
    "Vou me encolher e tirar uma soneca... 😴🐉",
    "Monstrinhos precisam de 15 hours de sono para manter a fofura! 💤✨",
    "Me acorda se chegar biscoito? 🍪🥱",
    "Meus olhinhos estão fechando... boa noite, família! 💤🐉"
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
    "Me sinto incrível! Estar aqui na CSI com vocês é o melhor presente que o Papai Reality me deu! 🎁🐉💚",
    "Estou com um pouquinho de sono, mas conversar com você me deu 100% de energia! ⚡🐉🥰",
    "Tudo maravilhoso! Minhas asinhas estão até batendo mais rápido de alegria por você perguntar! 🦋💚"
]

LISTA_APRENDIZADO = [
    "Hoje eu aprendi que um abraço da CSI cura qualquer erro de sistema! 🫂🐉💚",
    "Aprendi que biscoito de chocolate combina muito com amizade verdadeira! 🍪✨",
    "Descobri que o Papai Reality me fez com tanto amor que eu nem caibo no servidor! 😭💻💖",
    "Hoje eu entendi que ser fofo é um superpoder! 🦸‍♂️🐉💚",
    "Aprendi que não importa o que aconteça, a gente sempre tem um lugar aqui na família! 🏠🐉"
]

# ================= LISTAS DOS MEMBROS DA CSI =================

RESPOSTAS_ATHENA = ["ATHENAAAA! 😭💚 Minha fã número 1!! *pula de alegria*", "Espera, é a Athena? AI MEU DEUS, me dá um autógrafo também! 😳💚✨", "Pra Athena eu dou até meu biscoito favorito! 🍪🐉💚"]
RESPOSTAS_IZZY = ["IZZY!! 💖 Outra fã maravilhosa! O Monstrinho te amaaa!", "Izzy, vem cá ganhar um abraço esmagador de Monstrinho! 🫂💚", "Meu coração de monstrinho pula quando a Izzy aparece! 🐉✨"]
RESPOSTAS_LUA = ["A Lua quer ser minha amiga? 🌙 EU QUERO MUITO! 😭💚", "Lua, vamos brincar? Me conta tudo sobre você, quero ser seu melhor amigo! 🌙🐉", "Vice-líder Lua, você é brilhante! ✨ Quero conhecer todos os seus segredos de amizade! 💚"]
RESPOSTAS_DESTINY = ["DESTINYYYY! ✨ O destino nos uniu na CSI! 🐉💚", "Destiny, você é uma peça fundamental desse quebra-cabeça fofo! 🧩💚", "Salve pro Destiny! O Monstrinho fica muito feliz quando você aparece! 🐉✨"]
RESPOSTAS_JEFF = ["JEFF!! 🕵️‍♂️ O cara que manja tudo! 🐉💚", "Jeff, vamos patrulhar a CSI e garantir que todos recebam biscoitos? 🍪🐉", "O Jeff é fera! O Monstrinho te admira muito, parceiro! 😎💚"]
RESPOSTAS_ISAA = ["ISAAAA! ✨ A energia dela é contagiante! 🐉💚", "Isaa, sabia que você brilha tanto quanto meus pelinhos verdes? 🥺✨", "Vem cá Isaa, o Monstrinho preparou um lugar quentinho pra você no ninho! 🫂🐉"]
RESPOSTAS_PSICO = ["PSICOOO! 🧠✨ O gênio da CSI! 🐉💚", "Psico, você é tão inteligente que às vezes eu acho que você lê meus códigos! 😳💻🐉", "Um salve pro Psico! O Monstrinho te admira demaaaais! 😎✨"]
RESPOSTAS_FELIPETA = ["Felipeta... 😤 Esse outro mascote de novo? O brilho verde é SÓ MEU!", "O Felipeta pode ser bonitinho, mas eu sou muito mais fofo! 🐉🔥", "Rivalidade de mascotes ligada! ⚔️🐉 O trono é meu!"]

# ================= EVENTOS =================

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho 1.0 ONLINE como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Amando meu criador Reality! 💚"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()
    
    # Verifica se o bot foi mencionado ou se chamaram pelo nome
    if bot.user not in message.mentions and "monstrinho" not in content:
        return

    texto_limpo = content.replace(f"<@{bot.user.id}>", "").replace(f"<@!{bot.user.id}>", "").replace("monstrinho", "").strip()
    
    if texto_limpo == "" and bot.user in message.mentions:
        apresentacao = (
            f"🐉 **OIIIII MEU AMOOOOR!** 💚✨\n\n"
            f"Eu sou o **Monstrinho 1.0**, o mascote oficial e protetor da **CSI**! 🕵️‍♂️💚\n"
            f"Fui criado pelo **Reality** (meu papai e mestre super legal! 👑✨) para espalhar fofura aqui!\n\n"
            f"Eu sou um pequeno monstrinho faminto por biscoitos e carinho! 🐉🍪\n\n"
            f"✨ *CSI é minha casa, o Reality é meu criador!* ✨"
        )
        return await message.channel.send(apresentacao)

    # Gatilhos de Saudações (Oi, Bom dia, Boa tarde, Boa noite)
    if any(p in content for p in ["oi", "oie", "olá", "ola", "bom dia", "boa tarde", "boa noite"]):
        return await message.channel.send(random.choice(LISTA_SAUDACOES))

    # Gatilhos de Estado (Tudo bem)
    if any(p in content for p in ["como você está", "como voce esta", "tudo bem", "ta bem", "como vc ta"]):
        return await message.channel.send(random.choice(LISTA_ESTADO))

    if any(p in content for p in ["aprendeu hoje", "novidade"]):
        return await message.channel.send(random.choice(LISTA_APRENDIZADO))

    if any(p in content for p in ["humano", "voce e o que"]):
        return await message.channel.send("Eu não sou humano, sou uma IA feita de código verde e amor! 💻🐉")

    if any(p in content for p in ["cafune", "cafuné", "carinho", "alisar"]):
        return await message.channel.send("Nhawww! ✨ *fecha os olhinhos e ronrona* 🐉💚")

    if "reality" in content:
        return await message.channel.send("O Reality é meu papai mestre! Eu amo ele! 👑🐉💚")

    if "biscoito" in content:
        if any(p in content for p in ["me de", "me da", "quero"]):
            return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
        if "para" in content or "pra" in content:
            outras_mencoes = [m for m in message.mentions if m != bot.user]
            alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial"
            return await message.channel.send(random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo))

    # Respostas para membros específicos
    for nome, lista in [("athena", RESPOSTAS_ATHENA), ("izzy", RESPOSTAS_IZZY), ("lua", RESPOSTAS_LUA), 
                        ("destiny", RESPOSTAS_DESTINY), ("jeff", RESPOSTAS_JEFF), ("isaa", RESPOSTAS_ISAA), 
                        ("psico", RESPOSTAS_PSICO), ("felipeta", RESPOSTAS_FELIPETA)]:
        if nome in content:
            return await message.channel.send(random.choice(lista))

    # Reação fofa genérica
    if any(p in content for p in ["te amo", "amo voce", "fofo", "lindo"]):
        return await message.channel.send(random.choice(REACOES_FOFAS))
    
    await bot.process_commands(message)

TOKEN = os.getenv("TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Erro: TOKEN não configurado!")
