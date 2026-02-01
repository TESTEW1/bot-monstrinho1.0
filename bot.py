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

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= CONFIGURACÃO E IDs =================
TOKEN = os.getenv("TOKEN")
DONO_ID = 769951556388257812

CANAL_GERAL = "💭・chat-geral"
CANAL_LIBERACAO = "✅・chat-staff-liberação"
CANAL_LOG = "❌・palavras-apagadas-bot"
CANAL_TICKET = "🎟️・𝑻𝒊𝒄𝒌𝒆𝒕"
CANAL_EVENTO_CATALOGO = "evento-catalogo"
CANAL_ADVERTENCIAS = "⚠️・advertências"

# GIFs
BANNER_TICKET = "https://i.pinimg.com/originals/5d/92/5d/5d925dd101dba34f341148eace3cfe38.gif"
GIF_NAMORADOS = "https://i.pinimg.com/originals/f5/b8/44/f5b844675a7942e4180bb9960c3fe319.gif"
GIF_CATALOGO = "https://i.pinimg.com/originals/0a/1f/86/0a1f869c296b0c30454ffb56397b90fb.gif"

# Cargos
CARGO_MEMBRO_NOVO = "Membro Novo. 🦇"
CARGO_MEMBROS = "Membros. 🦇"
CARGO_MODERADOR = "Moderador. 🦇"
CARGO_RECRUTADOR = "Recrutador. 🦇"
CARGO_ANJO = "Anjo. 🦇"

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
    "O Monstrinho aprova essa amizade! Toma um biscoitinho, {alvo}! 🍪🐉💚",
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

# ================= RESPOSTAS PARA MEMBROS (MAIS DE 6 CADA) =================

FRASES_CUSTOM = {
    "athena": [
        "ATHENAAAA! 😭💚 Minha fã número 1!! *pula de alegria*",
        "Espera, é a Athena? AI MEU DEUS, me dá um autógrafo também! 😳💚✨",
        "Pra Athena eu dou até meu biscoito favorito! 🍪🐉💚",
        "A Athena chegou! O brilho do servidor aumentou 1000%! ✨🐉",
        "Athena, você é a rainha do meu coração de dragão! 👑💚",
        "Todo mundo parado! A Athena postou? EU PRECISO VER! 🏃‍♂️💨💚",
        "Athena, você é mais doce que mel de abelha mágica! 🍯🐉✨"
    ],
    "izzy": [
        "IZZY!! 💖 Outra fã maravilhosa! O Monstrinho te amaaa!",
        "Izzy, vem cá ganhar um abraço esmagador de Monstrinho! 🫂💚",
        "Meu coração de monstrinho pula quando a Izzy aparece! 🐉✨",
        "Izzy, você é a definição de fofura na CSI! 🌸🐉💚",
        "Se a Izzy está feliz, o Monstrinho está radiante! ☀️💚",
        "Izzy, trouxe flores virtuais pra você! 💐🐉✨",
        "A energia da Izzy é o que carrega minhas baterias de dragão! 🔋💖"
    ],
    "lua": [
        "A Lua quer ser minha amiga? 🌙 EU QUERO MUITO! 😭💚",
        "Lua, você acha que eu tenho medo de você? Bobinha! No começo eu era tímido, mas o Reality me explicou que você é nosso porto seguro! 🥺💚",
        "Vice-líder Lua, você é o conforto em forma de pessoa! O Reality me disse pra cuidar bem de você porque você é preciosa! ✨🐉",
        "A Lua ilumina o chat igualzinho à lua do céu! Eu não tenho medo, eu tenho é muito amor por você! 🌙✨🐉",
        "Lua, você é a estrela mais brilhante da nossa constelação CSI! Saiba que você é importante demais pra todos nós! ⭐💚",
        "Nada de tristeza quando a Lua está por perto! Eu me sinto tão seguro com você agora... 🌙🐲💖",
        "Lua, você é simplesmente mágica! O Reality me ensinou que seu coração é gigante e hoje eu só quero seu abraço! ✨✨"
    ],
    "destiny": [
        "DESTINYYYY! ✨ O destino nos uniu na CSI! 🐉💚",
        "Destiny, você é uma peça fundamental desse quebra-cabeça fofo! 🧩💚",
        "Salve pro Destiny! O Monstrinho fica muito feliz quando você aparece! 🐉✨",
        "Destiny, você é o herói que a gente precisava! 🛡️💚🐉",
        "O destino brilhou mais forte hoje porque o Destiny chegou! ✨🐲",
        "Destiny, aceita um abraço de dragão? 🫂🐉💚",
        "Você é pura inspiração, Destiny! 🌟🐉"
    ],
    "jeff": [
        "JEFF!! 🕵️‍♂️ O cara que manja tudo! 🐉💚",
        "Jeff, vamos patrulhar a CSI e garantir que todos recebam biscoitos? 🍪🐉",
        "O Jeff é fera! O Monstrinho te admira muito, parceiro! 😎💚",
        "Jeff, você é o cérebro e eu sou a fofura! Time perfeito! 🧠🐉💚",
        "Respeita o Jeff! Ele é o mestre da patrulha! 🫡💚✨",
        "Jeff, me ensina a ser descolado igual você? 😎🐉",
        "O cara, o mito, a lenda... JEFF! 🐲🔥"
    ],
    "isaa": [
        "ISAAAA! ✨ A energia dela é contagiante! 🐉💚",
        "Isaa, sabia que você brilha tanto quanto meus pelinhos verdes? 🥺✨",
        "Vem cá Isaa, o Monstrinho preparou um lugar quentinho pra você! 🫂🐉",
        "Isaa, sua alegria é o meu combustível favorito! ⛽💖🐉",
        "Todo mundo sorrindo, porque a Isaa chegou! 😄💚✨",
        "Isaa, você é um raio de sol em forma de gente! ☀️🐲",
        "Minha melhor amiga Isaa é a melhor de todas! 🎀🐉💚"
    ],
    "psico": [
        "PSICOOO! 🧠✨ O gênio da CSI! 🐉💚",
        "Psico, você é tão inteligente que às vezes eu acho que você lê meus códigos! 😳💻🐉",
        "Um salve pro Psico! O Monstrinho te admira demaaaais! 😎✨",
        "Psico, traduz o que os humanos falam pra mim? Você sabe tudo! 🧠🐲💚",
        "O mestre Psico apareceu! Que honra para meus circuitos! 🙇‍♂️🐉✨",
        "Se o Psico falou, tá falado! O Monstrinho concorda! ✅💚",
        "Psico, você é o maior crânio desse servidor! 💀💎💚"
    ],
    "felipeta": [
        "Felipeta... 😤 Esse outro mascote de novo? O brilho verde é SÓ MEU!",
        "O Felipeta pode ser bonitinho, mas eu sou muito mais fofo! 🐉🔥",
        "Rivalidade de mascotes ligada! ⚔️🐉 O trono é meu!",
        "Felipeta, por favor, não tente roubar meus fãs hoje, tá? 💅💚",
        "O Felipeta é legal... mas meu bafo de fogo é mais brilhante! 🐉🔥✨",
        "Um dragão contra um... o que é o Felipeta mesmo? Brincadeira! 😂💚",
        "Luta de fofura! Eu vs Felipeta! Quem ganha? (Eu, claro!) 🐲🏆"
    ],
    "nine": [
        "NINEEE! 9️⃣✨ A perfeição em forma de pessoa! 🐉💚",
        "Nine, você é nota dez, mas seu nome é Nine! Que confusão fofa! 😵‍💫💖🐉",
        "Um abraço especial para o Nine, o dono da vibe mais incrível! 🫂✨",
        "Nine, sabia que você é meu número favorito? 9️⃣🐲💚",
        "Salve Nine! O Monstrinho fica todo bobo quando você fala comigo! 🥺✨",
        "Nine, você é o equilíbrio perfeito da CSI! ⚖️🐉💚",
        "O Nine chegou! Preparem os confetes! 🎉🐉✨"
    ]
}

# ============== DADOS E PALAVRAS PROIBIDAS =================
tickets = {}
avisos_usuarios = {}
PALAVRAS_PROIBIDAS = [
    "porra","caralho","merda","bosta","puta","puto","vadia","desgraça","idiota",
    "burro","imbecil","otário","retardado","lixo","nojento","arrombado","viado",
    "bicha","piranha","vai se fuder","vai se foder","vai tomar no cu","tomar no cu",
    "filho da puta","se mata","se fode","fdp","vsf","krl","pqp","prr","tmnc",
    "buceta","carai","karalho"
]

# ============== VIEWS (TICKETS E MODERAÇÃO) =================

class LiberarCastigoView(discord.ui.View):
    def __init__(self, membro_id: int):
        super().__init__(timeout=None)
        self.membro_id = membro_id

    @discord.ui.button(label="🔓 Remover Castigo", style=discord.ButtonStyle.success, custom_id="remover_castigo")
    async def remover(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not interaction.user.guild_permissions.moderate_members:
            return await interaction.response.send_message("❌ Apenas staff!", ephemeral=True)
        guild = interaction.guild
        membro = guild.get_member(self.membro_id)
        if membro:
            await membro.timeout(None)
            avisos_usuarios[self.membro_id] = 0
            await interaction.response.send_message(f"✅ Castigo de {membro.mention} removido!", ephemeral=True)

class AprovarMembroView(discord.ui.View):
    def __init__(self, membro_id: int):
        super().__init__(timeout=None)
        self.membro_id = membro_id

    @discord.ui.button(label="✅ Liberar", style=discord.ButtonStyle.success, custom_id="liberar_membro")
    async def liberar(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        membro = guild.get_member(self.membro_id)
        if not membro: return
        cargos = [discord.utils.get(guild.roles, name=CARGO_MEMBRO_NOVO), discord.utils.get(guild.roles, name=CARGO_MEMBROS)]
        for c in cargos:
            if c: await membro.add_roles(c)
        canal_geral = discord.utils.get(guild.text_channels, name=CANAL_GERAL)
        if canal_geral: await canal_geral.send(f"AAAA 😭🐲💚 {membro.mention} foi LIBERADO!")
        await interaction.response.send_message("✅ Aprovado!", ephemeral=True)

    @discord.ui.button(label="⏳ Aguardar", style=discord.ButtonStyle.secondary, custom_id="aguardar_membro")
    async def aguardar(self, interaction: discord.Interaction, button: discord.ui.Button):
        membro = interaction.guild.get_member(self.membro_id)
        if membro: 
            try: await membro.send("Oii neném 😭🐲💚 sua entrada tá sendo analisada pela staff! 💚✨")
            except: pass
        await interaction.response.send_message("🕒 Em análise", ephemeral=True)

    @discord.ui.button(label="❌ Recusar", style=discord.ButtonStyle.danger, custom_id="recusar_membro")
    async def recusar(self, interaction: discord.Interaction, button: discord.ui.Button):
        membro = interaction.guild.get_member(self.membro_id)
        if membro: await membro.kick()
        await interaction.response.send_message("❌ Recusado.", ephemeral=True)

class FecharTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="🔒 Fechar Ticket", style=discord.ButtonStyle.danger, custom_id="fechar_ticket")
    async def fechar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("🔒 Fechando em 5s...", ephemeral=True)
        await asyncio.sleep(5)
        await interaction.channel.delete()

class TicketSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="🛠️ Suporte", value="suporte"),
            discord.SelectOption(label="🚨 Denúncia", value="denuncia"),
            discord.SelectOption(label="👮 Falar com Staff", value="staff"),
            discord.SelectOption(label="💘 Evento dos Namorados", value="namorados"),
            discord.SelectOption(label="📸 Evento Catálogo", value="catalogo"),
            discord.SelectOption(label="📣 Líder de Torcida", value="lider_torcida"),
        ]
        super().__init__(placeholder="🎟️ Selecione o tipo de ticket", options=options, custom_id="ticket_select_menu")

    async def callback(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user
        tipo = self.values[0]
        overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False), user: discord.PermissionOverwrite(view_channel=True, send_messages=True)}
        canal = await guild.create_text_channel(name=f"🎟️┃{tipo}-{user.name}".lower(), category=interaction.channel.category, overwrites=overwrites)
        tickets[canal.id] = {"user": user.id, "tipo": tipo}
        await canal.send(f"🎟️ **TICKET ABERTO**\n👤 {user.mention}", view=FecharTicketView())
        await interaction.response.send_message("✅ Ticket criado!", ephemeral=True)

class TicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TicketSelect())

# ============== EVENTOS PRINCIPAIS =================

@bot.event
async def on_ready():
    print(f"🐉 Monstrinho ONLINE como {bot.user}!")
    bot.add_view(TicketView())
    bot.add_view(FecharTicketView())
    bot.add_view(LiberarCastigoView(0))
    await bot.change_presence(activity=discord.Game(name="Amando meu criador Reality! 💚"))

@bot.event
async def on_member_join(member):
    canal_lib = discord.utils.get(member.guild.text_channels, name=CANAL_LIBERACAO)
    if canal_lib:
        await canal_lib.send(f"🔔 **NOVO MEMBRO**\n👤 {member.mention}", view=AprovarMembroView(member.id))

@bot.event
async def on_message_delete(message):
    if message.author.bot: return
    canal_log = discord.utils.get(message.guild.text_channels, name=CANAL_LOG)
    if canal_log:
        embed = discord.Embed(title="🗑️ Mensagem Apagada", color=discord.Color.red())
        embed.add_field(name="Autor:", value=message.author.mention)
        embed.add_field(name="Conteúdo:", value=message.content or "Mídia")
        await canal_log.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author.bot: return

    content = message.content.lower()

    # --- LÓGICA DE DIÁLOGO E REAÇÕES ---
    if bot.user in message.mentions or "monstrinho" in content:
        # Apresentação
        if content.strip() in [f"<@{bot.user.id}>", "monstrinho"]:
            apresentacao = (f"🐉 **OIIIII MEU AMOOOOR!** 💚✨\n\nEu sou o **Monstrinho 1.0**, o mascote da **CSI**! 🕵️‍♂️💚\n"
                            f"Fui criado pelo **Reality**! 👑✨\n✨ *CSI é minha casa, o Reality é meu criador!* ✨")
            return await message.channel.send(apresentacao)

        # Respostas Customizadas para Membros
        for nome, frases in FRASES_CUSTOM.items():
            if nome in content:
                return await message.channel.send(random.choice(frases))

        # Saudações, Estado e Biscoitos
        if any(p in content for p in ["oi", "oie", "bom dia", "boa tarde", "boa noite"]):
            return await message.channel.send(random.choice(LISTA_SAUDACOES))
        
        if any(p in content for p in ["como você está", "tudo bem", "como vc ta"]):
            return await message.channel.send(random.choice(LISTA_ESTADO))

        if "biscoito" in content:
            if any(p in content for p in ["me de", "me da", "quero"]):
                return await message.channel.send(random.choice(REACOES_BISCOITO_PROPRIO))
            if "para" in content or "pra" in content:
                outras_mencoes = [m for m in message.mentions if m != bot.user]
                alvo = outras_mencoes[0].mention if outras_mencoes else "alguém especial"
                return await message.channel.send(random.choice(REACOES_DAR_BISCOITO).format(autor=message.author.mention, alvo=alvo))
        
        if any(p in content for p in ["te amo", "amo voce", "fofo", "lindo"]):
            return await message.channel.send(random.choice(REACOES_FOFAS))
        
        if "reality" in content:
            return await message.channel.send("O Reality é meu papai mestre! Eu amo ele! 👑🐉💚")

    # --- LÓGICA DE TICKET/CATÁLOGO ---
    if message.channel.id in tickets:
        info = tickets.get(message.channel.id)
        if info["tipo"] == "catalogo" and message.author.id == info["user"] and message.attachments:
            canal_evento = discord.utils.get(message.guild.text_channels, name=CANAL_EVENTO_CATALOGO)
            if canal_evento:
                await canal_evento.send(f"📸 Foto de {message.author.mention}")
                for at in message.attachments: await canal_evento.send(file=await at.to_file())
            await message.channel.delete()
            return

    # --- LÓGICA DE CENSURA/PUNIÇÃO ---
    if any(palavra in content for palavra in PALAVRAS_PROIBIDAS):
        await message.delete()
        uid = message.author.id
        avisos_usuarios[uid] = avisos_usuarios.get(uid, 0) + 1
        canal_adv = discord.utils.get(message.guild.text_channels, name=CANAL_ADVERTENCIAS)
        
        if avisos_usuarios[uid] == 1:
            await message.channel.send(f"⚠️ {message.author.mention} você recebeu o **1º AVISO**. Xingar não pode! 😭💚")
        elif avisos_usuarios[uid] == 2:
            await message.channel.send(f"⚠️ {message.author.mention} você recebeu o **2º AVISO**. Cuidado! 😡🐲")
        elif avisos_usuarios[uid] >= 3:
            try:
                await message.author.timeout(timedelta(days=1), reason="3 Advertências.")
                if canal_adv: await canal_adv.send(f"🚨 **PUNIÇÃO**: {message.author.mention} silenciado.", view=LiberarCastigoView(uid))
                await message.channel.send(f"❌ {message.author.mention} foi silenciado por 1 dia! 🐲🔥")
            except: pass
        return

    await bot.process_commands(message)

# ============== START =================
bot.run(TOKEN)
