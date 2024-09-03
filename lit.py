import streamlit as st
import os
from PIL import Image

# Título da aplicação no Streamlit
st.title("Chatbot de Teoria Musical")

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
    historia_text = """

As origens da música remontam a tempos pré-históricos e, muitas vezes, se confundem com o próprio surgimento do ser humano na Terra. 

Alguns teóricos e filósofos relacionam a origem da música com a origem da linguagem, com muita discordância em torno de se a música surgiu antes, depois ou simultaneamente. 

Uma das primeiras teses canônicas a respeito surgiu com o filósofo Jean-Jacques Rousseau, que disse que nos primórdios os seres humanos utilizavam a língua cantada. Mas, apesar disso, nenhuma teoria alcançou ampla aprovação na comunidade científica até os dias de hoje. 

A maioria das culturas tem seus próprios mitos fundadores relacionados à invenção da música, geralmente enraizados em suas respectivas crenças mitológicas, religiosas ou filosóficas. Apesar de muitas espécies produzirem sons para se comunicarem, o ser humano é o único animal capaz de organizar os sons de uma forma recursiva, criando uma infinidade sonora com o corpo e com a natureza.

Todas as culturas conhecidas utilizaram a música como forma de expressão e, por isso, a música é considerada um universal cultural da humanidade. Mas, foi com o estudo de Pitágoras que os seres humanos começaram a estudar a música de forma científica.

Pitágoras desenvolveu o estudo (...)

Apesar de não ser uma medida exata, a história da música pode ser dividida entre diferentes períodos de acordo com as mudanças tecnológicas e expressivas do ser humano. Alguns desses períodos são: 

- *Pré-História*: Musicalidade corporal e instrumentos primitivos como flautas feitas de ossos e tambores.

- *Antiguidade*: A música era uma parte importante da vida religiosa e social. Instrumentos como a lira, harpa e flautas eram populares. Os gregos desenvolveram teorias musicais que influenciaram profundamente a música ocidental, principalmente nas sociedades da Mesopotâmia, Egito e Grécia Antiga 

- *Idade Média*: O canto gregoriano era predominante na Igreja Católica. Desenvolveram-se notações musicais primitivas. Troubadours e trovadores espalharam a música secular pela Europa.

- *Renascimento (1400-1600)*: Desenvolvimento da música polifônica, onde múltiplas linhas melódicas são tocadas simultaneamente. Forma popular de música vocal secular na Itália e Inglaterra. A popularidade dos instrumentos de tecla e corda aumentou.

- *Barroco (1600-1750)*: A ópera nasceu na Itália e se espalhou por toda a Europa. Formação das primeiras orquestras e desenvolvimento da música orquestral, apresentando compositores como Johann Sebastian Bach, George Frideric Handel, Antonio Vivaldi.

- *Clássico (1750-1820)*: A música clássica focava em clareza, ordem e equilíbrio, com as composições de Wolfgang Amadeus Mozart, Ludwig van Beethoven (período inicial), Franz Joseph Haydn.

- *Romântico (1820-1900)*: Maior foco na expressão emocional e individualismo. Expansão das orquestras e complexidade das composições. Ludwig van Beethoven (período tardio), Franz Schubert, Johannes Brahms, Pyotr Ilyich Tchaikovsky, Richard Wagner.

- *Moderno (Século XX)*: Surgimento de inúmeros estilos e gêneros populares, incluindo jazz, rock, pop, música eletrônica e hip-hop. Experimentação com formas, tonalidades e novas tecnologias permitiram maior intercâmbio e fusão de músicas de diferentes culturas.

        """
    st.write(historia_text)


elif choice == "Ritmos":
    st.subheader("Ritmos Musicais")
    
    ritmos_text = """
O ritmo musical, junto com a melodia e harmonia, é um dos três fundamentos da música. 

Os ritmos musicais definem a organização das notas e dos acordes que serão tocados em uma peça musical.

Para estudar o ritmo, usam-se os conceitos: 

*Beat*

O beat é a pulsação constante que pode ser sentida na música, similar ao batimento cardíaco, servindo como a base para a duração das notas e dos silêncios.

Assim, o beat é o que mantém a música organizada no tempo, ajudando os músicos a manterem-se sincronizados.

Por exemplo, em uma música com um tempo de 60 BPM (batidas por minuto), a pulsação ocorre a cada um segundo; enquanto que, em uma música de 120 BPM, a pulsação ocorre a cada meio segundo.

*Duração*

A duração marca o período das notas e das pausas, ou seja, marca por quanto tempo uma nota ou uma pausa deve ser tocada.

No contexto da teoria musical, usam-se os termos "mínima", "semínima", "colcheia", entre outros, para classificação da duração dos sons. 

Veja um resumo dos principais valores de notas e pausas:

- Semibreve:

    Nota: Uma semibreve equivale a quatro tempos em uma medida 4/4.
    Pausa: A pausa de semibreve também dura quatro tempos.

- Mínima:

    Nota: Uma mínima dura dois tempos.
    Pausa: A pausa de mínima também dura dois tempos.

- Semínima:

    Nota: Uma semínima dura um tempo.
    Pausa: A pausa de semínima também dura um tempo.

- Colcheia:

    Nota: Uma colcheia dura metade de um tempo.
    Pausa: A pausa de colcheia também dura metade de um tempo.

- Semicolcheia:

    Nota: Uma semicolcheia dura um quarto de um tempo.
    Pausa: A pausa de semicolcheia também dura um quarto de um tempo.

- Fusa:

    Nota: Uma fusa dura um oitavo de um tempo.
    Pausa: A pausa de fusa também dura um oitavo de um tempo.

- Semifusa:

    Nota: Uma semifusa dura um décimo sexto de um tempo.
    Pausa: A pausa de semifusa também dura um décimo sexto de um tempo.

Esses valores de notas e pausas são fundamentais para a leitura e escrita de partituras, permitindo aos músicos compreender a duração relativa das notas e pausas e, assim, interpretar corretamente o ritmo de uma peça musical.

*Compasso*

O compasso é a organização dos tempos em padrões regulares de batidas fortes e fracas.
Indicado por uma fórmula de compasso, como 4/4, 3/4, 6/8, etc.

Os diferentes tipos de compassos são:

- Simples:

    Exemplo: 4/4 (quatro tempos por compasso, cada tempo é uma semínima)
    Padrão de acentuação: Forte, fraco, médio-forte, fraco

- Composto:

    Exemplo: 6/8 (seis colcheias por compasso, organizado em dois grupos de três colcheias)
    Padrão de acentuação: Forte, fraco, fraco, médio-forte, fraco, fraco

*Ritmo*

O ritmo é o padrão de duração das notas e pausas em uma peça musical.

- Ritmo Simples:

    Uma sequência de semínimas em 4/4: ♩ ♩ ♩ ♩

- Ritmo Complexo:

    Uma sequência mista em 4/4: ♩ ♪ ♫ ♩ ♬

*Padrões Rítmicos*

Padrões rítmicos são sequências que foram consagradas em gêneros musicais, sendo os mais conhecidos entre os músicos:

- Bossa Nova: Originário do Brasil, caracteriza-se por um padrão rítmico sincopado e suave.

- Salsa: Ritmo de dança latino-americano com ênfase em padrões rítmicos complexos e percussão.

- Waltz: Ritmo de três tempos associado à dança de salão, caracterizado por um padrão de 1-2-3 repetitivo.

- Mazurka: Originária da Polônia, uma dança com um padrão rítmico característico de três tempos, com ênfase no segundo tempo.

- Hip-Hop: Utiliza batidas fortes e frequentemente sincopadas, com amostras de música e loops.

- Reggae: Originário da Jamaica, caracteriza-se por um ritmo distinto chamado de "batida" ou "beat" que enfatiza o terceiro tempo do compasso.

- Afro-Cubano: Combinação de influências africanas e cubanas, com ritmos como o "clavé" e complexas polirritmias.

- Flamenco: Originário da Espanha, possui um ritmo característico chamado "compás", com variações entre diferentes estilos.

- Samba: Ritmo brasileiro com raízes africanas, marcado por um padrão rítmico distintivo e percussivo.

- Tango: Originário da Argentina, com um ritmo de dois tempos e ênfase na melancolia e paixão.

Os ritmos não apenas estruturam a música, mas também são essenciais para criar atmosfera, emoção e movimento dentro de uma composição. Cada cultura e gênero musical desenvolveu seus próprios ritmos distintos, contribuindo para a diversidade e riqueza da música global.

        """
    st.write(ritmos_text)

elif choice == "Intervalos":
    st.subheader("Intervalos Musicais")
    intervalos_text = """

Os intervalos musicais são as distâncias entre dois sons, medidos em tons e semi-tons. 

Eles desempenham um papel fundamental na Teoria Musical porque são essas distâncias entre as notas que são o sentido sonoro de uma música.

Os intervalos musicais são usados tanto para serem tocados em sequência, criando linhas melódicas; quanto em conjunto, para formarem a harmonia de acordes.


Esses são os nomes dos intervalos musicais usando a nota dó (C) como referência:

- *Uníssono*: Nota que marca o tom da melodia, como C.

- *Segunda Menor*: Nota que está a meio tom (0,5T) de distância, como C - C# (D♭).

- *Segunda Maior*: Nota que está a um tom (1T) de distância, como C - D.

- *Terça Menor*: Nota que está a um tom e meio (1,5T) de distância, como C - D# (E♭). 

- *Terça Maior*: Nota que está a dois tons (2T) de distância, como C - E.

- *Quarta Justa*: Nota que está a dois tons e meio (2,5T) de distância, como C - F.

- *Quarta Aumentada ou Quinta Diminuta*: Nota que está a três tons (3T) de distância, como C - F♯ (G♭).

- *Quinta Justa*: Nota que está a três tons e meio (3,5T) de distância, como C - G.

- *Sexta Menor*: Nota que está a quatro tons (4T) de distância, como C - G# (A♭).

- *Sexta Maior*: Nota que está a quatro tons e meio (4,5T) de distância, como C - A.

- *Sétima Menor*: Nota que está a cinco tons (5T) de distância, como C - A# (B♭).

- *Sétima Maior*: Nota que está a cinco tons e meio (5,5T) de distância, como C - B.

- *Oitava*: Nota que está a seis tons de distância, como C - C. 



        Exemplo: /ia 
            
            "Quais são os intervalos musicais de Lá sustenido?"


Para saber como e quando utilizá-los, precisamos saber as características dos intervalos musicais, que podem ser: 

- *Dissonantes*: Intervalos que criam tensão, usados para criar movimento ou expectativa na música.

- *Consonantes*: Intervalos que criam resolução, usados para criar a sensação de descanso ou conclusão na música. 


- Uníssono -> Consonante

- Segunda Menor -> Dissonante

- Segunda Maior -> Dissonante

- Terça Menor -> Consonante imperfeita

- Terça Maior -> Consonante imperfeita

- Quarta Justa -> Consonante 

- Quarta Aumentada -> Dissonante

- Quinta Justa -> Consonante

- Sexta Menor -> Consonante imperfeita

- Sexta Maior -> Consonante imperfeita

- Sétima Menor -> Dissonante 

- Sétima Maior -> Dissonante

- Oitava -> Consonante


Para saber quando utilizar os intervalos dissonantes ou consonantes, podemos pensar na música como uma narrativa. 

Normalmente, para contar uma boa história, precisamos transitar entre momentos de conflitos e momentos de conclusão para criar uma trama envolvente.

Com a música ocorre algo muito parecido, porque para criar uma música emocionante é preciso transitar entre a tensão dos intervalos dissonantes e o relaxamento dos intervalos consonantes constantemente para envolver o ouvinte. Decidir como e quando fazer isso é o que vai determinar o seu estilo como músico e, por isso, não existe uma fórmula para criar uma música além do que estudamos em Teoria Musical. É aí que entra a sua criatividade em jogo...


Se você estiver com alguma dúvida sobre intervalos musicais, não hesite em perguntar para a assistente com inteligência artificial usando o comando /ia. 

Ou então, envie sua pergunta para ourcontentdigital@gmail.com que responderemos assim que possível. 

        """
    
    st.write(intervalos_text)

# Função para exibir texto e imagens sobre escalas
def exibir_escalas():
    st.subheader("Escalas Musicais")
    escalas_text = """
    
Escalas musicais são sequências ordenadas de notas musicais que seguem padrões específicos de intervalos entre cada nota. 

Elas formam a estrutura básica sobre a qual a música é construída, fornecendo um conjunto organizado de notas que determinam a sonoridade e o caráter de uma peça musical. 

Existem diferentes tipos de escalas, entre elas: 

- /Escalas_pentatonicas: Escalas pentatônicas são escalas musicais que consistem em cinco notas por oitava.

- /Escala_maior: Conjunto de escalas musicais amplamente utilizadas na música ocidental.

- /Escala_menor: Outro conjunto de escalas musicais amplamente difundidas entre músicos.

- /Escala_blues: Escala musical utilizada no blues, rock 'n' roll e jazz.



*Escalas Pentatônicas*

As escalas pentatônicas são escalas musicais que consistem em cinco notas por oitava, daí o termo "penta" que significa cinco. 

Elas são amplamente usadas em diversas culturas musicais ao redor do mundo devido à sua simplicidade e sonoridade agradável. 

Por não conterem semitons adjacentes, as escalas pentatônicas tendem a criar sonoridades mais estáveis e menos dissonantes.

*Tipos de Escalas Pentatônicas*

Veja as principais escalas pentatônicas:

- *Pentatônica Maior:* 

  Segunda Maior - Terça Maior - Quinta Justa - Sexta Maior - Oitava

  Tonalidade - 1T - 1T - 1,5T - 1T - 1,5T.
  
  Exemplo em Dó: C - D - E - G - A - C.

- *Pentatônica Menor:* 

  Terça Menor - Quarta Justa - Quinta Justa - Sétima Menor - Oitava

  Tonalidade - 1,5T - 1T - 1T - 1,5T - 1T. 
  
  Exemplo em Lá: A - C - D - E - G - A.

  *Escala Maior*

A escala maior é uma das escalas mais fundamentais e amplamente utilizadas na música ocidental, composta por sete notas separadas por intervalos específicos. 

As notas na escala maior formam acordes que são considerados estáveis e consonantes, facilitando a harmonização e composição musical. 

Muitas composições usam a escala maior como ponto de partida e modulam para outras tonalidades relacionadas durante o desenvolvimento da peça.


*Tipos de escalas maiores*

Veja agora as três principais escalas maiores


    - *Escala Maior Natural:* Comporta todas as notas naturais de Dó à Dó.

Segunda Maior - Terça Maior - Quarta Justa - Quinta Justa - Sexta Maior - Sétima Maior - Oitava

Tonalidade - T - T - ST - T - T - T - ST

    Exemplo: C - D - E - F - G - A - B - C


    - *Escala Maior Harmônica:* Semelhante à escala maior natural, mas com a sexta menor.

Segunda Maior - Terça Maior - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Maior - Oitava

Tonalidade - T - T - ST - T - ST - 1,5T - ST

    Exemplo: C - D - E - F - G - G# - B - C

    
    - *Escala Maior Melódica:* Semelhante à escala maior natural, mas com a sexta e a sétima menor. 

Segunda Maior - Terça Maior - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Menor - Oitava

Tonalidade - T - T - ST - T - ST - T - ST


*Escala Menor*

A escala menor é uma escala fundamental na música ocidental, conhecida por seu som mais sombrio e emotivo em comparação com a escala maior. 

Assim como na escala maior, a escala menor também pode ser usada como ponto de partida para modulações e desenvolvimentos tonais na composição.

Em muitas composições, a alternância entre escalas maior e menor é usada para criar contrastes emocionais e atmosféricos, já que muitas escalas menores são relativas às escalas maiores, ou seja, possuem as mesmas notas em diferentes ordens. 

*Tipos de Escalas Menores*

Veja agora as três principais escalas menores.


    - *Escala Menor Natural:* 


Segunda Maior - Terça Menor - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Menor - Oitava 

Tonalidade - T - ST - T - T - ST - T - T

    Exemplo: C - D - D# - F - G - G# - A# - C

    
    - *Escala Menor Harmônica:* Semelhante à escala menor natural, mas com a sétima maior

Segunda Maior - Terça Menor - Quarta Justa - Quinta Justa - Sexta Menor - Sétima Maior - Oitava 

Tonalidade - T - ST - T - T - ST - 1,5T - ST

    Exemplo: C - D - D# - F - G - G# - B - C


    - *Escala Menor Melódica:* Esta escala varia na subida e na descida. Quando ascendente, é semelhante à escala menor natural, mas com a sexta e a sétima maior. Já no movimento descente, retorna à escala menor natural.

Segunda Maior - Terça Menor - Quarta Justa - Quinta Justa - Sexta Maior - Sétima Maior - Oitava

Tonalidade - T - ST - T - T - T - T - ST

    Exemplo: C - D - D# - F - G - A - B - C

*Escala Blues*

A escala de blues é uma das escalas mais icônicas e reconhecíveis na música, especialmente no gênero do blues, mas também é amplamente utilizada em jazz, rock e outros estilos musicais. 

A característica mais distintiva da escala de blues são as "blue notes", que são notas alteradas ou inflexionadas. Essas notas geralmente incluem a *terça menor, a quinta diminuta e a sétima menor*, adicionando uma sonoridade única e emotiva à escala.

A escala de blues é essencialmente uma escala pentatônica com adição de blue notes. Isso significa que ela contém cinco notas principais (pentatônica) com a inclusão de uma ou mais blue notes, dependendo do contexto tonal e estilístico. 

A presença das blue notes permite aos músicos explorar uma ampla gama de emoções e expressões musicais. Essas notas adicionam tensão, melancolia e um sentimento de "blues" à música.


*Estrutura da Escala de Blues:* 

Terça Menor - Quarta Justa - Quinta Diminuta - Quinta Perfeita - Sétima Menor - Oitava

Tonalidade - 1,5T - T - ST - ST - 1,5T - T
    """
    st.write(escalas_text)

    # Exibir imagem
    image_path = os.path.join('images', 'escalas.jpeg')
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption='Escalas Musicais')

def acordes():
    st.subheader("Acordes")
    acordes_text = """
    

Acordes são um conjunto de notas tocadas simultaneamente de forma harmônica. 

São divididos conceitualmente em: 

- /Triades: Triades são os acordes mais básicos e fundamentais na teoria musical ocidental. Elas consistem em três notas que são sobrepostas de uma maneira específica para criar um som harmonioso.
    
- /Tetrades: Tetrades são acordes que consistem em quatro notas distintas tocadas simultaneamente. Esses acordes são mais complexos do que as triades porque adicionam uma quarta nota à estrutura básica.
        
- /Inversoes: Referem-se a diferentes arranjos de notas dentro de um acorde, onde a nota mais grave muda sem alterar as outras notas do acorde. 

*Tríades*

As tríades são elementos cruciais na teoria musical e na prática de composição. 

Elas proporcionam a estrutura básica para a harmonia tonal e são essenciais para músicos entenderem a relação entre notas e a construção de acordes dentro de uma determinada tonalidade. 


*Tipos de Tríades:*

Veja agora os principais tipos de sobreposições com três notas para compor acordes.


    - *Tríade Maior*: 

Possui uma sonoridade alegre e estável, frequentemente associada a sentimentos positivos.

Composta pela Tônica, Terça Maior e Quinta Justa.
        
    C + E + G -> Formando o acorde Dó maior (C)

        
    - *Tríade Menor*: 

Possui uma sonoridade melancólica, sombria e introspectiva, associada a emoções mais sérias e tristes.

Composta pela Tônica, Terça Menor e Quinta Justa. 

    A + C + E -> Formando o acorde de Lá menor (Am)

        
    - *Tríade Diminuta*: 

Possui uma sonoridade tensa e instável, usada para criar uma sensação de suspense e movimento, muitas vezes resolvendo para acordes mais estáveis. 

Composta pela Tônica, Terça Menor e Quinta Diminuta. 

    B + D + F -> Formando o acorde Si diminuto (B°)

    
    - *Tríade Aumentada*: 

Possui uma sonoridade expansiva, intrigante e ambígua, usada para criar efeitos de suspensão e para introduzir complexidade harmônica, sendo mais usada em passagens sofisticadas e progressões avançadas.

Composta pela Tônica, Terça Maior e Quinta Aumentada (Sexta Menor)

    F + A + C♯ -> Formando o acorde Fá aumentado

    *Tétrades*

As tetrades adicionam maior complexidade e riqueza sonora em comparação com as triades, sendo amplamente utilizadas em jazz, música erudita e estilos contemporâneos, permitindo a inclusão de extensões como nonas (9), décimas terças (11) e décimas quintas (13), expandindo ainda mais as possibilidades harmônicas. 

São fundamentais em progressões harmônicas complexas e na improvisação, oferecendo aos músicos uma base sólida para explorar diferentes sensações sonoras.


*Tipos de Tétrades:*

Veja agora os principais tipos de sobreposições com quatro notas para compor acordes complexos.


    - *Tétrade Maior (Maj7)*: 

Composta pela Tônica, Terça Maior, Quinta Justa e Sétima Maior.

    C - E - G - B -> Dó maior com sétima maior (Cmaj7)

    
    - *Tétrade Menor (m7)*: 

Composta pela Tônica, Terça Menor, Quinta Justa e Sétima Menor.

    D - F - A - C -> Ré menor com sétima menor (Dm7).
    

    - *Tétrade Dominante (7)*: 

Composta pela Tônica, Terça Maior, Quinta Justa e Sétima Menor.

    G - B - D - F -> Formando o acorde Sol maior com sétima menor (G7).

    
    - *Tétrade Diminuta (dim7)*: 

Composta pela Tônica, Terça Menor, Quinta Diminuta e Sexta Maior.

    B - D - F - Ab -> Formando o acorde Si diminuto com sétima diminuta (Bdmin7)

    
    - *Tétrade Aumentada (maj7#5)*: 

Composta pela Tônica, Terça Maior, Quinta Aumentada e Sétima Maior.

    F - A# - C# - E -> Formando o acorde Fá maior com sétima maior e quinta aumentada (Fmaj7#5)

*Inversões de acordes*

As inversões são técnicas essenciais na música que envolvem alterar a ordem das notas de um acorde, mantendo as mesmas notas básicas, mas mudando a nota mais grave do acorde. 

Isso resulta em diferentes disposições verticais das notas e afeta a sonoridade e a progressão harmônica. 

As inversões proporcionam variações na textura e no timbre dos acordes, criando uma sonoridade diferente em comparação com a forma original, facilitando transições mais suaves entre acordes, especialmente em músicas onde as mudanças bruscas podem ser indesejáveis. 

Em arranjos musicais, as inversões são usadas para distribuir melhor as vozes entre os instrumentos ou vocais, criando um equilíbrio harmonioso.


*Tipos de Inversões de Acordes*

Veja agora os principais tipos de inversões de acordes para utilizar nas suas progressões harmônicas.


    - *Inversão da terça (3ª)*: 
    
A terça da tríade no acorde torna-se a nota mais grave.

        Exemplo: C (C-E-G) torna-se (E-G-C), a nota E (terça) se torna a nota mais grave.

        
    - *Inversão da quinta (5ª)*: 

A quinta da tríade no acorde torna-se a nota mais grave.

        Exemplo: C (C-E-G) torna-se (G-C-E), a nota G (quinta) se torna a nota mais grave.

        
- *Inversão da sétima (7ª)*: 

A sétima da tétrade no acorde torna-se a nota mais grave.

        Exemplo: C7 (C-E-G-Bb) torna-se (Bb-C-E-G), a nota Bb (sétima) se torna a nota mais grave.

            
As inversões de acordes são poderosas e versáteis para expandir as possibilidades harmônicas na hora de criar sensações sonoras diferentes. 

Dominar as inversões não apenas melhora a compreensão da harmonia, mas também enriquece a interpretação e a expressão musical em geral.


    """
    st.write(acordes_text)

def harmonico():
    st.subheader("Campo Harmônico")
    harmonico_text = """
    

Campos harmônicos são uma coleção de acordes derivados de uma escala como base para gerar uma sensação sonora específica.

- /Campo_harmonico_maior: Conjunto de acordes derivados de uma escala maior para gerar a sensação de positividade e estabilidade.

- /Campo_harmonico_menor: Conjunto de acordes derivados de uma escala menor para gerar a sensação de melancolia e instabilidade.

- /Progressoes_harmonicas: Conjunto de acordes que, juntos, formam uma musicalidade típica. 

- /Modulacao: Processo pelo qual ocorre uma mudança de tonalidade ou centro tonal durante a execução de uma composição.

- /Ciclo_das_quartas: Sequência de acordes em que cada acorde sucessivo é formado pela adição de uma quarta perfeita acima do acorde anterior.

- /Ciclo_das_quintas: Sequência de acordes em que cada acorde sucessivo é formado pela adição de uma quinta justa acima do acorde anterior.


*Campo Harmônico Maior*

O campo harmônico maior é usado para criar progressões de acordes que seguem as regras de resolução tonal e proporcionam estruturas harmonicamente coesas. 

Muitas composições utilizam o campo harmônico maior como ponto de partida e modulam para outras tonalidades relacionadas durante o desenvolvimento da música. 

Músicos frequentemente improvisam e compõem dentro do campo harmônico maior, explorando suas possibilidades melódicas e harmônicas.

O campo harmônico maior é construído a partir das sete notas da escala maior natural. Cada grau da escala forma um acorde triádico ou tetrádico seguindo a seguinte fórmula: 

*Veja a fórmula para a construção do campo harmônico maior:* 

- I: Tríade Maior da nota correspondente

- II: Tríade Menor da nota correspondente

- III: Tríade Menor da nota correspondente

- IV: Tríade Maior da nota correspondente 

- V: Tríade Maior da nota correspondente

- VI: Tríade Menor da nota correspondente

- VII: Tétrade Meio-Diminuta da nota correspondente


Exemplo do campo harmônico maior em Dó: 

- I: C

- II: Dm

- III: Em

- IV: F

- V: G

- VI: Am

- VII: B°


*Funções harmônicas*

Para saber como utilizar cada um dos acordes, é preciso conhecer as funções de cada um deles no campo harmônico.

Estas funções são geralmente divididas em três categorias principais: Tônica (T), Subdominante (SD) e Dominante (D). Cada categoria tem um papel específico na progressão harmônica, que são: 

    - *Tônica (T)*: Estes acordes proporcionam uma sensação de repouso e estabilidade.

    - *Subdominante (SD)*: Estes acordes preparam a resolução e criam uma sensação de movimento.

    - *Dominante (D)*: Estes acordes geram tensão que normalmente resolve de volta à Tônica.

Exemplo das funções harmônicas no campo harmônico maior de Dó: 

- I: C -> Tônica 

- II: Dm -> Subdominante 

- III: Em -> Tônica 

- IV: F -> Subdominante 

- V: G -> Dominante 

- VI: Am -> Tônica 

- VII: B° -> Dominante 


*Campo Harmônico Menor*

Assim como no campo harmônico maior, o campo harmônico menor se refere à estrutura de acordes baseada em uma escala menor, seguindo os mesmos princípios de construção dos acordes que o campo harmônico maior, mas utilizando a escala menor como referência. Vamos explorar mais sobre o campo harmônico menor:

O campo harmônico menor é usado para criar progressões de acordes que seguem as regras de resolução tonal próprias da escala menor, proporcionando estruturas harmonicamente coesas.

Assim como no campo harmônico maior, é possível modular para outras tonalidades menores relacionadas durante a composição musical.

Músicos frequentemente exploram o campo harmônico menor para criar melodias e harmonizações que reflitam a tonalidade e o sentimento melancólico associado à escala menor.


*Veja a fórmula para a construção do campo harmônico menor:* 

Assim como no campo harmônico maior, o campo harmônico menor é formado pelos acordes construídos a partir das sete notas da escala menor diatônica.

- I: Tríade Menor da nota correspondente.

- II: Tétrade Diminuta da nota correspondente.

- III: Tríade Maior da nota correspondente.

- IV: Tríade Menor da nota correspondente.

- V: Tríade Menor da nota correspondente.

- VI: Tríade Maior da nota correspondente.

- VII: Tétrade Maior da nota correspondente.


Exemplo do campo harmônico menor em Lá:

- I: Am

- II: B°

- III: C

- IV: Dm

- V: Em

- VI: F

- VII: G


*Funções harmônicas*

Para saber como utilizar cada um dos acordes, é preciso conhecer as funções de cada um deles no campo harmônico.

Estas funções são geralmente divididas em três categorias principais: Tônica (T), Subdominante (SD) e Dominante (D). Cada categoria tem um papel específico na progressão harmônica, que são: 

    - *Tônica (T)*: Estes acordes proporcionam uma sensação de repouso e estabilidade.

    - *Subdominante (SD)*: Estes acordes preparam a resolução e criam uma sensação de movimento.

    - *Dominante (D)*: Estes acordes geram tensão que normalmente resolve de volta à Tônica.

    
Exemplo das funções harmônicas no campo harmônico menor de Lá: 

- I: Am -> Tônica 

- II: B° -> Subdominante 

- III: C -> Tônica 

- IV: Dm -> Subdominante 

- V: Em -> Dominante 

- VI: F -> Tônica 

- VII: G° -> Dominante 


*Ciclo das quartas*

O ciclo das quartas é uma fórmula de modulação organizada de acordo com o intervalo músical de quartas justas descendentes partindo da tônica. 

Esse conceito é fundamental na teoria musical e é amplamente utilizado em improvisação, composição, arranjo e análise harmônica, sendo usado para criar progressões harmônicas que têm uma sensação de movimento contínuo e fluido. 

Músicos frequentemente usam o ciclo das quartas para transpor acordes ou modular para novas tonalidades de uma maneira previsível e organizada.

É uma ferramenta valiosa para músicos que improvisam ou compõem, pois proporciona um caminho claro e lógico através das tonalidades e acordes, facilitando a exploração harmônica.


*Estrutura do Ciclo das Quartas*

O ciclo das quartas é construído começando de uma nota tônica e movendo-se em intervalos de quarta justa descendente para alcançar cada nova tonalidade ou acorde subsequente.

Por exemplo, a progressão no ciclo de quartas das notas naturais seria: 

C - F - Bb - Eb - Ab - Db - Gb - B - E - A - D - G - C


D - G - C - F - Bb - Eb - Ab - Db - Gb - B - E - A - D 


E - A - D - G - C - F - Bb - Eb - Ab - Db - Gb - B - E


F - Bb - Eb - Ab - Db - Gb - B - E - A - D - G - C - F


G - C - F - Bb - Eb - Ab - Db - Gb - B - E - A - D - G


A - D - G - C - F - Bb - Eb - Ab - Db - Gb - B - E - A


B - E - A - D - G - C - F - Bb - Eb - Ab - Db - Gb - B


*Ciclo das Quintas*

O ciclo das quintas é uma sequência de acordes ou tonalidades organizadas de acordo com o intervalo de quintas justas ascendentes entre elas.

O ciclo das quintas é usado para criar progressões harmônicas que têm uma sensação de movimento ascendente e resolução. É comum em muitas músicas como uma sequência de acordes que leva de volta à tônica inicial de maneira harmonicamente satisfatória.

Músicos frequentemente usam o ciclo das quintas para transpor acordes ou modular para novas tonalidades de uma forma previsível e estruturada.


*Estrutura do Ciclo das Quintas*

Cada acorde no ciclo das quintas é formado pela quinta justa subsequente. 

Por exemplo, a progressão no ciclo de quintas das notas naturais seria: 

C - G - D - A - E - B - F# - Db - Ab - Eb - Bb - F - C


D - A - E - B - F# - C# - G# - Eb - Bb - F - C - G - D


E - B - F# - C# - G# - D# - A# - F - C - G - D - A - E 


F - C - G - D - A - E - B - Gb - Db - Ab - Eb - Bb - F


G - D - A - E - B - F# - C# - Ab - Eb - Bb - F - C - G


A - E - B - F# - C# - G# - D# - Bb - F - C - G - D - A


Se você reparar, o ciclo de quartas e de quintas possuem os mesmos acordes; mas, enquanto o ciclo de quintas segue um movimento ascendente, o ciclo de quartas segue um movimento descendente. Ou seja, o ciclo de quartas é o ciclo de quintas lido ao contrário!


*Modulação*

A modulação na música refere-se à técnica de mudar de uma tonalidade ou centro tonal para outra dentro de uma composição. 

Essa mudança pode ser temporária ou permanente, sendo uma estratégia fundamental para criar interesse, variedade e desenvolvimento dentro de uma peça musical.

Pode ser usada para criar tensão, resolver conflitos musicais e destacar momentos emocionais específicos dentro de uma peça musical.


*Técnicas de Modulação*

    - Modulação por Acordes de Dominante: 

Muito comum na música tonal, onde acordes de dominante (por exemplo, V7) são usados para preparar e resolver em novas tonalidades.

    - Uso de Acordes Cromáticos: 

Acordes que não pertencem à tonalidade original podem ser usados como pontes para modulações, criando tensão que se resolve na nova tonalidade.


*Tipos de Modulação*

    - Modulação Direta: 
    
A modulação direta ocorre quando há uma mudança abrupta de uma tonalidade para outra. Isso pode ser feito através de um acorde que serve como ponte entre as duas tonalidades, muitas vezes um acorde de dominante que leva à nova tonalidade.
    
    - Modulação Gradual: 
    
A modulação gradual envolve uma transição suave de uma tonalidade para outra, utilizando acordes comuns às duas tonalidades ou progressões que gradualmente levam à nova tonalidade. Isso cria uma sensação de fluidez e continuidade na mudança tonal.

        Exemplo: Uma música em C maior pode modular para G maior usando um acorde de dominante (D7), que prepara a transição harmônica para a nova tonalidade.


    """
    st.write(harmonico_text)

def gregos():
    st.subheader("Modos gregos")
    gregos_text = """
    
Texto sobre modos gregos

    """
    st.write(gregos_text)

def recursos():
    st.subheader("Recursos adicionais")
    recursos_text = """
    
Encontre outros materiais para os estudos de Teoria Musical:

- /Ebooks: Livros digitais gratuitos

- /Sites: Sites e softwares gratuitos

- /Videos: Vídeos e aulas gratuitas

Veja os *sites e softwares gratuitos* que podem te ajudar com os seus estudos: 

https://www.oolimo.com/en/

https://www.bandlab.com/

https://musiclab.chromeexperiments.com/Song-Maker

https://www.pianoeletronico.com.br/index.html

https://www.musicca.com/pt/piano

https://www.musicca.com/pt/bateria

https://www.musicca.com/pt/caixa-de-ritmos

https://www.musicca.com/pt/metronomo

https://www.musicca.com/pt/gerador-de-acordes


Veja os recursos de *vídeos gratuitos na internet* para ampliar seus estudos: 

[Vídeo sobre teoria musical](https://www.youtube.com/watch?v=oU4i59Mf8Yo&pp=ygUMbXVzaWMgdGhlb3J5)

[Vídeo sobre a história da música](https://www.youtube.com/watch?v=tL3Vx6KTNJ0)

[Vídeo sobre ritmos musicais](https://www.youtube.com/watch?v=QLuHvLjl5t4&pp=ygUPcml0bW9zIG11c2ljYWlz)

[Vídeo sobre intervalos musicais](https://www.youtube.com/watch?v=Qh3CRTcPSg4&pp=ygUTaW50ZXJ2YWxvcyBtdXNpY2Fpcw%3D%3D)

[Vídeo sobre as escalas pentatônicas](https://www.youtube.com/watch?v=wN8tY790lxU&pp=ygUUZXNjYWxhcyBwZW50YXRvbmljYXM%3D)

[Vídeo sobre escala maior](https://www.youtube.com/watch?v=qXbcZJTcpvA&pp=ygUPZXNjYWxhcyBtYWlvcmVz)

[Vídeo sobre escalas menores](https://www.youtube.com/watch?v=eUrzhh_dHzU&pp=ygUPZXNjYWxhcyBtZW5vcmVz)

[Vídeo sobre a escala de blues](https://www.youtube.com/watch?v=3wbIsPLxF6U&pp=ygUNZXNjYWxhcyBibHVlcw%3D%3D)

[Vídeo sobre tríades](https://www.youtube.com/watch?v=6qoEfrEX_3A&pp=ygUHdHJpYWRlcw%3D%3D)

[Vídeo sobre tétrades](https://www.youtube.com/watch?v=zZhpSEObMZ4&pp=ygUIVGV0cmFkZXM%3D)

[Vídeo sobre inversões](https://www.youtube.com/watch?v=axUJrky7DT0&pp=ygUVaW52ZXJzw7VlcyBkZSBhY29yZGVz)

[Vídeo sobre campo harmônico maior](https://www.youtube.com/watch?v=ttzC5-VQ_Dc&pp=ygUWY2FtcG8gaGFybW9uaWNvIG1haW9yIA%3D%3D)

[Vídeo sobre campo harmônico menor](https://www.youtube.com/watch?v=Q9MP_2woISQ&pp=ygUVY2FtcG8gaGFybW9uaWNvIG1lbm9y)

[Vídeo sobre o ciclo das quartas](https://www.youtube.com/watch?v=soWL-r1vBD0&pp=ygURQ2ljbG8gZGFzIHF1YXJ0YXM%3D)

[Vídeo sobre o ciclo de quintas](https://www.youtube.com/watch?v=8fIouuBa3pA&pp=ygURQ2ljbG8gZGFzIHF1aW50YXM%3D)

[Vídeo sobre modulação](https://www.youtube.com/watch?v=fXS2D7tX1t4&pp=ygUTbW9kdWxhw6fDo28gbXVzaWNhbA%3D%3D)


    """
    st.write(recursos_text)


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
elif choice == "Acordes":
    acordes()
elif choice == "Campos harmônicos":
    harmonico()
elif choice == "Modos gregos":
    gregos()
elif choice == "Recursos adicionais":
    recursos()
