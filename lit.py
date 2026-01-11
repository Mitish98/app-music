import streamlit as st
import streamlit.components.v1 as components
import os
from PIL import Image
import base64

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
    menu = ["História", "Ritmo", "Intervalos", "Escalas Musicais", "Acordes & Arpejos", "Campos Harmônicos", "Tutoriais", "Recursos Adicionais"]
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
        

        if st.button("▶️ Ouvir Hymn to the Sun"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )

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

        if st.button("▶️ Ouvir De Spiritu Sancto"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344803/hwynylkgkytdtbriavxh.mp3")


        st.subheader("**- Leonin (1150–1201)**")
        st.markdown(""" monge ou cônego ligado à Catedral de Notre-Dame de Paris, foi um dos primeiros compositores a usar a notação moderna e é considerado o primeiro grande compositor de polifonia na história da música ocidental. Foi sucedido por Perotin, que desenvolveu ainda mais a técnica polifônica, escrevendo músicas a 3 e 4 vozes.

Ouça *Nostrum Organum Duplum*:
        """)

        if st.button("▶️ Ouvir Nostrum Organum Duplum"):
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


        if st.button("▶️ Ouvir Ave Maria ... virgo serena"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751486334/pcvqhxhbll6eacvxtlv5.mp3")


        st.subheader("**- Giovanni Palestrina (1525–1594)** ")
        st.markdown("""Palestrina foi um compositor italiano do Renascimento, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais. Seu estilo serviu como modelo pedagógico no estudo de contraponto, sendo estudado até hoje em conservatórios

Ouça *Missa Papae Marcelli*:
        """)

        if st.button("▶️ Ouvir Missa Papae Marcelli"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751488772/g0cuwgdeglakntyy6rgc.mp3")


        st.subheader("**- Orlando di Lasso (1532–1594)** ")
        st.markdown("""foi um compositor francês do Renascimento, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

Ouça *Lagrime di San Pietro: I. Il magnanimo Pietro*:
        """)

        if st.button("▶️ Ouvir Lagrime di San Pietro: I. Il magnanimo Pietro"):
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

        if st.button("▶️ Ouvir L`Orfeo"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")


        st.subheader("**- Antonio Vivaldi (1678-1741)**")
        st.markdown("""Um dos mais influentes músicos do Barroco e foi pioneiro no desenvolvimento do concerto instrumental, especialmente o concerto solo para violino. Ele escreveu mais de 500 concertos, além de óperas, cantatas, obras sacras e música de câmara. Como exímio violinista, suas obras exploram as possibilidades técnicas do instrumento, abrindo caminho para o concerto como forma de exibição da habilidade do solista. 
                    
Sua obra mais famosa, *Quatro Estações*, parte de um conjunto de 12 concertos onde Cada uma das estações (Primavera, Verão, Outono, Inverno) é representada por um concerto para violino. Cada peça é acompanhada de um soneto (provavelmente escrito pelo próprio Vivaldi) que descreve as cenas e sensações que a música retrata — como pássaros cantando, tempestades, brisa do outono, frio cortante etc.

Ouça *Four Seasons*:
        """)

        if st.button("▶️ Ouvir Four Seasons"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752259605/nhxy9zxf4qdyn9y8c8f3.mp3")

        st.subheader("**- Johann Sebastian Bach (1685-1750)** ")

        st.markdown("""É considerado um dos maiores gênios da história da música ocidental. Ele foi o ápice do estilo barroco, sintetizando com maestria todas as técnicas musicais de sua época — especialmente o contraponto, em que diferentes linhas melódicas se entrelaçam de forma complexa e harmônica. 
                    
Bach levou à perfeição gêneros como a fuga, a cantata, o concerto e a missão coral, criando obras que uniam profundidade espiritual, rigor técnico e beleza emocional. Sua música é ao mesmo tempo racional e sensível, estruturada e expressiva.
        
Uma de suas principais obras, *O Cravo Bem Temperado*, é uma coleção de prelúdios e fugas dividido em dois livro contendo 24 pares de peças — um prelúdio seguido de uma fuga — em todas as tonalidades maiores e menores, totalizando 48 peças ao todo.

O principal propósito de *O Cravo Bem Temperado* era mostrar a versatilidade do sistema tonal (uso das escalas maiores e menores) em todos os tons possíveis. Na época, existia um desafio técnico: a afinação dos instrumentos de teclado. Bach demonstrou que, com um sistema de afinação "temperado", era possível tocar em todas as tonalidades sem soar desafinado. Esse sistema temperado é o precursor do sistema de afinação moderna, em que o teclado é dividido de forma equilibrada para permitir modulações sem problemas sonoros.  
                    
Ouça uma de suas produções *Prelude and Fugue: No. 18 in G-Sharp Minor, BWV 887*:
                    """)
        
        if st.button("▶️ Ouvir Prelude and Fugue: No. 18 in G-Sharp Minor, BWV 887"):
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

        if st.button("▶️ Ouvir Symphony No. 25 in G minor"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752286273/bvzu89jgalpsqucqo3gt.mp3")

        st.subheader("**- Ludwig van Beethoven (1770–1827)**")
        st.markdown("""Redefiniu o papel da música, transformando-a de uma arte cortesã e decorativa em um veículo de expressão pessoal, emoção profunda e ideia filosófica. Ele é a figura de transição entre o Classicismo e o Romantismo, e sua vida e obra são uma jornada intensa de luta, superação, inovação e legado eterno.
                    
Escreveu em praticamente todos os gêneros musicais da época: sinfonias, sonatas, quartetos, concertos, óperas e música coral. Mas o que o diferencia não é a quantidade, e sim o impacto profundo de sua arte. 
                    
Beethoven via a música como drama puro, e é o primeiro compositor a tratar a estrutura musical como uma narrativa emocional. Isso influenciou profundamente os românticos: temas como luta, superação, liberdade e transcendência se tornaram o novo padrão.

Ouça uma de suas obras *Symphony No. 5, Op. 67*:
        """)

        if st.button("▶️ Ouvir Symphony No. 5, Op. 67"):
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

        if st.button("▶️ Ouvir Nocturne in E Flat Major (Op. 9 No. 2)"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1752335948/ymupj0sgwkyen9djqgwc.mp3")

        st.subheader("**- Piotr Ilitch Tchaikovsky (1840–1893)**")

        st.markdown("""Suas obras são marcadas por temas emocionantes, muitas vezes melancólicos. Ele transmitia suas crises pessoais, amores não correspondidos e sentimentos de angústia em sua música.

Tchaikovsky era um mestre da melodia emocional, da orquestração brilhante e da forma dramática. Embora sua linguagem fosse enraizada no romantismo europeu, seu espírito russo deu à sua música uma identidade inconfundível. Compôs sinfonias, concertos, óperas e balés como *O Lago dos Cisnes (1876)* e *A Bela Adormecida (1890)*. 

Ouça uma de suas sinfonias *Symphony No. 5 in E Minor Op. 64*:
        """)

        if st.button("▶️ Ouvir Symphony No. 5 in E Minor Op. 64"):
            st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")


        st.header("🎼 Estilos Musicais Contemporâneos")

        st.markdown("""
        A música é uma linguagem universal, moldada por séculos de intercâmbio entre culturas ao redor do mundo, sendo sua história muito mais abrangente do que o estudado pela tradição europeia. Cada sociedade desenvolveu estruturas e padrões rítmicos únicos que contribuíram de forma profunda para a diversidade da música contemporânea, veja alguns exemplos de gêneros musicais ao redor do mundo:

        - **Blues**: Base estrutural de grande parte da música popular ocidental, o blues nasceu da experiência afro-americana no sul dos EUA. Caracteriza-se por formas simples, expressividade intensa, uso de blue notes e uma relação direta entre música e emoção.            
        - **Jazz**: Surgido nos Estados Unidos a partir da herança africana e da harmonia europeia, o jazz consolidou a improvisação como linguagem central. Seu desenvolvimento passou pelo blues, swing, bebop, modal e fusion, influenciando praticamente toda a música popular contemporânea em termos de harmonia, ritmo e liberdade expressiva.
        - **Rock**: Resultado direto do blues e do rhythm & blues, o rock tornou-se um fenômeno cultural global. Ao longo das décadas, incorporou elementos do jazz, da música clássica, do folk e de tradições locais, dando origem a inúmeros subgêneros e movimentos estéticos.
        - **Reggae**: Originário da Jamaica, o reggae combina heranças africanas, caribenhas e cristãs, com forte ênfase no contratempo (offbeat). Tornou-se uma poderosa ferramenta de identidade cultural, resistência política e espiritualidade.
        - **Música Latina e Afro-Caribenha**: Estilos como salsa, rumba, son, mambo e cumbia derivam de estruturas rítmicas complexas baseadas na clave, um princípio organizador que guia acentos e frases musicais. Esses estilos influenciaram profundamente o jazz, o pop e a música brasileira.
        - **Música Eletrônica**: A partir do século XX, a tecnologia passou a integrar o processo criativo musical. Gêneros como techno, house, ambient e drum & bass exploram repetição, textura sonora, timbre e ritmo de forma inovadora, muitas vezes dialogando com tradições rítmicas antigas em novos contextos.
        - **World Music e Fusões Contemporâneas**: Termo que abrange projetos musicais que conectam tradições locais com linguagens modernas. Essas fusões mostram que a música contemporânea é, cada vez mais, um território híbrido e multicultural.

        Explorar esses estilos não é apenas aprender gêneros, mas compreender diferentes formas de organizar o tempo, o som e a expressão humana. Esse conhecimento amplia o vocabulário musical, aprofunda a escuta e fortalece a identidade artística do músico.

        Compreender esses ritmos amplia a percepção e a criatividade musical. Veja mais detalhes de alguns dos principais estilos da música contemporânea ao redor do mundo: 
        """)

    if choice == "Ritmo":
        st.title("🥁 Ritmos Musicais")

        st.markdown("""
        Junto com a harmonia e a melodia, o ritmo é um dos três elementos fundamentais da música, sendo o responsável pela organização do tempo das notas e acordes que estão sendo tocados definindo quando os sons acontecem e por quanto tempo eles duram. 
                    
Sem noções de ritmo não há sensação de continuidade musical e definitivamente não é possível criar coesão entre diferentes vozes (violão + canto + bateria + baixo ...) e, por isso, estudar a teoria do ritmo é fundamental para te desenvolver como um músico. 
           
        """)

        st.header("Conceitos Fundamentais de Ritmo")

        st.markdown("""Para entender como funciona o ritmo dentro da música, precisamos entender conceitos como:
- Pulso
- Tempo
- Compasso
- Acentuação
- Contra-tempo
- Figuras rítmicas               
                    
Com eles, podemos entender o ritmo para criar músicais que seja recursivas, ou seja, que admitem a inserção de novas vozes no arranjo. A seguir, vamos nos aprofundar cada um desses conceitos para dominar e executar corretamente: 
                    
                     """)

        st.subheader("Pulso (Beat)")

        st.markdown("""
        O pulso é a batida regular e constante que sentimos na música — aquilo que nos faz bater o pé ou balançar a cabeça. 
                    
        Normalmente, é medido pelo metrônomo e calculado em forma de batidas por minuto (BPM) sendo o que garante que todos os músicos de uma banda estejam "no tempo certo" da música. Sendo assim, o pulso deve ser estável e não mudar mesmo que as notas e durações das notas mudem, funcionando como um relógio musical a ser seguido. 
                    
        Por exemplo: 
        
        - Beat *Lento* (~60 BPM)
        - Beat *Moderado* (~90–120 BPM)
        - Beat *Rápido* (~140+ BPM)
                    
        A sequência de pulsos é chamada de tempo e indica a velocidade como cada pulso bate. 

        """)

        st.subheader("Compasso")

        st.markdown(""" 
        O compasso é o que organiza a música em um conjunto de pulsos para criar um bloco rítmico. É o conceito responsável por mapear o local de uma canção e garantir que todos estejam na mesma parte de uma música, podendo ser entendido como um "mapa músical". 
                    
        Sendo assim, esse mapa chamado compasso pode organizar 3 pulsos de uma vez, 4 pulsos de uma vez, 5 pulsos de uma vez e assim por diante, representado por frações como ... e permitem com que os músicos separem as partes musicais por compassos, como por exemplo: o primeiro compasso de uma música, o décimo compasso de uma música e o último compasso de uma música. 

        - O número de cima indica quantos pulsos há no compasso.
        - O número de baixo indica o valor da figura rítmica.

        """)

        st.subheader("Acentuação Ritmica")

        st.markdown("""

A acentuação é um recurso expressivo que dá enfâse a um ou outro pulso dentro de um compasso, fazendo com que nem todos os pulsos tenham o mesmo peso. 
                    
Em geral, um pulso é forte enquanto os outros do compasso são fracos e, normalmente, o primeiro pulso é quem tem o maior peso no compasso. Por exemplo: 
                    
- 4/4 → Forte e bem marcado – fraco – fraco – fraco

- 3/4 → Forte e bem marcado – fraco – fraco 

""")
        st.subheader("Contra-tempo")

        st.markdown("""Contra-tempo é a execução de um som nas subdivisões intermediárias do pulso, isto é, entre um tempo e outro do compasso. Por exemplo, se no compasso temos os pulsos 1 2 3 4, o contra-tempo seria o espaço que existe entre o pulso 1 e o 2, entre o 2 e o 3 , entre o 3 e 4 e assim por diante. 
                    
De forma prática, para encontrá-lo normalmente podemos inserir a letra "e" na contagem do tempo. Por exemplo: 

*1 **e** 2 **e** 3 **e** 4*

Cada uma dessas letras "e" marca o contra-tempo dentro de um compasso. 
                    
""")
        
        st.info("""⚠️ Se formos mais adiante na teoria, podemos perceber que entre um contra-tempo e o pulso (entre o 'e' e o pulso 2, por exemplo) existe uma nova subdivisão, podendo dividir o compasso em infinitas subunidades assim como um número fracionário. 
                
Mas, de forma prática, o mais utilizado são os pulsos numéricos tradicionais do compasso e a primeira divisão de contra-tempo entre eles representado pela letra 'e'.""")

        st.subheader("Figuras Rítmicas")

        st.markdown("""
        As figuras rítmicas indicam a duração dos sons dentro de cada pulso. Sendo que as principais são:

- **Semibreve** (𝅝): 4 tempos
- **Mínima** (𝅗𝅥): 2 tempos
- **Semínima** (𝅘𝅥): 1 tempo
- **Colcheia** (𝅘𝅥𝅮): ½ tempo
- **Semicolcheia** (𝅘𝅥𝅯): ¼ tempo

É importante compreender que essas durações são sempre relativas ao pulso do compasso. Ou seja, as figuras rítmicas não duram um compasso inteiro por si mesmas, mas sim um determinado número de tempos.

Por exemplo, um compasso 4/4 pode ser preenchido de diversas formas, entre elas: *4 semínimas, 2 mínimas, 1 semibreve, 8 colcheias, ou qualquer combinação que complete os 4 pulsos no tempo*. 
                    
Sendo assim, um único pulso pode conter até 8 figuras ritmicas (colcheia) e, ainda sim, respeitar o tempo lento de uma música.  
                    
Outro exemplo que diferencia pulso de figura ritmica é que, se uma semibreve aparecer no pulso 3 de um compasso 4/4, por exemplo, a duração dela vai extrapolar o compasso em que ela apareceu e atuar até o pulso 2 do compasso seguinte. 

E, se a semibreve aparecer no pulso 1 de um compasso maior (6/8, por exemplo) ela não vai preencher totalmente a duração do compasso e ainda será necessário preenchê-lo com silêncio ou então com outras figuras ritmicas até começar o compasso seguinte. 

Portanto, o pulso funciona como a referência do tempo, enquanto as figuras rítmicas representam como esse tempo é ocupado e dividido dentro do compasso.
        
        """)

        st.success("""✅ **De forma prática, podemos fazer um paralelo entre esses conceitos de ritmo musical e uma caminhada:** 
                   
- Pulsos são os passos que damos
- Compassos são as sequências de passos 
- Figuras ritmicas são os tamanhos dos passos em uma caminhada
                   
Por exemplo, nós podemos dar 4 passos curtos, 2 passos longos ou 1 passo muito longo e, ainda sim, percorrer o mesmo caminho. 
                   
                   
                   """)

        st.header("Conceitos Avançados de Ritmo")

        st.markdown("""Após compreender os elementos fundamentais do ritmo — pulso, compasso, acentuação, contra-tempo e figuras rítmicas — podemos avançar para conceitos que ampliam a expressividade musical e permitem uma maior complexidade rítmica nos arranjos e composições.
""")

        st.subheader("Síncope")

        st.markdown("""
A síncope ocorre quando um som é iniciado em um tempo fraco ou contra-tempo e se prolonga sobre o tempo forte seguinte, fazendo com que esse tempo forte deixe de ser marcado.

Diferente do contra-tempo, onde o som acontece apenas entre os pulsos, na síncope o som invade o pulso forte, criando uma sensação de deslocamento rítmico ainda mais evidente.

Por exemplo, em um compasso 4/4:

1 **e** 2 **e** 3 **e** 4  
                    
Se uma nota começa no “e” do tempo 1 e se estende até o tempo 2, o pulso 2 deixa de ser acentuado, caracterizando uma síncope.

A síncope é um dos elementos mais importantes da música popular e aparece com força em estilos como samba, jazz, funk, reggae, rock e música brasileira em geral, sendo fundamental para a criação de balanço, groove e identidade rítmica.
        """)

        st.subheader("Polirritmia")

        st.markdown("""
A polirritmia acontece quando dois ou mais padrões rítmicos diferentes são executados simultaneamente, mantendo pulsos ou divisões distintas entre si.

Esses ritmos coexistem dentro do mesmo tempo musical, criando camadas rítmicas independentes que se complementam.

Um exemplo simples de polirritmia é:
- uma mão batendo em 2 tempos
- enquanto a outra bate em 3 tempos, dentro do mesmo intervalo de tempo

Mesmo quando não percebida conscientemente, ela contribui para a riqueza rítmica e para a sensação de profundidade do arranjo.
        """)

        st.subheader("Organização temporal")

        st.markdown("""
                    
Além do ritmo interno dos compassos, a música também se organiza ritmicamente em estruturas maiores ao longo do tempo, formando seções que se repetem, contrastam e se desenvolvem para a criação de uma canção.

Essa organização é feita através da quantidade de compassos e é chamada de forma musical, sendo entendida como ritmo em grande escala de uma música.
                    
#### Intro
Quantidade estimada de compassos: 2 a 8
                    
A introdução estabelece o pulso, o andamento e o caráter rítmico da música. Ela prepara o ouvinte para o que virá, muitas vezes apresentando o groove principal ou criando expectativa.            

#### Verso
Quantidade estimada de compassos: 8 a 24

O verso geralmente possui uma estrutura rítmica única e estável, servindo como base para a narrativa da música. É comum que vários versos compartilhem exatamente o mesmo padrão rítmico com variações na letra, melodia ou harmônia.

#### Ponte
Quantidade estimada de compassos: 2 a 8
                    
A ponte quebra o ciclo rítmico estabelecido anteriormente. Ela cria contraste, variação e renovação do interesse do ouvinte, muitas vezes alterando o ritmo, a densidade ou a acentuação para criar tensão suficiente entre o verso e o refrão.             

#### Refrão
Quantidade estimada de compassos: 8 a 12           

O refrão é a seção mais marcante e memorável da música. Ritmicamentre, costuma ser mais enfático, com acentuações mais claras ou padrões mais amplos, reforçando a sensação de chegada.

#### Interlúdio
Quantidade estimada de compassos: 2 a 8
                    
O interlúdio é uma seção instrumental que ocorre entre partes da música, normalmente dividindo ao meio a canção. Ele serve para criar transição, respiro ou variação, mantendo o pulso e o andamento enquanto explora novas ideias rítmicas ou harmônicas, timbres ou texturas sem a presença da voz principal. Normalmente, é onde guitarristas ou pianistas colocam os solos.

#### Verso '
Quantidade estimada de compassos: 8 a 24

Após a ponte ou interlúdio, o retorno ao verso ou ao refrão gera uma sensação de familiaridade, pois o ritmo já foi assimilado pelo ouvinte. Esse retorno pode manter o mesmo padrão rítmico do verso inicial ou apresentar pequenas variações para evitar repetição excessiva.

#### Desfecho
Quantidade estimada de compassos: 2 a 8
                    
O desfecho encerra a organização temporal da música. Pode repetir o refrão, desacelerar o ritmo, reduzir gradualmente os elementos ou finalizar de forma abrupta, dependendo da proposta musical.
""")
        
        st.info("""⚠️ As secções da organização temporal não são mandatórias, ou seja, não é preciso colocar obrigatoriamente todas elas juntas para formar uma música. 

Essas são apenas as secções que usualmente aparecem na música popular, mas não são todas que possuem intro, interlúdio, desfecho ou até mesmo refrão. A escolha em inserir uma secção ou outra depende da inteção do artista e do objetivo que ele tem com a obra""")

        st.success("""✅ É muito comum que compositores utilizem a periodicidade métrica de compassos, ou seja, organizem as estruturas musicais em ciclos regulares e previsíveis para facilitar a memorização. 

Sendo assim, grande parte da música popular é estruturada a partir de frases de 4 compassos, formando seções de 8, 16 ou 32 compassos. Essa organização, conhecida como forma quadrada, facilita a percepção do tempo pelo ouvinte e a interação entre os músicos, criando ciclos rítmicos previsíveis e funcionais. Ex:

- 4 compassos (intro)

- 8 compassos (refrão)

- 16 compassos (verso)

Isso facilita a memória e aguça a percepção intuitiva da troca já que o cérebro reconhece o padrão com mais facilidade ao perceber 2 + 2, depois 4, depois 8, depois 16 e assim por diante para formar ciclos de tensão e resolução que funcionam independentemente e em conjunto ao mesmo tempo. 
                   
Com esse padrão, o ouvinte sente claramente o começo, meio e fim de cada parte como também percebe o começo meio e fim da obra como um todo, criando uma previsibilidade e segurança saudável sem causar monotonia. 
                   
Mas, lembre-se que isso não é uma regra, e sim apenas uma convenção funcional que facilita a composição e percepção do público; mas, se usado com maestria, a quebra desse padrão pode gerar um recurso artístico interessante para quebrar expectativas, se usado conscientemente.  
                   
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
| Nome do Intervalo       | Distância | Exemplo        | Qualidade             |
|-------------------------|-----------|----------------|------------------------|
| Uníssono                | 0T        | C – C          | Consonante            |
| Segunda menor           | ½T        | C – C♯/D♭       | Dissonante            |
| Segunda maior           | 1T        | C – D          | Dissonante            |
| Terça menor             | 1½T       | C – E♭         | Consonante imperfeita |
| Terça maior             | 2T        | C – E          | Consonante imperfeita |
| Quarta justa            | 2½T       | C – F          | Consonante            |
| Quarta aumentada / Quinta diminuta | 3T | C – F♯/G♭ | Dissonante |
| Quinta justa            | 3½T       | C – G          | Consonante            |
| Sexta menor             | 4T        | C – A♭         | Consonante imperfeita |
| Sexta maior             | 4½T       | C – A          | Consonante imperfeita |
| Sétima menor            | 5T        | C – B♭         | Dissonante            |
| Sétima maior            | 5½T       | C – B          | Dissonante            |
| Oitava justa            | 6T        | C – C (oitava) | Consonante            |
""")


        st.markdown("""*Os aúdios tocam os intervalos de uma mesma oitava e, depois, o intervalo entre uma oitava a cima*
                """)
    

        st.info("""**Dica¹:** Liste os intervalos musicais partindo da referência de outras notas. 
        
**Dica²:** Identifique no seu instrumento onde estão esses intervalos.

**Dica³:** Treine a identificação de intervalos de ouvido a partir de aplicativos como Tenuto, Perfect Ear ou teoria online como teoria.com.
        
        
        """)

        st.subheader("Oitavas")
        st.markdown("- Distância: 0 Tons / 6 Tons")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598963/image_arrwmk.png", caption="Representação com tônica em Mi (E)")


        st.subheader("Segunda Menor")
        st.markdown("- Distância: 0,5 Tons")
        st.markdown("- Qualidade: Dissonante ")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598964/image_1_uqbyfj.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Segunda Maior")
        st.markdown("- Distância: 1 Tons ")
        st.markdown("- Qualidade: Dissonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598964/image_2_kixclb.png", caption="Representação com tônica em Mi (E)")
        
        st.subheader("Terça Menor")
        st.markdown("- Distância: 1,5 Tons ")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598963/image_3_o1e1sb.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Terça Maior")
        st.markdown("- Distância: 2 Tons")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766599230/image_11_yhlqql.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Quarta Justa")
        st.markdown("- Distância: 2,5 Tons")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766599173/image_9_pntt5l.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Quarta Aumentada / Quinta Diminuta (Trítono)")
        st.markdown("- Distância: 3 Tons")
        st.markdown("- Qualidade: Dissonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598963/image_4_zrbzue.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Quinta Justa")
        st.markdown("- Distância: 3,5 Tons")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598963/image_5_f62wic.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Sexta Menor")
        st.markdown("- Distância: 4 Tons")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766599270/image_12_lyyqsl.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Sexta Maior")
        st.markdown("- Distância: 4,5 Tons ")
        st.markdown("- Qualidade: Consonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598964/image_6_jd0yg8.png", caption="Representação com tônica em Mi (E)")

        st.subheader("Sétima Menor")
        st.markdown("- Distância: 5 Tons ")
        st.markdown("- Qualidade: Dissonante ")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598963/image_7_irqlsy.png", caption="Representação com tônica em Mi (E)")
        
        st.subheader("Sétima Maior")
        st.markdown("- Distância:  5,5 Tons")
        st.markdown("- Qualidade: Dissonante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766598963/image_8_ckyguj.png", caption="Representação com tônica em Mi (E)")



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

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425184/image_fgi49h.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425181/image_1_w4dasc.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425180/image_2_oxrrur.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425180/image_3_yspcit.png")

        

        st.header("🎸 Escala Blues (6 notas)")

        st.markdown("""
        A **escala blues** deriva da escala pentatônica menor com a adição de uma nota chamada **blue note** (quinta diminuta), que dá seu caráter expressivo e melancólico.
""")
        
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425179/image_4_ugefvj.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425180/image_5_yza7x4.png")


        st.header("🔸 Escalas Maiores (7 notas)")

        st.markdown("""
        As **escalas maiores** (natural, harmônica e melódica) são fundamentais na teoria musical ocidental. Cada variação introduz alterações que afetam o caráter melódico e harmônico da música.

        | Tipo              | Distância                          | Intervalos                                 
        |-------------------|-------------------------------------|--------------------------------------------
        | Maior Natural     | T - T - ST - T - T - T - ST         | 1ª - 2ªM - 3ªM - 4ªJ - 5ªJ - 6ªM - 7ªM      

        """)

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766579876/image_qkphhz.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766579876/image_1_vxbqmb.png")

        st.header("🔹 Escalas Menores (7 notas)")

        st.markdown("""
        As **escalas menores** têm uma sonoridade introspectiva, emotiva ou melancólica. Existem três variações principais que se diferenciam especialmente nos graus 6 e 7:

        | Tipo              | Distância                             | Intervalos                                
        |-------------------|----------------------------------------|-------------------------------------------
        | Menor Natural     | T - ST - T - T - ST - T - T            | 1ª - 2ªM - 3ªm - 4ªJ - 5ªJ - 6ªm - 7ªm     
   
        """)

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766579876/image_2_negevb.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766579876/image_3_rd1ikt.png")


        st.success("💡 **Dica:** experimente tocar as escalas no seu instrumento em diferentes tons para sentir como cada uma afeta a sonoridade da música.")


        st.header(" 🔁 Escalas Relativas")

        st.markdown("""Escalas relativas são pares de escalas maior e menor que compartilham as mesmas notas e armadura de clave, mas têm tônicas (notas iniciais) diferentes. Cada escala maior tem uma relativa menor, e vice-versa. 
                    
""")

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766425567/escalas_jdmccj.jpg")

        st.success("💡 **Dica:** Para achar a relativa menor de uma escala maior desça 1 tom e meio (3 semitons) da tônica. Para achar a relativa maior de uma escala menor suba 1 tom e meio (3 semitons) da tônica.")
        st.header("O Sistema CAGED nas Escalas Naturais")
        st.markdown("O sistema CAGED é frequentemente utilizado no estudo das escalas naturais como uma referência para a sequência de notas que está sendo executada. Ao identificar a terça e a quinta da escala, é possível localizar o acorde de referência naquela região do instrumento, facilitando a visualização da harmonia e a aplicação prática no braço")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766970692/CAGED_in_Major_Pentatonic_Scale_-_Made_at_Guitarscientist.com_hisoo8.png")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766970350/CAGED_in_Minor_Pentatonic_Scale_-_Made_at_Guitarscientist.com_1_w1bilj.png")
        st.header("Demais Escalas Musicais...")
        st.markdown("""
        Além das escalas mais utilizadas na música tonal (maiores, menores, pentatônicas e blues), 
        existe uma enorme variedade de escalas alternativas, modais, simétricas, étnicas e experimentais.

        Cada escala surge a partir de uma organização específica de intervalos e cumpre funções musicais diferentes, como por exemplo : criar harmônicas específicas, produzir sensações de tensão, repouso ou instabilidade que fogem do comum, definir uma identidade sonora de única de estilos musicais diferentes, servir como uma base criativa para improvisação, composição e trilhas sonoras para explorar sonoridades não tradicionais que fogem dos padrões da tonalidade. 

        Muitas dessas escalas são amplamente usadas no jazz, música erudita moderna, música oriental, trilhas de filmes, metal, fusion e música experimental.
        """)

        st.markdown("""
        Abaixo está uma visão geral de **outras escalas musicais**, além das mais comuns, 
        usadas para expandir o vocabulário melódico, harmônico e expressivo do músico.
        """)
        
        st.markdown("""
        | Escala                         | Nº de Notas | Característica Sonora / Função Principal                          | Uso Comum / Estilo Musical              |
        |--------------------------------|-------------|---------------------------------------------------------------------|------------------------------------------|
        | Harmônica Menor                | 7           | Exótica, dramática, dominante forte                                 | Clássica, Flamenco, Metal               |
        | Melódica Menor                 | 7           | Flexível, moderna, rica harmonicamente                              | Jazz, Fusion                             |
        | Octatônica        | 8           | Simétrica, alta tensão                                              | Jazz, Música Contemporânea              |
        | Tons Inteiros                  | 6           | Flutuante, ambígua, sem centro tonal claro                           | Jazz, Trilhas Sonoras                   |
        | Super Lócria      | 7           | Máxima tensão sobre acordes dominantes                               | Jazz                                    |
        | Bebop                          | 8           | Fluxo rítmico contínuo em semicolcheias                              | Jazz tradicional                        |
        | Frígia Dominante               | 7           | Oriental, intensa, dominante                                        | Flamenco, Música Árabe                  |
        | Cromática                     | 12          | Todas as notas possíveis                                             | Estudo técnico, Música Experimental     |
        | Sintéticas                     | Variável    | Criadas artificialmente para fins específicos                        | Composição e Experimentação             |
        | Microtonais                    | Variável    | Intervalos menores que o semitom                                     | Música Contemporânea / Experimental     |
        """)

    
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

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766972833/CAGED_in_Major_Triads_1_-_3_-_5_-_Made_at_Guitarscientist.com_t3qujh.png", caption="Acordes Maiores")

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766972703/CAGED_in_Minor_Triads_I_-_b3_-_5_-_Made_at_Guitarscientist.com_kv79zv.png", caption="Acordes Menores")

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

        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766974098/CAGED_in_Maj7_1_-_3_-_5_-_7_-_Made_at_Guitarscientist.com_t1x6ej.png", caption="Acordes Maiores com Sétima Maior")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766974517/CAGED_in_m7_1_-_b3_-_5_-_b7_-_Made_at_Guitarscientist.com_ufclig.png", caption="Acordes Menores com Sétima Menor")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766974654/CAGED_in_Dominant_7_1_-_3_-_5_-_b7_-_Made_at_Guitarscientist.com_a6jn01.png", caption="Acordes Dominantes")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766974911/CAGED_in_m7_5_1_-_b3_-_b5_-_b7_-_Made_at_Guitarscientist.com_pc306m.png", caption="Acordes Meio-Diminutos")



        st.title("🎼 Arpejos")

        st.markdown("""
        Um **arpejo** é quando as notas de um acorde são tocadas **sequencialmente**, uma após a outra, em vez de simultaneamente. Isso cria um efeito melódico com base na harmonia do acorde e é muito usado em solos, acompanhamento e improvisação.

        Os arpejos também podem ser tocados de forma ascendente, descendente ou alternada, e são uma ferramenta essencial para explorar a sonoridade dos acordes no tempo.
        """)
        st.header("Tríade Maior (1 - 3 - 5)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766423844/image_rwbv5u.png", caption="Representação visual dos intervalos da tríade maior")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766423885/image_1_ok4oii.png", caption="Representação visual das notas da tríade maior")

        st.header("Tríade Menor (1 - b3 - 5)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424139/image_onkic5.png", caption="Representação visual dos intervalos da tríade menor")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424139/image_1_wsyivr.png", caption="Representação visual das notas da tríade menor")

        st.header("Tríade Diminuta (1 - b3 - b5)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424140/image_2_q7vq7q.png", caption="Representação visual dos intervalos da tríade diminuta")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424140/image_3_wzwedu.png", caption="Representação visual das notas da tríade diminuta")



        st.header("Tétrade Maior (1 - 3 - 5 - 7)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424140/image_4_hbazat.png", caption="Representação visual dos intervalos da tétrade maior")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424144/image_5_ww5skn.png", caption="Representação visual das notas da tétrade maior")


        st.header("Tétrade Menor (1 - b3 - 5 - b7)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424145/image_6_omcdoy.png", caption="Representação visual dos intervalos da tétrade menor")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424145/image_7_hbfxre.png", caption="Representação visual das notas da tétrade menor")


        st.header("Tétrade Dominante (1 - 3 - 5 - b7)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424145/image_8_gtcgyx.png", caption="Representação visual dos intervalos da tétrade dominante")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424145/image_9_g5413x.png", caption="Representação visual das notas da tétrade dominante")




        st.header("Tétrade Meia-Diminuta (1 - b3 - b5 - b7)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424148/image_10_lqqev7.png", caption="Representação visual dos intervalos da tétrade meia-diminuta")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424148/image_11_t9f2bs.png", caption="Representação visual das notas da tétrade meia-diminuta")


        st.header("Tétrade Menor com Sétima Maior (1 - b3 - 5 - 7)")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424149/image_12_z1uagj.png", caption="Representação visual dos intervalos da tétrade menor com sétima maior")
        st.image("https://res.cloudinary.com/dkbvui6sx/image/upload/v1766424150/image_13_noqiua.png", caption="Representação visual das notas da tétrade menor com sétima maior")


        st.title("Acordes Sofisticados")

        st.markdown("""
Os acordes sofisticados surgem quando vamos além das estruturas básicas de tríades e tétrades e começamos a explorar o movimento interno dos intervalos de uma escala para alcançar diferentes cores harmônicas, tensões controladas e resoluções criativas.

Assim, esses acordes servem principalmente para ampliar possibilidades expressivas e refinar o discurso musical do artista. E, por isso, vamos ver alguns dos principais conceitos que podem ampliar o seu vocabulário como músico.  

""")

        st.header("Inversões")

        st.markdown("""
Uma inversão ocorre quando a nota mais grave do acorde não é a tônica.

As inversões não mudam o nome do acorde, mas alteram o encadeamento, o movimento do baixo e a sensação de fluidez.
""")
        
        st.markdown("""
Exemplo: *Cmaj7 (C – E – G – B)*

| Posição | Sequência de notas | Nota do baixo | Notação |
|-------|-------------------|---------------|---------|
| Posição fundamental | C – E – G – B | C | Cmaj7 |
| 1ª inversão | E – G – B – C | E | Cmaj7/E |
| 2ª inversão | G – B – C – E | G | Cmaj7/G |
| 3ª inversão | B – C – E – G | B | Cmaj7/B |
""")
        
        st.success("""
🎯 **Por que usar inversões?**
- Criar linhas de baixo melódicas
- Evitar saltos grandes entre acordes
- Melhorar o encadeamento harmônico
- Dar sensação de movimento contínuo
""")


        st.header("Acordes com Extensões")
        st.markdown("""
Os acordes com 9ª, 11ª e 13ª surgem quando continuamos o empilhamento de terças além da sétima.

Essas extensões não criam novos acordes independentes, mas expandem a sonoridade dos acordes já existentes, adicionando cor, tensão e sofisticação à progressão.
""")
        st.subheader("Acordes com 9°")

        st.markdown("""
A 9ª é a mesma nota da 2ª, porém pensada uma oitava acima. Ela traz suavidade, riqueza harmônica e sensação de espaço ao acorde.

| Tipo de Acorde | Fórmula | Exemplo | Notação do Exemplo |
|----------------|--------|---------|-------------------|
| Maj9 | 1 – 3 – 5 – 7 – 9 | C – E – G – B – D | Cmaj9 |
| m9 | 1 – ♭3 – 5 – ♭7 – 9 | D – F – A – C – E | Dm9 |
| 9 (dominante) | 1 – 3 – 5 – ♭7 – 9 | G – B – D – F – A | G9 |
""")

        st.info("""
🎯 **Uso musical:**  
- Muito comum em Jazz, MPB, Soul e Pop moderno  
- Excelente para acordes de tônica e subdominante  
- Em dominantes, aumenta a tensão sem ficar agressivo
""")

        st.subheader("Acordes com 11ª")

        st.markdown("""
A 11ª corresponde à 4ª da escala e adiciona uma sensação mais aberta, suspensa e modal. Em acordes maiores, a 11ª pode colidir com a 3ª maior ao criar o intervalo de trítono e, por isso, muitas vezes usa-se sus4 ou 11#.
        
| Tipo de Acorde | Fórmula | Exemplo | Notação do Exemplo |
|----------------|--------|---------|-------------------|
| m11 | 1 – ♭3 – 5 – ♭7 – 9 – 11 | D – F – A – C – E – G | Dm11 |
| 11 (dominante) | 1 – 3 – 5 – ♭7 – 9 – 11 | G – B – D – F – A – C | G11 |
| sus4 | 1 – 4 – 5 – ♭7 | G – C – D – F | G7sus4 |
""")

        st.info("""
🎯 **Uso musical:**  
- Cria sensação de suspensão  
- Muito usada em contextos modais e grooves  
- Ótima para evitar resoluções óbvias
""")

        st.subheader("Acordes com 13ª")

        st.markdown("""
A 13ª corresponde à 6ª da escala e traz um som rico, elegante e sofisticado. Na prática, muitos acordes com 13ª não usam todas as notas — escolhem-se as mais importantes para manter clareza sonora.
        
| Tipo de Acorde | Fórmula | Exemplo | Notação do Exemplo |
|----------------|--------|---------|-------------------|
| 13 | 1 – 3 – 5 – ♭7 – 9 – 13 | G – B – D – F – A – E | G13 |
| m13 | 1 – ♭3 – 5 – ♭7 – 9 – 11 – 13 | D – F – A – C – E – G – B | Dm13 |

""")

        st.info("""
🎯 **Uso musical:**  
- Muito comum em dominantes finais  
- Ideal para cadências sofisticadas  
- Muito usada em Jazz, Fusion e MPB
""")
        
        st.header("Acordes Suspensos")

        st.markdown("""
Os acordes suspensos (sus) são acordes que não possuem a 3ª, a nota responsável por definir se o acorde é maior ou menor. Ou seja, os acordes suspensos não possuem a definição de maiores ou menores.

Ao remover a 3ª e substituí-la por outra nota, criamos uma sensação de suspensão, expectativa e ambiguidade tonal por não serem nem maiores e nem menores. 
""")

        st.subheader("Sus2 e Sus4")

        st.markdown("""
A diferença entre sus2 e **sus4 está na nota que substitui a 3ª do acorde.
        
| Tipo de Acorde | Fórmula | Exemplo | Notação do Exemplo |
|----------------|--------|---------|-------------------|
| sus2 | 1 – 2 – 5 | C – D – G | Csus2 |
| sus4 | 1 – 4 – 5 | C – F – G | Csus4 |
""")

        st.info("""
🎯 **Sensação sonora:**  
- **Sus2:** som aberto, leve e moderno  
- **Sus4:** mais tensão, sensação clara de suspensão  
""")

        st.subheader("Acordes Suspensos com Sétima")

        st.markdown("""
Os acordes suspensos também podem aparecer com **7ª**, especialmente em contextos dominantes.
Nesse caso, eles criam uma forte expectativa de resolução.
        
| Tipo de Acorde | Fórmula | Exemplo | Notação |
|----------------|--------|---------|---------|
| 7sus4 | 1 – 4 – 5 – ♭7 | G – C – D – F | G7sus4 |
| 9sus4 | 1 – 4 – 5 – ♭7 – 9 | G – C – D – F – A | G9sus4 |
""")

        st.success("""
🎯 **Uso musical:**  
- Muito comum antes de dominantes tradicionais  
- Excelente para evitar resoluções óbvias  
- Muito usado em Jazz, Funk, Gospel, MPB e Pop  
""")



        st.markdown("""
A característica mais importante dos acordes suspensos é que eles tendem a resolver para um acorde com a 3ª. Por exemplo:

- Csus4 → C
- Dsus2 → D
- G7sus4 → G7 → C
""")

        st.title("Resumo Geral sobre Acordes")


        st.markdown("""
Ao longo deste capítulo, vimos vários tipos de acordes. É importante entender que eles*não se excluem, mas atuam em **dimensões diferentes da harmonia**.

Abaixo está um resumo comparativo para organizar essas ideias:
""")

        st.markdown("""
| Tipo de Acorde | O que muda? | Função musical | Exemplo |
|----------------|------------|---------------|---------|
| **Tríades** | Estrutura básica (3 notas) | Define se o acorde é maior, menor, diminuto ou aumentado | C, Am, B° |
| **Acordes com 7ª** | Adiciona função harmônica | Cria tensão, resolução e movimento tonal | Cmaj7, G7, Dm7 |
| **Extensões (9, 11, 13)** | Adiciona cor e sofisticação | Enriquece a sonoridade sem mudar a função básica | Cmaj9, G13 |
| **Inversões** | Muda a nota do baixo | Melhora encadeamento e linhas de baixo | Cmaj7/E |
| **Suspensos (sus)** | Remove a 3ª | Cria suspensão e ambiguidade tonal | Csus4, G7sus4 |
""")

        st.success("""
🎯 **Ideia-chave:**  
Esses conceitos atuam em camadas diferentes do acorde:

- A **tríade** define a identidade básica  
- A **7ª** define a função harmônica  
- As **extensões** refinam a cor sonora  
- As **inversões** organizam o movimento  
- Os **sus** criam expectativa e suspensão
""")

        st.markdown("""
Veja como um único acorde pode acumular várias dessas ideias ao mesmo tempo:

**Cmaj7(9)/E**
  - Tom: C
  - Notas: E – G – B – C – D
  - Tétrade: maior com 7ª (Cmaj7)
  - Extensão: 9ª (D)
  - Inversão: E no baixo
                    

                    
**G7(13)/B**
  - Tom: G
  - Notas: B – D – F – A – E – G
  - Tétrade: dominante (G7)
  - Extensão: 13ª (E)
  - Inversão: B no baixo 

                    
**Dm11/F**
  - Tom: D
  - Notas: F – A – C – D – G
  - Tétrade: menor com 7ª (Dm7)
  - Extensão: 11ª (G)
  - Inversão: F no baixo 

                    
**A13sus4/C#**
  - Tom: A
  - Notas: C# – D – E – G – F#
  - Suspenso: sem 3ª (sus4)
  - Extensão: 13ª (F#)
  - Inversão: C# no baixo 

                    
**Fmaj7(#11)/A**
  - Tom: F
  - Notas: A – C – E – F – B
  - Tétrade: maior com 7ª (Fmaj7)
  - Extensão: #11 (B)
  - Inversão: A no baixo 

Ou seja: um único acorde pode ser sofisticado em vários níveis harmônicos simultaneamente.
""")

        st.info("""  
👉 **A sofisticação musical não vem de decorar todos esses acordes de uma vez,
mas sim de entender como pequenas mudanças estruturais dos intervalos transformam a função e a sensação sonora para causar um efeito desejado em uma progressão.**
""")

    

    def harmonico():

        # ======================================================
        st.header("🎼 O Que é Campo Harmônico e Como Construí-lo?")

        st.markdown("""
        Um campo harmônico é um conjunto de acordes que soam bem com a tonalidade que está sendo tocada. 
                    
        Os campos harmônicos são formados a partir da escala da nota tonal escolhida e, para construí-lo, é necessário aplicar o empilhamento de terças em cada uma das notas da escala.
        
        **Vamos construir um campo harmônico passo a passo para entender como ele é feito:**
            
                    """)


        st.markdown("""
        **1 - Escolha uma escala** -> Exemplo: Escala Maior Natural de Dó

        *C – D – E – F – G – A – B*
        """)

        st.markdown("""
        **2 -  Empilhando terças até formar tríades**

        Agora escolhemos uma nota da escala e, para empilhar terças de forma prática, pulamos sempre uma nota da escala para compor o acorde.
        """)

        st.markdown("""
        - **Grau I**:  *C → E → G* → estas são as notas da tríade de **C maior**

        - **Grau II**: *D → F → A* → estas são as notas da tríade de **D menor**

        - **Grau III**: *E → G → B* → estas são as notas da tríade de **E menor**

        - **Grau IV**: *F → A → C* → estas são as notas da tríade de **F maior**

        - **Grau V**: *G → B → D* → estas são as notas da tríade de **G maior**

        - **Grau VI**: *A → C → E* → estas são as notas da tríade de **A menor**

        - **Grau VII**: *B → D → F* → estas são as notas da tríade de **B diminuto**
        """)

        st.markdown("""
        Portanto, o campo harmônico de dó maior em tríades é:

        👉 *C – Dm – Em – F – G – Am – B°*
        """)

        
        st.info("""As tríades mostram a qualidade básica de cada acorde no campo harmônico, ou seja, quais graus terão acordes maiores ou menores.""")

        st.markdown("Veja a **tabela de campos harmônicos maiores** para todas as notas naturais:")

        st.markdown("""I  | II  | III | IV | V  | VI  | VII | 
-- | --- | --- | -- | -- | --- | ---- | 
**C**  | Dm  | Em  | F  | G  | Am  | B°   |
**G**  | Am  | Bm  | C  | D  | Em  | F#°  | 
**D**  | Em  | F#m | G  | A  | Bm  | C#°  | 
**A**  | Bm  | C#m | D  | E  | F#m | G#°  | 
**E**  | F#m | G#m | A  | B  | C#m | D#°  | 
**B**  | C#m | D#m | E  | F# | G#m | A#°  | 
**F#** | G#m | A#m | B  | C# | D#m | E#°  | 
**Db** | Ebm | Fm  | Gb | Ab | Bbm | C°   | 
**Ab** | Bbm | Cm  | Db | Eb | Fm  | G°   | 
**Eb** | Fm  | Gm  | Ab | Bb | Cm  | D°   | 
**Bb** | Cm  | Dm  | Eb | F  | Gm  | A°   | 
**F**  | Gm  | Am  | Bb | C  | Dm  | E°   | 
""")
        
        st.markdown("Veja a **tabela de campos harmônicos menores** para todas as notas naturais:")

        st.markdown("""I   | II | III | IV  | V   | VI | VII 
--- | --- | --- | --- | --- | -- | --- 
**Am**  | B°  | C   | Dm  | Em  | F  | G   |
**Em**  | F#° | G   | Am  | Bm  | C  | D   |
**Bm**  | C#° | D   | Em  | F#m | G  | A   |
**F#m** | G#° | A   | Bm  | C#m | D  | E   |
**C#m** | D#° | E   | F#m | G#m | A  | B   |
**G#m** | A#° | B   | C#m | D#m | E  | F#  |
**D#m** | E#° | F#  | G#m | A#m | B  | C#  |
**Bbm** | C°  | Db  | Ebm | Fm  | Gb | Ab  |
**Fm**  | G°  | Ab  | Bbm | Cm  | Db | Eb  |
**Cm**  | D°  | Eb  | Fm  | Gm  | Ab | Bb  |
**Gm**  | A°  | Bb  | Cm  | Dm  | Eb | F   |
**Dm**  | E°  | F   | Gm  | Am  | Bb | C   |
""")
        # ======================================================
        st.header(" Campos Harmônicos Com Tétrades")

        st.markdown("""
        O campo harmônico completo com tétrades surgem ao adicionarmos mais uma etapa de empilhamento de terças em cada um dos graus com a inserção das sétimas às tríades, definindo com mais clareza a função harmônica de cada grau.
        """)

        st.markdown("""
**3 - Adicionando mais uma etapa do empilhamento de terças:**
""")

        st.markdown("""
- **Grau I**: *C → E → G → B* → estas são as notas da tétrade de **Cmaj7**

- **Grau II**: *D → F → A → C* → estas são as notas da tétrade de **Dm7**

- **Grau III**: *E → G → B → D* → estas são as notas da tétrade de **Em7**

- **Grau IV**: *F → A → C → E* → estas são as notas da tétrade de **Fmaj7**

- **Grau V**: *G → B → D → F* → estas são as notas da tétrade de **G7**

- **Grau VI**: *A → C → E → G* → estas são as notas da tétrade de **Am7**

- **Grau VII**: *B → D → F → A* → estas são as notas da tétrade de **Bm7♭5**
""")

        st.markdown("""
Portanto, o campo harmônico de dó maior em tétrades é:

👉 *Cmaj7 – Dm7 – Em7 – Fmaj7 – G7 – Am7 – Bm7♭5*
""")


        st.success("""
        ✅ Em música moderna sofisticada, pensar em tétrades é o padrão já que o uso das tríades é feito para simplificações, escolhas estéticas rápidas ou validação de protótipos de progressões.
                   
As tétrades não apenas ampliam o som dos acordes, como também deixam evidente quem resolve, quem prepara e quem gera tensão no campo harmônico.
        """)

        st.subheader("Fórmula das Tétrades no Campo Harmônico Maior")
        st.markdown("""
        
        - **I**  → maj7  
        - **II** → m7  
        - **III** → m7  
        - **IV** → maj7  
        - **V**  → 7  
        - **VI** → m7  
        - **VII** → m7♭5
        """)

        st.markdown("""
        Exemplo - Campo Harmônico de C com tétrades:

        👉 *Cmaj7 – Dm7 – Em7 – Fmaj7 – G7 – Am7 – Bm7♭5*
        """)

        st.markdown("**Veja a tabela de campos harmônicos maiores com tétrades para todas as notas naturais:**")

        st.markdown("""
I       | II      | III     | IV       | V      | VI      | VII | 
------- | ------- | ------- | -------- | ------ | ------- | ----- | 
**Cmaj7**   | Dm7     | Em7     | Fmaj7    | G7     | Am7     | Bm7♭5 |
**Gmaj7**   | Am7     | Bm7     | Cmaj7    | D7     | Em7     | F#m7♭5 |
**Dmaj7**   | Em7     | F#m7    | Gmaj7    | A7     | Bm7     | C#m7♭5 |
**Amaj7**   | Bm7     | C#m7    | Dmaj7    | E7     | F#m7    | G#m7♭5 |
**Emaj7**   | F#m7    | G#m7    | Amaj7    | B7     | C#m7    | D#m7♭5 |
**Bmaj7**   | C#m7    | D#m7    | Emaj7    | F#7    | G#m7    | A#m7♭5 |
**F#maj7**  | G#m7    | A#m7    | Bmaj7    | C#7    | D#m7    | E#m7♭5 |
**Dbmaj7**  | Ebm7    | Fm7     | Gbmaj7   | Ab7    | Bbm7    | Cm7♭5 |
**Abmaj7**  | Bbm7    | Cm7     | Dbmaj7   | Eb7    | Fm7     | Gm7♭5 |
**Ebmaj7**  | Fm7     | Gm7     | Abmaj7   | Bb7    | Cm7     | Dm7♭5 |
**Bbmaj7**  | Cm7     | Dm7     | Ebmaj7   | F7     | Gm7     | Am7♭5 |
**Fmaj7**   | Gm7     | Am7     | Bbmaj7   | C7     | Dm7     | Em7♭5 |
""")


        st.subheader("Fórmula das Tétrades no Campo Harmônico Menor")

        st.markdown("""

- **I**   → m7  
- **II**  → m7♭5  
- **III** → maj7  
- **IV**  → m7  
- **V**   → m7  
- **VI**  → maj7  
- **VII** → 7
""")

        st.markdown("""
Exemplo — Campo Harmônico de Am com tétrades:

👉 *Am7 – Bm7♭5 – Cmaj7 – Dm7 – Em7 – Fmaj7 – G7*
""")

        st.markdown("**Veja a tabela de campos harmônicos menores com tétrades para todas as notas naturais:**")

        st.markdown("""
I       | II     | III     | IV      | V       | VI      | VII | 
------- | ------- | ------- | ------- | ------- | ------- | ----- | 
**Am7**  | Bm7♭5   | Cmaj7   | Dm7     | Em7     | Fmaj7   | G7   |
**Em7**  | F#m7♭5  | Gmaj7   | Am7     | Bm7     | Cmaj7   | D7   |
**Bm7**  | C#m7♭5  | Dmaj7   | Em7     | F#m7    | Gmaj7   | A7   |
**F#m7** | G#m7♭5  | Amaj7   | Bm7     | C#m7    | Dmaj7   | E7   |
**C#m7** | D#m7♭5  | Emaj7   | F#m7    | G#m7    | Amaj7   | B7   |
**G#m7** | A#m7♭5  | Bmaj7   | C#m7    | D#m7    | Emaj7   | F#7  |
**D#m7** | E#m7♭5  | F#maj7  | G#m7    | A#m7    | Bmaj7   | C#7  |
**Bbm7** | Cm7♭5   | Dbmaj7  | Ebm7    | Fm7     | Gbmaj7  | Ab7  |
**Fm7**  | Gm7♭5   | Abmaj7  | Bbm7    | Cm7     | Dbmaj7  | Eb7  |
**Cm7**  | Dm7♭5   | Ebmaj7  | Fm7     | Gm7     | Abmaj7  | Bb7  |
**Gm7**  | Am7♭5   | Bbmaj7  | Cm7     | Dm7     | Ebmaj7  | F7   |
**Dm7**  | Em7♭5   | Fmaj7   | Gm7     | Am7     | Bbmaj7  | C7   |
""")
 
        
        st.info("""
⚠️ Observe que o acorde **V (Em7)** não é dominante forte e, por isso, esse campo tem sensação mais modal e menos direcional se for usada a teória absoluta. Porém, em aplicações práticas, é muito comum substituir o acorde Em7 pelo E7 mesmo no campo harmônico menor natural para promover a função de dominante forte que as pessoas já estão acostumadas a ouvir nesse grau. 
                
**Então, na prática, você pode substituir o acorde do V grau Em7 por E7.**
""")




        # ======================================================
        st.header("🎯 Funções Harmônicas")

        st.markdown("""
        Cada acorde exerce uma função dentro do campo harmônico que define como se comporta em uma progressão. Sendo assim, as três funções principais são:
        """)

        st.markdown("""
        
        - **Tônica** (T) → repouso, estabilidade  
        - **Subdominante** (SD) → movimento, preparação  
        - **Dominante** (D) → tensão
        """)

        st.markdown("""
        **Tabela de Funções do Campo Harmônico por Grau**

        | Grau | Função | Característica |
        |------|--------|-----------------|
        | I    | Tônica Principal | Centro Tonal
        | II   | Subdominante | Preparação / Movimento
        | III  | Tônica | Expansão do Centro Tonal
        | IV   | Subdominante | Preparação / Movimento
        | V    | Dominante | Tensão
        | VI   | Tônica | Expansão do Centro Tonal
        | VII  | Dominante  | Tensão
        """)

        st.success("""
✅ Um dos conceitos mais importantes da harmonia funcional é entender que acordes que compartilham a mesma função harmônica podem se substituir.

Isso significa que, ao invés de pensar apenas em acordes específicos, podemos pensar em funções que os acordes exercem nos papéis harmônicos que desempenham naquele tom.

Essa ideia amplia drasticamente as possibilidades futuras para alcançar ideias de composição, reharmonização, modularidade e improvisação.
                 
                   """)

    

        st.markdown("""
Observe os exemplos abaixo:
""")

        st.markdown("""
**Exemplo 1: Cmaj7 → Am7 → Dm7 → G7 -> C**
""")
        if st.button("▶"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )

        st.markdown("""
Função Harmônica:
- Cmaj7 → Tônica
- Am7 → Tônica (prolongamento)
- Dm7 → Subdominante
- G7 → Dominante
""")

        st.markdown("""
Agora, compare com esta progressão:
""")

        st.markdown("""
**Exemplo 2: Cmaj7 → Em7 → Fmaj7 → G7 -> C**
""")
        if st.button("▶", key="1"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )


        st.markdown("""
Função Harmônica:
- Cmaj7 → Tônica
- Em7 → Tônica (prolongamento)
- Fmaj7 → Subdominante
- G7 → Dominante
""")

        st.success("""
✅ Apesar dos acordes serem diferentes, as duas progressões são funcionalmente equivalentes.

Elas têm o mesmo fluxo:
Tônica → Subdominante → Dominante → Tônica
""")

# ------------------------------------------------------
        st.info("""
🎸 **Aplicação prática (composição e improviso):**

- Pense em funções, não apenas em acordes
- Use substituições para variar progressões sem perder o sentido tonal
- No improviso, você pode manter a mesma ideia melódica enquanto os acordes mudam,
desde que a função seja preservada
""")

        # ======================================================
        st.header("🎯 Dominantes Secundários")

        st.markdown("""
        Um dominante secundário é o V grau dominante (7) de outro acorde usado para preparar temporariamente a aterrizagem em outro grau que não seja a tônica.
        """)

        st.markdown("""
        Por exemplo:

        Como já vimos, o campo harmônico natural de C é:
                    
        *Cmaj7 – Dm7 – Em7 – Fmaj7 – G7 – Am7 – Bm7♭5*
                    
        Se quisermos inserir um dominante secundário para preparar a aterrizagem em Dm7, por exemplo, colocamos o V grau do campo harmônico de D, que é A7, para sofisticar a nossa chegada em Dm7.

        Inserindo dominante secundário:
        Cmaj7 – **A7** – Dm7 
        """)

        st.success("""
        *Por que o acorde A7 funciona mesmo sem ele estar no campo harmônico de C?*
        - A7 é usado temporariamente como o V grau de Dm
        - Cria tensão extra para chegar em Dm
        - Direciona fortemente a progressão 
        - Na notação funcional, A7 → V/ii (dominante V do segundo grau)
        """)


        st.markdown("""
**Veja como ficaria o campo harmônico maior e menor se aplicarmos os dominantes secundários em todos os graus**: 
                    
Maior: *Cmaj7 – A7 – Dm7 – B7 – Em7 – C7 – Fmaj7 – D7 – G7 – E7 – Am7 – F#7 – Bm7♭5*

Menor: *Am – F#7 – Bm7♭5 – G7 – Cmaj7 – A7 – Dm7 – B7 – Em7 – C7 – Fmaj7 – D#7 – G#°*
        """)


        st.header("🎯 Empréstimo Modal")

        st.markdown("""
Empréstimo modal é quando utilizamos acordes de um modo paralelo para enriquecer a harmonia de uma progressão sem abandonar a tonalidade principal, ou seja, usamos um acorde do campo harmônico menor quando deveriamos usar do campo harmônico maior ou vice-versa para 'colorir' e diversificar melhor uma progressão.

Esse é um recurso amplamente usado em diversos gêneros musicais, como por exemplo: MPB, Jazz, Rock, Blues moderno, entre outros. Sendo assim, é um conceito fundamental para entender a harmonia de uma forma abrangente. 

""")
        
        st.info("""
⚠️ No empréstimo modal, a tônica não muda. O que muda é o modo emprestado por um curto período de tempo. 

Assim, para que tenha o efeito desejado, **o empréstimo modal deve ser excessão e não regra em uma progressão**.
""")
        
        st.markdown("""
Por exemplo,

- Campo harmônico natural: *Cmaj7 – Dm7 – Em7 – Fmaj7 – G7 – Am7 – Bm7♭5*

- Campo harmônico menor paralelo (Cm): *Cm7 – Dm7♭5 – Ebmaj7 – Fm7 – Gm7 – Abmaj7 – Bb7*
""")

        st.markdown("""
Para iniciar nossos estudos, podemos considerar alguns empréstimos modais específicos que encaixam bem em determinados graus.
""")
        
        st.markdown("**Veja a seguir a tabela de empréstimos modais:**")

        st.markdown("- *Exemplo em C Maior:*")

        st.markdown("""
| Grau | Acorde diatônico | Acorde emprestado | Efeito sonoro |
|------|------------------|------------------|----------------|
| IV   | F                | Fm               | Melancolia / contraste |
| VI   | Am               | Ab               | Profundidade emocional |
| VII  | B°               | Bb               | Sonoridade modal / folk |
| II   | Dm               | D°               | Instabilidade leve |
""")

        st.markdown("- *Exemplo em C Maior com tétrades:*")

        st.markdown("""
| Grau | Acorde diatônico | Acorde emprestado | Efeito sonoro |
|------|------------------|------------------|----------------|
| IV   | Fmaj7            | Fm7              | Melancolia / contraste |
| VI   | Am7              | Abmaj7           | Profundidade emocional |
| VII  | Bm7♭5            | Bb7              | Sonoridade modal / folk |
| II   | Dm7              | Dm7♭5            | Instabilidade leve |
""")

        st.markdown("- *Exemplo em A Menor:*")

        st.markdown("""
| Grau | Acorde diatônico | Acorde emprestado| Efeito sonoro |
|------|------------------|------------------|----------------|
| IV   | F                | Fm               | Melancolia / contraste |
| VI   | Am               | Ab               | Profundidade emocional |
| VII  | B°               | Bb               | Sonoridade modal / folk |
| II   | Dm               | D°               | Instabilidade leve |
""")

        st.markdown("- *Exemplo em A Menor com tétrades:*")

        st.markdown("""
| Grau | Acorde diatônico | Acorde emprestado | Efeito sonoro |
|------|------------------|------------------|----------------|
| I    | Am7              | Amaj7            | Clareza / brilho |
| IV   | Dm7              | Dmaj7            | Abertura sonora |
| V    | Em7              | E7               | Direcionalidade forte |
| VI   | Fmaj7            | F#m7             | Expansão sofisticada |
""")
  
# ------------------------------------------------------
        st.info("""
🎸 **Aplicação prática:**

- Use empréstimo modal para variar progressões previsíveis
- Mantenha o centro tonal claro e use o acorde do empréstimo com a mesma função do original

""")

        st.header("🎯 Progressões Harmônicas")

        st.markdown("""
Uma progressão harmônica é a organização dos acordes em um arranjo musical. Sendo assim, a progressão define o fluxo emocional, a direção e o nível de tensão e repouso de uma música.

E, agora que você já entende:
- Campo harmônico
- Funções harmônicas
- Tétrades
- Substituições funcionais
- Dominantes secundários
- Empréstimo modal

Vamos aprender a combinar tudo isso na prática.
""")

# ------------------------------------------------------
        st.subheader("🔹Progressões Básicas e Fundamentais")

        st.markdown("""
Essas progressões usam apenas acordes do campo harmônico principal, sem muitas sofisticações ou alterações. São a base da musica tonal que funciona muito bem se aplicado corretamente.
""")

        st.markdown("""
#### I – IV – V – I  
Exemplo com tríades: *C → F → G → C* """)
        
        if st.button("▶", key="2"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
            
        st.markdown("""
Exemplo com tétrades: *Cmaj7 → Fmaj7 → G7 → Cmaj7*
""")
        if st.button("▶", key="3"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
        
        st.markdown("""
#### I – V – IV – I
Exemplo com tríades: *C → G → F → C*
""")
        if st.button("▶", key="4"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )


        st.markdown("""
Exemplo com tétrades: *Cmaj7 → G7 → Fmaj7 → Cmaj7*
""")
        if st.button("▶", key="5"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
        
        st.markdown("""
#### II – V – I
Exemplo com tríades: *Dm → G → C*
""")
        if st.button("▶", key="6"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
            
        st.markdown("""
Exemplo com tétrades: *Dm7 → G7 → Cmaj7*
""")
        if st.button("▶", key="7"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
        
        st.markdown("""
#### I – VI – II – V – I 
Exemplo com tríades: *C → Am → Dm → G → C*
""")
        
        if st.button("▶", key="8"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
            
        st.markdown("""
Exemplo com tétrades: *Cmaj7 → Am7 → Dm7 → G7 → Cmaj7* 
""")
        
        if st.button("▶", key="9"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )

        st.markdown("""                    
#### I – V – VI – IV 
Exemplo com tríades: *C → G → Am → F*
""")
        if st.button("▶", key="10"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )
            
        st.markdown("""
Exemplo com tétrades: *Cmaj7 → G7 → Am7 → Fmaj7*
""")
        if st.button("▶", key="11"):
            st.audio(
        "https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3"
    )

# ------------------------------------------------------
        st.subheader("🔹Progressões com Dominantes Secundários")

        st.markdown("""
Como vimos, dominantes secundários criam tensão direcionada para acordes que não são a tônica.
""")

        st.markdown("""
#### I – V/ii – II – V – I
Exemplo com tríades: C -> A7 -> Dm -> G -> C

Exemplo com tétrades: *Cmaj7 → A7 → Dm7 → G7 → Cmaj7*
""")
        
        st.markdown("""
#### I – V/vi – VI – II – V – I 
Exemplo com tríades: C -> E7 -> Am -> Dm -> G -> C

Exemplo com tétrades: *Cmaj7 → E7 → Am7 → Dm7 → G7 → Cmaj7*
""")
        
        st.markdown("""
#### I – V/iii – III – VI – II – V – I  
Exemplo com tríades: C -> B7 -> Em -> Am -> Dm -> G -> C

Exemplo com tétrades: *Cmaj7 → B7 → Em7 → Am7 → Dm7 → G7 → Cmaj7*
""")
        
        st.markdown("""
#### I – V/IV – IV – V – I  
Exemplo com tríades: C -> C7 -> F -> G -> C

Exemplo com tétrades: *Cmaj7 → C7 → Fmaj7 → G7 → Cmaj7*
""")
        
        st.markdown("""
#### I – V/V – V – I 
Exemplo com tríades: C -> D7 -> G -> C

Exemplo com tétrades: *Cmaj7 → D7 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – VI – V/ii – II – V – I 
Exemplo com tríades: C -> Am -> A7 -> Dm -> G7 -> C

Exemplo com tétrades: *Cmaj7 → Am7 → A7 → Dm7 → G7 → Cmaj7*
""")
        
        st.markdown("""
#### I – VI – V/ii – II – V – I  
Exemplo com tríades: C -> Am -> A7 -> Dm -> G -> C

Exemplo com tétrades: *Cmaj7 → Am7 → A7 → Dm7 → G7 → Cmaj7*
""")



        st.subheader("🔹Progressões com Empréstimo Modal")

        st.markdown("""
O empréstimo modal adiciona cor emocional sem abandonar a tonalidade principal, muito usado para trazer mais sofisticações e imprivisibilidade à progressão.
""")

        st.markdown("""
#### I – IVm – V – I
Exemplo em tríades: *C → Fm → G → C*
                    
Exemplo em tétrades: *Cmaj7 → Fm7 → G7 → Cmaj7* 
""")

        st.markdown("""
#### I – VIm – V – I  
Exemplo em tríades: *C → Ab → G → C*
                    
Exemplo em tétrades: *Cmaj7 → Abmaj7 → G7 → Cmaj7*
""")
        
        st.markdown("""
#### I – IVm – ♭VII – I 
Exemplo em tríades: *C → Fm → Bb → C*  

Exemplo em tétrades: *Cmaj7 → Fm7 → Bb7 → Cmaj7*
""")

        st.markdown("""
#### I – ♭VII – IV – I
Exemplo em tríades: *C → Bb → F → C*  

Exemplo em tétrades: *Cmaj7 → Bb7 → Fmaj7 → Cmaj7*
""")

        st.markdown("""
#### I – IVm – ♭VI – V – I  
Exemplo em tríades: *C → Fm → Ab → G → C*  

Exemplo em tétrades: *Cmaj7 → Fm7 → Abmaj7 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – ♭VI – ♭VII – I  
Exemplo em tríades: *C → Ab → Bb → C*  

Exemplo em tétrades: *Cmaj7 → Abmaj7 → Bb7 → Cmaj7*
""")

        st.markdown("""
#### I – IIm7♭5 – V – I 
Exemplo em tríades: *C → D° → G → C*  

Exemplo em tétrades: *Cmaj7 → Dm7♭5 → G7 → Cmaj7*
""")

# ------------------------------------------------------
        st.subheader("🔹Progressões Complexas Combinando Vários Conceitos")

        st.markdown("""
Aqui começam as progressões mais sofisticadas que misturam tudo o que vimos até então.
""")
        
        st.markdown("""
#### I – V/ii – IIm – V – I  
(Dominante secundário + função clássica)

Exemplo em tríades: *C → A → Dm → G → C*  

Exemplo em tétrades: *Cmaj7 → A7 → Dm7 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – IVm – V/vi – VIm – V – I 

Exemplo em tríades: *C → Fm → E → Am → G → C*  

Exemplo em tétrades: *Cmaj7 → Fm7 → E7 → Am7 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – V/IV – IV – IVm – I  

Exemplo em tríades: *C → C7 → F → Fm → C*  

Exemplo em tétrades: *Cmaj7 → C7 → Fmaj7 → Fm7 → Cmaj7*
""")

        st.markdown("""
#### I – ♭VI – V/ii – IIm – V – I

Exemplo em tríades: *C → Ab → A → Dm → G → C*  

Exemplo em tétrades: *Cmaj7 → Abmaj7 → A7 → Dm7 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – IV – ♭VII – V/III – IIIm – V – I  

Exemplo em tríades: *C → F → Bb → B → Em → G → C*  

Exemplo em tétrades: *Cmaj7 → Fmaj7 → Bb7 → B7 → Em7 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – V/vi – VIm – IIm7♭5 – V – I  

Exemplo em tríades: *C → E → Am → D° → G → C*  

Exemplo em tétrades: *Cmaj7 → E7 → Am7 → Dm7♭5 → G7 → Cmaj7*
""")

        st.markdown("""
#### I – IVm – ♭VI – V/ii – IIm – V – I  

Exemplo em tríades: *C → Fm → Ab → A → Dm → G → C*  

Exemplo em tétrades: *Cmaj7 → Fm7 → Abmaj7 → A7 → Dm7 → G7 → Cmaj7*
""")

        st.success("""
🎯 Essas progressões representam o ponto de encontro entre:
- harmonia funcional tradicional
- empréstimo e linguagem modal
- sofisticação tonal moderna

Elas são extremamente comuns em Jazz, MPB, trilhas sonoras,
Neo Soul e diversos outros estilos de músicas sofisticados.
""")

        st.header("🎯 Modulação")

        st.markdown("""
Modulação é o processo em que uma música muda de tonalidade durante sua execução, ou seja,
o centro tonal deixa de ser um e passa a ser outro de forma perceptível
para o ouvinte enquanto a faixa esta sendo tocada. """)
        
        
        st.markdown("""
A modulação é muito usada para:

- Expandir a narrativa harmônica
- Criar contrastes fortes entre seções ou músicas
- Elevar tensão emocional e criar transições para não interromper a faixa entre músicas
- Evitar repetição excessiva para criar exclusividade em performances
""")

        st.success("""
🎯 Pensar modulação corretamente significa dominar profundamente a harmonia para distinguir quando você está colorindo a tonalidade
e quando você está mudando o chão onde pisa.

Esse domínio separa o músico funcional do músico consciente da linguagem harmônica abrindo espaço para performances criativas e exclusivas de expressões únicas. Ao dominar a modulação você pode criar uma passagem de uma música a outra sem precisar parar a sua performance.
""")


        st.markdown("""
Diferente do empréstimo modal e dos dominantes secundários, na modulação
a nova tonalidade se estabelece como principal para apresentar uma nova secção ou uma nova música que será tocada.
""")

        st.markdown("""
| Recurso | Tônica muda? | Duração | Função |
|-------|--------------|--------|--------|
| Empréstimo Modal | ❌ Não | Curta | Cor e contraste |
| Dominante Secundário | ❌ Não | Curta | Direcionamento |
| Modulação | ✅ Sim | Média ou longa | Mudança de centro tonal |
""")

# ------------------------------------------------------

        st.markdown("""
Existem diversas formas de modular na música tonal, mas a mais importante que vamos estudar nesse módulo é a **Modulação por Acorde Pivô**
""")

        st.markdown("""

Essa modulação ocorre quando um mesmo acorde pertence ao campo harmônico de duas tonalidades diferentes exercendo funções distintas entre as duas tonalidades,
servindo como ponte entre elas.
""")

        st.markdown("""
Por exemplo:

*Tom de C maior passando para o Tom de G maior*

- Campo Harmônico de C Maior: *Cmaj7 – **Dm7** – Em7 – Fmaj7 – G7 – Am7 – Bm7♭5*
                    
- Campo Harmônico de G Menor: *Gm7 – Am7♭5 – Bbmaj7 – Cm7 – **Dm7** – Ebmaj7 – F7* 

O Dm7 funciona como:
- II grau em C
- V grau em Gm 
                    
Se tomarmos a progressão *Cmaj7 → Em7 → Dm7 → Gm7 → Cm7 → F7 → Bbmaj7*, podemos perceber que a partir de Dm7 para Gm7 o centro tonal passa a ser Gm sendo usado os acordes desse novo centro tonal.

Assim, nota-se que podemos usar o Dm7 para modularizar o tom de C para G.    

**Veja outros exemplos de modulações possíveis em fórmulas para você estudar:**             
""")
        
        st.markdown("""
| Grau no tom de origem | Qualidade do acorde | Função no tom de origem | Pode virar função no novo tom | Novo centro tonal                |
| --------------------- | ------------------- | ----------------------- | ----------------------------- | -------------------------------- |
| **I**                 | Maior / Maj7        | Tônica                  | IV                            | Tom acima (V do tom de origem)   |
| **I**                 | Maior / Maj7        | Tônica                  | V                             | Tom abaixo (IV do tom de origem) |
| **II**                | Menor / m7          | Subdominante            | I                             | Tom menor relativo ao ii         |
| **II**                | Menor / m7          | Subdominante            | IV                            | Tom uma 4ª acima                 |
| **II**                | Menor / m7          | Subdominante            | V                             | Tom uma 5ª acima (menor)         |
| **III**               | Menor / m7          | Tônica relativa         | I                             | Tom relativo menor               |
| **III**               | Menor / m7          | Tônica relativa         | vi                            | Tom uma 3ª acima                 |
| **IV**                | Maior / Maj7        | Subdominante            | I                             | Mesmo acorde como nova tônica    |
| **IV**                | Maior / Maj7        | Subdominante            | V                             | Tom uma 4ª abaixo                |
| **V**                 | Maior / 7           | Dominante               | I                             | Tom uma 5ª acima                 |
| **VI**                | Menor / m7          | Tônica relativa         | I                             | Tom relativo menor               |
| **VI**                | Menor / m7          | Tônica relativa         | ii                            | Tom uma 5ª acima                 |
| **VII**              | Meio-diminuto       | Dominante fraca         | ii                            | Tom relativo menor               |


""")
        
        st.markdown("""
Por exemplo:

*Tom de C maior modulando para A menor*

- Campo Harmônico de C Maior: *Cmaj7 – Dm7 – Em7 – Fmaj7 – G7 – Am7 – Bm7♭5*

- Campo Harmônico de A Menor (natural): *Am7 – Bm7♭5 – Cmaj7 – Dm7 – Em7 – Fmaj7 – G7*

O acorde Am7 funciona inicialmente como VI grau em C maior e, para que haja modulação real para Am7, usamos o acorde Dm7 subdominante comum como preparação (II grau em C e IV grau em Am), introduzimos o grau dominante do novo tom Em7 (V grau em Am e III grau em C) e, para completar a modulação definitiva, mudamos o acorde para dominante 7 para não deixar dúvidas que vamos resolver agora em Am. 

Exemplo de progressão com modulação completa:

*Cmaj7 → G7 → Cmaj7 → Am7 → Dm7 → Em7 → E7 → Am7*

""")
        
        st.success("""🎯 **A partir desse ponto, Am se estabelece como novo tom e Cmaj7 pode ser entendido como o III grau com tônica estendida**. 
                   
Assim, apesar de os acordes serem os mesmos eles passam a desempenhar uma nova função na harmônia de Am em comparação com C.""")
        

        st.markdown("""
**Agora, digamos que queremos sair de Am e chegar em F:**



- Campo Harmônico de A Menor: *Am7 – Bm7♭5 – Cmaj7 – Dm7 – Em7 – Fmaj7 – G7*

- Campo Harmônico de F Maior: *Fmaj7 – Gm7 – Am7 – Bbmaj7 – C7 – Dm7 – Em7♭5*

O acorde Fmaj7 funciona inicialmente como o VI grau em Am e, para que a modulação se estabeleça de forma clara, introduzimos o acorde dominante do novo tom, o C7,
que resolve diretamente em **Fmaj7**, eliminando qualquer ambiguidade quanto ao novo centro tonal.

Exemplo de progressão com modulação completa saindo de C -> Am -> F:

***Cmaj7** → G7 → Cmaj7 → Am7 → Dm7 → Em7 → E7 → **Am7** → Dm7 → Fmaj7 → C7 → **Fmaj7***

""")
        
        st.success("""**✅ Nessa progressão, saimos de C, passamos pelo tom de Am e aterrizamos no tom F.**
                   
A partir disso, podemos continuar a progressão no campo harmônico de F ou escolher qualquer outro tom para iniciar nossa modularização.
                   
                   """)

            
    def set_video(url):
        st.session_state.video_ativo = url


    def tutoriais():
        st.title("Tutoriais De Repertório")

        st.markdown("""
    Os vídeos incorporados pertencem aos seus respectivos criadores e estão hospedados no YouTube. 
    Esta plataforma realiza curadoria e organização educacional de conteúdos públicos, 
    não reivindicando autoria sobre os materiais exibidos.

    Veja os tutoriais disponíveis gratuitamente na internet para desenvolver um repertório musical 
    vasto baseado no seu gênero musical favorito:
    """)
        
        if "video_ativo" not in st.session_state:
            st.session_state.video_ativo = None

        
                # =============================
        # Player único
        # =============================
        if st.session_state.video_ativo:
            st.divider()
            st.subheader("🎬 Vídeo selecionado")
            st.video(st.session_state.video_ativo)


        # =============================
        # Estado (sempre no topo)
        # =============================
        # =============================
        # Repertório
        # =============================

        st.divider()
        repertorio = {
            "Blues": {
                "Hit The Road Jack – Ray Charles": "https://www.youtube.com/watch?v=72JsVAtxxbQ",
                "Sweet Home Chicago – Robert Johnson": "https://youtu.be/VdiYasPjtDI",
                "Me And The Devil – Robert Johnson": "https://youtu.be/JhLqT1UwVf8",
                "My Babe – Little Walter": "https://youtu.be/4MhQ8fpVnYI",
                "Born Under a Bad Sign – Albert King": "https://youtu.be/E71arjUayhA",
                "Help Me – Sonny Boy Williamson": "https://youtu.be/xY26rgQ8cVE",
                "Still A Fool – Muddy Waters": "https://youtu.be/39lllqooF_g",
                "Before You Accuse Me – Eric Clapton": "https://youtu.be/ItSBRoyXQNw",
                "Baby Please Don't Go – Lightnin' Hopkins": "https://youtu.be/ecTUUDob4pg",
                "I Don't Need No Doctor – John Mayer": "https://youtu.be/zVrZNqcQARE",
            },

            "Rock": {
                "Little Wing – Jimi Hendrix": "https://youtu.be/A6Xqb6ZHipo",
                "Hey Joe – Jimi Hendrix": "https://youtu.be/oEp3RNg3UPU",
                "Smells Like Teen Spirit – Nirvana": "https://youtu.be/wBkJFsRxMJA",
                "Come As You Are – Nirvana": "https://youtu.be/ijkaVhLAB68",
                "Message In a Bottle – The Police": "https://youtu.be/fhzUGERg1jY",
                "Californication – Red Hot Chili Peppers": "https://youtu.be/9f1nMzbF6WE",
                "Otherside – Red Hot Chili Peppers": "https://youtu.be/vgrTaCU-WqE",
                "Johnny B. Goode – Chuck Berry": "https://youtu.be/5y3PRqVs6Vc",
                "Are U Mine? – Arctic Monkeys": "https://youtu.be/fvNB4OOcDgU",
                "Take A Look Around – Limp Bizkit": "https://youtu.be/r7VORLT6Kjs",
                "Ain't Talkin' 'Bout Love – Van Halen": "https://youtu.be/pQS92VgshDg",
                "Money For Nothing - Dire Straits": "https://www.youtube.com/watch?v=zZbSkA8wdRE",
            },

            "Pop": {
                "Bad – Michael Jackson": "https://youtu.be/PioLuT9l-4s",
                "Beat It – Michael Jackson": "https://youtu.be/b2dYQAejgqQ",
                "Thriller – Michael Jackson": "https://youtu.be/rtlB7SvMlY8",
                "They Don't Care About Us – Michael Jackson": "https://youtu.be/98e-VdYmhWg",
                "Somebody's Watching Me – Rockwell": "https://youtu.be/-pNFsGe0tAM",
                "Let It Be – The Beatles": "https://youtu.be/2a1VBXLCgQg",
                "Tears In Heaven – Eric Clapton": "https://youtu.be/XdPE58PFNmk",
            },
        }

        # =============================
        # Seleção (robusta)
        # =============================
        for genero, musicas in repertorio.items():
            st.subheader(genero)

            for titulo, url in musicas.items():
                st.button(
                    f"▶️ {titulo}",
                    key=f"{genero}-{titulo}",
                    on_click=set_video,
                    args=(url,),
                )




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
    - [🎸 Guitar Scientist (Diagramas)](https://guitarscientist.com/)
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
    elif choice == "Ritmo":
        st.write("")
    elif choice == "Intervalos":
        st.write("")
    elif choice == "Escalas Musicais":
        exibir_escalas()
    elif choice == "Acordes & Arpejos":
        acordes()
    elif choice == "Campos Harmônicos":
        harmonico()
    elif choice == "Tutoriais":
        tutoriais()
    elif choice == "Recursos Adicionais":
        recursos()
