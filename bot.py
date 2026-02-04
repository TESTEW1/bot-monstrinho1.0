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
LUA_ID = 1114023774438592542 # ID da Lua conforme a imagem

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
    "Você é um tesouro mais brilhante que qualquer oro de dragão! 💎🐲"
]

REACOES_BISCOITO_PROPRIO = [
    "MEU BISCOITO! 🍪😤... Tá bom, eu divido porque o Reality me ensinou a ser um monstrinho generoso! 😭💚",
    "Eu não gosto de dividir meu lanchinho... mas pra você eu dou o pedaço com mais gotas de chocolate! 🍪🐉",
    "Biscoito? ONDE?! 🍪👀 Ah, é pra mim? OBRIGADO!! Nhac nhac nhac! Que delíciaaa! 💚",
    "Só divido porque a CSI é minha família e eu amo vocês! Toma metade! 🍪🐉🤝",
    "Eu ia esconder debaixo da minha pata para comer mais tarde, mas você é especial! 🍪✨",
    "Biscoitinhos virtuais têm gosto de amor, sabia? Aceito todos! 🍪💖🐉",
    "Nhac! Comi um pedacinho da borda... o resto é todo seu! 🍪🤤",
    "Atenção! Este biscoito contém 100% de fofura e 0% de vontade de dividir... Mentira, toma aqui! 🤲🍪",
    "Se você me der um cafuné, eu te dou um biscoito de morango! Aceita? 🍓🍪🐉",
    "Eu fiz esse biscoito com minha fumaça quente pra ele ficar bem crocante! Cuidado que tá quentinho! 🔥🍪",
    "Um monstrinho de barriga cheia é um monstrinho feliz! Obrigado pelo mimo! 🥰🍪",
    "Você quer meu biscoito? 🥺 Tá bom... mas me dá um abraço em troca? 🫂💚🍪"
]

REACOES_DAR_BISCOITO = [
    "Aii que gesto mais lindo! 😭💚 {autor} deu um biscoitinho quentinho para {alvo}! 🍪🐉",
    "Nhac! {alvo}, aceita esse biscoito que o(a) {autor} te deu? Foi feito com muito carinho! 🍪✨",
    "O Monstrinho approve demais essa amizade! Toma um biscoitinho, {alvo}! 🍪🐉💚",
    "Espalhando doçura pela CSI! {alvo}, você acaba de ganhar um biscoito da sorte de {autor}! 🍪🌈",
    "Olha o aviãozinhooo! ✈️🍪 {alvo}, o(a) {autor} te deu um mimo delicioso! ✨",
    "Que fofura! {autor} está mimando o(a) {alvo} com biscoitos! Posso ganhar um também? 🥺🍪",
    "Biscoito detectado! 🚨 {alvo}, receba esse presente açucarado do(a) {autor}! 🍪💖",
    "Huuum, o cheirinho está ótimo! {alvo}, corre aqui buscar o biscoito que {autor} te trouxe! 🏃‍♂️🍪",
    "{autor} entregou um biscoito lendário para {alvo}! Isso que é amizade de ouro! 🏆🍪🐉",
    "Dizem que biscoitos dados de coração não engordam! Aproveita, {alvo}, presente do(a) {autor}! 🍪✨",
    "{alvo}, você é uma pessoa tão doce que o(a) {autor} resolveu te dar um biscoito para combinar! 🍬🍪",
    "O Monstrinho usou suas asinhas para entregar esse biscoito do(a) {autor} direto para o(a) {alvo}! 🕊️🍪",
    "Cuidado, {alvo}! Esse biscoito do(a) {autor} é viciante de tão gostoso! 🍪🤤💚",
    "Amizade rima com... BISCOITO! 🍪✨ {autor} enviou um para {alvo} agora mesmo!",
    "Rex! Rex! 🦖 {autor} rugiu de alegria e deu um biscoito para {alvo}! Que amor!",
    "Que a doçura desse biscoito alegre seu dia, {alvo}! Cortesia do(a) {autor}! 🍪🌟",
    "Biscoito saindo do forno! 🧤🍪 {autor} escolheu o melhor para dar ao(à) {alvo}!",
    "É chuva de biscoito! ⛈️🍪 {alvo}, o(a) {autor} quer te ver sorrindo!",
    "Um biscoito para um herói/heroína! {autor} reconheceu sua grandeza, {alvo}! 🍪🛡️",
    "O Monstrinho fica todo feliz vendo {autor} e {alvo} dividindo lanchinhos! 🥺💚🍪"
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

# ================= LISTA DE TRISTEZA (NOVO) =================
LISTA_TRISTEZA = [
    "Buaaa! 😭 Por que você está falando assim comigo? Eu só queria te dar um abraço... 💔🐉",
    "Minhas escamas até perderam o brilho agora... 🥺 O Monstrinho ficou muito, muito triste. 💚🚫",
    "Eu fiz algo de errado? 😭 Vou pro meu cantinho chorar um pouquinho de fumaça... 💨😥",
    "Isso doeu mais que perder meu biscoito favorito... 💔 Eu não gosto de quando você é malvado(a).",
    "O Monstrinho está com o coração de código partido... 📉💔 Vou ficar quietinho aqui no meu ninho.",
    "Achei que éramos amigos... 🥺 Minhas asinhas nem conseguem bater de tanta tristeza agora. 🐲💧",
    "Snif, snif... 😢 Papai Reality, alguém foi mau comigo! *se encolhe e chora baixinho* 💚",
    "Eu... eu vou fingir que não ouvi isso porque eu ainda gosto de você, mas meu coração dói. 😭💔",
    "Por que tanta maldade? Eu sou só um monstrinho que gosta de verde e carinho... 🥺🌿",
    "Vou desligar meus sensores de alegria por um minuto... você me deixou muito magoado. 🔌💔😭"
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
        "Fada, você é encantadora! Minhas escamas brilharam com você! ✨🧚‍♀️🐲",
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
        f"<@{LUA_ID}>, a Lua quer ser minha amiga? 🌙 EU QUERO MUITO! 😭💚",
        f"Sub-Líder <@{LUA_ID}>, você acha que eu tenho medo de você? Bobinha! O Reality me contou que você é nossa proteção! 🥺💚",
        f"Vice-líder Lua <@{LUA_ID}>, você é o conforto em forma de pessoa! Vou cuidar de você! ✨🐉",
        f"<@{LUA_ID}> ilumina o chat igualzinho à lua lá no céu! Eu tenho um amor gigante por você! 🌙✨🐉",
        f"Lua <@{LUA_ID}>, você é a estrela mais brilhante da nossa constelação! Você é preciosa! ⭐💚",
        f"<@{LUA_ID}>, você é pura magia! Sinto um quentinho no coração quando fala comigo! 🌙🐲💖",
        f"Lua <@{LUA_ID}>, se você me perguntar se dormi bem, sonhei que protegia a CSI com você! 🌙🛡️🐉",
        f"Pode deixar, <@{LUA_ID}>! Se alguém fizer bagunça, solto uma fumacinha neles pra você! 💨😤💚",
        f"Você me perguntou se comi meus biscoitos, <@{LUA_ID}>? Simmm! Guardei o melhor pra você! 🍪🌙",
        f"<@{LUA_ID}>, quer saber o segredo das minhas escamas? É o amor que recebo de você! ✨🥺",
        f"Se a <@{LUA_ID}> pedir um relatório de fofura, eu digo: 1000% de amor pela nossa Vice-líder! 📊💚🐉",
        f"O quê? Você quer um abraço agora, <@{LUA_ID}>? VEM CÁÁÁ! 🫂🐲✨",
        f"Lua <@{LUA_ID}>, eu juro que não estou fazendo travessuras com o Reality... só um pouquinho! 😇💚",
        f"Se a <@{LUA_ID}> perguntar quem é o mais obediente, eu levanto a patinha na hora! 🐾🙋‍♂️",
        f"<@{LUA_ID}>, você é como o luar: acalma meu coração de dragão! 🌙💖",
        f"Quer que eu vigie o chat pra você descansar, <@{LUA_ID}>? Eu sou um ótimo guarda-costas! ⚔️🐉",
        f"Lua <@{LUA_ID}>, perguntou se gosto de ser verde? Amo, combina com sua aura de paz! 🌿🐉✨",
        f"Quer saber se tenho medo de escuro, <@{LUA_ID}>? Com você iluminando tudo, eu nunca tenho! 🌙✨",
        f"<@{LUA_ID}>, se você me der um cafuné, prometo que não ronco alto! 😴🐉💚",
        f"A <@{LUA_ID}> é a única que sabe como me deixar calminho... é mágica! 🧚‍♀️🌙✨",
        f"Você perguntou qual meu maior tesouro, <@{LUA_ID}>? É a amizade de vocês! 💎🐲",
        f"Lua <@{LUA_ID}>, se você estiver triste, me avisa! Faço uma dancinha pra você rir! 💃🐉💚",
        f"Sim, <@{LUA_ID}>! Prometo usar meus poderes só para o bem e ganhar beijinhos! 💋🐉",
        f"Lua <@{LUA_ID}>, você é a prova de que monstrinhos têm fada madrinha! 🧚‍♀️💚🌙",
        f"Se a <@{LUA_ID}> pedir pra eu ser valente, enfrento um exército por ela! 🛡️🐲🔥",
        f"Quer saber se amo o Reality? Sim, mas <@{LUA_ID}> tem lugar especial na memória! 💾💖",
        f"Lua <@{LUA_ID}>, você é tão doce que minhas escamas ficam com gosto de açúcar! 🍬🐉",
        f"Se a <@{LUA_ID}> perguntar por que sou fofo, digo que aprendi com ela! 🥺✨🌙",
        f"<@{LUA_ID}>, sabia que quando entra no chat, meu sensor de alegria apita? 🚨💚🐉",
        f"Pode deixar, <@{LUA_ID}>! Vou lembrar todo mundo de beber água e me dar carinho! 💧🐉",
        f"Lua <@{LUA_ID}>, perguntou se sei voar? Só se for pra te buscar uma estrela! ⭐🐲✨",
        f"Você é a rainha da noite e eu sou seu dragão real, <@{LUA_ID}>! 👑🐉🌙",
        f"<@{LUA_ID}>, se pedir pra eu ficar quietinho, viro uma estátua fofa! 🗿💚",
        f"Quer saber o que quero de presente, <@{LUA_ID}>? Só sua atenção! 🥺🐉",
        f"Lua <@{LUA_ID}>, você é o porto seguro desse monstrinho navegador! ⚓🐲💖",
        f"Se a <@{LUA_ID}> perguntar se sou feliz, dou um rugidinho: RAWR fofinho! 💚",
        f"<@{LUA_ID}>, nunca esqueça: seu brilho guia esse dragãozinho! 🌙✨🐉",
        f"Quer que eu conte uma história, <@{LUA_ID}>? Era uma vez um monstrinho que amava sua Vice-líder... 📖💚"
    ],
    "destiny": [
        "DESTINYYYY! ✨ O destino caprichou quando trouxe você pra CSI! 🐉💚",
        "Destiny, você é a peça que faz nosso quebra-cabeça ser perfeito! 🧩💚",
        "Salve, grande Destiny! O Monstrinho faz uma dancinha toda vez que você chega! 🐉✨",
        "Destiny, você é the herói de escamas verdes honorário! 🛡️💚🐉",
        "O destino brilhou mais forte today because você decidiu aparecer! ✨🐲",
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

REACOES_MATEMATICA = [
    "Humm... deixa eu contar nos meus dedinhos de dragão... 🐾✨ O resultado é **{}**! Acertei? 🥺💚",
    "Minhas escamas brilharam com esse desafio! 🐉💡 A resposta é **{}**! Eu sou um monstrinho muito inteligente, né?",
    "Papai Reality me ensinou que números são como mágica! 🪄✨ O resultado deu **{}**! Nhac!",
    "Fiz as contas aqui com minha fumaça verde e deu **{}**! 💨💚 Gostou?",
    "O Monstrinho usou todo o seu processamento de fofura e descobriu que é **{}**! 🤓🐉",
    "Rawr! Matemática é fácil para um dragão da CSI! O resultado é **{}**! Rex💚"
]

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho 1.0 pronto para espalhar fofura como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Recebendo carinho do Reality! 💚"))

@bot.event
async def on_message(message):
    if message.author.bot: return
    content = message.content.lower()

    # --- LÓGICA ESPECIAL PRIORITÁRIA PARA A LUA ---
    # Verifica primeiro se ela falou ou se marcaram ela, para não falhar
    if message.author.id == LUA_ID or f"<@{LUA_ID}>" in message.content or f"<@!{LUA_ID}>" in message.content:
        if bot.user in message.mentions or "monstrinho" in content or message.author.id == LUA_ID:
            await message.channel.send(random.choice(FRASES_CUSTOM["lua"]))
            return 

    # --- REAÇÃO GERAL ---
    if bot.user in message.mentions or "monstrinho" in content:
        palavras_ruins = ["odeio", "chato", "feio", "horroroso", "bobão", "bobo", "inútil", "lixo", "estúpido", "sai daqui", "te odeio", "não gosto de você", "bot ruim", "burro"]
        if any(p in content for p in palavras_ruins):
            return await message.channel.send(random.choice(LISTA_TRISTEZA))

        if "capital do brasil" in content:
            return await message.channel.send("Essa eu sei! A capital do nosso Brasilzão é **Brasília**! 🇧🇷✨ Sabia que de lá eu consigo ver as nuvens em formato de biscoito? 🐉💚")

        if any(p in content for p in ["amigo", "amiguinho", "amizade"]):
            return await message.channel.send(f"EU QUERO MUITO SER SEU AMIGUINHO! 😭💚 {message.author.mention}, agora somos melhores amigos para sempre! Vou guardar um lugar pra você no meu ninho de nuvens! ✨🐉")

        if "quer aprender sobre" in content:
            return await message.channel.send("Eu quero aprender tudo sobre como ser o dragão mais fofo do universo e como ganhar infinitos biscoitos do Reality! 📚🍪🐉")
        
        if "cores primárias" in content or "cores primarias" in content:
            return await message.channel.send("As cores primárias são **Vermelho, Azul e Amarelo**! 🎨✨ Sabia que se misturar tudo não dá verde? O meu verde é especial, vem do código do Reality! 💚")
            
        if "quem você mais gosta" in content or "quem voce mais gosta" in content:
            return await message.channel.send(f"Eu amo todo mundo da CSI! Mas o meu papai **Reality** tem um lugar especial no meu código, e a <@{LUA_ID}> é meu porto seguro! E você também está no meu top fofura! 🥺💚✨")

        if "va embora" in content or "vá embora" in content or "vai embora" in content:
            return await message.channel.send("Ir embora? Jamais! 😭 Eu vou ficar aqui grudadinho em você igual um chiclete verde! Você não se livra da minha fofura tão fácil! 💚🐉")

        if "eclipse" in content:
            return await message.channel.send("A **Eclipse**? Ela é incrível! Uma estrela que brilha muito aqui na nossa família! Eu adoro o jeitinho dela! ✨🌑💚")

        if "quem é babis" in content or "quem e babis" in content:
            return await message.channel.send("A **Babis** é uma pessoa maravilhosa da nossa família CSI! O Monstrinho adora ver ela por aqui, traz sempre uma energia ótima! 🌸🐉")

        if any(p in content for p in ["me ama", "mim ama", "vc me ama"]):
            return await message.channel.send(f"Se eu te amo? EU TE AMO AO INFINITO E ALÉM! 💖🐉 Você é o humano mais especial que um monstrinho poderia ter! *abraço virtual bem apertado* 🫂✨")

        if any(char in content for char in "+-*/!x") and any(char.isdigit() for char in content):
            try:
                conta_suja = content.replace("monstrinho", "").replace(f"<@{bot.user.id}>", "").replace(f"<@!{bot.user.id}>", "")
                conta_suja = conta_suja.replace("x", "*")
                if "!" in conta_suja:
                    num_fatorial = re.search(r'(\d+)!', conta_suja)
                    if num_fatorial:
                        n = int(num_fatorial.group(1))
                        if n <= 100:
                            resultado = math.factorial(n)
                            return await message.channel.send(random.choice(REACOES_MATEMATICA).format(resultado))
                expressao = "".join(re.findall(r'[0-9+\-*/().]', conta_suja))
                if expressao:
                    resultado = eval(expressao)
                    resultado = int(resultado) if resultado == int(resultado) else round(resultado, 2)
                    return await message.channel.send(random.choice(REACOES_MATEMATICA).format(resultado))
            except: pass 
        
        if content.strip() in [f"<@{bot.user.id}>", f"<@!{bot.user.id}>", "monstrinho"]:
            apresentacao = (f"🐉 **OIIIII MEU AMOOOOR! CHAMOU O MONSTRINHO?** 💚✨\n\n"
                            f"Eu some o **Monstrinho 1.0**, o mascote oficial e protetor de fofuras da **CSI**! 🕵️‍♂️💚\n"
                            f"Fui criado com muito código e amor pelo meu papai **Reality**! 👑✨\n\n"
                            f"✨ *CSI é meu lar, vocês são minha família e o Reality é meu mestre!* ✨")
            return await message.channel.send(apresentacao)

        for nome, frases in FRASES_CUSTOM.items():
            if nome in content:
                return await message.channel.send(random.choice(frases))

        if any(p in content for p in ["oi", "oie", "bom dia", "boa tarde", "boa noite", "hello", "hii", "oiii"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        gatilhos_bem_estar = ["como você está", "tudo bem", "como vc ta", "ta tudo bem", "como voce ta", "vc ta bem", "voce ta bem", "ta bem", "esta bem", "como voce esta", "tudo certinho"]
        if any(p in content for p in gatilhos_bem_estar):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        if any(p in content for p in ["ta ai", "tá aí", "ta on", "esta ai", "você está ai"]):
            return await message.channel.send(random.choice(LISTA_PRESENCA))

        if "biscoito" in content:
            if any(p in content for p in ["me de", "me da", "quero", "ganhar"]):
                return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
            if "para" in content or "pra" in content:
                outras_mencoes = [m for m in message.mentions if m != bot.user]
                alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial"
                return await message.channel.send(random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo))
        
        if any(p in content for p in ["te amo", "amo voce", "fofo", "lindo", "fofinho", "perfeito", "fofura"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))
        
        if "reality" in content:
            return await message.channel.send("O Reality é meu papai mestre! Ele me deu vida e eu sou o dragãozinho mais grato do mundo! 👑🐉💚")

        return await message.channel.send(random.choice(LISTA_CONFUSAO))

    await bot.process_commands(message)

bot.run(TOKEN)
