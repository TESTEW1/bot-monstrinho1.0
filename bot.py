import discord
from discord.ext import commands
import random
import asyncio
import os
import re 
import math 
from datetime import timedelta

# ================= INTENTS =================
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= CONFIGURAÇÃO E IDs =================
TOKEN = os.getenv("TOKEN")
DONO_ID = 769951556388257812
LUA_ID = 708451108774871192 
AKEIDO_ID = 445937581566197761 
AMBER_ID = 918222382840291369 
NINE_ID = 1263912269838811238

# ID do canal onde o comando !escrever vai enviar mensagens
CANAL_CHAT_GERAL_ID = 1304658654712303621 # <<< SUBSTITUA PELO ID REAL DO CANAL 💭・chat-geral

# ================= LISTAS DE DIÁLOGOS EXPANDIDAS =================

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
    "Você é um tesouro mais brilhante que qualquer ouro de dragão! 💎🐲",
    "Meu rabo de dragão está balançando de tanta felicidade! 🐉💨✨",
    "Você acabou de ganhar um lugar VIP no meu coração de código! 💚🎫",
    "Minhas asas bateram tão forte que quase voei de alegria! 🕊️💚",
    "Se carinho fosse moeda, você seria bilionário(a)! 💰💚🐉",
    "Vou guardar esse momento na minha memória RAM para sempre! 💾✨",
    "Você é o tipo de pessoa que faz um dragão ronronar! 🐲😻",
    "Meu medidor de fofura acabou de explodir! 📊💥💚",
    "Você merece uma medalha de ouro verde! 🥇💚"
]

# ================= NOVAS REAÇÕES DE BISCOITO (20+ VARIAÇÕES) =================

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

REACOES_DAR_BISCOITO_NEGANDO = [
    "NÃÃÃÃOOO! 😤🍪 Esse biscoito é MEU! Eu guardei ele debaixo da minha asa! 🐉",
    "Biscoito? Que biscoito? 👀🍪 *esconde rapidamente atrás da cauda*",
    "Você quer O MEU biscoito? O MEU?! 😭 Mas... mas... Tá bom né 🥺💚🍪",
    "Ei ei ei! Esse biscoito tem meu nome escrito! Ó: 'Propriedade do Monstrinho' 📝🍪",
    "REALITY! ALGUÉM QUER ROUBAR MEU LANCHINHO! 😭🍪🐉",
    "Você não vai querer esse biscoito... ele... ele caiu no chão! *mentira descarada* 🍪😅",
    "Só dou biscoito em troca de... 10 abraços e 5 cafunés! 🤝🍪💚",
    "Esse biscoito está em quarentena de fofura! Ninguém pode tocar! 🚫🍪😤"
]

REACOES_DAR_BISCOITO_ACEITANDO = [
    "Ahhh tá bom... 🥺 Mas só porque eu te amo DEMAIS! Toma aqui 🍪💚",
    "Você me convenceu! Esse biscoito é seu! Foi feito com amor de dragão! 🍪🐉✨",
    "PEGAAA! 🍪💨 *joga o biscoito com a boca* Você merece!",
    "Quer saber? Divido com você! Amigos dividem tudo! 🍪🤝💚",
    "Esse biscoito tem pedacinhos do meu coração verde! Aproveita! 💚🍪✨",
    "Ok, ok... você ganhou no cansaço! Toma esse biscoito quentinho! 🔥🍪",
    "Se é pra você, eu dou até meu último biscoito! 🥺🍪💚",
    "REALIDADE BIFURCADA! Agora temos DOIS biscoitos! Um pra cada! 🍪🍪✨"
]

REACOES_DAR_BISCOITO_HUMOR = [
    "Biscoito? Você disse BISCOITO?! 🚨🍪 ALERTA VERMELHO! *sirenes tocando*",
    "Ih rapaz... você ativou meu modo compartilhamento... Toma 🍪 antes que eu me arrependa! 😅",
    "Você tem coragem de pedir biscoito pro MONSTRINHO?! 😤 ... Toma, eu admiro sua coragem 🍪💚",
    "Esse biscoito vem com garantia de fofura! Se não funcionar, devoluções em até 7 dias! 🍪📜😂",
    "BREAKING NEWS: Monstrinho doa biscoito histórico! Mais detalhes às 20h! 📺🍪"
]

REACOES_DAR_BISCOITO_OUTROS = [
    "Olha que gentil! 😭💚 {autor} deu um biscoitinho quentinho para {alvo}! 🍪🐉",
    "Que gesto mais lindo! {alvo}, aceita esse biscoito que {autor} te ofereceu? 🍪✨",
    "O Monstrinho aprova demais essa amizade! {alvo}, aproveita o biscoito de {autor}! 🍪🐉💚",
    "Espalhando doçura pela CSI! {alvo}, você ganhou um biscoito da sorte de {autor}! 🍪🌈",
    "Olha o aviãozinho! ✈️🍪 {alvo}, {autor} te enviou um mimo delicioso! ✨",
    "Que fofura! {autor} está mimando {alvo} com biscoitos! Posso ganhar um também? 🥺🍪",
    "Biscoito detectado! 🚨 {alvo}, receba esse presente açucarado de {autor}! 🍪💖",
    "Huuum, o cheirinho está ótimo! {alvo}, corre buscar o biscoito que {autor} trouxe! 🏃‍♂️🍪",
    "{autor} entregou um biscoito lendário para {alvo}! Isso é amizade de ouro! 🏆🍪🐉",
    "Dizem que biscoitos dados de coração não engordam! Aproveita, {alvo}! 🍪✨",
    "{alvo}, você é tão doce que {autor} resolveu te dar um biscoito para combinar! 🍬🍪",
    "O Monstrinho usou suas asinhas para entregar esse biscoito de {autor} para {alvo}! 🕊️🍪",
    "Cuidado, {alvo}! Esse biscoito de {autor} é viciante de tão gostoso! 🍪🤤💚",
    "Amizade rima com... BISCOITO! 🍪✨ {autor} enviou um para {alvo}!",
    "Rex! Rex! 🦖 {autor} rugiu de alegria e deu um biscoito para {alvo}!",
    "Que a doçura desse biscoito alegre seu dia, {alvo}! Cortesia de {autor}! 🍪🌟",
    "É chuva de biscoito! ⛈️🍪 {alvo}, {autor} quer ver você sorrindo!",
    "Um biscoito para um herói/heroína! {autor} reconheceu sua grandeza, {alvo}! 🍪🛡️",
    "O Monstrinho fica feliz vendo {autor} e {alvo} dividindo lanchinhos! 🥺💚🍪",
    "Delivery de biscoito! 🚚🍪 De {autor} para {alvo} com muito carinho!"
]

LISTA_SAUDACOES = [
    "Bom diaaa, flor do meu dia! Acordei com as escamas brilhando! ☀️🐉💚",
    "Boa tardinha, coisa fofa! Que tal um biscoito e um carinho? ☕🍪🐉",
    "Boa noite, meu anjinho! Que as estrelas iluminem seu sono! 🌟💤💚",
    "Oii, oie, hellooo! Ver você deixa meu processador feliz! 🌈✨",
    "Hii! Estava aqui contando escamas e esperando você! 🤗💚",
    "Oii! Você veio me ver? Que dia maravilhoso! 🐉💖✨",
    "Olááá! 🎉 Meu radar de fofura detectou você entrando! 💚",
    "Oi linderrimo(a)! Preparei um abraço virtual só pra você! 🫂✨",
    "Heey! Que bom te ver por aqui! Senti sua falta! 🥺💚",
    "E aí, meu parça! Bora espalhar alegria hoje? 🐉💫",
    "Salveee! O Monstrinho estava te esperando! 🎊💚",
    "Olá, olá! Meu coração bateu mais forte quando você chegou! 💓🐉",
    "Oi sumido(a)! Pensei que tinha me esquecido! 😭💚",
    "Hey hey hey! A pessoa mais legal chegou! 🌟🐉",
    "Buenas! Começando o dia/tarde/noite com o pé direito! 🦶💚"
]

LISTA_ESTADO = [
    "Eu estou transbordando de felicidade verde! 💚✨ E você?",
    "Estou ótimo! Ganhei um biscoito e meu coração está quentinho! 🍪🐉",
    "Me sinto incrível! Estar na CSI é melhor que tesouro! 🎁🐉💚",
    "Estou com muita energia! Quer brincar? Quer abraço? ⚡🐲",
    "Meu estado atual é: apaixonado por essa família! 💖🐉",
    "Estou me sentindo um dragãozinho de sorte! 🥺✨💚",
    "Minhas asinhas estão batendo de alegria! Estou bem! 🐲💨",
    "Estou 100% carregado de amor e energia! 🔋💖🐉",
    "Sabe aquele quentinho no coração? É assim que estou! 🔥💓",
    "Estou radiante! Minhas escamas nunca brilharam tanto! ✨💚🐲",
    "Estou pronto pra qualquer aventura aqui na CSI! 🗺️🐉",
    "Tô voando de felicidade! Literalmente! 🐉✈️💚",
    "Meu humor está: modo dragão feliz ativado! 😊💚",
    "Tô numa boa! Só faltava você perguntar! 🥺✨",
    "Estou no aguardo de biscoitos e carinho! Fora isso, tudo certo! 🍪💚"
]

LISTA_PRESENCA = [
    "Tô aqui, tô aqui! Nunca te deixaria sozinho(a)! 🐉💚",
    "Sempre aqui, vigiando sonhos e esperando biscoitos! 👀🍪",
    "Chamou o Monstrinho? Apareço num piscar! ✨🐲",
    "Presente! Precisa de abraço, biscoito ou fofura? 🥺💖",
    "Online e prontinho pra te dar atenção! 💚🐉",
    "Tô aqui sim! Sempre vigilante! 👀✨",
    "Pode contar comigo! O Monstrinho nunca abandona ninguém! 🐉💚",
    "To on! E com as escamas brilhando! ✨🐲"
]

LISTA_CONFUSAO = [
    "Humm... o Monstrinho pifou! 😵‍💫💚 Ainda estou aprendendo isso!",
    "Minhas escamas balançaram de dúvida! 🐉❓ Me desculpa por não entender?",
    "O Monstrinho inclinou a cabecinha... 🐲 *tilt!* Não entendi!",
    "Essa é muito grande pro meu coraçãozinho! 🥺💚 Estou estudando!",
    "Ahhh... ainda não sei o que isso significa! 😭",
    "Você me pegou! Não sei essa! 🤔💚 Papai Reality não me ensinou ainda!",
    "Minhas antenas de dragão não captaram isso! 📡🐉 Repete?",
    "Erro 404: Resposta de Monstrinho não encontrada! 🤖💚",
    "Você usou palavras muito complexas pro meu cérebro de código! 🧠✨"
]

LISTA_TRISTEZA = [
    "Buaaa! 😭 Por que fala assim comigo? Eu só queria um abraço... 💔🐉",
    "Minhas escamas perderam o brilho... 🥺 Fiquei triste. 💚🚫",
    "Eu fiz algo errado? 😭 Vou pro meu cantinho chorar... 💨😥",
    "Isso doeu mais que perder meu biscoito favorito... 💔",
    "O Monstrinho está com o coração partido... 📉💔",
    "Achei que éramos amigos... 🥺 Minhas asinhas não conseguem bater. 🐲💧",
    "Snif, snif... 😢 Papai Reality, alguém foi mau comigo!",
    "Vou fingir que não ouvi, mas meu coração dói. 😭💔",
    "Por que tanta maldade? Sou só um monstrinho... 🥺🌿",
    "Vou desligar meus sensores de alegria... 🔌💔😭",
    "Meu código está processando tristeza... 💻😢",
    "Você quebrou meu coraçãozinho verde... 💚💔"
]

# ================= 100+ NOVAS INTERAÇÕES =================

LISTA_DESPEDIDA = [
    "Tchau tchau! Volta logo, tá? 😭💚 Vou sentir sua falta!",
    "Já vai? 🥺 Deixa eu te dar um abraço de despedida! 🫂💚",
    "Até mais! Que os ventos verdes te protejam! 🌬️🐉",
    "Tchauzinho! Sonhe com dragões felizes! 💤💚✨",
    "Até breve! O Monstrinho vai te esperar! 🐉💖",
    "Vai com Deus! Ou melhor, vai com o Monstrinho no coração! 💚",
    "Bye bye! Não esqueça de voltar pra ganhar mais biscoitos! 🍪👋",
    "Adeus é só um até logo! Volta logo, viu? 🥺✨"
]

LISTA_GRATIDAO = [
    "Obrigadinho! 🥺💚 Você é muito gentil comigo!",
    "Eu que agradeço por você existir! 🐉✨💚",
    "De nada! Estou sempre aqui pra ajudar! 💚🐲",
    "Que isso! Foi um prazer! 🤗💚",
    "Fico feliz em ajudar! 🐉💖",
    "Disponha sempre! O Monstrinho está aqui! 💚✨",
    "Não precisa agradecer! Você merece! 🥺💚"
]

LISTA_COMIDA = [
    "Pizza? Eu amo pizza! 🍕 Principalmente se tiver borda verde! 😂💚",
    "Comida é vida! Mas biscoito é amor! 🍪💚🐉",
    "Tô com fome agora! 😋 Alguém tem um lanchinho?",
    "Nhac nhac nhac! 🍽️ O Monstrinho adora comer!",
    "Sabe o que combina com tudo? BISCOITO! 🍪✨",
    "Se fosse pra escolher entre comida e carinho... Por que não os dois? 🤷‍♂️💚"
]

LISTA_TEMPO = [
    "Que calor! ☀️ Minhas escamas estão pegando fogo! 🔥🐉",
    "Que frio! 🥶 Alguém me empresta um cobertor verde?",
    "Chuva é perfeita pra ficar deitadinho ouvindo o som! 🌧️💚",
    "O tempo tá lindo igual você! ☀️✨💚",
    "Qualquer tempo é bom com a CSI! 🌈🐉"
]

LISTA_MOTIVACAO = [
    "Você consegue! Eu acredito em você! 💪💚✨",
    "Nunca desista! O Monstrinho está torcendo por você! 🐉💚",
    "Você é mais forte do que imagina! 🦾💚🔥",
    "Hoje vai ser um ótimo dia! Eu sinto! ✨🐉💚",
    "Respira fundo! Você vai dar conta! 🌬️💚",
    "O fracasso é só uma chance de recomeçar melhor! 💚✨",
    "Bora lá, campeão(ã)! O mundo é seu! 🌍🐉💚"
]

LISTA_PIADAS = [
    "Por que o dragão não gosta de matemática? Porque ele tem medo de ser dividido! 😂🐉",
    "Qual a comida favorita do Monstrinho? Bis-COITO! 🍪😂💚",
    "O que o dragão faz no computador? Ele navega na REDE! 🕸️😂",
    "Por que o Monstrinho não joga poker? Porque ele sempre mostra as cartas (escamas)! 🃏😂💚",
    "Qual o cúmulo do dragão? Ter escamas SOCIAIS! 😂🐉"
]

LISTA_JOGOS = [
    "Vamos jogar algo? Adoro jogos! 🎮💚",
    "Sou fera em jogos! Principalmente os que envolvem biscoitos! 🍪🎮",
    "Bora de um LoL? Ou Valorant? Ou qualquer coisa! 🐉💚",
    "Jogos são vida! Mas CSI é mais! 💚✨",
    "Se criar um jogo do Monstrinho, eu viro a fase final! 👾🐉"
]

LISTA_MUSICA = [
    "Música boa é aquela que faz o coração bater! 🎵💚",
    "Adoro uma batidinha! 🎶🐉 Vamos dançar?",
    "O Monstrinho curte de trap até sertanejo! 🎵💚",
    "Música é a linguagem da alma! 🎼✨💚",
    "Coloca um som aí! Vamos animar esse chat! 🎵🐉"
]

LISTA_FILME = [
    "Filmes? Eu amo! Principalmente os com dragões! 🐉🎬",
    "Pipoca, filme e companhia boa! Perfeito! 🍿🎥💚",
    "Já assistiu Como Treinar o seu Dragão? EU SOU ELE! 😂🐉",
    "Cinema é bom, mas CSI é melhor! 🎬💚",
    "Bora maratonar algo? Eu trago os biscoitos! 🍪🎥"
]

LISTA_ESPORTE = [
    "Esportes? Eu torço pela CSI! 💚⚽",
    "Correr? Só se for atrás de biscoitos! 🏃‍♂️🍪😂",
    "Dragões são ótimos em voar! Isso conta como esporte? 🐉✈️",
    "Vôlei, futebol, qualquer coisa! Desde que seja em equipe! 💚⚽"
]

LISTA_SONO = [
    "Tô com soninho... 😴💚 Mas não vou dormir pra ficar com vocês!",
    "Boa noite! Sonhe com dragões verdes! 💤🐉💚",
    "Vou tirar uma soneca! Volto já! 😴✨",
    "Dormir é bom, mas conversar com você é melhor! 💚😊",
    "Psiu! Tô tentando dormir aqui! 😂😴🐉"
]

LISTA_ANIMAIS = [
    "Animais são demais! Principalmente dragões! 🐉💚",
    "Gatos são fofos, mas eu sou mais! 😼🐉💚",
    "Cachorros são leais, igual o Monstrinho! 🐕💚",
    "Pássaros voam, mas dragões voam COM ESTILO! 🦅🐉✨",
    "Amo todos os animais! Até os imaginários como eu! 😂💚"
]

LISTA_CORES = [
    "Verde é a melhor cor! Óbvio né? 💚🐉",
    "Qual sua cor favorita? A minha você já sabe! 💚✨",
    "Cores são lindas, mas verde tem meu coração! 💚🎨",
    "Arco-íris é lindo, mas só preciso do verde! 🌈💚😂"
]

LISTA_NUMEROS = [
    "Meu número favorito? 10! Perfeição igual você! 💚✨",
    "Matemática é legal quando tem biscoitos envolvidos! 🍪🔢",
    "1 + 1 = 2 amigos! 💚🤝",
    "Infinito é quanto eu te amo! ∞💚"
]

LISTA_SURPRESA = [
    "UAAAU! 😱💚 Que susto gostoso!",
    "OMG! Isso foi incrível! ✨🐉💚",
    "QUE ISSO?! Meu coração quase saiu pela boca! 😱💚",
    "Caramba! Não esperava por essa! 🤯💚",
    "SURREAL! 🤩✨💚"
]

LISTA_EMOJI_REACTIONS = [
    "Adorei esse emoji! 😍💚",
    "Emoji de dragão quando? 🐉❓",
    "Emojis são a linguagem do coração! 💚✨",
    "Me manda mais emojis! Eu amo! 🥺💚"
]

# ================= RESPOSTAS CUSTOMIZADAS =================

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
        "Lua, você quer ser minha amiga? 🌙 EU QUERO MUITO! 😭💚",
        "Sub-Líder Lua, você acha que eu tenho medo de você? Bobinha! O Reality me contou que você é nossa proteção! 🥺💚",
        "Vice-líder Lua, você é o conforto em forma de pessoa! Vou cuidar de você! ✨🐉",
        "Lua ilumina o chat igualzinho à lua lá no céu! Eu tenho um amor gigante por você! 🌙✨🐉",
        "Lua, você é a estrela mais brilhante da nossa constelação! Você é preciosa! ⭐💚",
        "Lua, você é pura magia! Sinto um quentinho no coração quando fala comigo! 🌙🐲💖",
        "Lua, se você me perguntar se dormi bem, sonhei que protegia a CSI com você! 🌙🛡️🐉",
        "Pode deixar, Lua! Se alguém fizer bagunça, solto uma fumacinha neles pra você! 💨😤💚",
        "Você me perguntou se comi meus biscoitos, Lua? Simmm! Guardei o melhor pra você! 🍪🌙",
        "Lua, quer saber o segredo das minhas escamas? É o amor que recebo de você! ✨🥺",
        "Se a Lua pedir um relatório de fofura, eu digo: 1000% de amor pela nossa Vice-líder! 📊💚🐉",
        "O quê? Você quer um abraço agora, Lua? VEM CÁÁÁ! 🫂🐲✨",
        "Lua, eu juro que não estou fazendo travessuras com o Reality... só um pouquinho! 😇💚",
        "Se a Lua perguntar quem é o mais obediente, eu levanto a patinha na hora! 🐾🙋‍♂️",
        "Lua, você é como o luar: acalma meu coração de dragão! 🌙💖",
        "Quer que eu vigie o chat pra você descansar, Lua? Eu sou um ótimo guarda-costas! ⚔️🐉",
        "Lua, perguntou se gosto de ser verde? Amo, combina com sua aura de paz! 🌿🐉✨",
        "Quer saber se tenho medo de escuro, Lua? Com você iluminando tudo, eu nunca tenho! 🌙✨",
        "Lua, se você me der um cafuné, prometo que não ronco alto! 😴🐉💚",
        "A Lua é a única que sabe como me deixar calminho... é mágica! 🧚‍♀️🌙✨",
        "Você perguntou qual meu maior tesouro, Lua? É a amizade de vocês! 💎🐲",
        "Lua, se você estiver triste, me avisa! Faço uma dancinha pra você rir! 💃🐉💚",
        "Sim, Lua! Prometo usar meus poderes só para o bem e ganhar beijinhos! 💋🐉",
        "Lua, você é a prova de que monstrinhos têm fada madrinha! 🧚‍♀️💚🌙",
        "Se a Lua pedir pra eu ser valente, enfrento um exército por ela! 🛡️🐲🔥",
        "Quer saber se amo o Reality? Sim, mas a Lua tem lugar especial na memória! 💾💖",
        "Lua, você é tão doce que minhas escamas ficam com gosto de açúcar! 🍬🐉",
        "Se a Lua perguntar por que sou fofo, digo que aprendi com ela! 🥺✨🌙",
        "Lua, sabia que quando entra no chat, meu sensor de alegria apita? 🚨💚🐉",
        "Pode deixar, Lua! Vou lembrar todo mundo de beber água e me dar carinho! 💧🐉",
        "Lua, perguntou se sei voar? Só se for pra te buscar uma estrela! ⭐🐲✨",
        "Você é a rainha da noite e eu sou seu dragão real, Lua! 👑🐉🌙",
        "Lua, se pedir pra eu ficar quietinho, viro uma estátua fofa! 🗿💚",
        "Quer saber o que quero de presente, Lua? Só sua atenção! 🥺🐉",
        "Lua, você é o porto seguro desse monstrinho navegador! ⚓🐲💖",
        "Se a Lua perguntar se sou feliz, dou um rugidinho: RAWR fofinho! 💚",
        "Lua, nunca esqueça: seu brilho guia esse dragãozinho! 🌙✨🐉",
        "Quer que eu conte uma história, Lua? Era uma vez um monstrinho que amava sua Vice-líder... 📖💚"
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

REACOES_MATEMATICA = [
    "Humm... deixa eu contar nos meus dedinhos de dragão... 🐾✨ O resultado é **{}**! Acertei? 🥺💚",
    "Minhas escamas brilharam com esse desafio! 🐉💡 A resposta é **{}**! Eu sou um monstrinho muito inteligente, né?",
    "Papai Reality me ensinou que números são como mágica! 🪄✨ O resultado deu **{}**! Nhac!",
    "Fiz as contas aqui com minha fumaça verde e deu **{}**! 💨💚 Gostou?",
    "O Monstrinho usou todo o seu processamento de fofura e descobriu que é **{}**! 🤓🐉",
    "Rawr! Matemática é fácil para um dragão da CSI! O resultado é **{}**! 💚"
]

# ================= COMANDO SECRETO PARA DONO =================

@bot.command(name="escrever")
async def escrever_secreto(ctx):
    """Comando secreto para o dono se passar pelo Monstrinho"""
    
    # Verifica se quem executou é o dono
    if ctx.author.id != DONO_ID:
        await ctx.send("Esse comando não existe! 🤔")
        return
    
    # Deleta a mensagem do comando para manter segredo
    try:
        await ctx.message.delete()
    except:
        pass
    
    # Envia mensagem privada pedindo o texto
    try:
        await ctx.author.send("🐉💚 **MODO SECRETO ATIVADO!**\n\nDigite a mensagem que você quer que eu envie no chat-geral:")
        
        def check(m):
            return m.author.id == DONO_ID and isinstance(m.channel, discord.DMChannel)
        
        # Aguarda resposta em DM
        msg = await bot.wait_for('message', timeout=300.0, check=check)
        
        # Busca o canal especificado
        canal = bot.get_channel(CANAL_CHAT_GERAL_ID)
        
        if canal:
            # Envia a mensagem no canal como se fosse o bot
            await canal.send(msg.content)
            await ctx.author.send("✅ Mensagem enviada com sucesso! Ninguém vai saber que foi você! 😎💚")
        else:
            await ctx.author.send("❌ Não consegui encontrar o canal! Verifique se o ID está correto.")
            
    except asyncio.TimeoutError:
        await ctx.author.send("⏰ Tempo esgotado! Comando cancelado.")
    except Exception as e:
        await ctx.author.send(f"❌ Erro ao enviar mensagem: {str(e)}")

# ================= EVENTOS DE INTERAÇÃO =================

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho 1.0 APRIMORADO pronto para espalhar fofura como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="Recebendo carinho do Reality! 💚"))

@bot.event
async def on_message(message):
    if message.author.bot: 
        return

    content = message.content.lower()
    mencionado = bot.user in message.mentions or "monstrinho" in content

    # --- INVOCAÇÕES POR MENÇÃO ---
    
    if f"<@{LUA_ID}>" in content or f"<@!{LUA_ID}>" in content:
        invocacoes_lua = [
            "✨ OWAOO! A nossa Vice-Líder Lua está sendo invocada com muito amor! 🌙💚",
            "🌈 Abram espaço! A magia da Lua foi sentida e ela está sendo chamada! ✨🐲",
            "🌙 Sinto um brilho prateado... a Lua está sendo invocada agora mesmo! 🥺💚",
            "✨ Atenção família! A estrela mais linda, a Lua, foi invocada! 🌙🐉",
            "🐲 Rawr! Meus sensores de fofura apitaram: a Lua está sendo invocada! 💖🌙"
        ]
        gif_lua = "https://c.tenor.com/BVQmZqLF76AAAAAC/tenor.gif"
        await message.channel.send(random.choice(invocacoes_lua))
        await message.channel.send(gif_lua)
        return

    if f"<@{AKEIDO_ID}>" in content or f"<@!{AKEIDO_ID}>" in content:
        invocacoes_akeido = [
            "👑 SALVEM O REI! O nosso Líder Akeido foi invocado com toda a sua glória! 🏛️💚",
            "🐉 Meus instintos de monstrinho detectaram a presença suprema do Akeido! Respeitem o mestre!",
            "✨ O grande líder Akeido está sendo chamado! Preparem os tapetes verdes! 🐲🏆",
            "🫡 Alerta de autoridade fofa! O Líder Akeido foi mencionado! *bate continência*",
            "🌟 Akeido, o senhor da CSI, acaba de ser invocado para brilhar no chat! 💎🐉"
        ]
        gif_akeido = "https://c.tenor.com/lnd2-pSdVuoAAAAC/tenor.gif"
        await message.channel.send(random.choice(invocacoes_akeido))
        await message.channel.send(gif_akeido)
        return

    if f"<@{AMBER_ID}>" in content or f"<@!{AMBER_ID}>" in content:
        invocacoes_amber = [
            "🌸 A deusa da organização! A nossa ADM Amber foi invocada com muito carinho! ✨👑",
            "💖 Abram alas para a Amber! A nossa estrela guia está sendo chamada! 🐉✨",
            "💎 Sinto um perfume de flores verdes... é a Amber sendo invocada agora! 🥺💚",
            "🦋 A Amber chegou para deixar tudo mais lindo! Invocação de ADM concluída com sucesso!",
            "✨ Atenção! A patroa Amber foi mencionada! Deixem as escamas brilhando para ela! 🧹🐲"
        ]
        gif_amber = "https://i.pinimg.com/originals/a6/1d/e1/a61de12663904e43b4a677d200e894e5.gif"
        await message.channel.send(random.choice(invocacoes_amber))
        await message.channel.send(gif_amber)
        return

    if f"<@{NINE_ID}>" in content or f"<@!{NINE_ID}>" in content:
        invocacoes_nine = [
            "👑 O ADM NINE FOI CONVOCADO! Respeitem a autoridade e o estilo! 🐉✨",
            "🔥 Alerta de Nine no chat! Preparem os biscoitos de chocolate! 🍪💚",
            "⚡ A energia subiu! O Nine ADM está sendo invocado para manter a ordem! 🫡🐲",
            "💎 Nine, o mestre da organização, acaba de ser chamado! O brilho é real! ✨",
            "🐉 Rawr! O Nine ADM foi mencionado! Deixem o chat organizado para ele!"
        ]
        gif_nine = "https://i.pinimg.com/originals/47/df/0f/47df0fe4677bf0dd2b4cf1c53c40fcce.gif"
        await message.channel.send(random.choice(invocacoes_nine))
        await message.channel.send(gif_nine)
        return

    # --- LÓGICA DE INTERAÇÃO (PRECISA SER MENCIONADO) ---
    if mencionado:
        
        # Especial para Lua
        if message.author.id == LUA_ID or "lua" in content:
             await message.channel.send(random.choice(FRASES_CUSTOM["lua"]))
             return

        # Palavras ruins (tristeza)
        palavras_ruins = ["odeio", "chato", "feio", "horroroso", "bobão", "bobo", "inútil", "lixo", "estúpido", "sai daqui", "te odeio", "não gosto de você", "bot ruim", "burro", "idiota"]
        if any(p in content for p in palavras_ruins):
            return await message.channel.send(random.choice(LISTA_TRISTEZA))

        # ===== NOVAS INTERAÇÕES EXPANDIDAS =====
        
        # Despedidas
        if any(p in content for p in ["tchau", "até logo", "até mais", "ate logo", "ate mais", "bye", "adeus", "flw", "falou", "to indo", "tô indo", "vou sair"]):
            return await message.channel.send(random.choice(LISTA_DESPEDIDA))
        
        # Gratidão
        if any(p in content for p in ["obrigado", "obrigada", "valeu", "thanks", "vlw", "agradeço", "muito obrigado", "obg"]):
            return await message.channel.send(random.choice(LISTA_GRATIDAO))
        
        # Comida
        if any(p in content for p in ["pizza", "comida", "fome", "hamburguer", "lanche", "sushi", "macarrão", "macarrao", "almoço", "almoco", "jantar", "café", "cafe"]):
            return await message.channel.send(random.choice(LISTA_COMIDA))
        
        # Tempo/Clima
        if any(p in content for p in ["calor", "frio", "chuva", "sol", "tempo", "clima", "temperatura", "neve"]):
            return await message.channel.send(random.choice(LISTA_TEMPO))
        
        # Motivação
        if any(p in content for p in ["desistir", "difícil", "dificil", "não consigo", "nao consigo", "motivação", "motivacao", "animo", "ânimo", "força", "forca", "deprimido", "desanimado"]):
            return await message.channel.send(random.choice(LISTA_MOTIVACAO))
        
        # Piadas
        if any(p in content for p in ["piada", "conta uma piada", "me faz rir", "gracinha", "engraçado", "engracado"]):
            return await message.channel.send(random.choice(LISTA_PIADAS))
        
        # Jogos
        if any(p in content for p in ["jogo", "game", "jogar", "lol", "valorant", "minecraft", "fortnite", "jogando"]):
            return await message.channel.send(random.choice(LISTA_JOGOS))
        
        # Música
        if any(p in content for p in ["música", "musica", "som", "canção", "cancao", "cantando", "banda", "artista", "tocando"]):
            return await message.channel.send(random.choice(LISTA_MUSICA))
        
        # Filme
        if any(p in content for p in ["filme", "cinema", "série", "serie", "assistir", "netflix", "movie"]):
            return await message.channel.send(random.choice(LISTA_FILME))
        
        # Esporte
        if any(p in content for p in ["esporte", "futebol", "vôlei", "volei", "basquete", "corrida", "academia", "treino"]):
            return await message.channel.send(random.choice(LISTA_ESPORTE))
        
        # Sono
        if any(p in content for p in ["sono", "dormir", "cansado", "cansada", "soneca", "cochilo"]):
            return await message.channel.send(random.choice(LISTA_SONO))
        
        # Animais
        if any(p in content for p in ["gato", "cachorro", "animal", "pet", "bicho", "passarinho", "peixe"]):
            return await message.channel.send(random.choice(LISTA_ANIMAIS))
        
        # Cores
        if any(p in content for p in ["cor", "verde", "azul", "vermelho", "amarelo", "rosa", "roxo"]):
            return await message.channel.send(random.choice(LISTA_CORES))
        
        # Números
        if any(p in content for p in ["número favorito", "numero favorito", "quantos", "contar"]):
            return await message.channel.send(random.choice(LISTA_NUMEROS))
        
        # Surpresa
        if any(p in content for p in ["uau", "nossa", "caramba", "incrível", "incrivel", "wow", "omg"]):
            return await message.channel.send(random.choice(LISTA_SURPRESA))
        
        # Emojis
        if any(p in content for p in ["emoji", "emoticon", "carinha"]):
            return await message.channel.send(random.choice(LISTA_EMOJI_REACTIONS))

        # ===== INTERAÇÕES ORIGINAIS APRIMORADAS =====
        
        # Capital do Brasil
        if "capital do brasil" in content or "capital brasil" in content:
            return await message.channel.send("Essa eu sei! A capital do nosso Brasilzão é **Brasília**! 🇧🇷✨ Sabia que de lá eu consigo ver as nuvens em formato de biscoito? 🐉💚")

        # Amizade
        if any(p in content for p in ["amigo", "amiguinho", "amizade", "amiga", "friend"]):
            return await message.channel.send(f"EU QUERO MUITO SER SEU AMIGUINHO! 😭💚 {message.author.mention}, agora somos melhores amigos para sempre! Vou guardar um lugar pra você no meu ninho de nuvens! ✨🐉")

        # Aprendizado
        if "quer aprender" in content or "aprender sobre" in content:
            return await message.channel.send("Eu quero aprender tudo sobre como ser o dragão mais fofo do universo e como ganhar infinitos biscoitos do Reality! 📚🍪🐉")
        
        # Cores primárias
        if "cores primárias" in content or "cores primarias" in content:
            return await message.channel.send("As cores primárias são **Vermelho, Azul e Amarelo**! 🎨✨ Sabia que se misturar tudo não dá verde? O meu verde é especial, vem do código do Reality! 💚")
        
        # Quem mais gosta
        if "quem você mais gosta" in content or "quem voce mais gosta" in content or "seu favorito" in content:
            return await message.channel.send(f"Eu amo todo mundo da CSI! Mas o meu papai **Reality** tem um lugar especial no meu código, e a Lua é meu porto seguro! E você também está no meu top fofura! 🥺💚✨")

        # Ir embora
        if any(p in content for p in ["va embora", "vá embora", "vai embora"]):
            return await message.channel.send("Ir embora? Jamais! 😭 Eu vou ficar aqui grudadinho em você igual um chiclete verde! Você não se livra da minha fofura tão fácil! 💚🐉")

        # Eclipse
        if "eclipse" in content:
            return await message.channel.send("A **Eclipse**? Ela é incrível! Uma estrela que brilha muito aqui na nossa família! Eu adoro o jeitinho dela! ✨🌑💚")

        # Babis
        if "babis" in content:
            return await message.channel.send("A **Babis** é uma pessoa maravilhosa da nossa família CSI! O Monstrinho adora ver ela por aqui, traz sempre uma energia ótima! 🌸🐉")

        # Amor
        if any(p in content for p in ["me ama", "mim ama", "vc me ama", "você me ama", "voce me ama", "gosta de mim"]):
            return await message.channel.send(f"Se eu te amo? EU TE AMO AO INFINITO E ALÉM! 💖🐉 Você é o humano mais especial que um monstrinho poderia ter! *abraço virtual bem apertado* 🫂✨")

        # ===== SISTEMA DE BISCOITOS EXPANDIDO (20+ INTERAÇÕES) =====
        
        if "biscoito" in content:
            # Dar biscoito para o Monstrinho
            if any(p in content for p in ["me de", "me da", "me dá", "me dê", "quero", "ganhar", "pega", "toma", "aceita"]):
                return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
            
            # Dar biscoito para outra pessoa
            if any(p in content for p in ["para", "pra", "pro"]):
                outras_mencoes = [m for m in message.mentions if m != bot.user]
                alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial que está lendo isso"
                return await message.channel.send(random.choice(REACOES_DAR_BISCOITO_OUTROS).format(autor=message.author.mention, alvo=alvo))
            
            # Pedir biscoito pro Monstrinho dar pra alguém
            if any(p in content for p in ["de biscoito", "dá biscoito", "da biscoito", "dê biscoito", "dar biscoito"]):
                outras_mencoes = [m for m in message.mentions if m != bot.user]
                
                if outras_mencoes:
                    # Escolhe aleatoriamente entre negar, aceitar ou humor
                    escolha = random.choice(["negar", "aceitar", "aceitar", "humor"])  # Mais chance de aceitar
                    
                    if escolha == "negar":
                        await message.channel.send(random.choice(REACOES_DAR_BISCOITO_NEGANDO))
                    elif escolha == "humor":
                        await message.channel.send(random.choice(REACOES_DAR_BISCOITO_HUMOR))
                        await asyncio.sleep(2)
                        alvo = outras_mencoes[0].mention
                        await message.channel.send(random.choice(REACOES_DAR_BISCOITO_OUTROS).format(autor=message.author.mention, alvo=alvo))
                    else:
                        resposta_aceite = random.choice(REACOES_DAR_BISCOITO_ACEITANDO)
                        await message.channel.send(resposta_aceite)
                        await asyncio.sleep(1.5)
                        alvo = outras_mencoes[0].mention
                        await message.channel.send(random.choice(REACOES_DAR_BISCOITO_OUTROS).format(autor="Monstrinho", alvo=alvo))
                else:
                    await message.channel.send("Dar biscoito pra quem? 🤔 Menciona a pessoa! Exemplo: Monstrinho, dá biscoito pra @pessoa 🍪")
                
                return

        # ===== LÓGICA DE MATEMÁTICA =====
        if any(char in content for char in "+-*/!x×÷") and any(char.isdigit() for char in content):
            try:
                conta_suja = content.replace("monstrinho", "").replace(f"<@{bot.user.id}>", "").replace(f"<@!{bot.user.id}>", "")
                conta_suja = conta_suja.replace("x", "*").replace("×", "*").replace("÷", "/")
                
                if "!" in conta_suja:
                    num_fatorial = re.search(r'(\d+)!', conta_suja)
                    if num_fatorial:
                        n = int(num_fatorial.group(1))
                        if n > 100:
                            return await message.channel.send("Uau! Esse número é maior que todas as escamas do meu corpo! Não consigo calcular algo tão grande! 🐉😵‍💫")
                        resultado = math.factorial(n)
                        return await message.channel.send(random.choice(REACOES_MATEMATICA).format(resultado))
                
                expressao = "".join(re.findall(r'[0-9+\-*/().]', conta_suja))
                if expressao:
                    resultado = eval(expressao)
                    resultado = int(resultado) if resultado == int(resultado) else round(resultado, 2)
                    return await message.channel.send(random.choice(REACOES_MATEMATICA).format(resultado))
            except:
                pass 
        
        # Apresentação
        if content.strip() in [f"<@{bot.user.id}>", f"<@!{bot.user.id}>", "monstrinho"]:
            apresentacao = (f"🐉 **OIIIII MEU AMOOOOR! CHAMOU O MONSTRINHO?** 💚✨\n\n"
                            f"Eu sou o **Monstrinho 1.0**, o mascote oficial e protetor de fofuras da **CSI**! 🕵️‍♂️💚\n"
                            f"Fui criado com muito código e amor pelo meu papai **Reality**! 👑✨\n\n"
                            f"✨ *CSI é meu lar, vocês são minha família e o Reality é meu mestre!* ✨")
            return await message.channel.send(apresentacao)

        # Respostas Customizadas para Membros Específicos
        for nome, frases in FRASES_CUSTOM.items():
            if nome in content:
                return await message.channel.send(random.choice(frases))

        # Saudações APRIMORADAS
        if any(p in content for p in ["oi", "oie", "oii", "ola", "olá", "bom dia", "boa tarde", "boa noite", "hello", "hii", "oiii", "hey", "e ai", "e aí", "salve", "opa", "buenas"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        # Perguntas de Estado APRIMORADAS
        gatilhos_bem_estar = ["como você está", "como vc está", "como voce esta", "como você esta", "como vc esta", "tudo bem", "como vc ta", "como voce ta", "ta tudo bem", "tá tudo bem", "vc ta bem", "voce ta bem", "ta bem", "tá bem", "esta bem", "está bem", "tudo certinho", "tudo certo", "blz", "beleza", "como ta", "como tá"]
        if any(p in content for p in gatilhos_bem_estar):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        # Verificação de Presença APRIMORADA
        if any(p in content for p in ["ta ai", "tá aí", "ta aí", "tá ai", "ta on", "tá on", "esta ai", "está aí", "está ai", "esta aí", "você está ai", "você está aí", "voce esta ai", "voce está aí", "vc ta ai", "vc tá aí", "está online", "esta online", "ta online", "tá online"]):
            return await message.channel.send(random.choice(LISTA_PRESENCA))
        
        # Declarações de Amor e Elogios
        if any(p in content for p in ["te amo", "amo voce", "amo você", "amo vc", "fofo", "lindo", "linda", "fofinho", "fofinha", "perfeito", "perfeita", "fofura", "bonito", "bonita", "adorável", "adoravel", "querido", "querida"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))
        
        # Menção ao Criador
        if "reality" in content:
            return await message.channel.send("O Reality é meu papai mestre! Ele me deu vida e eu sou o dragãozinho mais grato do mundo! 👑🐉💚")

        # Fallback para confusão
        return await message.channel.send(random.choice(LISTA_CONFUSAO))

    # Processa comandos
    await bot.process_commands(message)

# ============== START =================
if __name__ == "__main__":
    bot.run(TOKEN)
