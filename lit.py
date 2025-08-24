import streamlit as st
import streamlit.components.v1 as components
import os
from PIL import Image
import base64

def exibir_pdf(pdf_path):
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{base64_pdf}" '
            'width="100%" height="600" type="application/pdf"></iframe>',
            unsafe_allow_html=True
        )
    else:
        st.error(f"PDF não encontrado: {pdf_path}")

CODIGO_ACESSO = "MEUCODIGO123"  # Troque para o código que vai enviar na Hotmart

codigo_digitado = st.text_input("Digite seu código de acesso:", type="password")


def audio_embed(youtube_url):
    video_id = youtube_url.split("v=")[-1]
    embed_url = f"https://www.youtube.com/embed/{video_id}?start=0"
    st.markdown(
        f"""
        <iframe width="100%" height="40" src="{embed_url}" frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen></iframe>
        """,
        unsafe_allow_html=True,
    )

if codigo_digitado == CODIGO_ACESSO:

    # Menu de opções
    menu = ["História", "Ritmos", "Intervalos","Acordes & Arpejos", "Escalas Naturais", "Campos Harmônicos", "Recursos Adicionais"]
    choice = st.sidebar.selectbox("Escolha uma função", menu)

    if choice == "História":
        st.title("História da Música 🎼")

        st.markdown("""
        A música é uma das expressões mais antigas e universais da humanidade. Desde os primórdios, os seres humanos se afeiçoaram aos sons — não apenas como ruído do ambiente, mas como forma de organizar a experiência emocional, criar vínculos sociais e dar sentido ao mundo ao seu redor.

    A batida do coração, o som da respiração, o eco das cavernas, o ritmo dos passos: todos esses elementos naturais já traziam padrões que o ser humano começou a perceber e imitar. Ao bater pedras, soprar por ossos ou entoar sons com a voz, nossos ancestrais descobriram que certas vibrações causavam emoções e *transes mentais*. Assim, os sons poderiam emergir como uma extensão do corpo e mente.
        """)

        st.header("🪨 A Música na Pré-História")
        st.markdown("""
        Durante o período pré-histórico, a música não era feita para entretenimento como conhecemos hoje. Ela cumpria funções essenciais para a vida em comunidade, sendo usada em:

        - **Rituais mágicos e religiosos**: Acreditava-se que sons e ritmos podiam invocar espíritos, curar doenças, atrair chuva ou garantir sucesso na caça.
        - **Comunicação à distância**: Por meio de tambores e cantos, tribos podiam se comunicar entre grupos distantes.
        - **Expressão emocional e identidade coletiva**: A música ajudava a fortalecer os laços do grupo e transmitir sentimentos, histórias e tradições oralmente.

        Os instrumentos eram feitos de materiais disponíveis na natureza, como ossos, pedras, madeira e peles de animais. Alguns exemplos:

        - **Percussão corporal** (bater palmas, estalar os dedos, pisar no chão)
        - **Flautas de osso**
        - **Tambores com pele de animal**
        - **Apitos e chocalhos feitos com sementes e conchas**

        Não havia uma linguagem musical escrita ou regras harmônicas, mas já se percebia uma organização rítmica e melódica intencional. A música era uma linguagem instintiva e coletiva — ligada diretamente à sobrevivência, à espiritualidade e à cultura.
    """)

        # ANTIGUIDADE
        st.header("🏛️ Antiguidade")
        st.markdown("""
    Com o surgimento das primeiras civilizações, a música passou a ocupar um papel ainda mais estruturado nas sociedades da Antiguidade. Egípcios, sumérios, gregos, hebreus, indianos e chineses desenvolveram formas musicais ligadas à religião, à educação, à guerra e ao entretenimento.
    """)
        
        st.markdown("""
        **🎼 Características técnicas:**
        - Uso de escalas gregas (modos)
        - Música monofônica e ritualística
        - Instrumentação rudimentar (lira, aulos, harpa)""")

        st.markdown("""
    No **Egito Antigo**, a música era parte essencial dos cultos religiosos e cerimônias funerárias. Instrumentos como harpas, flautas e tamborins acompanhavam cantos dedicados aos deuses e aos faraós.

    Na **Grécia Antiga**, a música era considerada uma arte divina, ligada à matemática, à filosofia e à moral. Pitágoras descobriu proporções harmônicas entre sons, e pensadores como Platão e Aristóteles discutiram seu poder sobre a alma e a sociedade. Os gregos usavam a lira, a cítara e o aulos (instrumento de sopro) em festivais, teatro e educação.

    Na **Roma Antiga**, a música era muito influenciada pelos gregos e usada em banquetes, arenas, templos e exércitos. Embora com menor preocupação filosófica, os romanos expandiram o uso da música como forma de espetáculo e propaganda imperial.
    """)


        st.subheader("**- Terpandro (século VII a.C)** ")
        st.markdown("Foi um célebre poeta lírico e citharode (tocado de cítara, tipo de lira) da Antiga Grécia, ativo por volta do século VII a.C. Segundo Strabo e Plutarco, foi ele quem aumentou as cordas da lira de quatro para sete, dando forma ao que viria a se chamar kithara. Embora suas obras não tenham sobreviveram completas, fragmentos são citados por autores antigos, e sua influência perdurou – consideram-no o primeiro nome certo da história musical da Grécia ")

        st.subheader("**- Pitágoras (século VI a.C.)**")

        st.markdown("""
        Descobriu as relações matemáticas entre os sons — um marco fundamental que ajudou a fundar a base da teoria musical ocidental. Pitágoras percebeu que os sons agradáveis (ou consonantes) tinham relações diretas com o comprimento da corda que vibrava. Fazendo o experimento com um monocórdio, ou seja, um instrumento formado por uma única corda esticada sobre uma caixa de ressonância marcada com uma régua com marcações do comprimento da corda junto de um cavalete móvel que pode dividir a corda em diferentes posições. 
        
        Com esse experimento, Pitágoras obteve o seguinte resultado: 

            - Quando uma corda é dividida ao meio (1:2), produz um som uma oitava acima do som original.

            - Dividida na razão 2:3, resulta em uma quinta justa.

            - Na razão 3:4, uma quarta justa.

        """)


        st.subheader("**- Mesomedes de Creta (século II d.C)**")
        st.markdown("""Foi um importante poeta lírico e compositor grego do início do século II d.C. Ele viveu durante o período de Hadrian e foi liberto desse imperador, servindo também durante Antonino Pio. Mesomedes era cantor e tocador de kithara, escrevendo poemas — ao todo cerca de 15 — em grego antigo, dos quais pelo menos quatro acompanham a notação musical original, entre elas *Hymn to Nemesis*, *Hymn to the Sun*, *Prayer to Calliope and Apollo*, *Prayer to the Muse*.

Ouça *Hymn to the Sun*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3")



        # IDADE MÉDIA
        st.header("🕍 Idade Média (500–1400)")

        st.markdown("""
    Na Idade Média (aproximadamente do século V ao XV), a música europeia foi profundamente influenciada pela Igreja Católica, que a utilizava como instrumento de fé, liturgia e poder. O **canto gregoriano** — melódico, monofônico e em latim — dominava os mosteiros e catedrais, servindo para elevar o espírito e acompanhar as orações.
    """)
        
        st.markdown("""
        **🎼 Características técnicas:**
        - Canto gregoriano (monofônico e modal)
        - Desenvolvimento da notação musical
        - Polifonia nascente (Notre-Dame)
    """)
        
        st.markdown("""
    Nesse período, os monges desenvolveram os primeiros sistemas de **notação musical**, permitindo registrar e transmitir músicas com mais precisão. Guido d’Arezzo, por exemplo, criou a base do que viria a ser a pauta musical moderna e a **mão guidoniana**, uma técnica visual para ensinar os sons.

    Fora dos muros da Igreja, também floresceu a música **profana**. Trovadores, jograis e menestréis compunham e cantavam canções sobre amor, guerras e feitos heroicos, muitas vezes acompanhados por alaúdes, harpas e flautas. Essa música ajudava a preservar histórias e a entreter os nobres e o povo.

    A música medieval foi o ponto de partida para a polifonia (várias vozes simultâneas), que surgiria mais intensamente nos séculos finais da Idade Média, abrindo caminho para as inovações da Renascença.
    """)

    
        st.subheader("**- Guido d’Arezzo (991 – 1033)**")
        st.markdown("""Foi um monge beneditino italiano e um dos maiores teóricos musicais da Idade Média. Não é reconhecido por composições musicais como outros, mas sim por sua enorme contribuição teórica e pedagógica à música medieval ocidental. Ele foi um monge beneditino que revolucionou o ensino da música com invenções de notações e composições que usamos até hoje, considerado o *pai da notação musical moderna* e um dos grandes inovadores da pedagogia musical ocidental.                 
                    """)
        
        st.subheader("**- Hildegard von Bingen (1098–1179)**")
        st.markdown("""Monja beneditina, mística, médica, filósofa natural, compositora e visionária, ela viveu no Sacro Império Romano-Germânico e é considerada uma das primeiras compositoras da história da música ocidental cujas obras sobreviveram com autoria confirmada, sendo uma das mais importantes compositoras da Idade Média. Hildegard compôs mais de 70 obras litúrgicas (cânticos, hinos, responsórios) reunidas no ciclo *Symphonia armoniae celestium revelationum*. 

Ouça *De Spiritu Sancto*:
        """)

        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344803/hwynylkgkytdtbriavxh.mp3")


        st.subheader("**- Leonin (1150–1201)**")
        st.markdown(""" monge ou cônego ligado à Catedral de Notre-Dame de Paris, foi um dos primeiros compositores a usar a notação moderna e é considerado o primeiro grande compositor de polifonia na história da música ocidental. Foi sucedido por Perotin, que desenvolveu ainda mais a técnica polifônica, escrevendo músicas a 3 e 4 vozes.

Ouça *Nostrum Organum Duplum*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751392698/lggvrlwdh2ij3oc5ysbw.mp3")


        # RENASCIMENTO
        st.header("🎨 Renascimento (1400–1600)")

        st.markdown("""
    Durante o Renascimento (séculos XV e XVI), a música acompanhou o espírito humanista da época, buscando equilíbrio, clareza e expressividade. Com o avanço da imprensa e o redescobrimento das artes clássicas, os compositores passaram a valorizar mais a **emoção humana**, a **beleza sonora** e a **técnica polifônica** — ou seja, várias vozes independentes cantando em harmonia.
        """)

        
        st.markdown("""
        **🎼 Características técnicas:**
        - Polifonia rica e imitativa
        - Equilíbrio entre vozes
        - Música vocal e instrumental se desenvolvendo paralelamente

    """)
        st.markdown("""
    A música sacra ainda era muito presente, com missas e motetos mais elaborados e refinados. No entanto, a música **profana** ganhou força, com madrigais, chansons e villanellas tratando de temas cotidianos, amorosos e até humorísticos.

    Compositores como **Josquin des Prez**, **Palestrina**, **Orlando di Lasso** e **William Byrd** foram mestres em criar texturas vocais ricas, onde a música seguia de perto os sentimentos e significados do texto.

    Instrumentos como o alaúde, o cravo e a viola da gamba se popularizaram, e a música instrumental começou a ganhar espaço próprio — preparando o terreno para os grandes concertos e sonatas do período barroco.

    O Renascimento marcou uma transição da música como ferramenta da fé para a música como forma de arte e expressão individual.
    """)

        st.subheader("**- Josquin des Prez (1455–1521)**")
        st.markdown("""
        Foi um dos compositores mais influentes do Renascimento. Nascido possivelmente na região da atual fronteira entre França e Bélgica (então parte dos Países Baixos borgonheses), ele é considerado o maior compositor de sua época, comparado frequentemente a figuras como Michelangelo ou Leonardo da Vinci, mas na música. Josquin se destacou pela inovação e refinamento da polifonia vocal, isto é, várias vozes cantando melodias diferentes que se combinam harmonicamente. 
    

        Ouça *Ave Maria ... virgo serena*:
        """)

        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751486334/pcvqhxhbll6eacvxtlv5.mp3")


        st.subheader("**- Giovanni Palestrina (1525–1594)** ")
        st.markdown("""Palestrina foi um compositor italiano do Renascimento, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais. Seu estilo serviu como modelo pedagógico no estudo de contraponto, sendo estudado até hoje em conservatórios

Ouça *Missa Papae Marcelli*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751488772/g0cuwgdeglakntyy6rgc.mp3")


        st.subheader("**- Orlando di Lasso (1532–1594)** ")
        st.markdown("""foi um compositor francês do Renascimento, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

Ouça *Lagrime di San Pietro: I. Il magnanimo Pietro*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751497992/cwezwqiiugdezve7uecr.mp3")

        # BARROCO
        st.header("🎻 Barroco (1600–1750)")

        st.markdown("""
    O período Barroco foi uma era de grande inovação na música. Marcado pelo exagero, contraste e emoção intensa, o estilo barroco refletia o esplendor das cortes e da Igreja. A música tornou-se mais dramática, expressiva e ornamentada, com destaque para a criação de formas e gêneros que influenciariam toda a música ocidental posterior.
        """)

        st.markdown("""
        **🎼 Características técnicas:**
        - Baixo contínuo, uso de tonalidade maior/menor
        - Contraponto elaborado
        - Nasce a ópera, oratório e concerto
        """)


        st.markdown("""
    Foi nesse período que surgiram a **ópera**, o **concerto**, a **sonata** e a **fuga**. A música instrumental ganhou status de igualdade com a vocal, com compositores explorando a virtuosidade dos instrumentos e a riqueza das combinações sonoras.

    O **baixo contínuo** (acompanhamento harmônico constante) passou a ser a base das composições, e a **tonalidade** (sistema de escalas maior e menor) se consolidou como linguagem musical dominante.

    Grandes nomes como **Johann Sebastian Bach**, **George Frideric Handel**, **Antonio Vivaldi** e **Claudio Monteverdi** criaram obras-primas que combinavam técnica, emoção e espiritualidade.

    A música barroca procurava mover o ouvinte, exaltando sentimentos e criando atmosferas grandiosas — seja nos palácios, nas igrejas ou nos teatros.
    """)


        st.subheader("**- Claudio Monteverdi (1567–1643)**")
        st.markdown("""Sua carreira reflete a transformação profunda que a música europeia sofria ao sair do Renascimento e caminhar para o Barroco. Monteverdi foi o primeiro a aplicar emoção intensa à música polifônica, criando o que ele chamou de "Seconda Prattica" (segunda prática), onde a música serve ao texto, não o contrário. Monteverdi foi um dos primeiros compositores a escrever óperas completas e, por isso, é considerado como o pai da ópera e o pioneiro do Barroco. 

Ouça uma de suas óperas mais famosas *L`Orfeo*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")


        st.subheader("**- Antonio Vivaldi (1678-1741)**")
        st.markdown("""Um dos mais influentes músicos do Barroco e foi pioneiro no desenvolvimento do concerto instrumental, especialmente o concerto solo para violino. Ele escreveu mais de 500 concertos, além de óperas, cantatas, obras sacras e música de câmara. Como exímio violinista, suas obras exploram as possibilidades técnicas do instrumento, abrindo caminho para o concerto como forma de exibição da habilidade do solista. 
                    
Sua obra mais famosa, *Quatro Estações*, parte de um conjunto de 12 concertos onde Cada uma das estações (Primavera, Verão, Outono, Inverno) é representada por um concerto para violino. Cada peça é acompanhada de um soneto (provavelmente escrito pelo próprio Vivaldi) que descreve as cenas e sensações que a música retrata — como pássaros cantando, tempestades, brisa do outono, frio cortante etc.

Ouça *Four Seasons*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752259605/nhxy9zxf4qdyn9y8c8f3.mp3")

        st.subheader("**- Johann Sebastian Bach (1685-1750)** ")

        st.markdown("""É considerado um dos maiores gênios da história da música ocidental. Ele foi o ápice do estilo barroco, sintetizando com maestria todas as técnicas musicais de sua época — especialmente o contraponto, em que diferentes linhas melódicas se entrelaçam de forma complexa e harmônica. 
                    
Bach levou à perfeição gêneros como a fuga, a cantata, o concerto e a missão coral, criando obras que uniam profundidade espiritual, rigor técnico e beleza emocional. Sua música é ao mesmo tempo racional e sensível, estruturada e expressiva.
        
Uma de suas principais obras, *O Cravo Bem Temperado*, é uma coleção de prelúdios e fugas dividido em dois livro contendo 24 pares de peças — um prelúdio seguido de uma fuga — em todas as tonalidades maiores e menores, totalizando 48 peças ao todo.

O principal propósito de *O Cravo Bem Temperado* era mostrar a versatilidade do sistema tonal (uso das escalas maiores e menores) em todos os tons possíveis. Na época, existia um desafio técnico: a afinação dos instrumentos de teclado. Bach demonstrou que, com um sistema de afinação "temperado", era possível tocar em todas as tonalidades sem soar desafinado. Esse sistema temperado é o precursor do sistema de afinação moderna, em que o teclado é dividido de forma equilibrada para permitir modulações sem problemas sonoros.  
                    
Ouça uma de suas produções *Prelude and Fugue: No. 18 in G-Sharp Minor, BWV 887*:
                    """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752254587/bmf9qfbd5qqpjmdcncgn.mp3")


        # CLÁSSICO
        st.header("🎼 Clássico (1750–1820)")

        st.markdown("""
    O período Clássico buscou simplicidade, clareza e equilíbrio — em contraste com o estilo ornamentado do Barroco. Inspirados pelos ideais do Iluminismo, os compositores valorizavam a razão, a ordem e a forma musical bem definida.
        """)

        st.markdown("""
    Foi nesse contexto que se consolidaram gêneros como a **sinfonia**, o **quarteto de cordas** e a **sonata**, além da evolução da **forma sonata**, usada como estrutura principal nos movimentos de muitas obras instrumentais.

    """)

        st.markdown("""
        **🎼 Características técnicas:**
        - Harmonia tonal com progressões previsíveis e cadências claras.
        - Uso da forma sonata como estrutura central.
        - Desenvolvimento da orquestra clássica, com seções definidas de cordas, sopros e percussão leve.
                    
        """)

        st.markdown("""
    A música tornou-se mais acessível, voltada não só à aristocracia, mas também à nova burguesia em ascensão. A orquestra se estabilizou em sua formação, e o **piano** substituiu o cravo como instrumento dominante nos salões e nas casas.

    Ao contrário do Barroco, onde as óperas falavam de mitologia e reis, o período clássico trouxe personagens comuns e situações sociais reais, como em As Bodas de Fígaro (Mozart), que mostra criados desafiando senhores.

    """)

        st.subheader("**- Wolfgang Amadeus Mozart (1756–1791)** ")
        st.markdown("""
        Considerado um gênio precoce, ele marcou profundamente o período clássico e influenciou gerações com sua musicalidade intuitiva, sua riqueza expressiva e seu domínio técnico absoluto.
                    
    Mozart é o modelo do Classicismo musical: equilíbrio formal, clareza melódica e perfeição harmônica. Mas sua música vai muito além da beleza — ela é profundamente expressiva, emocionalmente inteligente e, muitas vezes, teatral e humana.
                    
    Mozart escreveu mais de 20 óperas e 40 sinfonias, sendo que várias delas são pilares do repertório até hoje. Foi o primeiro a trazer personagens realistas, com falhas e sentimentos humanos, para o palco da ópera. Antes, os personagens eram idealizados ou míticos. Mozart é considerado por muitos o maior compositor da história ocidental pela sua habilidade de unir complexidade técnica e profunda humanidade.
        
    Ouça uma de suas sinfonias *Symphony No. 25 in G minor*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752286273/bvzu89jgalpsqucqo3gt.mp3")

        st.subheader("**- Ludwig van Beethoven (1770–1827)**")
        st.markdown("""Redefiniu o papel da música, transformando-a de uma arte cortesã e decorativa em um veículo de expressão pessoal, emoção profunda e ideia filosófica. Ele é a figura de transição entre o Classicismo e o Romantismo, e sua vida e obra são uma jornada intensa de luta, superação, inovação e legado eterno.
                    
Escreveu em praticamente todos os gêneros musicais da época: sinfonias, sonatas, quartetos, concertos, óperas e música coral. Mas o que o diferencia não é a quantidade, e sim o impacto profundo de sua arte. 
                    
Beethoven via a música como drama puro, e é o primeiro compositor a tratar a estrutura musical como uma narrativa emocional. Isso influenciou profundamente os românticos: temas como luta, superação, liberdade e transcendência se tornaram o novo padrão.

Ouça uma de suas obras *Symphony No. 5, Op. 67*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752287831/uadibd8ti2vxuybt0hwi.mp3")

        # ROMÂNTICO
        st.header("🎭 Romântico (1820–1900)")

        st.markdown("""
    O período Romântico foi marcado pela valorização da emoção, da imaginação e da subjetividade. A música tornou-se uma forma profunda de expressão individual, refletindo paixões, dramas, sonhos e até revoltas sociais.

    Os compositores romperam com as regras rígidas do Classicismo e buscaram mais **liberdade formal**, **variedade de timbres** e **intensidade emocional**. A orquestra cresceu em tamanho e em cores sonoras, permitindo paisagens sonoras mais ricas e dramáticas.
                    
                    """)
        
        st.markdown("""
        **🎼 Características técnicas:**
        - Harmonia cromática, melodia expressiva
        - Nacionalismo e individualismo
        - Orquestras maiores e mais dramáticas
    """)
        
        st.markdown("""

    Temas como **amor trágico**, **natureza**, **heroísmo**, **nacionalismo** e **misticismo** tornaram-se comuns. Muitos músicos usaram suas obras para expressar sentimentos patrióticos ou inspirados em lendas e literaturas de seus países.

    A música romântica fala direto ao coração — é intensa, pessoal e muitas vezes arrebatadora, buscando tocar o ouvinte em sua alma mais profunda.
    """)

        st.subheader("**- Frédéric Chopin (1810–1849)**")

        st.markdown("""
    Nascido na Polônia e ativo principalmente em Paris, ele é considerado o poeta do piano por sua habilidade ímpar de expressar emoções profundas por meio desse instrumento. Chopin dedicou praticamente toda sua obra ao piano. Suas composições exploraram ao máximo o potencial expressivo do instrumento, com inovações técnicas, harmônicas e sonoras que influenciaram profundamente a forma de se tocar e compor para piano. 

    Ele transformou formas antes vistas como menores ou dançantes — como a mazurca, a polonaise, o noturno, o estudo, o prelúdio e o improviso — em obras-primas artísticas de alta complexidade emocional e técnica.
                                        
    Seu legado é fundamental para a música romântica do século XIX: sua música é marcada por uma sensibilidade profunda, lirismo e delicadeza, refletindo características românticas como o subjetivismo, a exaltação dos sentimentos e o nacionalismo. Mesmo vivendo na França, Chopin manteve viva a identidade polonesa em suas obras, incorporando danças e ritmos típicos do folclore polonês. Isso o tornou um símbolo cultural da Polônia e um precursor do nacionalismo musical no século XIX.

    Ouça uma de suas músicas *Nocturne in E Flat Major (Op. 9 No. 2)*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752335948/ymupj0sgwkyen9djqgwc.mp3")

        st.subheader("**- Piotr Ilitch Tchaikovsky (1840–1893)**")

        st.markdown("""Suas obras são marcadas por temas emocionantes, muitas vezes melancólicos. Ele transmitia suas crises pessoais, amores não correspondidos e sentimentos de angústia em sua música.

Tchaikovsky era um mestre da melodia emocional, da orquestração brilhante e da forma dramática. Embora sua linguagem fosse enraizada no romantismo europeu, seu espírito russo deu à sua música uma identidade inconfundível. Compôs sinfonias, concertos, óperas e balés como *O Lago dos Cisnes (1876)* e *A Bela Adormecida (1890)*. 

Ouça uma de suas sinfonias *Symphony No. 5 in E Minor Op. 64*:
        """)
        st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")


        st.header("🎼 Estilos Musicais Contemporâneos")

        st.markdown("""
        A música é uma linguagem universal, moldada por séculos de intercâmbio entre culturas ao redor do mundo, sendo sua história muito mais abrangente do que o estudado pela tradição europeia. Cada sociedade desenvolveu estruturas e padrões rítmicos únicos que contribuíram de forma profunda para a diversidade da música contemporânea, veja alguns exeplos ao redor do mundo:

        - **Brasil**: Fruto de um intenso encontro entre povos indígenas, africanos e europeus, a música brasileira desenvolveu uma riqueza rítmica ímpar. Estilos como samba, baião, maracatu e frevo nasceram da vivência popular e da resistência cultural, revelando dinâmicas corporais, rituais e afetos codificados em padrões complexos de percussão e dança.
        - **África Subsaariana Ocidental**: Em regiões como Mali, Senegal, Gana e Nigéria, a música é profundamente interligada à vida comunitária e espiritual. Os ritmos são frequentemente polirrítmicos, isto é, combinam camadas diferentes de pulsos e acentos simultâneos, criados com instrumentos como djembês, talking drums, balafons e kora. Essa complexidade rítmica foi uma das bases do desenvolvimento do jazz, do funk, do reggae e da música afro-brasileira.
        - **Oriente Médio e Norte da África**: Países como Egito, Turquia, Irã, Síria e Marrocos abrigam tradições musicais milenares que combinam modos melódicos (maqamat) com estruturas rítmicas intricadas (iqa'at ou usul). Esses ciclos rítmicos variam em duração, acentuação e função estética, muitas vezes utilizados em contextos litúrgicos, poéticos e cerimoniais. Sua influência pode ser percebida em fusões modernas, como o jazz modal, a música eletrônica experimental e a world music.
        - **Índia**: A música clássica indiana, tanto no sistema Carnático (sul) quanto no Hindustani (norte), desenvolveu sistemas rítmicos avançadíssimos conhecidos como talas. Esses ciclos podem ter 3, 7, 9, 16 ou até mais de 100 tempos, com subdivisões internas sofisticadas e ornamentações que desafiam a regularidade métrica. O domínio do tala exige um profundo senso temporal e uma abordagem meditativa do ritmo, e inspirou artistas ocidentais como The Beatles, John McLaughlin e Philip Glass.

        Compreender esses ritmos amplia a percepção e a criatividade musical. Veja mais detalhes de alguns dos principais estilos da música contemporânea ao redor do mundo: 
        """)
        st.subheader("Gospel")
        st.markdown("Essas músicas vêm de spirituals, work songs e early gospel do século XIX e início do século XX, e foram registradas por vozes como Mahalia Jackson, Thomas A. Dorsey, Sister Rosetta Tharpe, entre outros. Essas músicas representam as raízes espirituais e musicais da cultura afro-americana que foram precursoras gêneros como o blues e o country.")
        st.markdown("""

**1. Swing Low, Sweet Chariot**

*Swing Low, Sweet Chariot* é um spiritual — um tipo de canção religiosa criada por afro-americanos escravizados nos Estados Unidos, principalmente no século XIX. 
                    
Esses spirituals expressavam sofrimento, esperança, fé e o desejo de liberdade. Acredita-se que a canção tenha sido composta por Wallace Willis, um homem afro-americano escravizado no século XIX no estado de Oklahoma (então território indígena), por volta da década de 1860. Willis teria criado a música inspirando-se em passagens bíblicas, especialmente do Livro de Números (capítulo 21, versículo 17-18), que fala de Deus guiando o povo de Israel com uma nuvem e uma coluna de fogo para libertá-los da escravidão no Egito. 
                    
Durante o século XX, *Swing Low, Sweet Chariot* se tornou um símbolo de resistência e fé para os afro-americanos, sendo cantada em igrejas, manifestações e reuniões do movimento pelos direitos civis. Sua melodia simples e poderosa ressoava como um canto de esperança diante das adversidades. A música transcendeu o gênero gospel e espiritual e entrou para o repertório popular mundial, gravada e interpretada por inúmeros artistas em diversos estilos — do folk ao jazz, do blues ao pop - entre eles: B.B King, Elvis Presley, Eric Clapton, entre outros. 

**2. Wade in the Water**

*Wade in the Water* é outro spiritual que surgiu entre os escravos afro-americanos nos Estados Unidos, provavelmente no século XIX, durante o período da escravidão.

A música foi usada como um código para ajudar escravos fugitivos a escapar para a liberdade. Ela orientava os escravos a cruzar rios e córregos para evitar serem seguidos por cães farejadores dos caçadores de escravos, pois a água "apagava o cheiro".

Assim, *wade in the water* virou um alerta para atravessar as águas e despistar os perseguidores, uma tática vital para os que fugiam para o Norte ou para territórios livres. 
                    
*Wade in the Water* tornou-se uma das músicas mais emblemáticas do gênero espiritual. Foi gravada e interpretada por muitos artistas ao longo dos anos

**3. This Train (Is Bound for Glory)**

Famosamente interpretada por Sister Rosetta Tharpe. Influenciou diretamente o rock’n’roll. Woody Guthrie, Elvis e outros gravaram versões.

**4. Down by the Riverside**

Spiritual de protesto com refrão repetitivo. Fortemente adotado pelo jazz tradicional e pelo folk.

**5. Precious Lord, Take My Hand – Thomas A. Dorsey**
                    
Considerado o pai do gospel moderno, Dorsey era pianista de blues. Essa canção influenciou Ray Charles, Sam Cooke e Elvis Presley.

**6. I’ll Fly Away – Albert E. Brumley**

Um dos hinos gospel mais gravados na música country. Aparece em trilhas como "O Brother, Where Art Thou?".

**7. When the Saints Go Marching In**

Popularizado por Louis Armstrong. Mistura gospel, jazz e marching band. Hino universal do sul dos EUA.

**8. Were You There (When They Crucified My Lord)**

Espiritual do século XIX. Forte influência na música country espiritual e blues.

**9. Go Down Moses**

Cantado pelos escravizados como símbolo de liberdade. Seu tom grave e narrativo influenciou o canto de lamento do blues.

**10. Didn’t It Rain**

Gravada por Mahalia Jackson e Sister Rosetta Tharpe. Tem swing, estrutura de chamada e resposta, e base harmônica que influenciou o soul.

""")
        st.subheader("Blues")
        st.markdown("O blues surgiu no sul dos Estados Unidos no final do século XIX, profundamente enraizado nas canções de trabalho, spirituals e lamentos das comunidades afro-americanas. Com estruturas harmônicas simples e letras que expressam dor, resistência e ironia, o blues é a base de inúmeros gêneros modernos como o jazz, o rock, o soul e o R&B.")
        st.markdown("""

        **1. Cross Road Blues – Robert Johnson**

        Gravada em 1936, essa canção imortalizou o mito do pacto com o diabo. Influenciou profundamente o rock, especialmente artistas como Eric Clapton e The Rolling Stones.

        **2. Hellhound on My Trail – Robert Johnson**

        Expressa angústia e perseguição espiritual. É uma das músicas mais intensas do Delta Blues e inspiração para músicos do século XX inteiro.

        **3. I'm Your Hoochie Coochie Man – Muddy Waters**

        Símbolo do Chicago Blues elétrico. Composição de Willie Dixon, fundou a estética do blues urbano e influenciou o rock britânico.

        **4. The Thrill Is Gone – B.B. King**

        Uma balada de blues moderno com orquestração sofisticada. Representa o ápice emocional e técnico do gênero.

        **5. Smokestack Lightning – Howlin’ Wolf**

        Com riff hipnótico e vocal poderoso, influenciou diretamente o rock psicodélico e o blues-rock dos anos 60.

        **6. Boom Boom – John Lee Hooker**

        Mistura falada e cantada com um groove irresistível. Foi adotada por bandas de rock e soul, como The Animals.

        **7. Sweet Home Chicago – Robert Johnson**

        Um dos blues mais regravados da história. Símbolo da migração de músicos negros do sul para o norte industrial dos EUA.

        **8. Mannish Boy – Muddy Waters**

        Com estrutura de chamada e resposta, tornou-se hino da afirmação negra no blues. Amplamente usado em filmes e trilhas sonoras.

        **9. Got My Mojo Working – Muddy Waters**

        Com energia crua e magnetismo, essa faixa definiu o som de Chicago e abriu caminhos para o rhythm & blues.

        **10. Stormy Monday – T-Bone Walker**

        Uma das primeiras fusões entre o blues e o jazz. Clássico absoluto para guitarristas e pianistas de blues, jazz e soul.

        """)

        st.subheader("Country")
        st.markdown("O country surgiu no início do século XX nos estados do sul dos EUA, misturando música folclórica britânica, spirituals e blues rural. Caracteriza-se por melodias simples, narrativas diretas e uso do violão, banjo e fiddle.")
        st.markdown("""

        **1. Blue Yodel (T for Texas) – Jimmie Rodgers**

        Pioneiro do country, misturou yodel com blues e lançou as bases do gênero.

        **2. I’m So Lonesome I Could Cry – Hank Williams**

        Poética e melancólica, essa balada de 1949 é um marco do country tradicional.

        **3. Your Cheatin’ Heart – Hank Williams**

        Símbolo do country honky-tonk, com melodia simples e letra sobre traição amorosa.

        **4. Folsom Prison Blues – Johnny Cash**

        Mistura country, folk e rockabilly. Sua batida imita o som dos trilhos de trem.

        **5. Crazy – Patsy Cline**

        Composta por Willie Nelson, eternizada pela interpretação suave e melancólica de Cline.

        **6. I Walk the Line – Johnny Cash**

        Um dos maiores hits do gênero, com uma progressão harmônica única e ritmo constante.

        **7. Hey, Good Lookin’ – Hank Williams**

        Canção animada e popular, considerada um standard country com apelo popular.

        **8. Wildwood Flower – The Carter Family**

        Um hino do country rural com dedilhado tradicional que influenciou gerações.

        **9. Orange Blossom Special – Ervin T. Rouse**

        Instrumental rápido e técnico, conhecido como o “hino não oficial do fiddle”.

        **10. Take Me Home, Country Roads – John Denver**

        Canção icônica dos anos 70 com forte nostalgia e progressão acessível ao violão.

        """)

        st.subheader("Rock")
        st.markdown("O rock emergiu nos anos 1950 como uma fusão de blues, country e R&B. Com batida forte e guitarra em destaque, tornou-se a trilha sonora de mudanças sociais e culturais do século XX.")
        st.markdown("""

        **1. Johnny B. Goode – Chuck Berry**

        Guitarra elétrica em destaque, ritmo pulsante e letra sobre ascensão social. Base do rock moderno.

        **2. Tutti Frutti – Little Richard**

        Energia explosiva e vocal rasgado. Um dos primeiros sucessos do rock’n’roll.

        **3. Jailhouse Rock – Elvis Presley**

        Mistura de rockabilly com performance teatral. Um marco da cultura pop.

        **4. Rock Around the Clock – Bill Haley & His Comets**

        Símbolo do nascimento do rock. Popularizou o gênero nos cinemas e rádios.

        **5. Heartbreak Hotel – Elvis Presley**

        Uma balada lenta e profunda que introduziu o dramatismo no rock.

        **6. Whole Lotta Shakin’ Goin’ On – Jerry Lee Lewis**

        Piano frenético, performance ousada e energia contagiante.

        **7. That’ll Be the Day – Buddy Holly**

        Estilo limpo e melódico, com influência country. Fundamentou o pop-rock.

        **8. Hound Dog – Elvis Presley (original de Big Mama Thornton)**

        Versão explosiva que mistura R&B e rock com atitude.

        **9. La Bamba – Ritchie Valens**

        Mistura de rock’n’roll com música folclórica mexicana. Uma ponte entre culturas.

        **10. Good Golly, Miss Molly – Little Richard**

        Vocal visceral, piano marcante e estrutura simples. Influência direta no soul e no hard rock.

        """)

        
        st.subheader("Pop")
        st.markdown("A música pop abrange melodias acessíveis, refrões marcantes e produção polida. Desenvolveu-se a partir do rock, do soul e da música popular dos anos 1950 em diante.")
        st.markdown("""

        **1. Yesterday – The Beatles**

        Balada melancólica com violão e quarteto de cordas. Uma das músicas mais regravadas da história.

        **2. Imagine – John Lennon**

        Hino pacifista com piano marcante e letra universal.

        **3. Let It Be – The Beatles**

        Canção de consolo com progressão simples e poderosa.

        **4. Billie Jean – Michael Jackson**

        Revolucionou o pop com groove dançante, produção refinada e videoclipes inovadores.

        **5. Like a Prayer – Madonna**

        Pop com elementos gospel, polêmica e lirismo emocional.

        **6. Every Breath You Take – The Police**

        Pop/rock com atmosfera sombria e riffs marcantes.

        **7. Hallelujah – Leonard Cohen / Jeff Buckley**

        Balada espiritual e existencial, muito popular entre violonistas.

        **8. Piano Man – Billy Joel**

        Narrativa envolvente e melodia inesquecível. Ícone do pop com piano.

        **9. Time After Time – Cyndi Lauper**

        Balada sensível dos anos 80, muito usada em trilhas.

        **10. What a Wonderful World – Louis Armstrong**

        Pop nostálgico e orquestral, com mensagem otimista.

        """)


        st.subheader("Jazz")
        st.markdown("O jazz nasceu em Nova Orleans, fundindo blues, ragtime e música europeia. Marcado pela improvisação, harmonia sofisticada e swing, o jazz influenciou praticamente todos os gêneros modernos.")
        st.markdown("""

        **1. Take the 'A' Train – Duke Ellington / Billy Strayhorn**

        Hino do jazz de big band, com swing clássico e sofisticação harmônica.

        **2. All of Me – Gerald Marks & Seymour Simons**

        Standard das jam sessions, com estrutura acessível e melodia marcante.

        **3. Autumn Leaves – Joseph Kosma**

        Popular entre iniciantes e profissionais. Ótimo para estudar modulações e improviso.

        **4. Blue in Green – Miles Davis / Bill Evans**

        Balada introspectiva e modal do álbum “Kind of Blue”.

        **5. So What – Miles Davis**

        Representa o jazz modal. Simples, profundo e essencial ao piano.

        **6. Summertime – George Gershwin**

        Ária de ópera que virou jazz standard. Regravada em dezenas de estilos.

        **7. Round Midnight – Thelonious Monk**

        Complexa e melancólica. Um dos pilares do jazz moderno.

        **8. My Funny Valentine – Rodgers & Hart**

        Standard romântico, interpretado por Chet Baker e outros ícones.

        **9. Fly Me to the Moon – Bart Howard**

        Popularizado por Sinatra, mescla balada com swing.

        **10. Satin Doll – Duke Ellington**

        Melodia envolvente e progressão harmônica rica. Clássico do piano e guitarra.

        """)

        st.subheader("Bossa-Nova")
        st.markdown("A Bossa Nova surgiu no Brasil nos anos 1950, combinando samba com harmonia do jazz. Marcada pelo violão suave e letras intimistas, projetou a música brasileira internacionalmente.")
        st.markdown("""

        **1. Garota de Ipanema – Tom Jobim e Vinicius de Moraes**

        Hino internacional da bossa-nova, com acordes sofisticados e melodia envolvente.

        **2. Chega de Saudade – Tom Jobim e Vinicius de Moraes**

        Considerada a primeira bossa-nova. Mudou a música brasileira.

        **3. Desafinado – Tom Jobim e Newton Mendonça**

        Defende a imperfeição poética da música. Clássico do gênero.

        **4. Águas de Março – Tom Jobim**

        Letra minimalista e estrutura cíclica. Inovadora e hipnótica.

        **5. Corcovado – Tom Jobim**

        Balada calma que exalta o silêncio e a paz.

        **6. Samba de Uma Nota Só – Tom Jobim**

        Explora o minimalismo melódico com harmonia rica.

        **7. O Leãozinho – Caetano Veloso**

        Canção intimista e delicada, muito tocada no violão.

        **8. Manhã de Carnaval – Luiz Bonfá**

        Conhecida mundialmente, também presente no cinema.

        **9. Triste – Tom Jobim**

        Menos conhecida, mas sofisticada e recorrente entre músicos de jazz.

        **10. Insensatez – Tom Jobim e Vinicius de Moraes**

        Lenta, trágica e harmônica. Um dos maiores exemplos de lirismo da bossa.

        """)

        st.subheader("Samba")
        st.markdown("O samba é uma expressão essencial da cultura afro-brasileira, com raízes no batuque e no choro. Evoluiu em diversas formas: samba-canção, samba-enredo, samba de roda, partido-alto, entre outros.")
        st.markdown("""

        **1. O Sol Nascerá - Cartola**

        """)

        exibir_pdf("cifras/Cifra Club - Cartola - O Sol Nascerá.pdf")

        st.subheader("Choro")
        st.markdown("O choro é o primeiro gênero urbano tipicamente brasileiro. Instrumental, virtuoso e melódico, une elementos do lundu, da polca, da modinha e da música erudita europeia.")
        st.markdown("""

        **1. Carinhoso – Pixinguinha**

        Hino afetivo do choro. Simples, expressivo e universal.

        **2. Brasileirinho – Waldir Azevedo**

        Um dos choros mais técnicos e conhecidos do cavaquinho.

        **3. Tico-Tico no Fubá – Zequinha de Abreu**

        Virtuosismo e velocidade. Famoso internacionalmente.

        **4. Lamentos – Pixinguinha**

        Choro sofisticado com harmonias impressionantes.

        **5. Doce de Coco – Jacob do Bandolim**

        Delicado e expressivo, ótimo para violão solo.

        **6. Noites Cariocas – Jacob do Bandolim**

        Choro com andamento acelerado e melodias marcantes.

        **7. Ingênuo – Pixinguinha**

        Sofisticado, com improviso e lirismo.

        **8. Cochichando – Pixinguinha**

        Interplay entre os instrumentos, típico do choro tradicional.

        **9. Um a Zero – Pixinguinha e Benedito Lacerda**

        Choro-desafio que simula uma disputa futebolística.

        **10. Apanhei-te Cavaquinho – Ernesto Nazareth**

        Ponte entre o choro e o piano popular brasileiro.

        """)

        st.subheader("Baião")
        st.markdown("O baião surgiu no nordeste do Brasil, combinando ritmos indígenas, africanos e europeus. Com sanfona, zabumba e triângulo, influenciou forró, xaxado e até o tropicalismo.")
        st.markdown("""

        **1. Asa Branca – Luiz Gonzaga e Humberto Teixeira**
""")
        exibir_pdf("cifras/Cifra Club - Luiz Gonzaga - Asa Branca.pdf")

        st.markdown("""

        **2. Xote das Meninas – Luiz Gonzaga**
""")
        exibir_pdf("cifras/Cifra Club - Luiz Gonzaga - Xote Das Meninas.pdf")

        st.markdown("""

        **3. Eu Só Quero Um Xodó – Luiz Gonzaga**
""")
        exibir_pdf("cifras/Cifra Club - Luiz Gonzaga - Eu Só Quero Um Xodó.pdf")

        

        st.subheader("Reggae")
        st.markdown("Originado na Jamaica nos anos 1960, o reggae mistura ska, rocksteady e música afro-caribenha. Suas batidas sincopadas, letras conscientes e baixo pulsante o tornaram um fenômeno global.")
        
        st.markdown("""

        **1. One Love – Bob Marley**
        """)
        exibir_pdf("cifras/Cifra Club - Bob Marley - One Love.pdf")

        st.markdown("""

        **2. Natural Mystic – Bob Marley**
        """)
        exibir_pdf("cifras/Cifra Club - Bob Marley - Natural Mystic.pdf")

        st.markdown("""

        **3. Roots, Rock, Reggae – Bob Marley**
        """)
        exibir_pdf("cifras/Cifra Club - Bob Marley - Roots, Rock, Reggae.pdf")

        st.markdown("""

        **4. Stir It Up – Bob Marley**
        """)
        exibir_pdf("cifras/Cifra Club - Bob Marley - Stir It Up.pdf")

    if choice == "Ritmos":
        st.title("Ritmos Musicais 🥁")

        st.markdown("""
        O ritmo é um dos elementos fundamentais da música. Ele organiza o tempo musical e dá forma às melodias, criando padrões de duração, silêncio e repetição. Independentemente do estilo, é o ritmo que nos faz bater o pé, dançar ou reconhecer uma batida.
        """)

        st.header("🔹 Pulsação e Tempo")

        st.markdown("""
        A **pulsação** é a batida constante que sentimos ao ouvir uma música. Ela pode ser lenta ou rápida, mas é sempre regular. Já o **tempo (ou andamento)** é a velocidade dessa pulsação, normalmente medida em **BPM (batidas por minuto)**. Alguns exemplos:
        
        - 🎵 *Lento* (~60 BPM)
        - 🎵 *Moderado* (~90–120 BPM)
        - 🎵 *Rápido* (~140+ BPM)

        O metrônomo é a ferramenta utilizada para marcar o tempo de forma precisa durante os estudos.
        """)

        st.header("🔸 Compasso e Métrica")

        st.markdown("""
        O **compasso** organiza a música em pequenos blocos rítmicos com pulsos fortes e fracos. É representado por frações como **4/4**, **3/4**, **6/8** etc.

        - O número de cima indica quantos tempos há no compasso.
        - O número de baixo indica o valor da figura rítmica (ex: 4 = semínima).

        A **métrica** define o padrão acentual desses compassos. Exemplos:
        
        - 2/4 → binário simples (ex: marchas)
        - 3/4 → ternário simples (ex: valsa)
        - 6/8 → binário composto (ex: músicas celtas ou afro-brasileiras)
        """)

        st.header("🔹 Figuras Rítmicas")

        st.markdown("""
        As **figuras rítmicas** indicam a duração dos sons. Cada figura possui uma pausa correspondente:

        - **Semibreve (𝅝)**: 4 tempos
        - **Mínima (𝅗𝅥)**: 2 tempos
        - **Semínima (𝅘𝅥)**: 1 tempo
        - **Colcheia (𝅘𝅥𝅮)**: ½ tempo
        - **Semicolcheia (𝅘𝅥𝅯)**: ¼ tempo

        A combinação dessas figuras gera os padrões rítmicos que usamos nas músicas.
        """)

        st.header("🔸 Pausas Musicais")

        st.markdown("""
        O silêncio também é parte do ritmo. As **pausas** indicam momentos em que não há som, mas o tempo continua correndo. Cada figura tem sua pausa correspondente, com igual valor de tempo.
        """)

        st.header("🔹 Síncope e Contratempo")

        st.markdown("""
        A **síncope** desloca o acento natural do compasso, criando tensão rítmica. Ela ocorre quando um som prolongado atravessa uma batida forte e fraca, ou quando acentuamos uma parte fraca do compasso.

        O **contratempo** é o acento justamente nos tempos fracos, produzindo um efeito de “empurrão” na música. Ambos são comuns em estilos como samba, jazz e reggae.
        """)

        st.header("🔸 Polirritmia e Subdivisão")

        st.markdown("""
        A **polirritmia** ocorre quando dois ou mais ritmos diferentes são executados simultaneamente. É comum em músicas africanas, latinas e no jazz moderno.

        Já a **subdivisão** é a divisão interna do tempo. Por exemplo, uma semínima pode ser subdividida em duas colcheias ou quatro semicolcheias, permitindo criar diferentes grooves e variações rítmicas.
        """)


    elif choice == "Intervalos":
        st.title("Intervalos Musicais 🎶")

        st.markdown("""
        Os **intervalos musicais** são a distância entre duas notas. Eles são essenciais para compreender a construção de melodias e harmonias. Um intervalo pode ser tocado de forma **melódica** (notas em sequência) ou **harmônica** (notas simultâneas).
        """)

        st.markdown("""
        A unidade de medida para intervalos é o **tom** e o **semitom**:

        - **1 semitom (½ tom)**: distância entre duas notas adjacentes (ex: C para C♯)
        - **1 tom (2 semitons)**: distância equivalente a dois semitons (ex: C para D)

        """)

        st.markdown("""
        Intervalos podem ser classificados pela **qualidade da sensação** que causam:

        - **Consonantes**: sons estáveis, agradáveis ao ouvido (relaxamento).
        - **Dissonantes**: sons instáveis, que geram tensão (movimento).

        """)

        st.markdown("""
        | Nome do Intervalo       | Distância | Exemplo       | Qualidade             | Áudio |
        |-------------------------|-----------|----------------|------------------------|-------|
        | Uníssono                | 0T        | C – C          | Consonante            | <audio controls style="width:100px;" src="audios/unisono.mp3"></audio> |
        | Segunda menor           | ½T        | C – C♯/D♭       | Dissonante            | <audio controls style="width:100px;" src="audios/segunda_menor.mp3"></audio> |
        | Segunda maior           | 1T        | C – D          | Dissonante            | <audio controls style="width:100px;" src="audios/segunda_maior.mp3"></audio> |
        | Terça menor             | 1½T       | C – E♭         | Consonante imperfeita | <audio controls style="width:100px;" src="audios/terca_menor.mp3"></audio> |
        | Terça maior             | 2T        | C – E          | Consonante imperfeita | <audio controls style="width:100px;" src="audios/terca_maior.mp3"></audio> |
        | Quarta justa            | 2½T       | C – F          | Consonante            | <audio controls style="width:100px;" src="audios/quarta_justa.mp3"></audio> |
        | Quarta aumentada / Quinta diminuta | 3T | C – F♯/G♭ | Dissonante | <audio controls style="width:100px;" src="audios/quarta_aumentada.mp3"></audio> |
        | Quinta justa            | 3½T       | C – G          | Consonante            | <audio controls style="width:100px;" src="audios/quinta_justa.mp3"></audio> |
        | Sexta menor             | 4T        | C – A♭         | Consonante imperfeita | <audio controls style="width:100px;" src="audios/sexta_menor.mp3"></audio> |
        | Sexta maior             | 4½T       | C – A          | Consonante imperfeita | <audio controls style="width:100px;" src="audios/sexta_maior.mp3"></audio> |
        | Sétima menor            | 5T        | C – B♭         | Dissonante            | <audio controls style="width:100px;" src="audios/setima_menor.mp3"></audio> |
        | Sétima maior            | 5½T       | C – B          | Dissonante            | <audio controls style="width:100px;" src="audios/setima_maior.mp3"></audio> |
        | Oitava justa            | 6T        | C – C (oitava) | Consonante            | <audio controls style="width:100px;" src="audios/oitava_justa.mp3"></audio> |
        """, unsafe_allow_html=True)

        st.markdown("""*Os aúdios tocam os intervalos de uma mesma oitava e, depois, o intervalo entre uma oitava a cima*
                """)
    

        st.info("""**Dica¹:** Liste os intervalos musicais partindo da referência de outras notas. 
        
**Dica²:** Identifique no seu instrumento onde estão esses intervalos.

**Dica³:** Treine a identificação de intervalos de ouvido a partir de aplicativos como Tenuto, Perfect Ear ou teoria online como teoria.com.
        
        
        """)



        st.header("💡 Intervalos e Narrativa Musical")

        st.markdown("""
        Assim como uma boa história alterna entre tensão e resolução, uma boa música também equilibra **dissonâncias** e **consonâncias** para emocionar o ouvinte.

        - Os **intervalos dissonantes** criam suspense, energia ou conflito.
        - Os **intervalos consonantes** proporcionam resolução e conforto.

        Saber quando usar cada um é uma escolha estética e emocional. Essa alternância é o que dá vida à música e abre espaço para sua **criatividade** como compositor ou intérprete.
        """)

        st.info("""🎧 **Dica:** Ouça músicas conhecidas e tente identificar os intervalos presentes nas melodias. 
        
**Desafio**: Descubra onde ocorre uma terça maior, terça menor, quarta ou quinta justa em trechos de canções populares para conectar teoria à prática, fortalecendo sua percepção musical de forma contextualizada e prazerosa.
                
**Desafio²**: Faça uma melodia utilizando uma terça maior ou menor, uma quarta justa, quinta justa e outro intervalo de sua escolha. Lembre-se de seguir os padrões ritmicos com o metrônomo.""")

    # Função para exibir texto e imagens sobre escalas
    def exibir_escalas():
        st.title("Escalas Musicais 🎼")

        st.markdown("""
        Escalas são conjuntos organizados de notas dispostas em ordem ascendente ou descendente. Elas fornecem a base melódica e harmônica da música, guiando a escolha de acordes e melodias dentro de uma tonalidade.

        Cada escala é definida por um padrão fixo de **intervalos** (tons e semitons) e possui uma sonoridade característica, influenciando o clima da música — alegre, melancólico, misterioso ou enérgico.
        """)

        st.header("🎶 Escalas Pentatônicas (5 notas)")

        st.markdown("""
        As **escalas pentatônicas** contêm apenas cinco notas por oitava. São simples, versáteis e amplamente usadas em músicas folclóricas, blues, rock e músicas orientais. 

        | Tipo               | Distância                   | Intervalos            | Exemplo (C)        |
        |--------------------|------------------------------|----------------------------------|--------------------|
        | Pentatônica Maior  | T - T - 1½T - T - 1½T         | 1ª - 2ªM - 3ªM - 5ªJ - 6ªM          | C – D – E – G – A  |
        | Pentatônica Menor  | 1½T - T - T - 1½T - T         | 1ª - 3ªm - 4ªJ - 5ªJ - 7ªm         | A – C – D – E – G  |
        """)


        image_path = os.path.join('images', 'pentatonica-maior.jpg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Pentatônica Maior')

        image_path = os.path.join('images', 'pentatonica-menor.jpg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Pentatônica Menor')

        st.header("🎸 Escala Blues")

        st.markdown("""
        A **escala blues** deriva da escala pentatônica menor com a adição de uma nota chamada **blue note** (quinta diminuta), que dá seu caráter expressivo e melancólico.
""")
        
        st.markdown("""

| Tipo                 | Distância                           | Intervalos                    | Exemplo (C)             |
|----------------------|--------------------------------------|-------------------------------|-------------------------|
| Blues Maior          | T - ½T - ½T - 1T - 1½T - 1T           | 1ª - 2ªM - 3ªm - 3ªM - 5ªJ - 6ªM | C – D – D# – E – G – A   |
| Blues Menor          | 1½T - T - ½T - ½T - 1½T - T           | 1ª - 3ªm - 4ªJ - 4ª# - 5ªJ - 7ªm | A – C – D – D# – E – G   |
""")
        
        st.markdown("""
As **escalas pentatônicas e blues** são estruturas essenciais na música popular, especialmente no blues, rock e jazz. A escala blues é uma variação da pentatônica com a adição da "blue note".        """)

        st.subheader("Escala Blues Maior")
        image_path = os.path.join('images', 'escala-blues-maior.jpg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Pentatônica Menor')

        st.subheader("Escala Blues Menor")
        image_path = os.path.join('images', 'escala-blues-menor.jpg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Pentatônica Menor')

        st.success("💡 **Dica:** experimente tocar as escalas no seu instrumento em diferentes tons para sentir como cada uma afeta a sonoridade da música.")


        st.header("🔸 Escalas Maiores (7 notas)")

        st.markdown("""
        As **escalas maiores** (natural, harmônica e melódica) são fundamentais na teoria musical ocidental. Cada variação introduz alterações que afetam o caráter melódico e harmônico da música.

        | Tipo              | Distância                          | Intervalos                                 
        |-------------------|-------------------------------------|--------------------------------------------
        | Maior Natural     | T - T - ST - T - T - T - ST         | 1ª - 2ªM - 3ªM - 4ªJ - 5ªJ - 6ªM - 7ªM      
        | Maior Harmônica   | T - T - ST - T - ST - 1½T - ST      | 1ª - 2ªM - 3ªM - 4ªJ - 5ªJ - 6ªm - 7ªM      
        | Maior Melódica    | T - T - ST - T - T - T - ST         | 1ª - 2ªM - 3ªM - 4ªJ - 5ªJ - 6ªM - 7ªM       
        """)

        image_path = os.path.join('images', 'escala-maior-natural.jpg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Escala Maior Natural')

        st.header("🔹 Escalas Menores (7 notas)")

        st.markdown("""
        As **escalas menores** têm uma sonoridade introspectiva, emotiva ou melancólica. Existem três variações principais que se diferenciam especialmente nos graus 6 e 7:

        | Tipo              | Distância                             | Intervalos                                
        |-------------------|----------------------------------------|-------------------------------------------
        | Menor Natural     | T - ST - T - T - ST - T - T            | 1ª - 2ªM - 3ªm - 4ªJ - 5ªJ - 6ªm - 7ªm     
        | Menor Harmônica   | T - ST - T - T - ST - 1½T - ST         | 1ª - 2ªM - 3ªm - 4ªJ - 5ªJ - 6ªm - 7ªM     
        | Menor Melódica    | T - ST - T - T - T - T - ST (ascendente)| 1ª - 2ªM - 3ªm - 4ªJ - 5ªJ - 6ªM - 7ªM     
        """)

        image_path = os.path.join('images', 'escala-menor-natural.jpg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Escala Menor Natural')


        st.header(" 🔁 Escalas Relativas")

        st.markdown("""Escalas relativas são pares de escalas maior e menor que compartilham as mesmas notas e armadura de clave, mas têm tônicas (notas iniciais) diferentes. Cada escala maior tem uma relativa menor, e vice-versa. 
                    
""")

        image_path = os.path.join('images', 'escalas.jpeg')
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption='Escalas Relativas')

        st.success("💡 **Dica:** Para achar a relativa menor de uma escala maior desça 1 tom e meio (3 semitons) da tônica. Para achar a relativa maior de uma escala menor suba 1 tom e meio (3 semitons) da tônica.")

    def acordes():
        st.title("Acordes & Arpejos Musicais 🎹")

        st.markdown("Os acordes são combinações de notas tocadas simultaneamente que produzem uma harmonia. Eles são a base da harmonia na música e ajudam a definir o tom, a emoção e a direção da composição. Os arpejos nada mais são do que as notas de um acorde tocadas de forma melódica, ou seja, sequencial. ")

        st.header("Formação de Acordes")

        st.markdown("""

Os acordes são formados pela **sobreposição de terças** e podem variar de estruturas com três notas (tríades) ou estruturas de quatro notas (tétrades).
        
A sobreposição de terças consiste em empilhar intervalos de terça maior ou menor a partir de uma nota-base, chamada tônica. 

Para sobrepor terças, siga este processo:

**1. Escolha uma nota base (tônica): é o ponto de partida do acorde.**
        
- Exemplo: vamos usar a nota Dó (C).

**2. Adicione um intervalo de terça a partir da tônica:**

- Se for uma terça maior, adicione Mi (E)

- Se for uma terça menor, adicione Mi♭ (E♭)

**3. Sobreponha mais uma terça a partir da nota obtida:**

Aqui, você empilha mais uma terça (maior ou menor) sobre a anterior (Mi ou Mi♭).

- Se estava com C + E, adicionar uma terça menor dá Sol (G) → C-E-G (tríade maior)

- Se estava com C + E♭, adicionar uma terça maior dá G também → C-E♭-G (tríade menor)

**4. Adicione uma quarta nota (opcional - para formar tétrades)**
        
Empilhe mais uma terça sobre a terceira nota:

- Sobre G (que veio de C-E-G), uma terça maior dá B (Si) → C-E-G-B → Acorde Cmaj7

- Sobre G, uma terça menor dá B♭ (Si♭) → C-E-G-B♭ → Acorde C7 (dominante)

- Sobre G, outra terça menor com a base menor (C-E♭-G-B♭) → C-E♭-G-B♭ → Acorde Cm7
        """)

        st.header("🔹 Tipos de Tríades")

        st.markdown("""
        | Tipo               | Empilhamento de Terças         | Fórmula do acorde                  |Exemplos |
        |--------------------|-------------------------------|------------------------------|------------------|
        | Tríade Maior       | 3ª Maior + 3ª Menor            | Tônica - 3ª Maior - 5ª Justa | C – E – G        |
        | Tríade Menor       | 3ª Menor + 3ª Maior            | Tônica - 3ª Menor - 5ª Justa | A – C – E        |
        | Tríade Diminuta    | 3ª Menor + 3ª Menor            | Tônica - 3ª Menor - 5ª Dim   | B – D – F        |
        | Tríade Aumentada   | 3ª Maior + 3ª Maior            | Tônica - 3ª Maior - 5ª Aum   | F – A – C♯       |
        """)

        st.success("""💡 **Dica:** Construa uma tabela com as colunas *Tonalidade*, *Tipo de Tríade*, *Notas do Acorde* e *Empilhamento de Terças* para encontrar todos os acordes possíveis nas tríades dos 12 tons. 
        
*Obs: Há um total de 48 combinações possíveis para as tríades nos 12 tons.*
        """)

        st.subheader("Sistema C-A-G-E-D")

        st.markdown("""Qualquer acorde maior ou menor pode ser formado usando as formas básicas dos acordes abertos de C, A, G, E e D, apenas mudando a posição (ou "forma") com pestanas ao longo do braço.

Essas formas se repetem ciclicamente no braço do instrumento, permitindo tocar o mesmo acorde em diferentes regiões do braço com formas familiares. Esse recurso é essencial para você memorizar o braço da guitarra com mais facilidade, sendo um 'truque' para você encontrar todas as notas de uma tríade.""")

        st.markdown("""
        
        **Veja como encontrar todas as tríades no braço da guitarra com o sistema C-A-G-E-D.** 
        
        """)

        st.image("images/triade-maior.png", caption="Acordes de Sol Maior", use_column_width=True)

        st.image("images/triade-menor.png", caption="Acordes de Sol Menor", use_column_width=True)

        st.image("images/triade-diminuta.png", caption="Acordes de Sol Diminuto", use_column_width=True)

        st.image("images/triade-aumentada.png", caption="Acordes de Sol Aumentado", use_column_width=True)

        st.header("🔸 Tipos de Tétrades")

        st.markdown("""
        As **tétrades** acrescentam uma **quarta nota** à tríade, geralmente uma **sétima**, trazendo mais complexidade harmônica. São muito usadas em jazz, MPB e harmonias avançadas.

        | Tipo                | Empilhamento de Terças                       | Fórmula                               | Exemplo (notas)     |
        |---------------------|---------------------------------------------|--------------------------------------|---------------------|
        | Tétrade Maior (maj7)| 3ª Maior + 3ª Menor + 3ª Maior               | Tônica - 3ª Maior - 5ª Justa - 7ª Maior  | C – E – G – B       |
        | Tétrade Menor (m7)  | 3ª Menor + 3ª Maior + 3ª Menor               | Tônica - 3ª Menor - 5ª Justa - 7ª Menor  | D – F – A – C       |
        | Dominante (7)       | 3ª Maior + 3ª Menor + 3ª Menor               | Tônica - 3ª Maior - 5ª Justa - 7ª Menor  | G – B – D – F       |
        | Diminuta (dim7)     | 3ª Menor + 3ª Menor + 3ª Menor               | Tônica - 3ª Menor - 5ª Diminuta - 7ª Diminuta | B – D – F – A♭      |
        | Aumentada (maj7#5)  | 3ª Maior + 3ª Maior + 3ª Maior               | Tônica - 3ª Maior - 5ª Aumentada - 7ª Maior | F – A♯ – C♯ – E     |
        """)


        st.success("""💡 **Desafio:** Construa uma tabela com as colunas *Tonalidade*, *Tipo de Tríade*, *Notas do Acorde* e *Empilhamento de Terças* para encontrar todos os acordes possíveis nas tétrades dos 12 tons. 
        
*Obs: Há um total de 60 combinações possíveis para as tétrades nos 12 tons.*
        """)

        st.image("images/acordes-tetrades.png", caption="Acordes de Sol Maior com +7", use_column_width=True)

        st.title("🎼 Arpejos")

        st.markdown("""
        Um **arpejo** é quando as notas de um acorde são tocadas **sequencialmente**, uma após a outra, em vez de simultaneamente. Isso cria um efeito melódico com base na harmonia do acorde e é muito usado em solos, acompanhamento e improvisação.

        Os arpejos também podem ser tocados de forma ascendente, descendente ou alternada, e são uma ferramenta essencial para explorar a sonoridade dos acordes no tempo.
        """)
        st.header("Tríade Maior (1 - 3 - 5)")
        st.image("images/Arpejo-triade-maior.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tríade Menor (1 - b3 - 5)")
        st.image("images/Arpejo-triade-menor.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tétrade Maior (1 - 3 - 5 - 7)")
        st.image("images/Arpejo-tetrade-maior.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tétrade Menor (1 - b3 - 5 - b7)")
        st.image("images/Arpejos-tetrade-menor.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tétrade Dominante (1 - 3 - 5 - b7)")
        st.image("images/Arpejos-tetrade-dominante.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tétrade Meia-Diminuta (1 - b3 - b5 - b7)")
        st.image("images/Arpejos-tetrade-meia-diminuta.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tétrade Aumentada (1 - 3 - #5 - 7)")
        st.image("images/Arpejos-tetrade-aumentada.png", caption="Representação visual das tríades", use_column_width=True)
        st.header("Tétrade Menor com Sétima Maior (1 - b3 - 5 - 7)")
        st.image("images/Arpejos-tetrade-menor-com-setima-maior.png", caption="Representação visual das tríades", use_column_width=True)


    def harmonico():
        st.title("🎼 Campo Harmônico")

        st.markdown("""
    Os **campos harmônicos** são conjuntos de acordes derivados de uma **escala** (maior ou menor) usados para construir harmonias e progressões musicais.

    Eles são essenciais para compor, improvisar e entender como os acordes se relacionam entre si.

        """)

        st.header("🌞 Campo Harmônico Maior")

        st.markdown("""
    O **campo harmônico maior** é derivado da escala maior e forma a base para progressões estáveis, alegres e comuns em músicas populares e clássicas.

    **Fórmula:**
    - I: Tríade Maior
    - II: Tríade Menor
    - III: Tríade Menor
    - IV: Tríade Maior
    - V: Tríade Maior
    - VI: Tríade Menor
    - VII: Tétrade Meio-diminuta

    **Exemplo em C Maior:**
    C – Dm – Em – F – G – Am – B°
    """)

        st.header("🌑 Campo Harmônico Menor")

        st.markdown("""
    O **campo harmônico menor** é baseado na escala menor natural. Tem uma sonoridade mais introspectiva e emocional.

    **Fórmula:**
    - I: Tríade Menor
    - II: Tétrade Diminuta
    - III: Tríade Maior
    - IV: Tríade Menor
    - V: Tríade Menor
    - VI: Tríade Maior
    - VII: Tétrade Maior

    **Exemplo em A Menor:**
    Am – B° – C – Dm – Em – F – G
    """)

        st.header("🎯 Funções Harmônicas")

        st.markdown("""
            No campo harmônico, cada acorde cumpre uma **função harmônica**. As funções são classificadas em:

            - **Tônica (T)**: sensação de repouso, estabilidade;
            - **Subdominante (SD)**: cria movimento, prepara a tensão;
            - **Dominante (D)**: cria tensão e conduz de volta à tônica.

            **Exemplo – Campo harmônico maior de C:**

            | Grau | Acorde | Função        |
            |------|--------|----------------|
            | I    | C      | Tônica (T)     |
            | II   | Dm     | Subdominante   |
            | III  | Em     | Tônica         |
            | IV   | F      | Subdominante   |
            | V    | G      | Dominante      |
            | VI   | Am     | Tônica         |
            | VII  | B°     | Dominante      |
            """)


        st.header("🎯 Progressões Harmônicas")

        st.header("🔁 Ciclo das Quintas")
        
        st.header("🔄 Ciclo das Quartas")

        st.markdown("""
    O **ciclo das quartas** move-se por **quartas justas descendentes** (ou quintas ascendentes lidas ao contrário). Usado para:

    - Modulação entre tonalidades;
    - Progressões harmônicas previsíveis;
    - Improvisação e prática.

    **Exemplo:**

    C → F → Bb → Eb → Ab → Db → Gb → B → E → A → D → G → C
    """)


        st.markdown("""
    O **ciclo das quintas** move-se por **quintas justas ascendentes**. É uma ferramenta fundamental para:

    - Compor progressões que retornam naturalmente à tônica;
    - Navegar entre tonalidades;
    - Construir músicas com cadência satisfatória.

    **Exemplo:**

    C → G → D → A → E → B → F♯ → C♯ → G♯ → D♯ → A♯ → F → C

    > 💡 O ciclo das quartas é o ciclo das quintas lido de trás pra frente!
    """)

    
    def gregos():
        st.header("🏛️ Modos Gregos")

        st.markdown("""
    Os **Modos Gregos** são escalas derivadas da **escala maior diatônica**, cada uma começando em um grau diferente da escala.

    Cada modo possui uma **personalidade sonora única**, com diferentes sensações emocionais e funções harmônicas. Eles são muito utilizados na música modal, jazz, rock, música medieval e contemporânea.

    ---

    🎼 **Modos derivados da escala maior (modo jônio):**

    | Grau | Nome     | Fórmula Intervalar        | Exemplo em C maior          | Característica Principal       |
    |------|----------|---------------------------|-----------------------------|--------------------------------|
    | I    | Jônio    | T – T – ST – T – T – T – ST | C – D – E – F – G – A – B   | Brilhante, estável (Escala maior) |
    | II   | Dórico   | T – ST – T – T – T – ST – T | D – E – F – G – A – B – C   | Menor com sexta maior          |
    | III  | Frígio   | ST – T – T – T – ST – T – T | E – F – G – A – B – C – D   | Oriental, sombrio              |
    | IV   | Lídio    | T – T – T – ST – T – T – ST | F – G – A – B – C – D – E   | Maior com quarta aumentada     |
    | V    | Mixolídio| T – T – ST – T – T – ST – T | G – A – B – C – D – E – F   | Maior com sétima menor         |
    | VI   | Eólio    | T – ST – T – T – ST – T – T | A – B – C – D – E – F – G   | Triste, introspectivo (Menor natural) |
    | VII  | Lócrio   | ST – T – T – ST – T – T – T | B – C – D – E – F – G – A   | Instável, dissonante           |

    ---

    ## 📌 Dicas para entender e aplicar:

    - **Jônio**: É o modo da escala maior tradicional. Ideal para músicas alegres e resolutivas.
    - **Dórico**: Mistura de menor com brilho. Muito usado no jazz, funk e música latina.
    - **Frígio**: Modo obscuro, muito comum no flamenco e no metal.
    - **Lídio**: Possui som etéreo e moderno, comum em trilhas sonoras e música cinematográfica.
    - **Mixolídio**: Perfeito para o blues, rock e música popular. Traz tensão leve com a 7ª menor.
    - **Eólio**: Modo da escala menor natural. Tristeza, melancolia e emoção.
    - **Lócrio**: Som instável e misterioso. Pouco usado sozinho, mas muito útil para criar tensão harmônica.

    ---

    ## 🧠 Como praticar?

    - Escolha um **modo** e toque suas notas no teclado ou instrumento;
    - Crie **acompanhamentos harmônicos** com base no modo;
    - Tente compor pequenas frases melódicas com a sonoridade do modo;
    - Compare dois modos seguidos (ex: Dórico vs Eólio) e perceba como muda a sensação sonora.

    ---

    ## 🎹 Exemplo prático: Escala de C maior e seus modos

    | Modo        | Notas                             |
    |-------------|-----------------------------------|
    | Jônio       | C – D – E – F – G – A – B         |
    | Dórico      | D – E – F – G – A – B – C         |
    | Frígio      | E – F – G – A – B – C – D         |
    | Lídio       | F – G – A – B – C – D – E         |
    | Mixolídio   | G – A – B – C – D – E – F         |
    | Eólio       | A – B – C – D – E – F – G         |
    | Lócrio      | B – C – D – E – F – G – A         |

    ---

    ## 🎯 Aplicações Musicais

    - **Jazz e improvisação modal**
    - **Rock progressivo e psicodélico**
    - **Música medieval e folclórica**
    - **Trilhas sonoras épicas**

    ---

    ### Quer explorar cada modo separadamente?

    Use os comandos:

    - `/modo_jonio`
    - `/modo_dorico`
    - `/modo_frigio`
    - `/modo_lidio`
    - `/modo_mixolidio`
    - `/modo_eolio`
    - `/modo_locio`

    """)

    def recursos():
        st.title("📚 Recursos Adicionais")

        recursos_text = """
    Explore aqui uma curadoria de **materiais gratuitos** para aprofundar seus estudos em Teoria Musical.

    """

        st.markdown(recursos_text)

        # SITES E SOFTWARES
        st.markdown("## 🌐 Sites e Softwares Gratuitos")
        st.markdown("""
    Ferramentas online para você praticar e aplicar os conhecimentos de teoria musical:

    - [🎸 Oolimo (Teoria e acordes para guitarra)](https://www.oolimo.com/en/)
    - [🎛️ BandLab (Estúdio de produção musical gratuito)](https://www.bandlab.com/)
    - [🎼 Song Maker (Google Music Lab)](https://musiclab.chromeexperiments.com/Song-Maker)
    - [🎹 Piano Eletrônico Virtual](https://www.pianoeletronico.com.br/index.html)
    - [🎹 Musicca – Piano interativo](https://www.musicca.com/pt/piano)
    - [🥁 Musicca – Bateria online](https://www.musicca.com/pt/bateria)
    - [🪘 Musicca – Caixa de ritmos](https://www.musicca.com/pt/caixa-de-ritmos)
    - [🕰️ Musicca – Metrônomo](https://www.musicca.com/pt/metronomo)
    - [🎵 Musicca – Gerador de acordes](https://www.musicca.com/pt/gerador-de-acordes)

    ---

    """)

        # VÍDEOS EDUCATIVOS
        st.markdown("## 🎥 Vídeos Educativos")
        st.markdown("""
    Vídeos selecionados para te ajudar a entender e visualizar os principais conceitos da teoria musical:

    - [🧠 Introdução à teoria musical](https://www.youtube.com/watch?v=oU4i59Mf8Yo)
    - [📜 História da música](https://www.youtube.com/watch?v=tL3Vx6KTNJ0)
    - [🕺 Ritmos musicais](https://www.youtube.com/watch?v=QLuHvLjl5t4)
    - [📏 Intervalos musicais](https://www.youtube.com/watch?v=Qh3CRTcPSg4)
    - [🌿 Escalas pentatônicas](https://www.youtube.com/watch?v=wN8tY790lxU)
    - [🌞 Escalas maiores](https://www.youtube.com/watch?v=qXbcZJTcpvA)
    - [🌑 Escalas menores](https://www.youtube.com/watch?v=eUrzhh_dHzU)
    - [🎷 Escala de blues](https://www.youtube.com/watch?v=3wbIsPLxF6U)
    - [🎶 Tríades](https://www.youtube.com/watch?v=6qoEfrEX_3A)
    - [🎵 Tétrades](https://www.youtube.com/watch?v=zZhpSEObMZ4)
    - [🔁 Inversões de acordes](https://www.youtube.com/watch?v=axUJrky7DT0)
    - [🏰 Campo harmônico maior](https://www.youtube.com/watch?v=ttzC5-VQ_Dc)
    - [🌌 Campo harmônico menor](https://www.youtube.com/watch?v=Q9MP_2woISQ)
    - [🔄 Ciclo das quartas](https://www.youtube.com/watch?v=soWL-r1vBD0)
    - [🔁 Ciclo das quintas](https://www.youtube.com/watch?v=8fIouuBa3pA)
    - [🔧 Modulação musical](https://www.youtube.com/watch?v=fXS2D7tX1t4)

    ---

    Aproveite esses recursos para estudar no seu ritmo e transformar a teoria em prática musical!
    """)


    # Exibindo conteúdo baseado na escolha do usuário
    if choice == "História":
        st.write("")
    elif choice == "Períodos Históricos":
        st.write("")
    elif choice == "Ritmos":
        st.write("")
    elif choice == "Intervalos":
        st.write("")
    elif choice == "Escalas Naturais":
        exibir_escalas()
    elif choice == "Acordes & Arpejos":
        acordes()
    elif choice == "Campos Harmônicos":
        harmonico()
    elif choice == "Modos Gregos":
        gregos()
    elif choice == "Recursos Adicionais":
        recursos()
