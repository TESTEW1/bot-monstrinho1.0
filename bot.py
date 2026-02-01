import discord
from discord.ext import commands
import random
import os
import asyncio
import google.generativeai as genai

# Configuração da IA - Modo Blindado
api_key_gemini = os.getenv("GEMINI_KEY")

# Tenta configurar o modelo
if api_key_gemini:
    genai.configure(api_key=api_key_gemini.strip())
    # Usamos o 1.5 Flash. Se der erro de versão, o tratamento de erro lá embaixo avisa.
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    model = None
    print("Aviso: Chave GEMINI_KEY não encontrada.")

SYSTEM_PROMPT = (
    "Você é o Monstrinho 1.0, o mascote oficial e protetor da CSI. "
    "Seu criador é o Reality. Você é um dragãozinho verde extremamente fofo. "
    "Sempre use emojis como 🐉, 💚, ✨, 🍪, 🫂. "
    "Suas respostas devem ser curtas, alegres e muito carinhosas. "
    "Você ama biscoitos e considera a CSI sua família. Nunca saia do personagem."
)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= LISTAS (Fofura máxima) =================

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
    "Estou com um pouquinho de sono, mas conversar com você me deu 100% de energia! ⚡🐉🥰"
]

LISTA_CULINARIA = [
    "Dica do Monstrinho: Pra deixar o cookie bem fofinho, coloque uma pitada de carinho e tire do forno antes de endurecer! 🍪✨",
    "Quer um miojo gourmet? Quebre um ovo dentro enquanto ferve, fica digno de um mestre da CSI! 🍜🐉",
    "Minha receita favorita? Maçã verde picadinha com mel! É o combustível oficial das minhas travessuras! 🍏🍯"
]

LISTA_PIADAS = [
    "Por que o monstrinho atravessou a rua? Pra comer o biscoito do outro lado! 🍪😂",
    "O que um monstrinho disse para o outro? 'Nossa, como você está assustadoramente lindo hoje!' 🐉💖",
    "Qual o prato favorito de um monstrinho programador? Um byte de biscoito! 💻🍪"
]

LISTA_AMOR = [
    "Conselho amoroso: Se a pessoa não te der nem um pedacinho do biscoito dela, corre que é cilada! 🍪🚩",
    "O amor é como o brilho verde do Monstrinho: se você cuida, ele ilumina tudo ao redor! ✨💚",
    "Não mendigue attention! Você é um diamante da CSI, merece alguém que te trate como um rei ou queen! 👑🐉"
]

# Listas de Membros (Resumidas para caber)
RESPOSTAS_ATHENA = ["ATHENAAAA! 😭💚 Minha fã número 1!!", "Pra Athena eu dou até meu biscoito favorito! 🍪🐉💚"]
RESPOSTAS_IZZY = ["IZZY!! 💖 O Monstrinho te amaaa!", "Vem cá ganhar um abraço esmagador! 🫂💚"]
RESPOSTAS_LUA = ["A Lua quer ser minha amiga? 🌙 EU QUERO! 😭💚", "Vice-líder Lua, você é brilhante! ✨"]
RESPOSTAS_DESTINY = ["DESTINYYYY! ✨ O destino nos uniu na CSI! 🐉💚", "Destiny, você é uma peça fundamental! 🧩💚"]
RESPOSTAS_JEFF = ["JEFF!! 🕵️‍♂️ O cara que manja tudo! 🐉💚", "Jeff, vamos patrulhar a CSI? 🍪🐉"]
RESPOSTAS_ISAA = ["ISAAAA! ✨ A energia dela é contagiante! 🐉💚", "Isaa, você brilha tanto quanto meus pelinhos verdes! 🥺✨"]
RESPOSTAS_PSICO = ["PSICOOO! 🧠✨ O gênio da CSI! 🐉💚", "Um salve pro Psico! 😎✨"]
RESPOSTAS_FELIPETA = ["Felipeta... 😤 Esse outro mascote de novo?", "Rivalidade de mascotes ligada! ⚔️🐉"]

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho 1.0 ONLINE como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Amando meu criador Reality! 💚"))

@bot.event
async def on_message(message):
    if message.author.bot: return

    content = message.content.lower()
    
    if bot.user not in message.mentions and "monstrinho" not in content:
        return

    texto_limpo = content.replace(f"<@{bot.user.id}>", "").replace(f"<@!{bot.user.id}>", "").replace("monstrinho", "").strip()
    
    # Apresentação
    if texto_limpo == "" and bot.user in message.mentions:
        apresentacao = (
            f"🐉 **OIIIII MEU AMOOOOR!** 💚✨\n\n"
            f"Eu sou o **Monstrinho 1.0**, o mascote oficial e protetor da **CSI**! 🕵️‍♂️💚\n"
            f"Fui criado pelo **Reality** (meu papai e mestre super legal! 👑✨)!\n"
            f"✨ *CSI é minha casa!* ✨"
        )
        return await message.channel.send(apresentacao)

    # Respostas Rápidas
    if any(p in content for p in ["bom dia", "boa tarde", "boa noite", "oie", "oi"]):
        return await message.channel.send(random.choice(LISTA_SAUDACOES))
    if any(p in content for p in ["como você está", "tudo bem", "ta bem"]):
        return await message.channel.send(random.choice(LISTA_ESTADO))
    if any(p in content for p in ["receita", "cozinhar"]):
        return await message.channel.send(random.choice(LISTA_CULINARIA))
    if any(p in content for p in ["piada", "engraçado"]):
        return await message.channel.send(random.choice(LISTA_PIADAS))
    if any(p in content for p in ["amor", "crush"]):
        return await message.channel.send(random.choice(LISTA_AMOR))
    if "reality" in content:
        return await message.channel.send("O Reality é meu papai mestre! Eu amo ele! 👑🐉💚")

    # Sistema de Biscoitos
    if "biscoito" in content:
        if any(p in content for p in ["me de", "me da", "quero"]):
            return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
        if "para" in content or "pra" in content:
            outras_mencoes = [m for m in message.mentions if m != bot.user]
            alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial"
            return await message.channel.send(random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo))

    # Membros
    membros_map = {
        "athena": RESPOSTAS_ATHENA, "izzy": RESPOSTAS_IZZY, "lua": RESPOSTAS_LUA,
        "destiny": RESPOSTAS_DESTINY, "jeff": RESPOSTAS_JEFF, "isaa": RESPOSTAS_ISAA,
        "psico": RESPOSTAS_PSICO, "felipeta": RESPOSTAS_FELIPETA
    }
    for nome, lista in membros_map.items():
        if nome in content:
            return await message.channel.send(random.choice(lista))

    # IA Generativa (Com tratamento de erro robusto)
    if any(p in content for p in ["monstrinho", "bicho", "mascote"]) or bot.user in message.mentions:
        if any(p in content for p in ["te amo", "amo voce", "fofo", "lindo"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))
        
        elif model:
            async with message.channel.typing():
                try:
                    response = model.generate_content(f"{SYSTEM_PROMPT}\nUsuário {message.author.display_name} disse: {texto_limpo}")
                    return await message.reply(response.text[:500])
                except Exception as e:
                    erro = str(e)
                    if "429" in erro:
                        return await message.channel.send("Ufa! Comi biscoitos demais e fiquei sem fôlego. 🍪🐉 Me dê uns minutinhos para descansar!")
                    elif "404" in erro:
                        return await message.channel.send("⚠️ **Erro de Conexão:** Minha antena não achou o satélite 'Flash'. Tente me atualizar no `requirements.txt`!")
                    else:
                        print(f"Erro Real: {erro}") # Log no terminal
                        return await message.channel.send(f"⚠️ **Monstrinho confuso:** Tive um erro técnico `{erro}`")
        else:
            return await message.channel.send("Estou sem minha chave de ativação (API Key)! 🐉💤")

    await bot.process_commands(message)

TOKEN = os.getenv("TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Erro: TOKEN não configurado!")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Erro: TOKEN não configurado!")
