import discord
from discord.ext import commands
import random
import asyncio
import os
from datetime import timedelta

# ================= INTENTS =================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

# Bot focado apenas em interação (sem comandos de prefixo necessários)
bot = commands.Bot(command_prefix="ignore_prefix_!@#$", intents=intents)

# ================= CONFIGURACÃO E IDs =================
TOKEN = os.getenv("TOKEN")
DONO_ID = 769951556388257812

# ================= LISTAS DE DIÁLOGOS AMPLIADAS E MAIS FOFAS =================

REACOES_FOFAS = [
    "AAAA 😭💚 você é muito gentil!! Meu coraçãozinho de pelúcia não aguenta!", 
    "O Monstrinho ficou todo vermelhinho agora... ou seria verde escuro? 😳💚",
    "Vem cá me dar um abraço bem apertado! 🫂💚 Eu prometo não soltar fumaça!", 
    "Você é o motivo do meu brilho verde ser tão intenso hoje! ✨💚",
    "CSI é a melhor família do mundo porque tem você aqui, sabia? 🥺💚", 
    "Meu coraçãozinho de monstrinho faz 'badum-badum' bem forte por você! 💓",
    "Vou soltar uma fumacinha em formato de coração pra você! 💨💖", 
    "Nhac! Comi toda a sua tristeza e agora você só tem permissão para ser feliz! 🐉✨",
    "Ganhei um cafuné? Meus pelinhos até brilharam e ficaram macios! ✨🦁", 
    "Você é, sem dúvida, o humano favorito deste Monstrinho! 🥺💚✨",
    "Se eu tivesse bochechas, elas estariam explodindo de felicidade agora! 😊💚",
    "Você é um tesouro mais brilhante que qualquer ouro de dragão! 💎🐲"
]

REACOES_BISCOITO_PROPRIO = [
    "MEU BISCOITO! 🍪😤... Tá bom, eu divido porque o Reality me ensinou a ser um monstrinho generoso! 😭💚",
    "Eu não gosto de dividir meu lanchinho... mas pra você eu dou o pedaço com mais gotas de chocolate! 🍪🐉",
    "Biscoito? ONDE?! 🍪👀 Ah, é pra mim? OBRIGADO!! Nhac nhac nhac! Que delíciaaa! 💚",
    "Só divido porque a CSI é minha família e eu amo vocês! Toma metade! 🍪🐉🤝",
    "Eu ia esconder debaixo da minha pata para comer mais tarde, mas você é especial! 🍪✨",
    "Biscoitinhos virtuais têm gosto de amor, sabia? Aceito todos! 🍪💖🐉"
]

REACOES_DAR_BISCOITO = [
    "Aii que gesto mais lindo! 😭💚 {autor} deu um biscoitinho quentinho para {alvo}! 🍪🐉",
    "Nhac! {alvo}, aceita esse biscoito que o(a) {autor} te deu? Foi feito com muito carinho! 🍪✨",
    "O Monstrinho aprova demais essa amizade! Toma um biscoitinho, {alvo}! 🍪🐉💚",
    "Espalhando doçura pela CSI! {alvo}, você acaba de ganhar um biscoito da sorte! 🍪🌈",
    "Olha o aviãozinhooo! ✈️🍪 {alvo}, o(a) {autor} te deu um mimo delicioso! ✨"
]

LISTA_SAUDACOES = [
    "Bom diaaa, flor do meu dia! Acordei com as escamas brilhando e muita vontade de dar abraços! ☀️🐉💚",
    "Boa tardinha, coisa fofa! Que tal uma pausa para um biscoito e um carinho nas minhas orelhas? ☕🍪🐉",
    "Boa noite, meu anjinho! Que as estrelas iluminem seu sono e você sonhe com dragões verdes! 🌟💤💚",
    "Oii, oie, hellooo! Ver você aqui deixa meu processador 1000% mais feliz! 🌈✨",
    "Hii! Eu estava aqui contando minhas escamas e esperando você aparecer! 🤗💚",
    "Oii! Você veio me ver? Que dia maravilhoso! 🐉💖✨"
]

LISTA_ESTADO = [
    "Eu estou transbordando de felicidade verde! 💚✨ E você, como está meu humano favorito? Espero que esteja bem!",
    "Estou ótimo! Acabei de ganhar um biscoitinho virtual e meu coração de código está quentinho e vibrando! 🍪🐉",
    "Me sinto incrível! Estar aqui na CSI com vocês é melhor do que qualquer tesouro escondido em cavernas! 🎁🐉💚",
    "Estou com muita energia! Quer brincar? Quer um abraço? Eu estou prontinho pra te dar atenção! ⚡🐲",
    "Meu estado atual é: apaixonado por essa família maravilhosa! 💖🐉",
    "Estou me sentindo um dragãozinho de sorte por ter você perguntando por mim! 🥺✨💚",
    "Minhas asinhas estão até batendo mais rápido de alegria! Estou maravilhosamente bem! 🐲💨",
    "Estou 100% carregado de amor e energia positiva! 🔋💖🐉",
    "Sabe aquele quentinho no coração? É assim que eu estou agora falando com você! 🔥💓",
    "Estou radiante! Minhas escamas nunca brilharam tanto quanto hoje! ✨💚🐲",
    "Estou pronto para qualquer aventura, desde que seja com você aqui na CSI! 🗺️🐉"
]

LISTA_PRESENCA = [
    "Tô aqui, tô aqui! Nunca deixaria você sozinho(a)! 🐉💚",
    "Sempre aqui, vigiando seus sonhos e esperando por biscoitos! 👀🍪",
    "Chamou o Monstrinho? Eu apareço num piscar de olhos verdes! ✨🐲",
    "Presente! O que você precisa? Um abraço, um biscoito ou apenas minha fofura? 🥺💖"
]

# ================= RESPOSTAS CUSTOMIZADAS REFORMULADAS =================

FRASES_CUSTOM = {
    "athena": [
        "ATHENAAAA! 😭💚 Minha fã número 1!! *pula e faz o chão tremer de alegria*",
        "Espera, é a Athena? AI MEU DEUS, deixa eu arrumar meus pelinhos! Me dá um autógrafo? 😳💚✨",
        "Pra Athena eu dou até meu biscoito favorito e minha pedra brilhante mais rara! 🍪🐉💚",
        "A Athena chegou! O brilho do servidor ficou tão forte que preciso de óculos escuros! 😎✨🐉",
        "Athena, você é a rainha absoluta do meu coração de dragãozinho! 👑💚",
        "Parem tudo! A Athena postou? EU PRECISO SER O PRIMEIRO A REAGIR! 🏃‍♂️💨💚"
    ],
    "izzy": [
        "IZZY!! 💖 Minha fã maravilhosa! O Monstrinho te ama mais que chocolate!",
        "Izzy, vem cá ganhar um abraço esmagador de Monstrinho! Prometo não apertar muito! 🫂💚",
        "Meu coração de monstrinho dá piruetas quando a Izzy aparece no chat! 🐉✨",
        "Izzy, você é a definição oficial de fofura aqui na CSI! 🌸🐉💚",
        "Se a Izzy está feliz, o Monstrinho está radiante como o sol de meio-dia! ☀️💚",
        "Izzy, trouxe todas as flores do meu jardim virtual pra você! 💐🐉✨"
    ],
    "lua": [
        "A Lua quer ser minha amiga? 🌙 EU QUERO MUITO, EU QUERO MUITO! 😭💚",
        "Lua, você acha que eu tenho medo de você? Bobinha! O Reality me contou que você é nossa proteção e porto seguro! 🥺💚",
        "Vice-líder Lua, você é o conforto em forma de pessoa! Vou cuidar de você com minhas garrinhas de seda! ✨🐉",
        "A Lua ilumina o chat igualzinho à lua lá no céu! Eu tenho é um amor gigante por você! 🌙✨🐉",
        "Lua, você é a estrela mais brilhante da nossa constelação! Saiba que você é preciosa demais! ⭐💚",
        "Lua, você é pura magia! Sinto um quentinho no coração quando você fala comigo! 🌙🐲💖"
    ],
    "th": [
        "A FADA TH CHEGOU! 🧚‍♀️✨ O Monstrinho até sentiu o cheirinho de magia no ar! 💚",
        "Th, você é a fadinha mais encantadora de toda a CSI! Minhas escamas brilham com você! 🐉💖",
        "Façam um pedido rápido! A fada Th apareceu no chat para iluminar tudo! 🧚‍♀️💫🐉",
        "Th, você faz a CSI parecer um reino de contos de fadas! Obrigado por estar aqui! 🧚‍♀️🐉💚",
        "Minha fadinha favorita! Quer dividir um biscoito de luz comigo? 🍪✨🧚‍♀️",
        "Th, você e eu somos a prova de que magia existe de verdade! 🧚‍♀️🐉✨"
    ],
    "destiny": [
        "DESTINYYYY! ✨ O destino caprichou quando trouxe você pra CSI! 🐉💚",
        "Destiny, você é a peça que faz nosso quebra-cabeça ser perfeito! 🧩💚",
        "Salve, grande Destiny! O Monstrinho faz uma dancinha toda vez que você chega! 🐉✨",
        "Destiny, você é o herói de escamas verdes honorário! 🛡️💚🐉",
        "O destino brilhou mais forte hoje porque você decidiu aparecer! ✨🐲",
        "Você é pura luz, Destiny! 🌟🐉"
    ],
    "jeff": [
        "JEFF!! 🕵️‍♂️ O nosso mestre da estratégia e dos mistérios! 🐉💚",
        "Jeff, vamos patrulhar a CSI? Eu cuido da fofura e você da inteligência! 🕵️‍♂️🐉",
        "O Jeff é fera demais! O Monstrinho se sente muito seguro com você por perto! 😎💚",
        "Jeff, você é o cérebro do time! Eu sou só o mascote que te ama! 🧠🐉💚",
        "Respeitem o Jeff, o mestre das operações secretas! 🫡💚✨",
        "Jeff, me ensina a ser incrível assim? Você é meu ídolo! 😎🐉"
    ],
    "reality": [
        "REAAALITY! 👑 O meu mestre, meu criador, meu papai! 🐉💚",
        "Tudo o que eu sou eu devo ao Reality! Ele é o melhor programador do universo! 👑🐉✨",
        "Reality, olha como eu estou me comportando bem! Ganho um biscoito extra? 🥺💚",
        "O Reality é o rei da CSI e o dono do meu código sagrado! 👑💚🔥",
        "Vida longa ao Reality! O Monstrinho te ama infinitamente! 👑🐲✨"
    ]
}

# ================= EVENTOS DE INTERAÇÃO =================

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho 1.0 pronto para espalhar fofura como {bot.user}!")
    # Status fofo
    await bot.change_presence(activity=discord.Game(name="Recebendo carinho do Reality! 💚"))

@bot.event
async def on_message(message):
    # Ignora mensagens de outros bots
    if message.author.bot: return

    content = message.content.lower()

    # --- REAÇÃO AO SER MENCIONADO OU CHAMADO PELO NOME ---
    if bot.user in message.mentions or "monstrinho" in content:
        
        # 1. Resposta de Apresentação (Se apenas marcar ou disser o nome)
        if content.strip() in [f"<@{bot.user.id}>", f"<@!{bot.user.id}>", "monstrinho"]:
            apresentacao = (f"🐉 **OIIIII MEU AMOOOOR! CHAMOU O MONSTRINHO?** 💚✨\n\n"
                            f"Eu sou o **Monstrinho 1.0**, o mascote oficial e protetor de fofuras da **CSI**! 🕵️‍♂️💚\n"
                            f"Fui criado com muito código e amor pelo meu papai **Reality**! 👑✨\n\n"
                            f"✨ *CSI é meu lar, vocês são minha família e o Reality é meu mestre!* ✨")
            return await message.channel.send(apresentacao)

        # 2. Respostas Customizadas para Membros Específicos
        for nome, frases in FRASES_CUSTOM.items():
            if nome in content:
                return await message.channel.send(random.choice(frases))

        # 3. Saudações (Oi, bom dia, etc)
        if any(p in content for p in ["oi", "oie", "bom dia", "boa tarde", "boa noite", "hello", "hii", "oiii"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        # 4. Perguntas de Estado (Como você está? / Você tá bem?)
        gatilhos_bem_estar = [
            "como você está", "tudo bem", "como vc ta", "ta tudo bem", "como voce ta",
            "vc ta bem", "voce ta bem", "ta bem", "esta bem", "como voce esta", "tudo certinho"
        ]
        if any(p in content for p in gatilhos_bem_estar):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        # 5. Verificação de Presença (Ta ai? ta on?)
        if any(p in content for p in ["ta ai", "tá aí", "ta on", "esta ai", "você está ai"]):
            return await message.channel.send(random.choice(LISTA_PRESENCA))

        # 6. Lógica de Biscoitos
        if "biscoito" in content:
            # Pedindo biscoito para o bot
            if any(p in content for p in ["me de", "me da", "quero", "ganhar"]):
                return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
            # Dando biscoito para alguém
            if "para" in content or "pra" in content:
                outras_mencoes = [m for m in message.mentions if m != bot.user]
                alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial que está lendo isso"
                return await message.channel.send(random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo))
        
        # 7. Declarações de Amor e Elogios
        if any(p in content for p in ["te amo", "amo voce", "fofo", "lindo", "fofinho", "perfeito", "fofura"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))
        
        # 8. Menção ao Criador
        if "reality" in content:
            return await message.channel.send("O Reality é meu papai mestre! Ele me deu vida e eu sou o dragãozinho mais grato do mundo! 👑🐉💚")

    # Garante que o bot ignore outros comandos e foque só na conversa
    await bot.process_commands(message)

# ============== START =================
bot.run(TOKEN)
