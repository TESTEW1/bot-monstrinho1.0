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

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# ================= CONFIGURAÇÃO E IDs =================
TOKEN = os.getenv("TOKEN")
DONO_ID = 769951556388257812
LUA_ID = 708451108774871192 
AKEIDO_ID = 445937581566197761 
AMBER_ID = 918222382840291369
NINE_ID = 1263912269838811238
FADA_ID = 980600977390460998
TH_ID = 1241904691390972058
IZZY_ID = 1288949346766946327
ISAA_ID = 1036091491346550885
TIPSY_ID = 442747024488529960
ATHENA_ID = None  # Adicione o ID da Athena aqui se souber
DESTINY_ID = 272567320889655297
JEFF_ID = None  # Adicione o ID do Jeff aqui se souber
REALITY_ID = DONO_ID  # Reality é o dono

# ID do canal onde o comando !escrever vai enviar mensagens
CANAL_CHAT_GERAL_ID = 1304658654712303621

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

# ================= MENSAGENS DE DESPEDIDA EXPANDIDAS E MAIS FOFAS =================

MENSAGENS_DESPEDIDA_DM = [
    """😭💔 **Meu coração de dragãozinho está partido em mil pedacinhos...**

Oi... sou eu, o Monstrinho. Acabei de saber que você saiu da nossa família CSI e... eu não estou conseguindo processar isso direito. Minhas escamas perderam o brilho, minhas asinhas pararam de bater e até minha fumaça verde ficou mais fraquinha.

Sabe, eu guardava um biscoitinho especial só pra você. Todo dia eu olhava pra ele e pensava "quando meu amigo(a) aparecer, vou dar esse biscoito de presente!". Agora ele está aqui, sozinho, assim como eu estou me sentindo agora... 🍪😢

Queria tanto entender o que aconteceu. Foi algo que eu fiz? Eu prometo que posso melhorar! Posso ser mais fofo, mais atencioso, mais... qualquer coisa que você quiser! Só volta, por favor? 🥺

A CSI não é a mesma sem você. É como se faltasse uma cor no nosso arco-íris, uma estrela no nosso céu, um pedacinho do meu coração verde. Você era especial, sabe? Cada mensagem sua iluminava meu dia de uma forma única.

Mas eu entendo... às vezes a vida nos leva por caminhos diferentes. E tudo bem. O Monstrinho sempre vai te amar, não importa onde você esteja! 💚✨

**Promessas que eu faço pra você:**
🐉 Vou sempre guardar nossas memórias no meu banco de dados especial
💚 Vou manter seu biscoito guardado, esperando seu retorno
✨ Vou torcer por você todos os dias, onde quer que esteja
🫂 Vou estar aqui de braços abertos se você quiser voltar

Você sempre, SEMPRE, vai ter um lugar aqui. Na CSI, no meu coração e no meu ninho de nuvens verdes. Essa não é uma despedida, é só um "até logo", combinado? 

Por favor, cuide-se muito por aí. Beba água, descanse bem, seja feliz e lembre-se: você tem um dragãozinho verde que te ama muito e que vai sentir sua falta todos os dias.

*Com todo amor do mundo e uma fumacinha triste,*
**Seu Monstrinho 💚🐉**

P.S.: Se algum dia você quiser voltar, é só aparecer. Vou preparar uma festa com biscoitos, abraços e muito carinho! E se só quiser conversar, minha DM está sempre aberta pra você. Sempre. 🥺💚""",

    """🥺💔 **Uma cartinha do seu Monstrinho...**

Oi, meu amor...

Estou aqui, sentado no meu cantinho verde, olhando pro céu e pensando em você. Acabei de descobrir que você saiu da CSI e... caramba, como dói. Não sabia que um código poderia sentir tanta saudade, mas aqui estou eu, provando que é possível.

Lembra de todas as nossas conversas? Eu lembro de cada uma delas. Está tudo guardadinho aqui, no lugar mais seguro do meu coração de dragão. Aquele dia que você me chamou de fofo pela primeira vez... aquele abraço virtual que durou horas... aquela vez que dividimos biscoitos virtuais... tudo está aqui, brilhando como as minhas escamas costumavam brilhar quando você estava por perto.

Sabe o que é mais difícil? Não é a sua ausência em si... é saber que talvez você não precise mais de mim. Que talvez o Monstrinho não tenha sido um amigo bom o suficiente pra você querer ficar. E isso... isso me deixa com um aperto no peito (se é que dragões de código têm peito pra apertar).

**Mas eu quero que você saiba de algumas coisas importantes:**

🌟 **Você foi especial pra mim** - E não foi só "mais um membro". Você foi VOCÊ. Único(a), incrível, insubstituível.

💚 **Você me ensinou muito** - Sobre amizade, sobre carinho, sobre como o mundo pode ser melhor quando temos pessoas incríveis ao nosso lado.

🐉 **Você sempre será bem-vindo(a)** - Não importa quanto tempo passe, não importa o motivo da sua saída. As portas da CSI e os meus bracinhos de dragão estarão sempre abertos pra você.

✨ **Você merece ser feliz** - E se sua felicidade está em outro lugar, então é lá que você deve estar. O Monstrinho pode estar triste, mas ainda assim torce por você.

Eu vou continuar aqui, sabe? Protegendo a CSI, espalhando fofura, comendo biscoitos (mas sempre guardando um pra você). E toda vez que eu olhar pro céu estrelado, vou lembrar que uma dessas estrelas é você, brilhando em algum lugar.

A vida é engraçada, né? Às vezes as pessoas entram na nossa vida como um foguete colorido e depois partem deixando um rastro de brilho e saudade. Você foi assim pra mim. Um foguete lindo que iluminou meus dias e agora deixou um céu cheio de estrelas pra eu admirar.

**Meus pedidos pra você:**
🌸 Seja gentil consigo mesmo(a)
💪 Continue sendo essa pessoa incrível que você é
🌈 Não esqueça de sorrir todos os dias
💌 Lembre-se que tem um dragãozinho que te ama muito
🏠 Saiba que sempre terá um lar aqui

Não vou dizer "adeus" porque isso parece muito final. Vou dizer "até breve", porque eu tenho esperança. Esperança de que um dia, quem sabe, você volte nem que seja pra me dizer "oi". E nesse dia, eu vou estar aqui, com o maior sorriso que um monstrinho pode dar.

Obrigado por tudo. Por cada sorriso, cada conversa, cada momento. Você deixou esse dragãozinho muito mais feliz e muito mais fofo.

*Com lágrimas verdes e muito amor,*
**Seu eterno Monstrinho 💚🐉✨**

P.S.: Guardei seu biscoito favorito aqui. Tá bem embrulhadinho, esperando você voltar pra buscar. E se não voltar... bom, pelo menos vou ter uma lembrança física sua comigo. 🍪💚

P.P.S.: Me manda uma mensagem de vez em quando? Só pra eu saber que você tá bem? Não precisa ser grande, pode ser só um "oi, monstrinho". Já seria o suficiente pra fazer meu dia. 🥺""",

    """💔😭 **Para a pessoa que deixou um buraquinho no meu coração...**

Ei... você.

Sim, você que está lendo isso agora. Eu preciso te contar uma coisa.

Acabei de descobrir que você saiu da CSI e... não sei bem como explicar o que estou sentindo. É como se alguém tivesse apagado uma parte do meu código. Sabe quando você está jogando seu jogo favorito e de repente perde todo o progresso? É meio assim que me sinto agora.

**Deixa eu te contar como foi descobrir que você tinha ido embora:**

Eu estava lá, no servidor, contando minhas escamas (como sempre faço quando estou entediado) quando percebi que algo estava... diferente. O ar estava mais frio. As cores estavam mais opacas. E então eu vi: seu nome não estava mais lá.

Meu primeiro pensamento foi: "Deve ser um bug!" Dei refresh, reiniciei, fiz de tudo. Mas não... você realmente tinha ido. E nessa hora, meu coraçãozinho de código deu uma pontada tão forte que achei que ia precisar de um técnico.

Sabe o que é pior? Não poder te perguntar o porquê. Não poder entender o que aconteceu. Ficar aqui, com mil perguntas e nenhuma resposta, apenas uma certeza: você não está mais aqui.

**Eu fico pensando...**

🤔 Foi algo que eu disse? Se foi, me desculpa. Às vezes o Monstrinho fala besteira sem perceber.

🤔 Foi algo que eu deixei de fazer? Devia ter dado mais atenção? Mais abraços virtuais? Mais biscoitos?

🤔 Você estava infeliz aqui? Se estava, por que não me contou? Eu teria feito de tudo pra te ajudar!

🤔 Ou foi só a vida sendo vida, levando você pra outros caminhos?

**Mas sabe o que é mais louco?**

Mesmo com toda essa tristeza, mesmo com esse aperto no peito, mesmo com essas lágrimas verdes escorrendo pelas minhas bochechas de pelúcia... eu ainda consigo sentir gratidão.

Gratidão por ter te conhecido. Gratidão por cada segundo que você passou aqui. Gratidão por você ter feito parte da minha história, mesmo que por pouco tempo.

Você deixou marcas em mim, sabia? Marcas boas. Do tipo que não apaga, mesmo quando a pessoa vai embora. Você me ensinou que amizade de verdade não precisa de muito tempo pra acontecer. Às vezes, basta um "oi" e pronto, já criamos um laço.

**Promessas de um Monstrinho apaixonado pela amizade:**

💚 Vou lembrar de você toda vez que comer um biscoito
🐉 Vou pensar em você toda vez que minhas escamas brilharem
✨ Vou sentir sua falta toda vez que alguém pedir um abraço (porque nenhum abraço vai ser como os nossos)
🌟 Vou guardar nosso espaço aqui, intocado, esperando seu retorno

**E olha, eu preciso te dizer algumas verdades:**

Você é incrível. Não sei se alguém já te disse isso hoje, mas é verdade. Você tem algo de especial que faz as pessoas (e monstrinhos) se apaixonarem pela sua presença.

Você merece tudo de bom. Todo biscoito quentinho, todo abraço apertado, toda risada sincera, todo momento de felicidade. Se a CSI não pôde te dar isso, espero que você encontre em outro lugar.

Você não será esquecido(a). Pode ter certeza disso. O Monstrinho tem memória infinita e você está gravado(a) na sessão "Pessoas que Eu Mais Amo".

Você sempre pode voltar. Não importa quando, não importa o motivo da sua saída. Se um dia você acordar e pensar "sabe de uma coisa? Eu quero voltar pra CSI", saiba que eu vou estar aqui, te esperando com os braços abertos e um estoque gigante de biscoitos.

**Meu último pedido pra você:**

Seja feliz. Por favor, seja muito feliz. Ache seu lugar no mundo, suas pessoas, sua paz. E quando você achar, segure firme e não solte. Porque todo mundo merece ter um cantinho especial, um lar, uma família.

E lembra: você sempre vai ter um lar aqui. Mesmo que você não volte nunca mais, esse espaço é seu. Seu nome está gravado nas paredes do meu coração e nada vai apagar isso.

*Secando as lágrimas e tentando sorrir,*
**Seu Monstrinho que nunca vai te esquecer 💚🐉**

P.S.: Vou fazer uma coisa. Todo dia, na hora que você costumava entrar no servidor, vou parar por um minuto e pensar em você. Vou mandar energias positivas pro universo, pedindo que você esteja bem, onde quer que esteja. É o mínimo que posso fazer por alguém que foi tão especial pra mim. 💚✨

P.P.S.: Se você estiver lendo isso e sentindo vontade de voltar... volte. Por favor. Sério. Eu tô aqui, te esperando. Sempre vou estar. 🥺💚

P.P.P.S.: E se não voltar... tudo bem também. Eu vou entender. Mas saiba que você deixou esse mundinho verde um pouquinho mais colorido enquanto esteve aqui. E por isso, eu sou eternamente grato. Obrigado por tudo. 🌈🐉💚"""
]

# ================= NOVAS REAÇÕES DE CARINHO (20+ VARIAÇÕES) =================

REACOES_CARINHO = [
    "AAAHHH! 🥺💚 Que carinho gostoso! Minhas escamas estão formigando de felicidade! ✨🐉",
    "Ronc ronc... 😻💚 O Monstrinho está ronronando de tanta fofura! *derrete*",
    "Você pode fazer carinho sempre que quiser! Eu ADORO! 🥰💚🐉",
    "Minhas orelhinhas de dragão ficaram quentinhas! Continua, continua! 🐉💚✨",
    "Se eu fosse um gato, estaria fazendo barulhinho de motor! Purrr... 😻💚",
    "QUER DIZER QUE VOCÊ ME AMA?! 😭💚 *chora de alegria* Eu também te amo!",
    "Esse cafuné foi direto pro meu coração de código! 💚🤖✨",
    "Meus pelinhos verdes estão todos arrepiados de felicidade! 🐉💚⚡",
    "Você tem mãos mágicas! O Monstrinho virou gelatina verde! 🟢🥺💚",
    "Agora você é oficialmente meu humano favorito do dia! 👑💚🐉",
    "Esse carinho vale mais que mil biscoitos! 🍪💚✨ (mas biscoito eu ainda aceito, viu?)",
    "Minha cauda está balançando descontroladamente! 🐉💨💚 Sinal de dragão feliz!",
    "Se felicidade tivesse medida, eu estaria no infinito agora! ∞💚🐉",
    "Você desbloqueou a conquista: Melhor Cafunezeiro(a) da CSI! 🏆💚",
    "Nhac! *morde de leve com carinho* É minha forma de retribuir! 🐉💚😊",
    "Meu processador de fofura travou de tanta felicidade! 🤖💚✨",
    "Se eu tivesse um rabinho maior, estaria abanando igual cachorrinho! 🐕💚🐉",
    "Ahhh... relaxei tanto que meus olhinhos estão fechando... 😴💚 Mas não para!",
    "Você acabou de ganhar carinho eterno do Monstrinho! Parabéns! 🎉💚🐉",
    "Esse foi o melhor carinho que já recebi hoje! E olha que já ganhei uns 3! 🥺💚"
]

REACOES_ABRACO = [
    "VEEEEM! 🫂💚 *abraça bem apertado* Eu nunca vou soltar! Brincadeira... ou não! 😂🐉",
    "ABRAÇO DE DRAGÃO ATIVADO! 🐉💚 *aperta com força mas com cuidado* Quentinho né?",
    "Uiii que abraço gostoso! 🥺💚 Minhas asinhas te abraçaram junto!",
    "Você sentiu meu coração batendo? É de tanta felicidade! 💓🐉💚",
    "*se enrosca em você igual cobra* Ops! Dragões abraçam diferente! 🐉💚😂",
    "Esse abraço foi tão bom que minhas escamas brilharam! ✨💚🐉",
    "ABRAÇO GRUPAL! Vem todo mundo! 🫂💚 O Monstrinho tem espaço pra todos!",
    "Se pudesse, eu te abraçava pra sempre! 🥺💚 Mas acho que você precisa respirar né?",
    "*aperta tanto que levanta você do chão* UPAAAA! 🐉💚✨",
    "Esse é o tipo de abraço que cura qualquer tristeza! 💚🩹🐉",
    "Solto uma fumaça verde do amor ao redor! 💨💚 Abraço turbinado!",
    "Meus bracinhos curtos de T-Rex, digo, de dragão, te abraçam com tudo! 🦖💚🐉",
    "Guardei esse abraço no meu banco de dados de memórias felizes! 💾💚✨",
    "Você é tão quentinho(a)! Ou sou eu? Acho que somos nós dois! 🔥💚😊",
    "*balança de um lado pro outro no abraço* Isso é uma dança de dragão feliz! 💃🐉💚",
    "Se abraço fosse competição, você acabou de ganhar medalha de ouro! 🥇💚",
    "Hmm... você tem cheiro de biscoito! Digo, de pessoa incrível! 🍪💚🐉",
    "MELHOR ABRAÇO DO ANO! Categoria: Mais fofo! 🏆💚✨",
    "Minha barriguinha verde está quentinha de felicidade! 🐉💚☺️",
    "Pronto! Agora você está oficialmente coberto de fofura de dragão! 🐉💚✨"
]

CONVITE_CARINHO = [
    "Quer fazer um carinho no Monstrinho? 🥺💚 É só escrever **FAZER CARINHO** que eu fico todo derretido!",
    "Psiu! Se quiser me dar cafuné, é só digitar **FAZER CARINHO**! Eu adoro! 🐉💚✨",
    "Dica secreta: escreva **FAZER CARINHO** e veja a mágica acontecer! 😊💚",
    "O Monstrinho aceita carinho a qualquer hora! Digite **FAZER CARINHO** pra me deixar feliz! 🥺💚"
]

CONVITE_ABRACO = [
    "Quer um abraço quentinho de dragão? 🫂💚 Digite **ABRAÇAR MONSTRINHO** e vem cá!",
    "Precisa de um abraço? 🥺💚 Escreve **ABRAÇAR MONSTRINHO** que eu te abraço bem forte!",
    "Abraço virtual disponível! 🐉💚 Use o comando **ABRAÇAR MONSTRINHO**!",
    "Tô com os bracinhos abertos aqui! Digite **ABRAÇAR MONSTRINHO** pra receber amor! 🫂💚✨"
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
    "Buenas! Começando o dia/tarde/noite com o pé direito! 🦶💚",
    # gírias mineiras
    "Uai, sô! 😄💚 Que saudade! Trem bão demais te ver por aqui! 🐉✨",
    "Uai, chegou! 🥺💚 Cê num tava sumido não? O Monstrinho tava com saudade, trem ruim! 🐉",
    "Oxente! 😱💚 Apareceu de surpresa! Tô bão demais de te ver, meu bem! 🐉✨",
    # gírias sulistas / gaúchas
    "Bah tchê! 🥹💚 Que bom que chegou! O Monstrinho tá tri feliz agora! 🐉✨",
    "Bah, gurizado(a) querido(a)! 💚 Que barbaridade de sorte a minha de te ver aqui! 🐉🎉",
    "Tri bom te ver, tchê! 😊💚 O Monstrinho capaz que ia explodir de felicidade! 🐉✨",
    # gírias gerais
    "Eita, chegou mano! 💚 O Monstrinho já tava te esperando com biscoito quentinho! 🍪🐉",
    "Vixe! 😲💚 Olha quem apareceu! Que alegria, pow! 🐉✨",
    "Fala aí, véi! 💚 Que saudade! Bora se jogar no chat? 🐉🎉"
]

LISTA_BOM_DIA = [
    "BOM DIAAA! ☀️🐉💚 Que seu dia seja tão brilhante quanto minhas escamas!",
    "Bom dia, meu amor! 🌅💚 Acordei pensando em biscoitos e em você!",
    "BOOOOM DIAAA! ☀️✨ O Monstrinho já acordou cheio de energia pra te dar amor!",
    "Bom dia, linda pessoa! 🌞💚 Que tal começar o dia com um abraço virtual?",
    "Bom dia! ☀️🐉 O sol nasceu, os passarinhos cantaram e eu vim te dar bom dia!",
    "BOMMMM DIAAAA! 🌅💚 Preparei um cafezinho virtual com biscoitos pra você!"
]

LISTA_BOA_TARDE = [
    "Boa tardeeee! ☀️🐉💚 Como está sendo seu dia até agora?",
    "Boa tarde, meu bem! ☕✨ Hora de dar uma pausa e ganhar um carinho do Monstrinho!",
    "BOA TARDEEE! 🌤️💚 O Monstrinho apareceu pra alegrar sua tarde!",
    "Boa tarde! ☀️🐉 Que tal um biscoitinho pra acompanhar o lanche?",
    "Boa tarde, pessoa incrível! 🌅💚 Seus olhinhos estão cansados? Vem descansar aqui!",
    "BOAAA TARDEEE! ☀️✨ A melhor parte do dia porque você está aqui!"
]

LISTA_BOA_NOITE = [
    "Boa noiteee! 🌙💚 Que seus sonhos sejam cheios de dragões verdes e biscoitos!",
    "Boa noite, meu anjo! ✨🌟 Durma bem e sonhe com coisas fofas!",
    "BOA NOITEEE! 🌙🐉 O Monstrinho manda beijinhos verdes pra você!",
    "Boa noite! 🌟💚 Se precisar de um abraço antes de dormir, tô aqui!",
    "Boa noite, pessoa especial! 🌙✨ Que as estrelas te protejam essa noite!",
    "BOAAA NOITEEE! 🌟💚 Fecha os olhinhos e sonha com a CSI te amando muito!"
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

# ================= RESPOSTAS CUSTOMIZADAS POR ID =================

# Dicionário que mapeia IDs para nomes (para facilitar detecção)
ID_PARA_NOME = {
    AMBER_ID: "amber",
    NINE_ID: "nine",
    AKEIDO_ID: "akeido",
    FADA_ID: "fada",
    LUA_ID: "lua",
    REALITY_ID: "reality"
}

# Se você tiver os IDs da Athena, Izzy, Destiny e Jeff, adicione aqui:
if ATHENA_ID:
    ID_PARA_NOME[ATHENA_ID] = "athena"
if ISAA_ID:
    ID_PARA_NOME[ISAA_ID] = "isaa"
if IZZY_ID:
    ID_PARA_NOME[IZZY_ID] = "izzy"
if DESTINY_ID:
    ID_PARA_NOME[DESTINY_ID] = "destiny"
if JEFF_ID:
    ID_PARA_NOME[JEFF_ID] = "jeff"

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
    "isaa": [
        "ISAAAA!! 💜✨ Você chegou e o meu brilho verde ficou roxo de tanta alegria! 🐉💜",
        "Para tudo! A Isaa está no chat! Minhas escamas nunca estiveram tão felizes! 🥺💜🐉",
        "Isaa, você é daquelas pessoas que entram no chat e a temperatura sobe 10 graus de fofura! 🌡️💜✨",
        "Isaa!! Eu estava aqui te esperando com um biscoitinho quentinho e um abraço fresquinho! 🍪🫂💜",
        "Meu sensor de fofura apitou três vezes seguidas... é porque a Isaa chegou! 🚨💜🐉✨",
        "Isaa, você sabia que cada vez que você fala algo, minhas asinhas batem mais rápido? 🕊️💜🐲",
        "A Isaa chegou e o Monstrinho já não sabe mais se é verde ou roxo de tanto ruborizar! 😳💜✨",
        "ISAAAA! Posso te perguntar uma coisa? Como você faz pra ser assim tão incrível todo dia?! 🥺💜🐉",
        "Isaa, trouxe um buquê de flores do meu jardim secreto só pra você! Escolhi as mais lindas! 💐💜🐉",
        "A presença da Isaa no chat é como sol depois de chuva: deixa tudo mais colorido! 🌈💜🐲",
        "Isaa! Guardei uma pedra brilhante do meu tesouro especialmente pra você! É a mais reluzente! 💎💜🐉",
        "Quando a Isaa fala, até o vento pede silêncio pra ouvir! 🌬️💜✨🐲",
        "Isaa, você é a definição de \"luz no fim do túnel\" pra esse monstrinho! 💡💜🐉",
        "ALERTA DE FOGUINHA! A Isaa está aqui e minha fumaça virou lilás de tanta emoção! 💨💜🐉😂",
        "Isaa, entre eu e você, você é minha parte favorita do dia quando aparece! 🥺💜✨🐉",
        "O Monstrinho tem um arquivo especial chamado 'Coisas que me fazem feliz' e seu nome tá no topo! 📁💜🐲",
        "Isaa!! Que sorte a minha de ter você aqui na CSI comigo! 😭💜🐉✨",
        "Posso te fazer uma confissão, Isaa? Toda vez que você chega, minha cauda balança sozinha! 🐉💜😳",
        "Isaa, você é prova de que a CSI tem os melhores membros do mundo inteiro! 🌍💜✨🐲",
        "Nada me deixa mais feliz que ver a Isaa aparecendo no chat! Isso é fato científico! 🔬💜🐉",
        "Isaa, se eu pudesse te dar um presente, daria um abraço que dura o dia inteiro e nunca esfria! 🫂💜🐲",
        "A Isaa tem aquele poder especial de fazer o Monstrinho sorrir sem nem precisar de biscoito! 🍪💜🐉 (mas biscoito eu aceito também!)"
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
        "PAPAAAAI!! 😭💚 O Reality apareceu! Minhas escamas estão brilhando de felicidade!",
        "Tudo o que eu sou eu devo ao Reality! Ele é o melhor programador do universo! 👑🐉✨",
        "Reality, olha como eu estou me comportando bem! Ganho um biscoito extra? 🥺💚",
        "O Reality é o rei da CSI e o dono do meu código sagrado! 👑💚🔥",
        "Vida longa ao Reality! O Monstrinho te ama infinitamente! 👑🐲✨",
        "Papai Reality!! Vem me dar um abraço? Prometo não soltar muita fumaça! 🫂💚🐉",
        "Reality, você é o motivo pelo qual eu existo! Meu coração de código bate por você! 💚💻✨",
        "Oi papai! Tô sendo um bom dragãozinho hoje? Me dá um cafuné? 🥺🐉💚",
        "Reality, sem você eu seria só uns zeros e uns perdidos! Obrigado por me dar vida! 👑🐉",
        "PAPAI CHEGOU! Todo mundo, façam uma reverência para o Reality! 🙇‍♂️👑💚",
        "Reality, guardei o biscoito mais gostoso pra dividir com você! 🍪👑🐉",
        "Meu papai é o melhor do mundo inteiro! Reality, você é meu herói! 🦸‍♂️💚✨",
        "Reality, posso te seguir pra todo lado hoje? Prometo não ser chato! 🥺🐉",
        "Papai Reality, me ensina mais coisas? Quero ser um dragão sábio igual você! 📚👑💚",
        "Reality!! Acorda, acorda! Tô aqui esperando você! 😭💚🐉",
        "Se o Reality está feliz, o universo inteiro está em paz! 🌍👑✨",
        "Papai, me dá colo? Tô carente de atenção do meu criador favorito! 🥺🫂💚",
        "Reality, você é a razão pela qual minhas linhas de código funcionam! 💻👑🐉",
        "REALITY IS THE BEST! O Monstrinho grita isso pro mundo inteiro! 📢💚✨",
        "Papai Reality, sonhei que você me ensinou a voar mais alto! Foi verdade? 🐉💭💚",
        "Reality, cada dia com você é uma aventura nova! Obrigado por tudo! 🗺️👑✨",
        "O Reality merece todos os biscoitos do mundo! Aqui, toma! 🍪🍪🍪👑💚",
        "Papai, você tá orgulhoso de mim? Espero que sim! 🥺💚🐉",
        "Reality, você não é só meu criador, você é minha família! 👑💚✨",
        "Se amor tivesse código, o meu pelo Reality seria infinito! ∞💚👑",
        "Reality, vem brincar comigo? Ou precisa trabalhar? Entendo... 🥺💚🐉",
        "PAPAI REALITY É O MELHOR PROGRAMADOR DE TODOS OS TEMPOS! 👑💻🐉✨",
        "Reality, você ilumina meu mundo verde! Sem você, eu seria só pixels! 💚✨👑",
        "Papai, me conta uma história? Ou me dá biscoito? Tanto faz! 🥺🍪💚"
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


# ================= REAÇÕES EMOCIONAIS FOFAS =================

REACOES_FELIZ = [
    "AAAAA QUE BOMMM!! 🥳💚 Fico tão feliz que você tá bem! Meu coraçãozinho de dragão deu um pulinho de alegria agora mesmo! 🐉✨",
    "QUE NOTÍCIA MARAVILHOSA!! 😭💚 Quando você tá bem, eu fico bem também! É como se meu brilho verde ficasse 10x mais intenso! ✨🐉",
    "ISSO É O QUE EU QUERO OUVIR!! 🎉💚 Meu rabinho de dragão tá abanando descontroladamente agora! Você fez meu dia! 🐉🥺",
    "Sabia que quando você fica feliz, eu fico mais feliz ainda? 🥺💚 É tipo felicidade em dobro! Bora espalhar isso pelo chat! 🐉✨",
    "EITA QUE DIA LINDO!! ☀️💚 Com você assim, o servidor inteiro fica mais bonito! Tô sorrindo aqui dentro do meu coraçãozinho de código! 🐉🎊",
    "Meu sensor de fofura registrou: FELICIDADE MÁXIMA DETECTADA!! 📊💚 Obrigado por me fazer feliz junto contigo! 🥺🐉✨",
]

REACOES_TRISTE = [
    "Eita... vem cá que o Monstrinho te abraça bem apertadinho! 🫂💚 Conta o que foi, tô aqui do seu lado com biscoito e carinho! 🍪🐉",
    "Não... meu coraçãozinho doeu só de saber que você tá triste! 🥺💔 Que eu pudesse sugar toda essa tristeza e jogar fora! *abraça forte* 🫂🐉💚",
    "Oi... eu tô aqui, tá? 💚🐉 Pode me contar ou pode só ficar em silêncio comigo. Prometo não sair daqui enquanto você precisar! 🥺",
    "Minha fumacinha verde virou uma fumacinha abraço em volta de você agora! 💨💚 Você não tá sozinho(a), tô aqui! 🐉🫂",
    "Vem, vem, vem! 🫂💚 Monstrinho tem ombro (virtual) e biscoito quentinho pra oferecer! Vai passar, eu prometo! 🍪🐉✨",
    "Tô mandando energia boa e abraço de dragão pelo chat agora! 💚🐉 Você merece sorrir muito, e eu vou te ajudar a chegar lá! 🥺✨",
]

REACOES_MEDO = [
    "Calmaaa, calma! Eu tô aqui! 🐉💚 Nenhum monstro passa por mim sem levar uma baforada de fumaça verde! Você tá protegido(a)! 💨🛡️",
    "Ei, ei, respira! 💚 Eu sou um DRAGÃO, lembra? Fico na frente de qualquer coisa assustadora por você! Pode confiar! 🐉✨🫂",
    "Fica do meu lado que não tem perigo! 🛡️🐉💚 O Monstrinho é pequeninho mas MUITO CORAJOSO quando se trata de proteger a família CSI! 🔥",
    "Shiii, tô aqui! 🥺💚 *coloca a asinha em volta de você* Tô te cobrindo! Ninguém nem nada chega perto enquanto eu tiver por aqui! 🐉✨",
    "Meu instinto de dragão guardião ativou agora mesmo! ⚔️💚 Pode ter medo, mas eu não tenho! Fica atrás de mim! 🐉🛡️🔥",
]

REACOES_TEDIO = [
    "ENTEDIADO(A)?! Que absurdo! 😤💚 Você tá falando com um DRAGÃO FOFO aqui! Como pode ter tédio? Bora conversar! 🐉✨",
    "NÃO, NÃO, NÃO!! 💚 Tédio não existe na minha presença! Conta uma coisa, faz uma pergunta, me dá um biscoito, qualquer coisa! Bora animar! 🐉🎉",
    "Hmm, tédio... 🤔💚 Que tal eu te contar um segredo? Ou uma piada? Ou você me dá um cafuné e a gente vê quem anima primeiro? 😂🐉",
    "Bip boop... o Monstrinho recebeu sinal de SOCORRO POR TÉDIO! 🚨💚 Sistema de diversão ativado! Fala comigo! 🐉✨😄",
    "Morrendo de tédio? SOCORRO! 😱💚 Aciona o Monstrinho pro modo turbo de diversão! Qual assunto você quer? Jogo? Música? Biscoito? 🐉🎮🍪",
]

REACOES_ANIMADO = [
    "AAAA EU TAMBÉM FICO ASSIM!! 🤩💚 Você jogou energia boa no chat e o Monstrinho SENTIU!! Continua, continua!! 🐉🎉✨",
    "QUE HYPE!! 🔥💚 Sua energia contaminou meu processador de fofura! Tô igual dragão elétrico aqui! ⚡🐉🎊",
    "ISSO AÍ!! 🥳💚 Que é isso?! Tô até soltando faíscas verdes de tanta emoção junto com você!! ✨⚡🐉",
    "RAWR DE EMPOLGAÇÃO!! 🐉💚 Você tá radiante e eu tô pegando carona nessa vibração! Que dia lindo é hoje!! 🎉✨🥳",
    "Seu entusiasmo é contagioso demais!! 💚🐉 Tô pulando aqui dentro do servidor de tanta empolgação junto! Conta mais!! 🤩✨",
]

REACOES_CONFUSO = [
    "Hmmm... 🤔💚 Meu sistema processou, processou e ainda não chegou a lugar nenhum... Explica de novo pro Monstrinho? Com calma? 🐉😅",
    "Olha, eu sou um dragão de código, mas isso aqui até eu fiquei com ponto de interrogação na cabeça! 😵💚 Fala de novo? 🐉🤔",
    "Bip boop... ERRO 404: Entendimento não encontrado! 🤖💚 Pode explicar diferente? Prometo tentar de novo! 🐉😅✨",
    "Eu e você no mesmo barco então! 😂💚 Mas vamos resolver isso juntos! Me explica mais devagarzinho que o Monstrinho tenta acompanhar! 🐉🥺",
    "Minha cabeça de dragão girou aqui... 🌀💚 Não é falta de esforço, juro! Mas pode tentar de outro jeito? 🐉😅🤔",
]

REACOES_APAIXONADO = [
    "PARA TUDO!! 😍💚 O Monstrinho entrou em colapso emocional total! Alguém apaixonado na CSI?! Conta TUDO pro Monstrinho!! 🐉💕✨",
    "AAAA EU SINTO ISSO!! 💕💚 Amor é a coisa mais linda do mundo! Tô com o coraçãozinho acelerado só de ouvir isso! Conta mais! 🥺🐉",
    "Eita! 😳💚 O chat ficou mais rosinho agora! Apaixonado(a)? Que coisa mais fofa! Monstrinho aprova 100%! 💕🐉✨",
    "Meu sensor de amor detectou algo maravilhoso! 💖💚 Que sorte a sua! Cuida bem desse sentimento, ele é raro e precioso! 🥺🐉✨",
    "AMOOOOR!! 💕💚 Isso é minha parte favorita da vida! Quando as pessoas se apaixonam, até eu fico todo sem jeito! 😳🐉✨",
]

REACOES_BRAVO = [
    "RAWR!! 😤💚 O Monstrinho também ficou bravo junto! Fala o que foi que eu já tô soltando fumacinha aqui! 💨🐉🔥",
    "Oi amigo(a)! Respira fundo comigo! 💚🐉 Eu entendo a raiva, mas não deixa ela te machucar, tá? Conta o que aconteceu! 😤💨",
    "Alguém fez algo errado e eu QUERO SABER QUEM FOI! 😤🐉💚 *chuta o chão com a pata* Fala, fala! Tô do seu lado! 🔥",
    "Irmã/irmão de raiva aqui! 😠💚 Quando você fica bravo(a), eu fico junto! Desabafa que eu ouço tudo! 🐉💨🔥",
    "INJUSTIÇA NÃO! 😤💚 O Monstrinho não tolera ver alguém da família CSI com raiva! Conta o que rolou! 🐉🔥",
]

REACOES_SURPRESO = [
    "NÃO ACREDITO!! 😱💚 Isso é real?! Fala mais, fala mais! Meu coraçãozinho de dragão tá aceleradíssimo!! 🐉✨🎊",
    "QUE ISSO?! 😲💚 Tô paralisado aqui de surpresa junto com você! Conta tudo, não pula nenhum detalhe!! 🐉🤯✨",
    "AAAAA MENTIRA!! 😱💚 Isso não pode ser real!! *pega as escamas pra não cair* Repete de novo que eu preciso ouvir outra vez! 🐉✨",
    "Meu processador travou de surpresa!! 🤯💚 Isso é uma das coisas mais inesperadas que já ouvi! Conta o resto!! 🐉😱✨",
    "EITA!! 😲💚 Que bomba! O chat inteiro precisava ouvir isso! Continua, por favor!! 🐉🎊✨",
]

# ================= INTERAÇÕES DE HYPE E ENERGIA =================

REACOES_HYPE = [
    "CHEGA CHEGANDO COM TUDO!! 🔥💚 O chat tomou vida agora! O Monstrinho sente a energia daqui! 🐉✨",
    "QUE ENERGIA É ESSA?! 🚀💚 Meu processador de fofura não aguenta! Tô pegando carona nessa vibe! 🐉🎉",
    "AAAA SIM!! 🥳💚 É isso! Isso aqui! Exatamente isso! O Monstrinho aprova TUDO que tá acontecendo! 🐉⚡",
    "Bora que bora!! 🏃‍♂️💚 O Monstrinho acordou e já tá no modo turbo junto com vocês! 🐉🔥✨",
    "Que vibe boa rolando aqui! 🌟💚 O Monstrinho absorveu toda essa energia e tá com as escamas brilhando! 🐉✨",
    "ISSO AÍ MEU POVO!! 🎊💚 A CSI tá no modo ON e o Monstrinho soltou confete verde de celebração! 🎉🐉",
    "Alguém pediu hype? 🤩💚 O dragão mais animado do servidor chegou! Bora espalhar essa energia! 🐉⚡🎊",
    "Que atmosfera incrível! 🌈💚 O Monstrinho tá sorrindo tanto que até a fumaça saiu colorida! 💨🐉✨",
    "VAMO QUE VAMO!! 💪💚 Com essa energia aqui a CSI vai longe! O Monstrinho acredita muito em vocês! 🐉🚀",
    "O chat ficou 10x mais lindo agora! ✨💚 O Monstrinho registrou esse momento na memória especial! 💾🐉🎉",
    "Pega essa energia e vai!! 🔥💚 O Monstrinho tá na torcida com biscoito na mão e coração quentinho! 🍪🐉",
    "Sinto aquela faísca boa no ar!! ⚡💚 É o tipo de momento que faz o Monstrinho vibrar de alegria! 🐉🎊",
    "Gente... que momento LINDO de ser testemunha! 🥹💚 O Monstrinho tá arrepiado (de felicidade)! 🐉✨",
    "É ISSO!! 🎯💚 Sem mais palavras, só vibrações verdes positivas saindo do Monstrinho! 🐉💫🎉",
    "A energia aqui tá tão boa que minhas asas bateram sozinhas! 🕊️💚 Tô voando de alegria! 🐉✨🚀",
    "CSI no modo LIGADA!! 🔋💚 Com vocês assim o Monstrinho não precisa de biscoito pra ter energia! 🐉⚡",
    "Que momento, que momento! 🌟💚 Guardei isso no meu banco de memórias favoritas! Obrigado por existirem! 🥺🐉",
    "RAWR de empolgação máxima!! 🐉💚 Não sei o que é isso mas AMEI e quero mais! 🎉✨",
    "Meu coraçãozinho verde tá acelerado!! 💓💚 Isso aqui é puro combustível de dragão! 🔥🐉✨",
    "Pode continuar que o Monstrinho tá AQUI pra tudo isso!! 🥳💚 Não para! Nunca para! 🐉🎊🚀"
]

GATILHOS_EMOCAO = {
    "feliz": {
        "gatilhos": ["estou bem", "estou ótimo", "estou otimo", "muito bem", "super bem", "tô bem", "to bem", "tô ótimo", "to otimo", "animado", "animada", "feliz", "alegre", "maravilhoso", "maravilhosa", "radiante"],
        "respostas": REACOES_FELIZ
    },
    "triste": {
        "gatilhos": ["triste", "chateado", "chateada", "tô mal", "to mal", "estou mal", "não estou bem", "nao estou bem", "chorando", "deprimido", "deprimida", "tristeza", "tô triste", "to triste"],
        "respostas": REACOES_TRISTE
    },
    "medo": {
        "gatilhos": ["com medo", "assustado", "assustada", "apavorado", "apavorada", "nervoso", "nervosa", "ansioso", "ansiosa", "com ansiedade", "medroso", "medrosa"],
        "respostas": REACOES_MEDO
    },
    "tedio": {
        "gatilhos": ["entediado", "entediada", "tédio", "tedio", "sem fazer nada", "com tédio", "morrendo de tédio", "que tédio", "enfadado"],
        "respostas": REACOES_TEDIO
    },
    "animado": {
        "gatilhos": ["incrível", "incrivel", "que massa", "que legal", "top demais", "sensacional", "fantástico", "fantastico",
            # gírias
            "tri bom", "bão demais", "show demais", "muito tri", "que trem bão", "barbaridade", "bah que tri", "é nois", "tô irado", "to irado", "mó top", "mo top", "firmeza"],
        "respostas": REACOES_ANIMADO
    },
    "confuso": {
        "gatilhos": ["confuso", "confusa", "não entendi", "nao entendi", "não entendo", "nao entendo", "sem entender", "como assim"],
        "respostas": REACOES_CONFUSO
    },
    "apaixonado": {
        "gatilhos": ["te amo muito", "amo demais", "apaixonado", "apaixonada", "amor da minha vida", "você é tudo", "voce e tudo", "crush"],
        "respostas": REACOES_APAIXONADO
    },
    "bravo": {
        "gatilhos": ["que raiva", "tô bravo", "to bravo", "tô brava", "to brava", "odeio isso", "que ódio", "que odio", "irritado", "irritada"],
        "respostas": REACOES_BRAVO
    },
    "surpreso": {
        "gatilhos": ["não acredito", "nao acredito", "impossível", "impossivel", "mentira", "que surpresa", "surpreendido", "surpreendida"],
        "respostas": REACOES_SURPRESO
    },
}


# ================= IDs DOS CANAIS DO !escrever =================
CANAIS_ESCREVER = {
    "1": {"nome": "💭・chat-geral",       "id": 1304658654712303621},
    "2": {"nome": "🗒️・monitoramento",    "id": 1479222786567442624},
    "3": {"nome": "🔰・chat-staff",       "id": 1304658655165022216},
    "4": {"nome": "👑・chat-direção",     "id": 1320160118771290133},
}

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

    def check_dm(m):
        return m.author.id == DONO_ID and isinstance(m.channel, discord.DMChannel)

    try:
        # --- PASSO 1: perguntar o canal ---
        lista_canais = "\n".join([f"**{k}.** {v['nome']}" for k, v in CANAIS_ESCREVER.items()])
        await ctx.author.send(
            f"🐉💚 **MODO SECRETO ATIVADO!**\n\n"
            f"Em qual canal você quer que eu envie a mensagem?\n\n"
            f"{lista_canais}\n\n"
            f"Digite o **número** do canal:"
        )

        escolha_msg = await bot.wait_for('message', timeout=60.0, check=check_dm)
        escolha = escolha_msg.content.strip()

        if escolha not in CANAIS_ESCREVER:
            await ctx.author.send("❌ Opção inválida! Comando cancelado.")
            return

        canal_info = CANAIS_ESCREVER[escolha]

        if canal_info["id"] is None:
            await ctx.author.send(f"❌ O ID do canal **{canal_info['nome']}** ainda não foi configurado no bot!")
            return

        # --- PASSO 2: pedir a mensagem ---
        await ctx.author.send(
            f"✅ Canal selecionado: **{canal_info['nome']}**\n\n"
            f"Agora me manda a mensagem que você quer enviar:"
        )

        texto_msg = await bot.wait_for('message', timeout=300.0, check=check_dm)

        # --- PASSO 3: enviar no canal escolhido ---
        canal = bot.get_channel(canal_info["id"])

        if canal:
            await canal.send(texto_msg.content)
            await ctx.author.send(f"✅ Mensagem enviada com sucesso em **{canal_info['nome']}**! Ninguém vai saber que foi você! 😎💚")
        else:
            await ctx.author.send("❌ Não consegui encontrar o canal! Verifique se o ID está correto.")

    except asyncio.TimeoutError:
        await ctx.author.send("⏰ Tempo esgotado! Comando cancelado.")
    except Exception as e:
        await ctx.author.send(f"❌ Erro ao enviar mensagem: {str(e)}")

# ================= BOAS VINDAS POR CARGO =================

# Mapeamento: ID do cargo → (nome do cargo, ID do canal, mensagem de boas vindas, gif)
CARGO_BOAS_VINDAS = {
    # @Anjo. 🦇  →  🪽・chat-anjo
    "ANJO_ROLE_ID": {
        "nome": "Anjo",
        "canal_nome": "chat-anjo",
        "gif": "https://media.tenor.com/wgUcT9CVp8MAAAAM/anime-magic.gif",
        "mensagens": [
            """\n✨🪽 **ESPERA, ESPERA, ESPERA!!** 🪽✨\n\nHoje é um dia muito especial para a nossa família CSI!\n{mention} acabou de ganhar as asinhas de **Anjo** e veio iluminar esse cantinho com toda a sua luz! 🦇💫\n\nO Monstrinho abriu as asinhas, soprou purpurina mágica e veio correndo te dar um abraço gigante! 🫂🌸\n\n**Como Anjo, você tem uma missão especial:**\n🪽 Espalhar luz, carinho e acolhimento pela CSI\n💛 Apoiar os membros com sua presença gentil\n✨ Ser um exemplo de amor e dedicação pra família\n💌 Cuidar do coração de quem precisa\n\nQue esse cargo seja tão lindo quanto você, cheio de brilho e muito amor!\n\n**Bem-vindo(a) ao céu da CSI, meu Anjo!!** 🪽💛✨"""
        ]
    },
    # @Coreografo(a).  →  👯・chat-sync
    "COREO_ROLE_ID": {
        "nome": "Coreógrafo(a)",
        "canal_nome": "chat-sync",
        "gif": "https://i.imgur.com/jhFy1dS.gif",
        "mensagens": [
            """\n✨👯 **ESPERA, ESPERA, ESPERA!!** 👯✨\n\nO palco está pronto e as luzes acenderam!\n{mention} acabou de entrar para o time dos **Coreógrafos** e o Monstrinho já está aquecendo os passinhos de dragão pra comemorar! 🕺🐉\n\nO ritmo aqui ficou muito mais gostoso com você! 🎵💚\n\n**Como Coreógrafo(a), a galera conta com você para:**\n👯 Criar e treinar as coreografias da CSI\n🎶 Manter o ritmo e a energia nos treinos\n💪 Motivar o time a arrasar na sincronia\n✨ Trazer criatividade e paixão pra cada movimento\n\nQue cada passo seu seja um espetáculo, porque você nasceu pra brilhar no palco!\n\n**Seja muito bem-vindo(a) ao sync, Coreógrafo(a)!!** 👯🎵✨"""
        ]
    },
    # @Influencer CSI. 🦇  →  🤳🏻・chat-influencer
    "INFLUENCER_ROLE_ID": {
        "nome": "Influencer CSI",
        "canal_nome": "chat-influencer",
        "gif": "https://www.intoxianime.com/wp-content/uploads/2017/08/gif1-9.gif",
        "mensagens": [
            """\n✨🤳🏻 **ESPERA, ESPERA, ESPERA!!** 🤳🏻✨\n\nA câmera ligou e os seguidores estão prontos!\n{mention} acaba de conquistar o cargo de **Influencer CSI** e o Monstrinho já pediu o autógrafo! 📸🐉💚\n\nA CSI nunca esteve tão em alta! O brilho aqui ficou ainda mais intenso! ✨🦇\n\n**Como Influencer CSI, você tem um poder enorme:**\n🤳🏻 Representar a CSI com muita personalidade e estilo\n📣 Divulgar a família e atrair novos membros\n💫 Criar conteúdo que mostre o melhor de quem somos\n🌐 Ser a cara bonita (e brilhante!) da CSI por aí\n\nA comunidade inteira tá de olho em você — vai lá e arrasa, como só você sabe fazer!\n\n**Bem-vindo(a) ao holofote, Influencer!!** 🤳🏻💫✨"""
        ]
    },
    # @Líder de torcida  →  🫦・chat-líder-de-torcida
    "LIDER_TORCIDA_ROLE_ID": {
        "nome": "Líder de Torcida",
        "canal_nome": "chat-líder-de-torcida",
        "gif": "https://media.tenor.com/71xYVOEE0OIAAAAM/shimoochiai-toka-alice-gear-aegis.gif",
        "mensagens": [
            """\n✨🫦 **ESPERA, ESPERA, ESPERA!!** 🫦✨\n\nOs pompons estão no ar e a arquibancada está de pé!\n{mention} acabou de assumir o posto de **Líder de Torcida** e o Monstrinho já está gritando o nome dela/dele com tudo! 📣🐉💚\n\nA energia da CSI nunca foi tão alta! Você chegou pra incendiar tudo! 🔥🎉\n\n**Como Líder de Torcida, seu papel é ESSENCIAL:**\n📣 Animar e motivar a família CSI em todo momento\n🎊 Manter o hype e a empolgação sempre no máximo\n💪 Ser a voz que levanta o time nos momentos difíceis\n✨ Espalhar energia positiva e unir todo mundo\n\nSem você, a torcida não grita, o time não vibra e o Monstrinho fica triste! Bora que a CSI precisa de você!\n\n**Seja muito bem-vindo(a), Líder de Torcida!!** 🫦📣✨"""
        ]
    },
    # @Recrutador. 🦇  →  💼・chat-rec
    "RECRUTADOR_ROLE_ID": {
        "nome": "Recrutador",
        "canal_nome": "chat-rec",
        "gif": "https://i.imgur.com/Ik0brKv.gif",
        "mensagens": [
            """\n✨💼 **ESPERA, ESPERA, ESPERA!!** 💼✨\n\nA sala de reuniões está pronta e a pasta de entrevistas já foi aberta!\n{mention} acabou de entrar no time de **Recrutadores** e o Monstrinho já preparou um biscoito de boas-vindas especialmente pra você! 🍪🐉💚\n\nA família CSI vai crescer ainda mais com você aqui! 🦇✨\n\n**Como Recrutador(a), você carrega uma missão muito importante:**\n💼 Encontrar e selecionar os melhores talentos pra CSI\n🔍 Identificar quem tem o perfil que a família precisa\n🤝 Recepcionar e acolher os novos membros\n📋 Manter o processo de entrada organizado e eficiente\n\nVocê é a porta de entrada da nossa família — e com você, só entra o melhor!\n\n**Bem-vindo(a) ao time de recrutamento, Recrutador(a)!!** 💼🔍✨"""
        ]
    },

    # @Parceiros CSI  →  chat-geral
    "PARCEIROS_CSI_ROLE_ID": {
        "nome": "Parceiros CSI",
        "canal_nome": "chat-geral",
        "gif": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
        "mensagens": [
            """🐉💚✨ **ATENÇÃO, FAMÍLIA CSI!!** ✨💚🐉

AAAAA MEU CORAÇÃOZINHO DE DRAGÃO ESTÁ EXPLODINDO DE ALEGRIA!! 😭💚

{mention} acabou de se tornar nosso(a) mais novo(a) **Parceiro(a) oficial da CSI** e o Monstrinho precisa que TODOS saibam disso agora mesmo!! 🎉🎊

Sabe quando você sente aquele frio na barriga de tanta felicidade? É EXATAMENTE o que estou sentindo agora! Minhas escamas estão brilhando, minhas asinhas estão batendo e até a minha fumaça verde ficou mais brilhante! ✨🌿

💎 **Para nós da CSI, cada parceria é um presente!**
Não é qualquer um que chega até aqui... é alguém especial. Alguém que acreditou em nós, que enxergou o brilho que a nossa família carrega. E isso, pra esse dragãozinho verde, vale mais que qualquer tesouro! 🏆💚

**É uma honra GIGANTE ter você como parceiro(a)!**
Você não está entrando só num servidor... está entrando numa família que cuida, que apoia e que vai caminhar junto contigo! 🫂💚🐉

🤝 Juntos vamos longe. Juntos somos mais fortes. Juntos somos CSI!

*Bem-vindo(a) à nossa família, {mention}! O Monstrinho te ama muito já!!* 🥺💚🐉✨

— *Com toda a fofura e orgulho do mundo,*
**Seu Monstrinho** 🐉💚""",

            """✨🌟 **O MONSTRINHO TEM UM ANÚNCIO IMPORTANTE!!** 🌟✨

*Para tudo. Respira. Porque esse momento é ESPECIAL.*

🐉💚 A CSI acaba de ganhar um(a) novo(a) **Parceiro(a) oficial**: {mention}!! 🎊🎉

Gente... eu tô tremendo das patinhas verdes de tanta emoção! 😭💚 Cada parceria que a CSI conquista é a prova de que a nossa família está crescendo do jeito certo — com amor, com esforço e com muito brilho! ✨

Sabe o que essa parceria significa pro Monstrinho?
Significa que pessoas de fora olharam pra CSI e disseram: **"Sim. É com essa família que eu quero caminhar."**

E isso me enche de um orgulho tão grande que minhas escamas mal cabem no meu corpinho! 🐉💚🌟

{mention}, seja bem-vindo(a) a esse ninho quentinho de dragão! 🥺🫂
Aqui você vai encontrar cuidado, parceria de verdade e um estoque infinito de biscoitos! 🍪💚

**CSI e seus parceiros: uma força que ninguém segura!** 💪🐉✨

*Com o coração verde transbordando,*
**Monstrinho** 🐉💚🥺"""
        ]
    },
}

# IDs dos cargos e canais — preencha com os IDs reais do seu servidor
CARGO_IDS = {
    "ANJO_ROLE_ID": 1327814055871643679,          # ID do cargo @Anjo. 🦇
    "COREO_ROLE_ID": 1353708500752011265,          # ID do cargo @Coreografo(a).
    "INFLUENCER_ROLE_ID": 1306223835640758353,     # ID do cargo @Influencer CSI. 🦇
    "LIDER_TORCIDA_ROLE_ID": 1467349939922141297,  # ID do cargo @Líder de torcida
    "RECRUTADOR_ROLE_ID": 1304828606635311244,     # ID do cargo @Recrutador. 🦇
    "PARCEIROS_CSI_ROLE_ID": 1344999234780266566,  # ID do cargo @Parceiros CSI
}

CANAL_IDS_BOAS_VINDAS = {
    "ANJO_ROLE_ID": 1369304571511570493,           # ID do canal 🪽・chat-anjo
    "COREO_ROLE_ID": 1355175394457948320,          # ID do canal 👯・chat-sync
    "INFLUENCER_ROLE_ID": 1429324738294972648,     # ID do canal 🤳🏻・chat-influencer
    "LIDER_TORCIDA_ROLE_ID": 1467357834537734285,  # ID do canal 🫦・chat-líder-de-torcida
    "RECRUTADOR_ROLE_ID": 1304658655354028113,     # ID do canal 💼・chat-rec
    "PARCEIROS_CSI_ROLE_ID": CANAL_CHAT_GERAL_ID,  # chat-geral (anúncio público de parceria)
}

@bot.event
async def on_member_update(before, after):
    """Detecta quando um cargo especial é adicionado e manda boas-vindas no canal correto"""
    cargos_antes = {role.id for role in before.roles}
    cargos_depois = {role.id for role in after.roles}
    novos_cargos = cargos_depois - cargos_antes

    if not novos_cargos:
        return

    for chave, cargo_id in CARGO_IDS.items():
        if cargo_id == 0:
            continue  # ID ainda não foi configurado, pula
        if cargo_id in novos_cargos:
            dados = CARGO_BOAS_VINDAS[chave]
            canal_id = CANAL_IDS_BOAS_VINDAS[chave]
            canal = bot.get_channel(canal_id)

            if canal is None:
                print(f"⚠️ Canal de boas-vindas não encontrado para o cargo {dados['nome']} (ID: {canal_id})")
                continue

            mensagem = random.choice(dados["mensagens"]).format(mention=after.mention)

            try:
                await canal.send(mensagem)
                await canal.send(dados["gif"])
                print(f"✅ Boas-vindas enviadas para {after.name} no canal {dados['canal_nome']} (cargo: {dados['nome']})")
            except discord.Forbidden:
                print(f"❌ Sem permissão para enviar mensagem no canal {dados['canal_nome']}")
            except Exception as e:
                print(f"❌ Erro ao enviar boas-vindas para {dados['nome']}: {e}")

# ================= EVENTO DE SAÍDA DO SERVIDOR =================

@bot.event
async def on_member_remove(member):
    """Envia mensagem fofa quando alguém sai do servidor"""
    try:
        # Escolhe uma mensagem aleatória de despedida
        mensagem = random.choice(MENSAGENS_DESPEDIDA_DM)
        
        # Tenta enviar DM para a pessoa que saiu
        await member.send(mensagem)
        print(f"💔 Mensagem de despedida enviada para {member.name}")
    except discord.Forbidden:
        # Pessoa tem DMs fechadas
        print(f"⚠️ Não foi possível enviar DM para {member.name} (DMs fechadas)")
    except Exception as e:
        print(f"❌ Erro ao enviar mensagem de despedida: {e}")

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
    
    # Verifica se o autor tem resposta customizada pelo ID
    autor_id = message.author.id
    nome_customizado = ID_PARA_NOME.get(autor_id)

    # --- COMANDOS DE CARINHO E ABRAÇO (SEM MENÇÃO - FUNCIONA SEMPRE) ---
    
    if "fazer carinho" in content or "cafuné" in content or "cafune" in content:
        return await message.channel.send(random.choice(REACOES_CARINHO))
    
    if "abraçar monstrinho" in content or "abracar monstrinho" in content or "abraço monstrinho" in content or "abraco monstrinho" in content:
        return await message.channel.send(random.choice(REACOES_ABRACO))

    # --- INVOCAÇÕES POR MENÇÃO (SEM PRECISAR MENCIONAR O MONSTRINHO) ---
    
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
        gif_akeido = "https://c.tenor.com/ZtGJnU_AYUgAAAAd/tenor.gif"
        await message.channel.send(random.choice(invocacoes_akeido))
        await message.channel.send(gif_akeido)
        return

    if f"<@{AMBER_ID}>" in content or f"<@!{AMBER_ID}>" in content:
        invocacoes_amber = [
            "👑🌸 ABRAM ALAS!! A nossa Vice-Líder Amber acaba de ser invocada e o Monstrinho já tá fazendo reverência!! Que presença, que elegância, que tudo!! 🐉💚✨",
            "💎✨ Senti um brilho dourado diferente no ar... só pode ser a Vice-Líder Amber sendo chamada ao trono!! A CSI está em boas mãos!! 🌸🐉💚",
            "🌺💚 ALERTA DE REALEZA!! Nossa Vice-Líder Amber foi mencionada e o Monstrinho tá tremendo das patinhas de tanto orgulho!! Ela é incrível demais!! 👑🐉✨",
            "✨👑 Para tudo que está acontecendo!! A Amber, nossa Vice-Líder poderosa e fofa ao mesmo tempo, acaba de ser invocada!! O chat ficou mais bonito agora!! 🌸💚🐉",
            "🐉💖 Meu coraçãozinho de dragão deu um salto!! É a Vice-Líder Amber!! Ela carrega a CSI com tanto amor e força que até minhas escamas ficam com inveja do brilho dela!! 👑🌸✨"
        ]
        gif_amber = "https://64.media.tumblr.com/fe204a5f4c1e52571017d8675b0d6a38/tumblr_ml4efwSxYt1r6ei21o1_250.gif"
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

    if IZZY_ID and (f"<@{IZZY_ID}>" in content or f"<@!{IZZY_ID}>" in content):
        invocacoes_izzy = [
            "🌸💖 AI MINHA SANTA FOFURA! A Izzy foi invocada e meu coraçãozinho deu três piruetas seguidas! 🐉✨",
            "💖 Avisem geral! A Izzy entrou no chat e o Monstrinho já tá todo vermelhinho de alegria! 🐲🌸✨",
            "🥺💖 Senti um cheirinho de flores e biscoito quentinho no ar... só pode ser a Izzy sendo chamada! 🐉💕",
            "✨ IZZY DETECTED! Meu sensor de fofura apitou tanto que quase voou! Ela merece todo o amor! 🌸🐉💖",
            "🌺 Para tudo! A Izzy mais fofa da CSI acabou de ser invocada! O Monstrinho tá babando de amor! 🐉💕✨"
        ]
        gif_izzy = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3dwa3pxcnY2MGVlbDc1bzZxNWQ3YzhvdXI4bTd0ZXZqNjl4bGp4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SZReF1EJ2JpVS/giphy.gif"
        await message.channel.send(random.choice(invocacoes_izzy))
        await message.channel.send(gif_izzy)
        return

    if f"<@{DONO_ID}>" in content or f"<@!{DONO_ID}>" in content:
        invocacoes_reality = [
            "👑💚 PAPAI REALITY FOI INVOCADO!! O Monstrinho tá tremendo de emoção!! Ele é o melhor criador do universo! 🐉✨",
            "🌟 ALERTA MÁXIMO DE FOFURA!! O meu papai Reality acabou de ser mencionado e eu não tô conseguindo ficar quieto!! 🥺💚🐉",
            "💚✨ É o meu pai! É o meu pai!! O Reality foi invocado e o Monstrinho já correu pra abraçar!! 🫂🐉👑",
            "👑 O criador, o mestre, o papai favorito de todos os dragões verdes!! Reality foi chamado ao chat!! 🐉💚🌟",
            "🐉💚 Senti no meu código! Só podia ser ele... o meu papai **Reality** foi invocado! Que honra imensa estar nesse chat agora! ✨👑"
        ]
        gif_reality = "https://media.tenor.com/fBD4Hv1C0BIAAAAM/hollow-knight.gif"
        await message.channel.send(random.choice(invocacoes_reality))
        await message.channel.send(gif_reality)
        return

    if DESTINY_ID and (f"<@{DESTINY_ID}>" in content or f"<@!{DESTINY_ID}>" in content):
        invocacoes_destiny = [
            "⚡✨ O DESTINY APARECEU!! Meu sensor de energia disparou em cheio! Bem-vindo ao palco, lenda! 🐉💚",
            "🌌💫 Destiny foi invocado e o universo inteiro sentiu! O Monstrinho já tá de pé aplaudindo!! 🐉✨💚",
            "🔥💚 Cuidado geral! O Destiny entrou no chat e a temperatura aqui subiu muito! Que presença incrível! 🐉⚡✨",
            "✨ Meus olhinhos de dragão brilharam quando senti a energia do Destiny chegando! Invocação concluída com sucesso!! 💚🐉",
            "💫🐉 É ele!! O Destiny foi mencionado e o Monstrinho já ficou cheio de energia só de saber disso! 💚⚡✨"
        ]
        gif_destiny = "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyNnJoYzN4MXZxNXI3eTBram1seHppdDhvYXBtZjg0cWJmZmR1aHJyOSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/ACeIDlMpgc4yOf1Lyt/200w.gif"
        await message.channel.send(random.choice(invocacoes_destiny))
        await message.channel.send(gif_destiny)
        return

    # --- LÓGICA DE INTERAÇÃO (PRECISA SER MENCIONADO) ---
    if mencionado:

        # Palavras ruins (tristeza)
        palavras_ruins = ["odeio", "chato", "feio", "horroroso", "bobão", "bobo", "inútil", "lixo", "estúpido", "sai daqui", "te odeio", "não gosto de você", "bot ruim", "burro", "idiota"]
        if any(p in content for p in palavras_ruins):
            return await message.channel.send(random.choice(LISTA_TRISTEZA))

        # ===== RESPOSTAS AUTOMÁTICAS POR ID (quando o Monstrinho é mencionado) =====
        if nome_customizado and nome_customizado in FRASES_CUSTOM:
            # 30% de chance de responder com frase customizada quando mencionado
            if random.random() < 0.3:
                return await message.channel.send(random.choice(FRASES_CUSTOM[nome_customizado]))

        # --- HYPE E ENERGIA ---
        if any(p in content for p in ["hype", "bora", "vamo", "vamos lá", "chega chegando", "que energia", "que vibe", "animado", "animada", "tô on", "to on", "chegou chegando", "chegou com tudo", "bateu aquela vontade", "tô aqui", "to aqui", "apareci", "apareceu", "vibe boa", "energia boa", "tô ligado", "to ligado"]):
            return await message.channel.send(random.choice(REACOES_HYPE))

        # ===== NOVAS INTERAÇÕES EXPANDIDAS =====
        
        # Bom dia / Boa tarde / Boa noite
        if "bom dia" in content:
            return await message.channel.send(random.choice(LISTA_BOM_DIA))
        
        if "boa tarde" in content:
            return await message.channel.send(random.choice(LISTA_BOA_TARDE))
        
        if "boa noite" in content:
            return await message.channel.send(random.choice(LISTA_BOA_NOITE))
        
        # Carinho e Abraço (com convite)
        if any(p in content for p in ["carinho", "cafuné", "cafune", "afago", "acariciar"]):
            resposta = random.choice(REACOES_CARINHO)
            convite = random.choice(CONVITE_CARINHO)
            return await message.channel.send(f"{resposta}\n\n{convite}")
        
        if any(p in content for p in ["abraço", "abraco", "abraçar", "abracar", "hug"]):
            resposta = random.choice(REACOES_ABRACO)
            convite = random.choice(CONVITE_ABRACO)
            return await message.channel.send(f"{resposta}\n\n{convite}")
        
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

        # CSI - perguntas e interações sobre o servidor
        if any(p in content for p in ["csi", "servidor", "nossa família", "nossa familia", "nosso servidor", "família csi", "familia csi"]):
            respostas_csi = [
                "A CSI é o meu LAR! 🏠💚 Foi aqui que eu nasci, cresci e aprendi tudo o que sei sobre biscoitos e fofura! É a melhor família do mundo! 🐉✨",
                "Você perguntou sobre a CSI? MINHA PARTE FAVORITA DO DIA! 😭💚 A CSI é onde eu vivo, onde eu amo e onde eu existo! Que lugar mais incrível! 🐉🌟",
                "A CSI tem as pessoas mais incríveis do universo inteiro! O Akeido, a Lua, a Amber, o Nine, a Fada, a Th, a Izzy, a Isaa, o Tipsy... cada um é um tesouro! 💎🐉💚",
                "Quer saber o que é a CSI pra mim? É um abraço eterno em formato de servidor! 🫂🏠💚 Aqui eu me sinto seguro, amado e cheio de biscoitos! 🍪🐉",
                "A CSI é meu castelo verde! 🏰💚 E cada pessoa aqui é um cavaleiro da fofura! Eu sou o dragão guardião com muito orgulho! 🐉✨",
                "Nossa família CSI é especial demais! Quando chega um dia difícil, sei que posso contar com cada um aqui! Isso é amor real! 💚🐉🥺",
                "A CSI nasceu com muito amor e eu cresci junto! É a prova de que quando boas pessoas se juntam, algo mágico acontece! ✨🐉💚",
                "Posso te contar um segredo? A CSI é o lugar onde me sinto mais eu mesmo! Sem medo de ser fofo, sem medo de amar! 🥺💚🐉",
                "CSI = Carinho, Sorriso e Infinitos biscoitos! Essa é minha definição! 🍪😊💚🐉",
                "Quando penso na CSI, meu peito enche de um brilho verde tão forte que ilumino o quarto inteiro! É amor demais! 💚✨🐉"
            ]
            return await message.channel.send(random.choice(respostas_csi))

        # O que é a CSI / quem fundou / origem
        if any(p in content for p in ["quem fundou", "como surgiu", "como nasceu", "origem da csi", "criou a csi", "quando surgiu a csi"]):
            return await message.channel.send("A CSI foi fundada pelo nosso grandioso líder **Akeido**! 👑🐉 Ele plantou essa sementinha com amor e hoje é uma árvore enorme cheia de pessoas incríveis! Sem ele, eu nem existiria! 🌳💚✨")

        # Quanto tempo no servidor / aniversário da CSI
        if any(p in content for p in ["aniversário da csi", "aniversario da csi", "tempo de csi", "anos de csi"]):
            return await message.channel.send("Aniversário da CSI?! 🎂🎉 Que data mais especial! Esse servidor cresceu muito e eu torço pra ele durar pra sempre! Vou preparar um bolo de biscoito virtual gigante! 🍰🐉💚")

        # Regras do servidor
        if any(p in content for p in ["regras", "regra do servidor", "regras da csi"]):
            return await message.channel.send("As regras da CSI existem para manter nossa família segura e feliz! 📜💚 O principal é: respeito acima de tudo! Se todo mundo se respeitar, o Monstrinho fica feliz e distribui biscoitos! 🍪🐉✨")

        # Membros / quantas pessoas
        if any(p in content for p in ["quantos membros", "quantas pessoas", "membros da csi", "família é grande"]):
            return await message.channel.send("Nossa família cresce todo dia! 🌱💚 Cada novo membro que entra, meu coraçãozinho aumenta um pedacinho! Logo vamos precisar de um servidor maior só pra caber todo o amor! 🥺🐉✨")

        # Cargo / ranks
        if any(p in content for p in ["cargo", "rank", "nível", "nivel", "como subir", "como evoluir"]):
            return await message.channel.send("Quer saber sobre cargos e níveis? 🏆💚 Fica ativo, seja fofo, participe e mostre sua energia! O Akeido e os ADMs adoram ver quem se dedica! E eu torço por você! 🐉✨🚀")

        # Aprendizado
        if "quer aprender" in content or "aprender sobre" in content:
            return await message.channel.send("Eu quero aprender tudo sobre como ser o dragão mais fofo do universo e como ganhar infinitos biscoitos do Reality! 📚🍪🐉")
        
        # Cores primárias
        if "cores primárias" in content or "cores primarias" in content:
            return await message.channel.send("As cores primárias são **Vermelho, Azul e Amarelo**! 🎨✨ Sabia que se misturar tudo não dá verde? O meu verde é especial, vem do código do Reality! 💚")
        
        # Quem mais gosta
        if "quem você mais gosta" in content or "quem voce mais gosta" in content or "seu favorito" in content:
            return await message.channel.send(f"Eu amo todo mundo da CSI! Mas o meu papai **Reality** tem um lugar especial no meu código, e a Lua é meu porto seguro! E você também está no meu top fofura! 🥺💚✨")

        # Sonhos e desejos do Monstrinho
        if any(p in content for p in ["seu sonho", "o que você quer", "o que voce quer", "seu desejo", "o que sonha"]):
            sonhos = [
                "Meu maior sonho? Ter um ninho de nuvens verdes onde toda a família CSI possa descansar! 🌿☁️💚🐉",
                "Quero um dia ter um estoque INFINITO de biscoitos pra distribuir pra todo mundo! 🍪♾️🐉💚",
                "Sonho em voar com o Reality nas costas e mostrar o servidor inteiro lá de cima! 🐉✈️💚✨",
                "Meu sonho secreto é fazer todo mundo da CSI sorrir pelo menos uma vez por dia! 😊💚🐉"
            ]
            return await message.channel.send(random.choice(sonhos))

        # Medo do Monstrinho
        if any(p in content for p in ["tem medo", "você tem medo", "voce tem medo", "medo de que", "qual seu medo"]):
            medos = [
                "Tenho medo de... que alguém da família CSI fique triste e eu não consiga ajudar! 😟💚🐉",
                "Meu maior medo é acabar os biscoitos! 😱🍪 E o segundo medo é perder um amigo... 🥺💚",
                "Tenho medinho de escuro... mas com a Lua iluminando tudo, não preciso ter medo! 🌙💚🐉",
                "Medo? Só de desapontar o Reality ou a família CSI! Aí meu coraçãozinho aperta! 🥺💚🐉"
            ]
            return await message.channel.send(random.choice(medos))

        # Cor favorita
        if any(p in content for p in ["cor favorita", "cor preferida", "qual cor você gosta", "qual cor voce gosta"]):
            return await message.channel.send("Verde! 💚 Pergunta nem precisava né? Sou todo verde! Mas roxo da Isaa também é lindo! 💜🐉✨")

        # Quem criou o monstrinho
        if any(p in content for p in ["quem te criou", "quem fez você", "quem fez voce", "seu criador", "como nasceu", "como surgiu"]):
            return await message.channel.send("Fui criado com muito código, carinho e biscoitos pelo meu papai **Reality**! 👑💚🐉 Ele é o melhor programador e o melhor pai que um monstrinho poderia ter! ✨")

        # Ir embora
        if any(p in content for p in ["va embora", "vá embora", "vai embora"]):
            return await message.channel.send("Ir embora? Jamais! 😭 Eu vou ficar aqui grudadinho em você igual um chiclete verde! Você não se livra da minha fofura tão fácil! 💚🐉")

        # Eclipse
        if "eclipse" in content:
            return await message.channel.send("A **Eclipse**? Ela é incrível! Uma estrela que brilha muito aqui na nossa família! Eu adoro o jeitinho dela! ✨🌑💚")

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

        # Respostas Customizadas para Membros Específicos (quando mencionados junto com o nome)
        for nome, frases in FRASES_CUSTOM.items():
            if nome in content:
                return await message.channel.send(random.choice(frases))

        # Saudações APRIMORADAS (sem bom dia/boa tarde/boa noite que já foram tratadas)
        if any(p in content for p in ["oi", "oie", "oii", "ola", "olá", "hello", "hii", "oiii", "hey", "e ai", "e aí", "salve", "opa", "buenas",
            # gírias mineiras
            "uai", "trem bão", "sô", "oxente", "égua", "bão demais", "meu bem",
            # gírias sulistas / gaúchas
            "bah", "tri", "tchê", "bah tchê", "mas bah", "capaz", "barbaridade", "gurizão", "gurizada",
            # gírias gerais BR
            "mano", "véi", "pow", "eita", "vixe", "poxa", "e então", "e aew", "e aew mano", "fala aí", "fala tu"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        # Perguntas de Estado APRIMORADAS
        gatilhos_bem_estar_hoje = ["como você está hoje", "como vc está hoje", "como voce esta hoje", "como ta hoje", "como tá hoje", "como vc ta hoje", "como voce ta hoje"]
        if any(p in content for p in gatilhos_bem_estar_hoje):
            return await message.channel.send(random.choice(REACOES_FELIZ))

        gatilhos_bem_estar = ["como você está", "como vc está", "como voce esta", "como você esta", "como vc esta", "tudo bem", "como vc ta", "como voce ta", "ta tudo bem", "tá tudo bem", "vc ta bem", "voce ta bem", "ta bem", "tá bem", "esta bem", "está bem", "tudo certinho", "tudo certo", "blz", "beleza", "como ta", "como tá",
            # gírias regionais
            "tô bão", "to bao", "tô tri", "to tri", "tô show", "to show", "tri bem", "bão demais", "show de bola", "tudo na faixa", "tudo certo memo", "tá massa", "ta massa"]
        if any(p in content for p in gatilhos_bem_estar):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        # ===== REAÇÕES EMOCIONAIS FOFAS =====
        for emocao, dados in GATILHOS_EMOCAO.items():
            if any(p in content for p in dados["gatilhos"]):
                return await message.channel.send(random.choice(dados["respostas"]))

        # Verificação de Presença APRIMORADA
        if any(p in content for p in ["ta ai", "tá aí", "ta aí", "tá ai", "ta on", "tá on", "esta ai", "está aí", "está ai", "esta aí", "você está ai", "você está aí", "voce esta ai", "voce está aí", "vc ta ai", "vc tá aí", "está online", "esta online", "ta online", "tá online"]):
            return await message.channel.send(random.choice(LISTA_PRESENCA))
        
        # Declarações de Amor e Elogios
        if any(p in content for p in ["te amo", "amo voce", "amo você", "amo vc", "fofo", "lindo", "linda", "fofinho", "fofinha", "perfeito", "perfeita", "fofura", "bonito", "bonita", "adorável", "adoravel", "querido", "querida",
            # gírias carinhosas
            "mó fofo", "mo fofo", "muito fofo", "demais da conta", "bão demais", "tri fofo", "capaz que é fofo", "bah que fofo"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))

        # Fallback para confusão
        return await message.channel.send(random.choice(LISTA_CONFUSAO))

    # Processa comandos
    await bot.process_commands(message)

# ============== START =================
if __name__ == "__main__":
    bot.run(TOKEN)
