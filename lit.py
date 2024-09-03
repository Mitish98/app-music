import streamlit as st
import os
from PIL import Image

# Título da aplicação no Streamlit
st.title("Chatbot de Música")

# Adicionar uma descrição
st.write("""
Bem-vindo ao Chatbot de Música! 
Este é um chatbot que ajuda você a entender teoria musical, ritmos, e muito mais. 
Navegue pelas funcionalidades e explore o mundo da música com nosso assistente interativo.
""")

# Menu de opções
menu = ["História", "Ritmos", "Intervalos", "Escalas", "Acordes", "Campos harmônicos", "Modos gregos", "Recursos adicionais"]
choice = st.sidebar.selectbox("Escolha um tema", menu)

# Interface para inserir comandos e receber respostas
if choice == "História":
    st.subheader("História da Música")
    if st.button("Mostrar História"):
        historia_text = """
*História da Música*

As origens da música remontam a tempos pré-históricos e, muitas vezes, se confundem com o próprio surgimento do ser humano na Terra. 

Alguns teóricos e filósofos relacionam a origem da música com a origem da linguagem, com muita discordância em torno de se a música surgiu antes, depois ou simultaneamente. 

Uma das primeiras teses canônicas a respeito surgiu com o filósofo Jean-Jacques Rousseau, que disse que nos primórdios os seres humanos utilizavam a língua cantada. Mas, apesar disso, nenhuma teoria alcançou ampla aprovação na comunidade científica até os dias de hoje. 

A maioria das culturas tem seus próprios mitos fundadores relacionados à invenção da música, geralmente enraizados em suas respectivas crenças mitológicas, religiosas ou filosóficas. Apesar de muitas espécies produzirem sons para se comunicarem, o ser humano é o único animal capaz de organizar os sons de uma forma recursiva, criando uma infinidade sonora com o corpo e com a natureza.

Todas as culturas conhecidas utilizaram a música como forma de expressão e, por isso, a música é considerada um universal cultural da humanidade. Mas, foi com o estudo de Pitágoras que os seres humanos começaram a estudar a música de forma científica.

Pitágoras desenvolveu o estudo (...)
        """
        st.write(historia_text)


elif choice == "Ritmos":
    st.subheader("Ritmos Musicais")
    if st.button("Mostrar Ritmos"):
        ritmos_text = """
*Ritmos Musicais*

Os ritmos são uma parte fundamental da música, proporcionando a estrutura temporal e a organização dos sons. Aqui estão alguns conceitos importantes relacionados aos ritmos:

- *Pulsação*: A pulsação é o batimento regular que serve como o "tempo" da música. É o que você sentiria como a batida básica em uma música.

- *Métrica*: A métrica organiza a pulsação em grupos regulares chamados de compassos. Cada compasso é subdividido em batidas, e essas batidas são agrupadas em padrões regulares.

- *Tempo*: O tempo refere-se à velocidade com que a pulsação é apresentada. Pode ser rápido (allegro) ou lento (adagio), e é geralmente indicado por uma marcação no início da peça.

- *Duração das Notas*: As notas musicais têm diferentes durações, que podem ser representadas por valores como semínimas, colcheias, e mínimas. Essas durações definem o comprimento dos sons e das pausas na música.

- *Ritmo e Sincope*: O ritmo é a forma como as notas são organizadas em relação à pulsação. A síncope é um deslocamento rítmico que cria um efeito de surpresa ao colocar notas em lugares inesperados.

- *Polirritmia*: A polirritmia é a combinação de dois ou mais ritmos diferentes tocados simultaneamente. É comum em músicas africanas e jazz.

        """
        st.write(ritmos_text)

elif choice == "Intervalos":
    st.subheader("Intervalos Musicais")
    if st.button("Mostrar Intervalos"):
        intervalos_text = """
*Intervalos Musicais*

Os intervalos são as distâncias entre duas notas e são fundamentais para a construção de acordes e melodias. Aqui estão alguns conceitos chave sobre intervalos:

- *Intervalo de Primeira*: A distância entre duas notas da mesma altura. Também chamado de intervalo uníssono.

- *Intervalo de Segunda*: A distância entre duas notas adjacentes. Pode ser maior (ex.: C a D) ou menor (ex.: C a C#).

- *Intervalo de Terça*: A distância de três notas. Pode ser maior (ex.: C a E) ou menor (ex.: C a Eb).

- *Intervalo de Quarta*: A distância de quatro notas. Pode ser perfeita (ex.: C a F) ou aumentada (ex.: C a F#).

- *Intervalo de Quinta*: A distância de cinco notas. Pode ser perfeita (ex.: C a G) ou diminuta (ex.: C a Gb).

- *Intervalo de Sexta*: A distância de seis notas. Pode ser maior (ex.: C a A) ou menor (ex.: C a Ab).

- *Intervalo de Sétima*: A distância de sete notas. Pode ser maior (ex.: C a B) ou menor (ex.: C a Bb).

- *Intervalos Aumentados e Diminutos*: São intervalos que ultrapassam os intervalos perfeitos e maiores/méiores, criando uma tensão adicional.

        """
        st.write(intervalos_text)

# Função para exibir texto e imagens sobre escalas
def exibir_escalas():
    st.subheader("Escalas Musicais")

    escalas_text = """
    Escalas musicais são sequências ordenadas de notas musicais que seguem padrões específicos de intervalos entre cada nota. 
    
    Elas formam a estrutura básica sobre a qual a música é construída, fornecendo um conjunto organizado de notas que determinam a sonoridade e o caráter de uma peça musical. 
    
    Existem diferentes tipos de escalas, entre elas: 
    
    - **Escalas Pentatônicas**: Escalas musicais que consistem em cinco notas por oitava.
    - **Escala Maior**: Conjunto de escalas musicais amplamente utilizadas na música ocidental.
    - **Escala Menor**: Outro conjunto de escalas musicais amplamente difundidas entre músicos.
    - **Escala Blues**: Escala musical utilizada no blues, rock 'n' roll e jazz.
    """
    st.write(escalas_text)

    # Exibir imagem
    image_path = os.path.join('images', 'escalas.jpeg')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption='Escalas Musicais')

# Função para exibir texto e imagens sobre escalas pentatônicas
def exibir_escalas_pentatonicas():
    st.title("Escalas Pentatônicas")

    escalas_pentatonicas_text = """
    *Escalas Pentatônicas*

    As escalas pentatônicas são escalas musicais que consistem em cinco notas por oitava, daí o termo "penta" que significa cinco. 

    Elas são amplamente usadas em diversas culturas musicais ao redor do mundo devido à sua simplicidade e sonoridade agradável. 

    Por não conterem semitons adjacentes, as escalas pentatônicas tendem a criar sonoridades mais estáveis e menos dissonantes.

    *Tipos de Escalas Pentatônicas*

    - **Pentatônica Maior:** 

      Segunda Maior - Terça Maior - Quinta Justa - Sexta Maior - Oitava

      Tonalidade - 1T - 1T - 1,5T - 1T - 1,5T.
      
      Exemplo em Dó: C - D - E - G - A - C.

    - **Pentatônica Menor:** 

      Terça Menor - Quarta Justa - Quinta Justa - Sétima Menor - Oitava

      Tonalidade - 1,5T - 1T - 1T - 1,5T - 1T. 
      
      Exemplo em Lá: A - C - D - E - G - A.
    """
    st.write(escalas_pentatonicas_text)

    # Exibir imagens
    image_path_maior = os.path.join('images', 'pentatonica-maior.jpg')
    if os.path.exists(image_path_maior):
        image = Image.open(image_path_maior)
        st.image(image, caption='Pentatônica Maior')

    image_path_menor = os.path.join('images', 'pentatonica-menor.jpg')
    if os.path.exists(image_path_menor):
        image = Image.open(image_path_menor)
        st.image(image, caption='Pentatônica Menor')

# Função para exibir texto e imagens sobre escalas maiores
def exibir_escala_maior():
    st.title("Escala Maior")

    escala_maior_text = """
    *Escala Maior*

    A escala maior é uma das escalas mais fundamentais e amplamente utilizadas na música ocidental, composta por sete notas separadas por intervalos específicos. 

    As notas na escala maior formam acordes que são considerados estáveis e consonantes, facilitando a harmonização e composição musical. 

    Muitas composições usam a escala maior como ponto de partida e modulam para outras tonalidades relacionadas durante o desenvolvimento da peça.

    *Tipos de escalas maiores*

    - **Escala Maior Natural:** 

      Segunda Maior - Terça Maior - Quarta Justa - Quinta Justa - Sexta Maior - Sétima Maior - Oitava

      Tonalidade - T - T - ST - T - T - T - ST

      Exemplo: C - D - E - F - G - A - B - C

    - **Escala Maior Harmônica:** 

      Semelhante à escala maior natural, mas com a sexta menor.

      Segunda Maior - Terça Maior - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Maior - Oitava

      Tonalidade - T - T - ST - T - ST - 1,5T - ST

      Exemplo: C - D - E - F - G - G# - B - C

    - **Escala Maior Melódica:** 

      Semelhante à escala maior natural, mas com a sexta e a sétima menor. 

      Segunda Maior - Terça Maior - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Menor - Oitava

      Tonalidade - T - T - ST - T - ST - T - ST
    """
    st.write(escala_maior_text)

# Função para exibir texto e imagens sobre escalas menores
def exibir_escala_menor():
    st.title("Escala Menor")

    escala_menor_text = """
    *Escala Menor*

    A escala menor é uma escala fundamental na música ocidental, conhecida por seu som mais sombrio e emotivo em comparação com a escala maior. 

    Assim como na escala maior, a escala menor também pode ser usada como ponto de partida para modulações e desenvolvimentos tonais na composição.

    Em muitas composições, a alternância entre escalas maior e menor é usada para criar contrastes emocionais e atmosféricos, já que muitas escalas menores são relativas às escalas maiores, ou seja, possuem as mesmas notas em diferentes ordens. 

    *Tipos de Escalas Menores*

    - **Escala Menor Natural:** 

      Segunda Maior - Terça Menor - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Menor - Oitava 

      Tonalidade - T - ST - T - T - ST - T - T

      Exemplo: C - D - D# - F - G - G# - A# - C

    - **Escala Menor Harmônica:** 

      Semelhante à escala menor natural, mas com a sétima maior

      Segunda Maior - Terça Menor - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Maior - Oitava 

      Tonalidade - T - ST - T - T - ST - 1,5T - ST

      Exemplo: C - D - D# - F - G - G# - B - C

    - **Escala Menor Melódica:** 

      Esta escala varia na subida e na descida. Quando ascendente, é semelhante à escala menor natural, mas com a sexta e a sétima maior. Já no movimento descente, retorna à escala menor natural.

      Segunda Maior - Terça Menor - Quarta Justa - Quinta Justa - Sexta Maior - Sétima Maior - Oitava

      Tonalidade - T - ST - T - T - T - T - ST
    """
    st.write(escala_menor_text)

# Função para exibir texto e imagens sobre escalas blues
def exibir_escala_blues():
    st.title("Escala Blues")

    escala_blues_text = """
    *Escala Blues*

    A escala de blues é uma das escalas mais icônicas e reconhecíveis na música, especialmente no gênero do blues, mas também é amplamente utilizada em jazz, rock e outros estilos musicais. 

    A característica mais distintiva da escala de blues são as "blue notes", que são notas alteradas ou inflexionadas. Essas notas geralmente incluem a *terça menor, a quinta diminuta e a sétima menor*, adicionando uma sonoridade única e emotiva à escala.

    A escala de blues é essencialmente uma escala pentatônica com adição de blue notes. Isso significa que ela contém cinco notas principais (pentatônica) com a inclusão de uma ou mais blue notes, dependendo do contexto tonal e estilístico. 

    *Composição da Escala*

    - **Escala de Blues:** 

      Nota Fundamental - Terça Menor - Quarta Justa - Quinta Diminuta - Quinta Justa - Sétima Menor - Oitava 

      Tonalidade - T - ST - ST - ST - T - ST - T

      Exemplo: C - Eb - F - F# - G - Bb - C
    """
    st.write(escala_blues_text)

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
