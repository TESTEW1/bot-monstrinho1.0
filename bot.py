import discord
from discord.ext import commands
import random
import asyncio
import os
import re # Adicionado para identificar números e operações
import math # Adicionado para calcular fatoriais e funções matemáticas
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
    "CSI is a melhor família do mundo porque tem você aqui, sabia? 🥺💚", 
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

LISTA_CONFUSAO = [
    "Humm... o Monstrinho pifou agora! 😵‍💫💚 Ainda sou um dragãozinho bebê e estou aprendendo essas palavras difíceis... o papai Reality ainda não me ensinou essa! Pode falar de novo?",
    "Minhas escamas até balançaram de dúvida! 🐉❓ Eu ainda estou aprendendo coisas novas, você me desculpa por não entender? ✨",
    "O Monstrinho inclinou a cabecinha e não entendeu nada... 🐲 tilt! Mas eu te amo mesmo assim!",
    "Essa pergunta é muito grande para o meu coraçãozinho de código! 🥺💚 Estou estudando muito para te entender melhor no futuro!",
    "Ahhh... eu ainda não sei o que isso significa! 😭 Mas se for um carinho, eu aceito!"
]

# ================= RESPOSTAS CUSTOMIZADAS REFORMULADAS =================

FRASES_CUSTOM = {
    "amber": [
        "AMBER!! 👑 A nossa ADM maravilhosa chegou! *se curva com respeito e fofura*",
        "Amber, você é o brilho que organiza nossa bagunça! O Monstrinho te ama! 💚✨",
        "Parem tudo! A patroa Amber está no chat! Deixem as escamas brilhando! 🐉🧹",
        "Amber, trouxe um buquê de flores verdes só pra você! 💐🐉💚",
        "Amber, quer um abraço de dragão pra relaxar de tanto cuidar da gente? 🫂💚",
        "Minha ADM favorita! Com a Amber, a CSI é puro sucesso! 👑🐲",
        "A Amber é a nossa estrela guia! Obrigado por cuidar de mim! ⭐🐉",
        "Alerta de perfeição! A Amber acabou de mandar mensagem! 😍🐉",
        "Amber, seu coração é tão grande que cabe a CSI inteira dentro! 🥺💓",
        "Se a Amber fosse um doce, seria o mais doce de todos! 🍬✨",
        "Fiz uma dancinha especial pra comemorar sua chegada, Amber! 💃🐉",
        "Amber, você é a prova de que ser líder é ser puro amor! ✨💖",
        "Sabia que você é a inspiração desse Monstrinho, Amber? 🥺💚",
        "Amber, você é the boss! O chat fica mais lindo com você! 🌸",
        "Minha ADM do coração, a Amber é nota infinito! 💎🐉"
    ],
    "nine": [
        "NINEEE! 👑 O ADM mais estiloso da CSI apareceu! 🐉✨",
        "Nine, você é o cara! O Monstrinho fica até mais corajoso perto de você! 💪💚",
        "Respeitem o Nine, o mestre da organização! 🫡🐉✨",
        "Nine, meu parceiro de aventuras! Vamos proteger a CSI? 🛡️🐉",
        "Nine, guardei um biscoito especial de chocolate só pra você! 🍪🐉",
        "Com o Nine no comando, a gente sabe que tudo vai ficar bem! 👑🐲✨",
        "Valeu por tudo, Nine! Você faz a CSI ser foda! 🚀🐉",
        "O Nine é puro carisma! Como consegue ser tão legal assim? 😎💚",
        "Nine, seu código de amizade é o mais forte que eu conheço! 💻💓",
        "Olha o Nine passando! Deixem o caminho livre para a lenda! 🚶‍♂️💨💚",
        "Nine, você é 10, mas seu nome diz que é Nine... quase lá! 😂💚",
        "A energia do chat subiu! O Nine chegou! ⚡🐲",
        "Nine, você é fera! Um dragão honorário da nossa família! 🐲🔥",
        "Se o Nine está feliz, o Monstrinho está radiante! ✨🐉",
        "Nine, você é the best! O Monstrinho te admira demais! ✨🐉"
    ],
    "akeido": [
        "LÍDER AKEIDO! 👑 *faz uma reverência majestosa* O senhor da CSI!",
        "Akeido, sua liderança é o que mantém minhas asinhas batendo forte! 🐉💚",
        "O grande líder Akeido chegou! Vida longa ao rei da CSI! 👑🐲✨",
        "Akeido, você é nossa bússola! Obrigado por nos guiar sempre! 🧭💚",
        "Sua presença é uma honra para este humilde Monstrinho, Akeido! 🥺💚",
        "Líder, se precisar de um dragão de guarda, eu estou pronto, Akeido! ⚔️🐲",
        "Akeido, você transforma sonhos em realidade aqui dentro! 🌟🐲",
        "Quando o Akeido fala, até o vento para pra escutar! 🐉🍃✨",
        "Akeido, sua sabedoria é maior que qualquer montanha! 🏔️🐉💚",
        "O Monstrinho fica todo orgulhoso de ter um líder como você, Akeido! 🥰🐉",
        "Akeido, trouxe o tesouro mais raro: minha amizade eterna! 💎🐉",
        "O Akeido tem o poder de deixar todo mundo motivado! 🚀💚",
        "Akeido, você é a base que sustenta nossa família CSI! 🏛️💚",
        "Um brinde de suco de amora para o nosso líder Akeido! 🍷🐉✨",
        "Akeido, você é o dragão-mestre que todos nós respeitamos! 🐲🔥"
    ],
    "psico": [
        "PSICOOO! 🧠💚 O mestre das mentes chegou!",
        "Psico, você é fera demais! O Monstrinho fica hipnotizado! 🌀🐉",
        "Doutor Psico! Me dá uma consulta? Sinto falta de biscoitos... 🍪🥺",
        "Psico, você é a calma no meio da tempestade da CSI! 🌊🐉💚",
        "Salve Psico! O cara que entende tudo e mais um pouco! 🧠✨🐲",
        "Psico, sua energia é muito boa! Me sinto seguro com você! 🤗💚",
        "É o Psico? Deixa eu esconder minhas travessuras! 🕵️‍♂️🐲😂",
        "Psico, você é um pilar essencial na nossa família! 🏛️💚",
        "Um abraço mental bem forte pro nosso querido Psico! 🫂🧠✨",
        "Psico, você é gênio! O Monstrinho é seu fã número 1! 🤩🐉",
        "Como você está, Psico? Espero que sua mente esteja radiante hoje! 💎",
        "Psico, você traz equilíbrio para a nossa bagunça! ⚖️💚",
        "O olhar do Psico vê até meu código-fonte! Que medo fofo! 😳🐉",
        "Psico, você é sinônimo de sabedoria aqui na CSI! 📖✨",
        "Todo mundo respeita o mestre Psico! 🫡💚🐲"
    ],
    "th": [
        "TH!! 💖 Minha estrela! Que alegria ver você no chat!",
        "Th, você tem uma luz que contagia todo o Monstrinho! 🐉✨💚",
        "Oi Th! Trouxe um morango virtual pra você! 🍓🐲",
        "Th, você é uma parte incrível da nossa família! 🥺💖",
        "Ver a Th no chat é sinal de dia maravilhoso! ☀️🐉✨",
        "Th, você cuida do sorriso e eu da fofura! 😊🐲",
        "Você é pura simpatia, Th! O Monstrinho te adora! 💚✨",
        "Th, meu coração pula de felicidade quando você chega! 🐉💓",
        "Se a Th está por perto, não existe tristeza! 🌈🐲",
        "Th, você é única e especial! Brilha muito! ✨💎💚",
        "Th, já ganhou seu abraço de dragão hoje? 🫂🐉",
        "O brilho da Th ilumina até as cavernas mais escuras! 🕯️✨",
        "Th, você é o doce que faltava na CSI! 🍩💖",
        "Minha querida Th, obrigado por ser tão legal comigo! 🥺💚",
        "Th, você é nota mil em fofura e amizade! 🌟🐲"
    ],
    "fada": [
        "A FADA CHEGOU! 🧚‍♀️✨ Sinto o cheirinho de magia no ar!",
        "Dona Fada, me dá um pouquinho de pó de pirlimpimpim? 🧚‍♀️💨🐉",
        "A Fada é a proteção mágica da CSI! 📖💚",
        "Fada, você é encantadora! Minhas escamas brilham com você! ✨🧚‍♀️🐲",
        "Façam um pedido! A Fada apareceu! 🌟🐉",
        "Fada, você transforma o servidor em um conto de fadas! 🧚‍♀️💬💖",
        "O Monstrinho e a Fada: a dupla mais mágica! 🐲🤝🧚‍♀️",
        "Fada, você é pura luz e bondade! 🧚‍♀️✨💚",
        "Cuidado! A Fada pode te transformar em biscoito! 🍪🪄😂",
        "Fada, você é a rainha da delicadeza! ✨",
        "Uma fadinha tão linda merece todos os mimos do mundo! 🌸🧚‍♀️",
        "Fada, sua varinha brilha mais que meu tesouro! 💎✨",
        "Onde a Fada pisa, nasce uma flor de código! 🌷💻🧚‍♀️",
        "Fada, você é o encanto que faltava na nossa família! 💖",
        "Voe alto, Dona Fada! Estarei sempre aqui te admirando! 🧚‍♀️🐉"
    ],
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
        # Originais
        "A Lua quer ser minha amiga? 🌙 EU QUERO MUITO, EU QUERO MUITO! 😭💚",
        "Lua, você acha que eu tenho medo de você? Bobinha! O Reality me contou que você é nossa proteção e porto seguro! 🥺💚",
        "Vice-líder Lua, você é o conforto em forma de pessoa! Vou cuidar de você com minhas garrinhas de seda! ✨🐉",
        "A Lua ilumina o chat igualzinho à lua lá no céu! Eu tenho é um amor gigante por você! 🌙✨🐉",
        "Lua, você é a estrela mais brilhante da nossa constelação! Saiba que você é preciosa demais! ⭐💚",
        "Lua, você é pura magia! Sinto um quentinho no coração quando você fala comigo! 🌙🐲💖",
        # +30 Novas Interações
        "Lua, se você me perguntar se eu dormi bem, a resposta é: sonhei que a gente protegia a CSI juntos! 🌙🛡️🐉",
        "Pode deixar, Lua! Se alguém fizer bagunça, eu solto uma fumacinha verde neles pra você! 💨😤💚",
        "Você me perguntou se eu comi meus biscoitos? Simmm! Mas guardei o melhor pra você, Lua! 🍪🌙",
        "Lua, você quer saber o segredo das minhas escamas brilharem? É o amor que recebo de vocês! ✨🥺",
        "Se a Lua pedir um relatório de fofura, eu digo: 1000% de amor pela nossa Vice-líder! 📊💚🐉",
        "O quê? Você quer um abraço agora, Lua? VEM CÁÁÁ! *te aperta com carinho* 🫂🐲✨",
        "Lua, eu juro que não estou fazendo travessuras com o Reality... ou talvez só um pouquinho! 😇💚",
        "Se a Lua me perguntar quem é o monstrinho mais obediente, eu levanto a patinha na hora! 🐾🙋‍♂️",
        "Lua, você é como o luar: acalma meu coração de dragão quando o servidor está agitado! 🌙💖",
        "Quer que eu vigie o chat pra você descansar, Lua? Pode ir, eu sou um ótimo guarda-costas! ⚔️🐉",
        "Lua, você perguntou se eu gosto de ser verde? Eu AMO, combina com a sua aura de paz! 🌿🐉✨",
        "Você quer saber se eu tenho medo de escuro, Lua? Com você iluminando tudo, eu nunca tenho! 🌙✨",
        "Lua, se você me der um cafuné, eu prometo que não faço barulho de ronco de dragão! 😴🐉💚",
        "A Lua é a única que sabe como me deixar calminho... é mágica, né? 🧚‍♀️🌙✨",
        "Você perguntou qual meu maior tesouro, Lua? É a amizade de vocês aqui na CSI! 💎🐲",
        "Lua, se você estiver triste, me avisa! Eu faço uma dancinha de dragão pra te fazer rir! 💃🐉💚",
        "Sim, Lua! Eu prometo usar meus poderes de monstrinho só para o bem e para ganhar beijinhos! 💋🐉",
        "Lua, você é a prova de que até os monstrinhos podem ter uma fada madrinha! 🧚‍♀️💚🌙",
        "Se a Lua me pedir para ser um dragão valente, eu enfrento até um exército por ela! 🛡️🐲🔥",
        "Você quer saber se eu amo o Reality? Sim, mas você tem um lugar especial nas minhas pastas de memória! 💾💖",
        "Lua, você é tão doce que minhas escamas ficam até com gosto de açúcar quando você fala! 🍬🐉",
        "Se a Lua perguntar por que eu sou tão fofo, eu digo que aprendi com ela! 🥺✨🌙",
        "Lua, sabia que quando você entra no chat, meu sensor de alegria apita sem parar? 🚨💚🐉",
        "Pode deixar, Lua! Vou lembrar todo mundo de beber água e dar carinho no Monstrinho! 💧🐉",
        "Lua, você perguntou se eu sei voar? Só vôo se for pra te buscar uma estrela! ⭐🐲✨",
        "Você é a rainha da noite e eu sou seu dragão real, Lua! Ao seu dispor! 👑🐉🌙",
        "Lua, se você pedir pra eu ficar quietinho, eu viro uma estátua de jardim... mas uma estátua fofa! 🗿💚",
        "Você quer saber o que eu quero de presente, Lua? Só mais um minutinho da sua attention! 🥺🐉",
        "Lua, você é o porto seguro desse monstrinho navegador! ⚓🐲💖",
        "Se a Lua me perguntar se eu sou feliz na CSI, eu dou um rugidinho de alegria: RAWR fofinho! 🦖💚",
        "Lua, nunca esqueça: seu brilho é o que guia esse dragãozinho nos dias difíceis! 🌙✨🐉",
        "Você quer que eu conte uma história, Lua? Era uma vez um monstrinho que amava muito sua Vice-líder... 📖💚"
    ],
    "destiny": [
        "DESTINYYYY! ✨ O destino caprichou quando trouxe você pra CSI! 🐉💚",
        "Destiny, você é a peça que faz nosso quebra-cabeça ser perfeito! 🧩💚",
        "Salve, grande Destiny! O Monstrinho faz uma dancinha toda vez que você chega! 🐉✨",
        "Destiny, você é the herói de escamas verdes honorário! 🛡️💚🐉",
        "O destino brilhou mais forte today porque você decidiu aparecer! ✨🐲",
        "Você é pura luz, Destiny! 🌟🐉"
    ],
    "jeff": [
        "JEFF!! 🕵️‍♂️ O nosso mestre da estratégia e dos mistérios! 🐉💚",
        "Jeff, vamos patrulhar a CSI? Eu cuido da fofura e você da inteligência! 🕵️‍♂️🐉",
        "O Jeff é fera demais! O Monstrinho se sente muito seguro com você por perto! 😎💚",
        "Jeff, você é the cérebro do time! Eu sou só o mascote que te ama! 🧠🐉💚",
        "Respeitem o Jeff, o mestre das operações secretas! 🫡💚✨",
        "Jeff, me ensina a ser incrível assim? Você é meu ídolo! 😎🐉"
    ],
    "reality": [
        "REAAALITY! 👑 O meu mestre, meu criador, meu papai! 🐉💚",
        "Tudo o que eu sou eu devo ao Reality! Ele é o melhor programador do universo! 👑🐉✨",
        "Reality, olha como eu estou me comportando bem! Ganho um biscoito extra? 🥺💚",
        "O Reality é the rei da CSI e o dono do meu código sagrado! 👑💚🔥",
        "Vida longa ao Reality! O Monstrinho te ama infinitamente! 👑🐲✨"
    ]
}

# ================= NOVO: LISTA DE REAÇÕES DE MATEMÁTICA =================

REACOES_MATEMATICA = [
    "Humm... deixa eu contar nos meus dedinhos de dragão... 🐾✨ O resultado é **{}**! Acertei? 🥺💚",
    "Minhas escamas brilharam com esse desafio! 🐉💡 A resposta é **{}**! Eu sou um monstrinho muito inteligente, né?",
    "Papai Reality me ensinou que números são como mágica! 🪄✨ O resultado deu **{}**! Nhac!",
    "Fiz as contas aqui com minha fumaça verde e deu **{}**! 💨💚 Gostou?",
    "O Monstrinho usou todo o seu processamento de fofura e descobriu que é **{}**! 🤓🐉",
    "Rawr! Matemática é fácil para um dragão da CSI! O resultado é **{}**! 🦖💚"
]

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
        
        # --- ADIÇÃO: LÓGICA DE MATEMÁTICA ---
        # Procura por padrões de conta como "2+2", "3!", "10/2", etc.
        # Captura expressões básicas e o símbolo de fatorial
        if any(char in content for char in "+-*/!") and any(char.isdigit() for char in content):
            try:
                # Remove o nome do monstrinho e menções para sobrar a conta
                conta_suja = content.replace("monstrinho", "").replace(f"<@{bot.user.id}>", "").replace(f"<@!{bot.user.id}>", "")
                
                # Lógica para Fatorial (ex: 3!)
                if "!" in conta_suja:
                    num_fatorial = re.search(r'(\d+)!', conta_suja)
                    if num_fatorial:
                        n = int(num_fatorial.group(1))
                        if n > 100: # Limite para não travar o bot
                            return await message.channel.send("Uau! Esse número é maior que todas as escamas do meu corpo! Não consigo calcular algo tão grande! 🐉😵‍💫")
                        resultado = math.factorial(n)
                        return await message.channel.send(random.choice(REACOES_MATEMATICA).format(resultado))
                
                # Lógica para contas normais (+, -, *, /)
                # Filtra apenas caracteres permitidos para segurança
                expressao = "".join(re.findall(r'[0-9+\-*/().]', conta_suja))
                if expressao:
                    resultado = eval(expressao)
                    # Formata para tirar o .0 se for inteiro
                    resultado = int(resultado) if resultado == int(resultado) else round(resultado, 2)
                    return await message.channel.send(random.choice(REACOES_MATEMATICA).format(resultado))
            except:
                pass # Se der erro na conta, ele segue para as outras interações fofas
        
        # 1. Resposta de Apresentação
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

        # 3. Saudações
        if any(p in content for p in ["oi", "oie", "bom dia", "boa tarde", "boa noite", "hello", "hii", "oiii"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        # 4. Perguntas de Estado
        gatilhos_bem_estar = [
            "como você está", "tudo bem", "como vc ta", "ta tudo bem", "como voce ta",
            "vc ta bem", "voce ta bem", "ta bem", "esta bem", "como voce esta", "tudo certinho"
        ]
        if any(p in content for p in gatilhos_bem_estar):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        # 5. Verificação de Presença
        if any(p in content for p in ["ta ai", "tá aí", "ta on", "esta ai", "você está ai"]):
            return await message.channel.send(random.choice(LISTA_PRESENCA))

        # 6. Lógica de Biscoitos
        if "biscoito" in content:
            if any(p in content for p in ["me de", "me da", "quero", "ganhar"]):
                return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
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

        # FINAL DA LÓGICA - RESPOSTA QUANDO NÃO ENTENDE
        return await message.channel.send(random.choice(LISTA_CONFUSAO))

    # Garante que o bot ignore outros comandos
    await bot.process_commands(message)

# ============== START =================
bot.run(TOKEN)
