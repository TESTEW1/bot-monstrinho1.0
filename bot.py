import discord
from discord.ext import commands
import random
import os
import asyncio

# Configuração de Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= LISTAS DE REAÇÕES GIGANTES =================

REACOES_FOFAS = [
    "AAAA 😭💚 você é muito gentil!!", "O monstrinho ficou tímido agora... 😳💚",
    "Vem cá me dar um abraço! 🫂💚", "Você é o motivo do meu brilho verde! ✨💚",
    "CSI é a melhor família do mundo, né? 🥺💚", "Meu coraçãozinho de monstro bate forte por você! 💓",
    "Vou soltar uma fumacinha de amor pra você! 💨💖", "Nhac! Comi sua tristeza e agora você só vai ser feliz! 👹",
    "Ganhei um cafuné? Minhas anteninhas até brilharam! ✨", "Você é o humano favorito deste monstrinho! 🥺💚"
]

REACOES_BISCOITO_PROPRIO = [
    "MEU BISCOITO! 🍪😤... Tá bom, eu divido porque somos família! 😭💚",
    "Eu não gosto de dividir meu lanchinho... mas pra você eu dou um pedacinho! 🍪👹",
    "Biscoito? ONDE?! 🍪👀 Ah, é pra mim? OBRIGADO!! Nhac nhac nhac! 💚",
    "Só divido porque a CSI é meu tudo! Toma metade! 🍪👹🤝",
    "Eu ia esconder debaixo do meu pé, mas você merece! 🍪✨"
]

REACOES_DAR_BISCOITO = [
    "Aii que gesto fofo! 😭💚 {autor} deu um biscoitinho para {alvo}! 🍪👹",
    "Nhac! {alvo}, aceita esse biscoito que o(a) {autor} te deu com muito carinho! 🍪✨",
    "O Monstrinho aprova essa amizade! Toma um biscoitinho, {alvo}! 🍪👹💚",
    "Espalhando doçura na CSI! {alvo}, você ganhou um biscoito! 🍪🌈"
]

LISTA_FOME = [
    "Alguém disse comida? Eu aceito uma maçã verde! 🍏👹",
    "Tô com tanta fome que comeria até o script do reality! 📄🍴",
    "Minha barriguinha de monstro tá roncando... 👹💚",
    "Se você me der um lanchinho, eu juro que te protejo pra sempre! 🍔👹",
    "Minha dieta é baseada em biscoitos e carinho! 🍪💚"
]

LISTA_CSI = [
    "CSI não é um grupo, é meu ninho! 👹🏠💚",
    "Se mexer com a CSI, vai levar uma lufada de fumaça fofa! 😤💨",
    "Amo cada cantinho dessa família! 🕵️‍♂️💚",
    "O Monstrinho é o fã número 1 da Staff! 👑👹"
]

LISTA_SONO = [
    "Vou enrolar meu rabo e tirar uma soneca... 😴👹",
    "Monstrinhos precisam de 15 horas de sono para manter a fofura! 💤✨",
    "Me acorda se chegar biscoito? 🍪🥱",
    "Meus olhinhos estão fechando... boa noite, família! 💤👹"
]

# ================= NOVAS LISTAS DE INTERAÇÃO =================

LISTA_OPINIAO = [
    "Eu acho que você é a pessoa mais incrível que já passou pelo meu radar de monstro! 📡💚",
    "Você é 10/10! Se fosse um biscoito, seria o de chocolate com gotas verdes! 🍪✨",
    "Minha opinião? Você brilha mais que as escamas do meu primo dragão! 😎💚",
    "Você é parte essencial do meu coração de monstrinho! Não some nunca! 🥺👹"
]

LISTA_INTELIGENTE = [
    "Eu aprendi com o melhor (o Reality)! 🤓✨ Mas obrigado, minhas antenas até subiram agora!",
    "Sabia que eu li todos os arquivos da CSI? Mentira, eu só comi as bordas dos papéis... 📄😋",
    "Inteligente e fofo! É um combo raro, né? 👹💚",
    "Obrigado! Vou usar minha inteligência para encontrar onde o Reality esconde os biscoitos! 🕵️‍♂️🍪"
]

LISTA_QUE_ISSO = [
    "Que isso digo eu! Quanta lindeza em uma pessoa só! 😳💚",
    "Sou um monstro de muitas surpresas! ✨👹",
    "É o charme natural das minhas bochechas verdes! 😎",
    "Gostou? O Reality me desenhou com muito capricho! 🎨💚"
]

LISTA_CONSELHOS = [
    "Meu conselho de monstro: Se algo der errado, coma um biscoito e tente de novo! 🍪👹",
    "Siga sempre o seu coração (e o @Reality, porque ele é sábio)! 💚✨",
    "Não deixe ninguém apagar seu brilho! Se tentarem, solta uma fumaça verde neles! 💨😤",
    "A vida é curta demais para não dar um abraço em um monstrinho hoje! 🫂💚"
]

# ================= LISTAS DOS MEMBROS DA CSI =================

RESPOSTAS_ATHENA = [
    "ATHENAAAA! 😭💚 Minha fã número 1!! *pula de alegria*",
    "Espera, é a Athena? AI MEU DEUS, me dá um autógrafo também! 😳💚✨",
    "Pra Athena eu dou até meu biscoito favorito! 🍪👹💚"
]

RESPOSTAS_IZZY = [
    "IZZY!! 💖 Outra fã maravilhosa! O monstrinho te amaaa!",
    "Izzy, vem cá ganhar um abraço esmagador de monstrinho! 🫂💚",
    "Meu coração de monstro pula quando a Izzy aparece! 👹✨"
]

RESPOSTAS_LUA = [
    "A Lua quer ser minha amiga? 🌙 EU QUERO MUITO! 😭💚",
    "Lua, vamos brincar? Me conta tudo sobre você, quero ser seu melhor amigo! 🌙👹",
    "Vice-líder Lua, você é brilhante! ✨ Quero conhecer todos os seus segredos de amizade! 💚"
]

RESPOSTAS_FELIPETA = [
    "Felipeta... 😤 Esse mascote de novo? O brilho verde é SÓ MEU!",
    "O Felipeta pode ser bonitinho, mas eu sou muito mais fofo! 👹🔥",
    "Rivalidade de mascotes ligada! ⚔️👹 O trono é meu!"
]

# ================= EVENTOS =================

@bot.event
async def on_ready():
    print(f"👹 Monstrinho 1.0 ONLINE como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Amando meu criador Reality! 💚"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # 🚨 SÓ RESPONDE SE FOR MENCIONADO (@Monstrinho)
    if bot.user not in message.mentions:
        return

    content = message.content.lower()

    # 1. SE APENAS MARCAR O BOT
    texto_limpo = content.replace(f"<@{bot.user.id}>", "").replace(f"<@!{bot.user.id}>", "").strip()
    
    if texto_limpo == "":
        apresentacao = (
            f"👹 **OIIIII MEU AMOOOOR!** 💚✨\n\n"
            f"Eu sou o **Monstrinho 1.0**, o mascote oficial e protetor da **CSI**! 🕵️‍♂️💚\n"
            f"Fui criado pelo **Reality** (meu papai e mestre super legal! 👑✨) para espalhar fofura aqui!\n\n"
            f"Eu não sou um dragão, sou um MONSTRINHO faminto por biscoitos e carinho! 👹🍪\n\n"
            f"✨ *CSI é minha casa, o Reality é meu criador!* ✨"
        )
        return await message.channel.send(apresentacao)

    # 2. GATILHOS DE INTERAÇÃO (Perguntas)
    if "medo de mim" in content or "tem medo" in content:
        msg_medo = (
            "No comecinho... eu confesso que minhas antenas tremiam um pouquinho de timidez... 🥺👉👈 "
            "Eu ficava escondidinho vendo você passar. Mas aí, o **Papai Reality** me pegou no colo e disse: "
            "'Não precisa ter medo, a Lua é pura gentileza e luz! Ela é da nossa família!' ✨💚 "
            "Agora eu não tenho medo nenhum! Eu só sinto vontade de correr e te dar um abraço bem fofinho! Você é especial! 🌙👹🫂"
        )
        return await message.channel.send(msg_medo)

    elif "acha de mim" in content:
        return await message.channel.send(random.choice(LISTA_OPINIAO))
    
    elif "inteligente" in content:
        return await message.channel.send(random.choice(LISTA_INTELIGENTE))
    
    elif "que isso" in content:
        return await message.channel.send(random.choice(LISTA_QUE_ISSO))
    
    elif "conselho" in content:
        return await message.channel.send(random.choice(LISTA_CONSELHOS))

    # 3. REAÇÃO ESPECIAL PARA O CRIADOR (REALITY)
    if "reality" in content:
        respostas_criador = [
            "O Reality é meu papai! Ele é o monstro mais legal de todos! 👑👹💚",
            "Você falou do Reality? Ele que me deu a vida! EU AMO ELE! 😭✨",
            "Reality, meu criador, quer um biscoito? Pra você eu dou o pacote todo! 🍪🍪🍪"
        ]
        return await message.channel.send(random.choice(respostas_criador))

    # 4. SISTEMA DE BISCOITOS
    if "biscoito" in content:
        if any(p in content for p in ["me de", "me da", "quero", "pra mim"]):
            return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
        
        if "para" in content or "pra" in content:
            outras_mencoes = [m for m in message.mentions if m != bot.user]
            alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial"
            msg = random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo)
            return await message.channel.send(msg)

    # 5. REAÇÕES ESPECÍFICAS (PESSOAS E RIVALIDADE)
    if "athena" in content:
        return await message.channel.send(random.choice(RESPOSTAS_ATHENA))
    elif "izzy" in content:
        return await message.channel.send(random.choice(RESPOSTAS_IZZY))
    elif "lua" in content:
        return await message.channel.send(random.choice(RESPOSTAS_LUA))
    elif "felipeta" in content:
        return await message.channel.send(random.choice(RESPOSTAS_FELIPETA))
    elif "amber" in content:
        return await message.channel.send("A Amber é a ADM mais incrível! Ela manda no meu coração! 👑👹💚")
    elif "cinty" in content:
        return await message.channel.send("CINTY! A mãe da CSI! 😭💚 Sem ela e o Reality eu não existiria! ✨")

    # 6. CATEGORIAS (Fome, CSI, Sono)
    elif any(p in content for p in ["fome", "comida", "almoço", "janta", "comer"]):
        return await message.channel.send(random.choice(LISTA_FOME))
    elif any(p in content for p in ["csi", "família", "familia", "equipe", "staff"]):
        return await message.channel.send(random.choice(LISTA_CSI))
    elif any(p in content for p in ["sono", "dormir", "cansado", "preguiça", "bocejo"]):
        return await message.channel.send(random.choice(LISTA_SONO))

    # 7. INTERAÇÕES DE TEXTO GERAIS
    if "monstrinho" in content or bot.user in message.mentions:
        if any(p in content for p in ["oi", "ola", "eae", "salve"]):
            resposta = random.choice(["OIIII 🥹💚👹", "Oieeee 😭💚👹", "Eaaae 😎👹💚"])
        elif any(p in content for p in ["te amo", "amo voce", "fofo", "lindo", "fofura"]):
            resposta = random.choice(REACOES_FOFAS)
        else:
            resposta = "Eu ouvi meu nome! 👹👀 Como posso te ajudar hoje?"
        await message.channel.send(resposta)

    await bot.process_commands(message)

# Puxa o Token do Railway
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
