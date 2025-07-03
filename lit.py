import streamlit as st
import streamlit.components.v1 as components
import os
from PIL import Image

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


# Título da aplicação no Streamlit
st.title("Chatbot de Teoria Musical")

# Adicionar uma descrição
st.write("""
Bem-vindo ao curso interativo para estudos em Teoria Musical! Escolha o tema que você quer estudar e mão na massa! 

Entre em contato pelo e-mail ourcontentdigital@gmail.com
         
Bons estudos e até mais!!!
""")

# Menu de opções
menu = ["História", "Ritmos", "Intervalos", "Escalas", "Acordes & Arpejos", "Campos harmônicos", "Modos gregos", "Recursos adicionais"]
choice = st.sidebar.selectbox("Escolha uma função", menu)

if choice == "História":
    st.header("História da Música 🎼")

    st.markdown("""
    A música é uma das expressões mais antigas da humanidade. Nas civilizações pré-históricas, ela era praticada como parte de rituais religiosos, caças e celebrações. Utilizando o corpo e instrumentos rudimentares, os sons simbolizavam conexões com a natureza, com os deuses e com os membros da tribo. Essa musicalidade ajudava a criar coesão social, comunicação simbólica e identidade coletiva.
    """)

    st.subheader("📐 A sistematização da teoria musical")
    st.markdown("""
    A tentativa de entender a música de forma lógica e científica começou com Pitágoras no século VI a.C. Observando os sons de martelos e cordas, ele percebeu relações matemáticas entre as notas. Seu principal experimento foi com o monocórdio — uma corda esticada que, ao ser dividida em proporções simples (como 2:1 ou 3:2), produzia intervalos musicais consonantes. Essa descoberta lançou as bases para a teoria musical ocidental, unindo matemática e som.
    """)

    # ANTIGUIDADE
    st.subheader("🏛️ Antiguidade")
    st.markdown("""
    **🎼 Características técnicas:**
    - Uso de escalas gregas (modos)
    - Música monofônica e ritualística
    - Instrumentação rudimentar (lira, aulos, harpa)

    **👤 Compositores/Filósofos:**
    - **Pitágoras:**
    """)
    st.markdown("- **Terpandro:** foi um célebre poeta lírico e citharode (tocado de cítara, tipo de lira) da Antiga Grécia, ativo por volta do século VII a.C. Segundo Strabo e Plutarco, foi ele quem aumentou as cordas da lira de quatro para sete, dando forma ao que viria a se chamar kithara. Embora suas obras não tenham sobreviveram completas, fragmentos são citados por autores antigos, e sua influência perdurou – consideram-no o primeiro nome certo da história musical da Grécia ")

    st.markdown("""- **Mesomedes de Creta:** Mesomedes de Creta foi um importante poeta lírico e compositor grego do início do século II d.C. Ele viveu durante o período de Hadrian e foi liberto desse imperador, servindo também durante Antonino Pio. Mesomedes era cantor e tocador de kithara, escrevendo poemas — ao todo cerca de 15 — em grego antigo, dos quais pelo menos quatro acompanham a notação musical original, entre elas *Hymn to Nemesis*, *Hymn to the Sun*, *Prayer to Calliope and Apollo*, *Prayer to the Muse*.


    Ouça Hymn to the Sun:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344173/suoop7qv2kyqzaawngvw.mp3")



    # IDADE MÉDIA
    st.subheader("🕍 Idade Média (500–1400)")
    st.markdown("""
    **🎼 Características técnicas:**
    - Canto gregoriano (monofônico e modal)
    - Desenvolvimento da notação musical
    - Polifonia nascente (Notre-Dame)

    **👤 Compositores:**""")

    st.markdown("""- **Guido d’Arezzo (991 – 1033):** foi um monge beneditino italiano e um dos maiores teóricos musicais da Idade Média. Não é reconhecido por composições musicais como outros, mas sim por sua enorme contribuição teórica e pedagógica à música medieval ocidental. Ele foi um monge beneditino que revolucionou o ensino da música com invenções de notações e composições que usamos até hoje, considerado o *pai da notação musical moderna* e um dos grandes inovadores da pedagogia musical ocidental.                 
                """)
    

    st.markdown("""- **Hildegard von Bingen (1098–1179):** monja beneditina, mística, médica, filósofa natural, compositora e visionária, ela viveu no Sacro Império Romano-Germânico e é considerada uma das primeiras compositoras da história da música ocidental cujas obras sobreviveram com autoria confirmada, sendo uma das mais importantes compositoras da Idade Média. Hildegard compôs mais de 70 obras litúrgicas (cânticos, hinos, responsórios) reunidas no ciclo *Symphonia armoniae celestium revelationum*. 

    Ouça *De Spiritu Sancto*:
    """)

    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751344803/hwynylkgkytdtbriavxh.mp3")


  
    st.markdown("""- **Leonin (1150–1201):** monge ou cônego ligado à Catedral de Notre-Dame de Paris, foi um dos primeiros compositores a usar a notação moderna e é considerado o primeiro grande compositor de polifonia na história da música ocidental. Foi sucedido por Perotin, que desenvolveu ainda mais a técnica polifônica, escrevendo músicas a 3 e 4 vozes.

    Ouça *Nostrum Organum Duplum*:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751392698/lggvrlwdh2ij3oc5ysbw.mp3")


    # RENASCIMENTO
    st.subheader("🎨 Renascimento (1400–1600)")
    st.markdown("""
    **🎼 Características técnicas:**
    - Polifonia rica e imitativa
    - Equilíbrio entre vozes
    - Música vocal e instrumental se desenvolvendo paralelamente

    **👤 Compositores:**
    - **Josquin des Prez (1455–1521):** foi um dos compositores mais influentes do Renascimento. Nascido possivelmente na região da atual fronteira entre França e Bélgica (então parte dos Países Baixos borgonheses), ele é considerado o maior compositor de sua época, comparado frequentemente a figuras como Michelangelo ou Leonardo da Vinci, mas na música. Josquin se destacou pela inovação e refinamento da polifonia vocal, isto é, várias vozes cantando melodias diferentes que se combinam harmonicamente. 
  

    Ouça *Ave Maria ... virgo serena*:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751486334/pcvqhxhbll6eacvxtlv5.mp3")

    st.markdown("""- **Giovanni Palestrina (1525–1594):** Palestrina foi um compositor italiano do Renascimento, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais. Seu estilo serviu como modelo pedagógico no estudo de contraponto, sendo estudado até hoje em conservatórios

    Ouça *Missa Papae Marcelli*:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751488772/g0cuwgdeglakntyy6rgc.mp3")

    st.markdown("""- **Orlando di Lasso (1532–1594):** foi um compositor francês do Renascimento, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça *Lagrime di San Pietro: I. Il magnanimo Pietro*:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751497992/cwezwqiiugdezve7uecr.mp3")

    # BARROCO
    st.subheader("🎻 Barroco (1600–1750)")
    st.markdown("""
    **🎼 Características técnicas:**
    - Baixo contínuo, uso de tonalidade maior/menor
    - Contraponto elaborado
    - Nasce a ópera, oratório e concerto

    **👤 Compositores:**
    - **J.S. Bach:  **
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Vivaldi:** Vivaldi foi um compositor italiano do Barroco, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Handel:** Handel foi um compositor alemão do Barroco, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Monteverdi:** Monteverdi foi um compositor italiano do Barroco, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Purcell:** Purcell foi um compositor inglês do Barroco, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    # CLÁSSICO
    st.subheader("🎼 Clássico (1750–1820)")
    st.markdown("""
    **🎼 Características técnicas:**
    - Forma sonata, simetria e equilíbrio
    - Textura homofônica
    - Crescimento da orquestra sinfônica

    **👤 Compositores:**
    - **Mozart:** Mozart foi um compositor austríaco do Clássico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Haydn:** Haydn foi um compositor austríaco do Clássico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Beethoven (1ª fase):** Beethoven foi um compositor alemão do Clássico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    # ROMÂNTICO
    st.subheader("🎭 Romântico (1820–1900)")
    st.markdown("""
    **🎼 Características técnicas:**
    - Harmonia cromática, melodia expressiva
    - Nacionalismo e individualismo
    - Orquestras maiores e mais dramáticas

    **👤 Compositores:**
    - **Chopin:** Chopin foi um compositor polonês do Romântico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Wagner:** Wagner foi um compositor alemão do Romântico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Tchaikovsky:** Tchaikovsky foi um compositor russo do Romântico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Verdi:** Verdi foi um compositor italiano do Romântico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Brahms:** Brahms foi um compositor alemão do Romântico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""- **Liszt:** Liszt foi um compositor húngaro do Romântico, considerado um dos maiores compositores de sua época. Ele é conhecido por sua habilidade em combinar a simplicidade da música popular com a complexidade da música erudita, criando uma forma de música que era acessível a todos os níveis sociais.

    Ouça uma de suas músicas:
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    # MODERNO E CONTEMPORÂNEO
    st.subheader("🌐 Moderno e Contemporâneo (1900–presente)")
    st.markdown("""
    **🎼 Características técnicas e evolução histórica:**

    - **Blues (final do século XIX – início do século XX):**  
      Robert Johnson, B.B. King  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""
    - **Jazz (início do século XX):**  
      Louis Armstrong, Miles Davis, John Coltrane  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""
    - **Soul (1950s–60s):**  
      Aretha Franklin, Otis Redding  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""
    - **R&B (desde os anos 40):**  
      Ray Charles, Marvin Gaye, Beyoncé  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""
    - **Funk (1960s–70s):**  
      James Brown, Stevie Wonder  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""
    - **Rock (desde os anos 50):**  
      Elvis Presley, The Beatles, Led Zeppelin  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")

    st.markdown("""
    - **Pop (desde os anos 50):**  
      Michael Jackson, Madonna, Taylor Swift  
    """)
    st.audio("https://res.cloudinary.com/dkbvui6sx/video/upload/v1751334700/eu2ofdspdrmzfwosa5ij.mp3")


if choice == "Ritmos":
    st.header("Ritmos Musicais 🥁")

    st.markdown("""
    O ritmo é um dos elementos fundamentais da música. Ele organiza o tempo musical e dá forma às melodias, criando padrões de duração, silêncio e repetição. Independentemente do estilo, é o ritmo que nos faz bater o pé, dançar ou reconhecer uma batida.
    """)

    st.subheader("🔹 Pulsação e Tempo")

    st.markdown("""
    A **pulsação** é a batida constante que sentimos ao ouvir uma música. Ela pode ser lenta ou rápida, mas é sempre regular. Já o **tempo (ou andamento)** é a velocidade dessa pulsação, normalmente medida em **BPM (batidas por minuto)**. Alguns exemplos:
    
    - 🎵 *Lento* (~60 BPM)
    - 🎵 *Moderado* (~90–120 BPM)
    - 🎵 *Rápido* (~140+ BPM)

    O metrônomo é a ferramenta utilizada para marcar o tempo de forma precisa durante os estudos.
    """)

    st.subheader("🔸 Compasso e Métrica")

    st.markdown("""
    O **compasso** organiza a música em pequenos blocos rítmicos com pulsos fortes e fracos. É representado por frações como **4/4**, **3/4**, **6/8** etc.

    - O número de cima indica quantos tempos há no compasso.
    - O número de baixo indica o valor da figura rítmica (ex: 4 = semínima).

    A **métrica** define o padrão acentual desses compassos. Exemplos:
    
    - 2/4 → binário simples (ex: marchas)
    - 3/4 → ternário simples (ex: valsa)
    - 6/8 → binário composto (ex: músicas celtas ou afro-brasileiras)
    """)

    st.subheader("🔹 Figuras Rítmicas")

    st.markdown("""
    As **figuras rítmicas** indicam a duração dos sons. Cada figura possui uma pausa correspondente:

    - **Semibreve (𝅝)**: 4 tempos
    - **Mínima (𝅗𝅥)**: 2 tempos
    - **Semínima (𝅘𝅥)**: 1 tempo
    - **Colcheia (𝅘𝅥𝅮)**: ½ tempo
    - **Semicolcheia (𝅘𝅥𝅯)**: ¼ tempo

    A combinação dessas figuras gera os padrões rítmicos que usamos nas músicas.
    """)

    st.subheader("🔸 Pausas Musicais")

    st.markdown("""
    O silêncio também é parte do ritmo. As **pausas** indicam momentos em que não há som, mas o tempo continua correndo. Cada figura tem sua pausa correspondente, com igual valor de tempo.
    """)

    st.subheader("🔹 Síncope e Contratempo")

    st.markdown("""
    A **síncope** desloca o acento natural do compasso, criando tensão rítmica. Ela ocorre quando um som prolongado atravessa uma batida forte e fraca, ou quando acentuamos uma parte fraca do compasso.

    O **contratempo** é o acento justamente nos tempos fracos, produzindo um efeito de “empurrão” na música. Ambos são comuns em estilos como samba, jazz e reggae.
    """)

    st.subheader("🔸 Polirritmia e Subdivisão")

    st.markdown("""
    A **polirritmia** ocorre quando dois ou mais ritmos diferentes são executados simultaneamente. É comum em músicas africanas, latinas e no jazz moderno.

    Já a **subdivisão** é a divisão interna do tempo. Por exemplo, uma semínima pode ser subdividida em duas colcheias ou quatro semicolcheias, permitindo criar diferentes grooves e variações rítmicas.
    """)

    st.subheader("🎼 Padrões Rítmicos no Mundo")

    st.markdown("""
    Cada cultura desenvolveu padrões rítmicos próprios que influenciaram a música ocidental:

    - **Brasil**: Samba, Baião, Maracatu, Frevo
    - **África Ocidental**: Ritmos polirrítmicos com djembês
    - **Oriente Médio**: Usos complexos de ciclos rítmicos (maqams)
    - **Índia**: Talas (estruturas rítmicas com até 108 tempos)

    Compreender esses ritmos amplia a percepção e a criatividade musical.
    """)


elif choice == "Intervalos":
    st.header("Intervalos Musicais 🎶")

    st.markdown("""
    Os **intervalos musicais** são a distância entre duas notas. Eles são essenciais para compreender a construção de melodias e harmonias. Um intervalo pode ser tocado de forma **melódica** (notas em sequência) ou **harmônica** (notas simultâneas).
    """)

    st.subheader("📏 O que mede um intervalo?")

    st.markdown("""
    A unidade de medida para intervalos é o **tom** e o **semitom**:

    - **1 semitom (½ tom)**: distância entre duas notas adjacentes (ex: C para C♯)
    - **1 tom (2 semitons)**: distância equivalente a dois semitons (ex: C para D)

    A classificação do intervalo depende da **quantidade de tons** entre as duas notas e do **nome das notas envolvidas**.
    """)

    st.subheader("🎵 Tipos de Intervalos com a nota C como exemplo")

    st.markdown("""
    | Nome do Intervalo       | Distância | Exemplo       |
    |-------------------------|-----------|----------------|
    | Uníssono                | 0T        | C – C          |
    | Segunda menor           | ½T        | C – C♯/D♭       |
    | Segunda maior           | 1T        | C – D          |
    | Terça menor             | 1½T       | C – E♭         |
    | Terça maior             | 2T        | C – E          |
    | Quarta justa            | 2½T       | C – F          |
    | Quarta aumentada / Quinta diminuta | 3T | C – F♯/G♭ |
    | Quinta justa            | 3½T       | C – G          |
    | Sexta menor             | 4T        | C – A♭         |
    | Sexta maior             | 4½T       | C – A          |
    | Sétima menor            | 5T        | C – B♭         |
    | Sétima maior            | 5½T       | C – B          |
    | Oitava justa            | 6T        | C – C (oitava) |
    """)

    st.subheader("🎯 Consonância e Dissonância")

    st.markdown("""
    Intervalos podem ser classificados pela sensação que causam:

    - **Consonantes**: sons estáveis, agradáveis ao ouvido (relaxamento).
    - **Dissonantes**: sons instáveis, que geram tensão (movimento).

    | Intervalo               | Classificação       |
    |-------------------------|---------------------|
    | Uníssono                | Consonante          |
    | Segunda menor/maior     | Dissonante          |
    | Terça menor/maior       | Consonante imperfeita |
    | Quarta justa            | Consonante          |
    | Quarta aumentada        | Dissonante          |
    | Quinta justa            | Consonante          |
    | Sexta menor/maior       | Consonante imperfeita |
    | Sétima menor/maior      | Dissonante          |
    | Oitava justa            | Consonante          |
    """)

    st.subheader("💡 Intervalos e Narrativa Musical")

    st.markdown("""
    Assim como uma boa história alterna entre tensão e resolução, uma boa música também equilibra **dissonâncias** e **consonâncias** para emocionar o ouvinte.

    - Os **intervalos dissonantes** criam suspense, energia ou conflito.
    - Os **intervalos consonantes** proporcionam resolução e conforto.

    Saber quando usar cada um é uma escolha estética e emocional. Essa alternância é o que dá vida à música e abre espaço para sua **criatividade** como compositor ou intérprete.
    """)

    st.info("🎧 Dica: Treine identificar os intervalos de ouvido usando aplicativos como Tenuto, Perfect Ear ou teoria online como teoria.com.")

# Função para exibir texto e imagens sobre escalas
def exibir_escalas():
    st.header("Escalas Musicais 🎼")

    st.markdown("""
    Escalas são conjuntos organizados de notas dispostas em ordem ascendente ou descendente. Elas fornecem a base melódica e harmônica da música, guiando a escolha de acordes e melodias dentro de uma tonalidade.

    Cada escala é definida por um padrão fixo de **intervalos** (tons e semitons) e possui uma sonoridade característica, influenciando o clima da música — alegre, melancólico, misterioso ou enérgico.
    """)

    st.subheader("🔹 Escalas Pentatônicas (5 notas)")

    st.markdown("""
    As **escalas pentatônicas** contêm apenas cinco notas por oitava. São simples, versáteis e amplamente usadas em músicas folclóricas, blues, rock e músicas orientais. 

    | Tipo               | Intervalos                             | Exemplo (C)        |
    |--------------------|-----------------------------------------|--------------------|
    | Pentatônica Maior  | T - T - 1½T - T - 1½T                   | C – D – E – G – A  |
    | Pentatônica Menor  | 1½T - T - T - 1½T - T                   | A – C – D – E – G  |
    """)

    image_path = os.path.join('images', 'pentatonica-maior.jpg')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption='Pentatônica Maior')

    image_path = os.path.join('images', 'pentatonica-menor.jpg')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption='Pentatônica Menor')

    st.subheader("🔸 Escalas Maiores (7 notas)")

    st.markdown("""
    As escalas maiores são conhecidas por sua sonoridade alegre, brilhante e estável. A **escala maior natural** é a base do sistema tonal ocidental.

    | Tipo              | Intervalos                              | Exemplo (C)           |
    |-------------------|------------------------------------------|------------------------|
    | Maior Natural     | T - T - ST - T - T - T - ST             | C – D – E – F – G – A – B – C |
    | Maior Harmônica   | T - T - ST - T - ST - 1½T - ST          | C – D – E – F – G – G♯ – B – C |
    | Maior Melódica    | T - T - ST - T - ST - T - ST            | C – D – E – F – G – A – B – C |
    """)

    image_path = os.path.join('images', 'escalas.jpeg')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption='Escalas Maiores e Relativas')

    st.subheader("🔹 Escalas Menores (7 notas)")

    st.markdown("""
    As escalas menores têm uma sonoridade introspectiva, emotiva ou melancólica. Existem três variações principais:

    | Tipo              | Intervalos                              | Exemplo (C)           |
    |-------------------|------------------------------------------|------------------------|
    | Menor Natural     | T - ST - T - T - ST - T - T             | C – D – E♭ – F – G – A♭ – B♭ – C |
    | Menor Harmônica   | T - ST - T - T - ST - 1½T - ST          | C – D – E♭ – F – G – A♭ – B – C |
    | Menor Melódica    | T - ST - T - T - T - T - ST (ascendente)| C – D – E♭ – F – G – A – B – C |
    """)

    st.subheader("🎸 Escala Blues")

    st.markdown("""
    A **escala blues** deriva da escala pentatônica menor com a adição de uma nota chamada **blue note** (quinta diminuta), que dá seu caráter expressivo e melancólico.

    | Notas da Escala Blues (C)         |
    |----------------------------------|
    | C – E♭ – F – F♯ – G – B♭ – C      |

    **Intervalos:** 1½T - T - ST - ST - 1½T - T

    Essa escala é fundamental para o blues, jazz e rock, pois permite improvisações emotivas e com forte identidade sonora.
    """)

    st.success("💡 Dica: experimente tocar as escalas no seu instrumento em diferentes tons para sentir como cada uma afeta a sonoridade da música.")

def acordes():
    st.header("Acordes & Arpejos Musicais 🎹")

    st.markdown("""
    Os **acordes** são combinações de notas tocadas simultaneamente que produzem harmonia. Eles são a base da harmonia na música e ajudam a definir o tom, a emoção e a direção da composição.

    Os acordes são formados por sobreposição de **terças** e podem variar de estruturas simples (tríades) a mais complexas (tétrades e extensões).
    """)

    st.subheader("🔹 Tríades (3 notas)")

    st.markdown("""
    As **tríades** são acordes básicos compostos por três notas: **tônica**, **terça** e **quinta**. Elas são o alicerce de praticamente toda a música tonal ocidental.

    | Tipo               | Fórmula                  | Exemplo (notas) | Sonoridade                   |
    |--------------------|---------------------------|------------------|------------------------------|
    | Tríade Maior       | Tônica - 3ª Maior - 5ª Justa | C – E – G        | Alegre, estável              |
    | Tríade Menor       | Tônica - 3ª Menor - 5ª Justa | A – C – E        | Triste, introspectiva        |
    | Tríade Diminuta    | Tônica - 3ª Menor - 5ª Dim  | B – D – F        | Instável, tensa              |
    | Tríade Aumentada   | Tônica - 3ª Maior - 5ª Aum  | F – A – C♯       | Ambígua, expansiva           |
    """)

    st.image("images/triade-maior.png", caption="Representação visual das tríades", use_column_width=True)

    st.image("images/triade-menor.png", caption="Representação visual das tríades", use_column_width=True)

    st.image("images/triade-diminuta.png", caption="Representação visual das tríades", use_column_width=True)

    st.image("images/triade-aumentada.png", caption="Representação visual das tríades", use_column_width=True)

    st.subheader("🔸 Tétrades (4 notas)")

    st.markdown("""
    As **tétrades** acrescentam uma **quarta nota** à tríade, geralmente uma **sétima**, trazendo mais complexidade harmônica. São muito usadas em jazz, MPB e harmonias avançadas.

    | Tipo                | Fórmula                               | Exemplo (notas)     | Sonoridade                     |
    |---------------------|----------------------------------------|----------------------|--------------------------------|
    | Tétrade Maior (maj7)| T - 3M - 5J - 7M                      | C – E – G – B        | Brilhante, suave               |
    | Tétrade Menor (m7)  | T - 3m - 5J - 7m                      | D – F – A – C        | Suave, emotiva                 |
    | Dominante (7)       | T - 3M - 5J - 7m                      | G – B – D – F        | Tensa, pede resolução          |
    | Diminuta (dim7)     | T - 3m - 5d - 6M (7 diminuta)         | B – D – F – A♭       | Extremamente instável          |
    | Aumentada (maj7#5)  | T - 3M - 5A - 7M                      | F – A♯ – C♯ – E      | Ambígua, moderna               |
    """)

    st.image("images/tetrade-maior7+.png", caption="Representação visual das tríades", use_column_width=True)

    st.image("images/tetrade-dominante7.png", caption="Representação visual das tríades", use_column_width=True)

    st.image("images/tetrade-menor7.png", caption="Representação visual das tríades", use_column_width=True)

    st.image("images/tetrade-meiodiminuta.png", caption="Representação visual das tríades", use_column_width=True)

    st.subheader("🎼 Arpejos")

    st.markdown("""
    Um **arpejo** é quando as notas de um acorde são tocadas **sequencialmente**, uma após a outra, em vez de simultaneamente. Isso cria um efeito melódico com base na harmonia do acorde e é muito usado em solos, acompanhamento e improvisação.

    Os arpejos podem seguir o mesmo formato dos acordes (tríades, tétrades, etc.) e são essenciais para músicos que desejam entender e aplicar harmonia de forma fluida em seus instrumentos.

    | Tipo de Arpejo        | Fórmula                  | Exemplo (notas)     | Aplicação comum                         |
    |------------------------|---------------------------|----------------------|-----------------------------------------|
    | Arpejo Maior           | Tônica - 3ª Maior - 5ª Justa | C – E – G            | Pop, rock, clássico                     |
    | Arpejo Menor           | Tônica - 3ª Menor - 5ª Justa | A – C – E            | Blues, jazz, música triste              |
    | Arpejo Dominante (7)   | T - 3M - 5J - 7m             | G – B – D – F        | Jazz, modulações, resoluções harmônicas|
    | Arpejo Menor 7 (m7)    | T - 3m - 5J - 7m             | D – F – A – C        | Jazz, bossa nova, soul                  |
    | Arpejo Diminuto        | T - 3m - 5d - 6M             | B – D – F – A♭       | Música de suspense, tensão harmônica   |

    Os arpejos também podem ser tocados de forma ascendente, descendente ou alternada, e são uma ferramenta essencial para explorar a sonoridade dos acordes no tempo.
    """)

    st.image("images/Arpejos Tríades 5ª Corda.png", caption="Representação visual das tríades", use_column_width=True)
    st.image("images/Arpejos Tríades 6ª Corda.png", caption="Representação visual das tríades", use_column_width=True)

    

def harmonico():
    st.header("🎼 Campo Harmônico")

    st.markdown("""
Os **campos harmônicos** são conjuntos de acordes derivados de uma **escala** (maior ou menor) usados para construir harmonias e progressões musicais.

Eles são essenciais para compor, improvisar e entender como os acordes se relacionam entre si.

Explore também:

- `/Campo_harmonico_maior` – Acordes derivados da escala maior;
- `/Campo_harmonico_menor` – Acordes da escala menor;
- `/Progressoes_harmonicas` – Padrões típicos usados em músicas;
- `/Modulacao` – Como mudar de uma tonalidade para outra;
- `/Ciclo_das_quartas` e `/Ciclo_das_quintas` – Progressões cíclicas de acordes.
    """)

    st.subheader("🎯 Funções Harmônicas")

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

    st.subheader("🌞 Campo Harmônico Maior")

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

    st.subheader("🌑 Campo Harmônico Menor")

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

    st.subheader("🔄 Ciclo das Quartas")

    st.markdown("""
O **ciclo das quartas** move-se por **quartas justas descendentes** (ou quintas ascendentes lidas ao contrário). Usado para:

- Modulação entre tonalidades;
- Progressões harmônicas previsíveis;
- Improvisação e prática.

**Exemplo:**

C → F → Bb → Eb → Ab → Db → Gb → B → E → A → D → G → C
""")

    st.subheader("🔁 Ciclo das Quintas")

    st.markdown("""
O **ciclo das quintas** move-se por **quintas justas ascendentes**. É uma ferramenta fundamental para:

- Compor progressões que retornam naturalmente à tônica;
- Navegar entre tonalidades;
- Construir músicas com cadência satisfatória.

**Exemplo:**

C → G → D → A → E → B → F♯ → C♯ → G♯ → D♯ → A♯ → F → C

> 💡 O ciclo das quartas é o ciclo das quintas lido de trás pra frente!
""")

    st.subheader("🎚️ Modulação")

    st.markdown("""
A **modulação** é a transição de uma tonalidade para outra durante uma música. Ela pode:

- Aumentar a expressividade;
- Evitar monotonia;
- Reforçar a narrativa musical.

**Tipos de Modulação:**

| Tipo                   | Descrição |
|------------------------|-----------|
| **Direta**             | Mudança abrupta, sem preparação |
| **Gradual**            | Usa acordes comuns entre tonalidades |
| **Dominante secundária** | Usa o acorde V da nova tonalidade |
| **Cromática**          | Usa notas/intervalos fora da escala original |

**Exemplo:**  
C → G usando um acorde de D7 (dominante secundária de G)
""")

    st.success("💡 Dica: Tente tocar uma progressão do campo harmônico maior e depois modular para seu relativo menor. Você notará um contraste emocional instantâneo!")

    st.markdown("""
---
Explore os tópicos complementares:

- `/Campo_harmonico_maior`
- `/Campo_harmonico_menor`
- `/Progressoes_harmonicas`
- `/Modulacao`
- `/Ciclo_das_quartas`
- `/Ciclo_das_quintas`
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
    st.header("📚 Recursos Adicionais")

    recursos_text = """
Explore aqui uma curadoria de **materiais gratuitos** para aprofundar seus estudos em Teoria Musical.

Use também os comandos rápidos para navegar diretamente:

- `/Ebooks` → 📖 Livros digitais gratuitos  
- `/Sites` → 🌐 Ferramentas e simuladores online  
- `/Videos` → 🎥 Aulas em vídeo

---
"""

    st.markdown(recursos_text)

    # EBOOKS
    st.markdown("## 📖 Ebooks Gratuitos")
    st.markdown("""
Esses ebooks são indicados para complementar seus estudos em tópicos como harmonia, percepção musical, leitura de partituras e improvisação.  

*(Disponíveis via aba `/Ebooks` ou buscáveis na internet em plataformas como IMSLP ou bibliotecas digitais de música.)*

---

""")

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
    st.write("Conteúdo sobre a história da música")
elif choice == "Períodos Históricos":
    st.write("Conteúdo sobre os períodos históricos da música")
elif choice == "Ritmos":
    st.write("Conteúdo sobre ritmos musicais")
elif choice == "Intervalos":
    st.write("Conteúdo sobre intervalos musicais")
elif choice == "Escalas":
    exibir_escalas()
elif choice == "Acordes & Arpejos":
    acordes()
elif choice == "Campos harmônicos":
    harmonico()
elif choice == "Modos gregos":
    gregos()
elif choice == "Recursos adicionais":
    recursos()
