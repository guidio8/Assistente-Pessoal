# Assistente-Pessoal
 Projeto por diversão para automatizar algumas funções do computador com reconhecimento de voz

## Bibliotecas Utilizadas
- speech_recognition
- pyttsx3
- pywhatkit
- datetime
- wikipedia
- sys
- pyjokes
- os
- webbrowser
- re
- threading
- time
- googlesearch
- subprocess
- pyautogui
- winapps 

## Execução
    ~$ python assistentePessoal.py

## Utilização
    Primeiramente começar falando "ativar" caso o idioma esteja em português e "my guy" caso esteja em inglês, o assistente irá responder para que então possa fazer a chamada de alguma da funções implementadas

### Toca
    Ao falar Toca "algo" outra palavra vai abrir no seu browser principal o primeiro video do youtube quando se procura "algo".

### Horas
    Ao falar qualquer frase que contenha a palavra horas ele irá dizer a hora atual

### Wikipédia
    Ao falar "quem é tal pessoa" ou "algo wikipédia" o assistente responde com a primeira sentença da página da wikipédia dessa pesquisa

### Quanto Custa
    Ao falar quanto custa algo ele faz uma piada (sempre a mesma)

### Abre o site
    Ao falar abre o site "tal" o assistente abre no seu browser principal o primeiro resultado que o google fornece ao pesquisar pela palabra "tal"

### Procura no google
    Ao falar Procura "algo" no google ele abre a página de pesquisa do google onde foi procurado tudo que foi dito entre "procura" e "no google"

### Manda whats
    Ao falar Manda "tal mensagem" no whats o assistente responde perguntando para quem você gostaria de mandar uma mensagem escrita "tal mensagem" porém precisa implementar cada número separadamente e para publicar no git eu tirei os números cadastrados mas a função foi testada e funciona

### Iniciar
    Ao falar Iniciar "tal programa" o assistente procura nos seus aplicativos baixados por um programa que contenha todas as palavras ditas após o Iniciar, utilizando a biblioteca winapps, caso encontre o app *tenta* executar o "tal programa".exe ou "tal programa launcher".exe, caso não consiga realizar nenhuma dessas duas opções, responde que não foi possível abrir o programa
    
### Atualizar(kinda)
    Por enquanto só funciona com o Call of Duty Modern Warfare, o assistente abre o programa desejado e compara a tela deste programa com as imagens fornecidas (cod.png para saber se o launcher do jogo está aberto e update_button_cod.png para ver se existe o botão de update, em caso positivo para ambos, clica no botão de update)

### Fechar
    Precisa de mais imagens do botão de fechar, o assistente procura o botao "X.png" na tela com uma margem de erro e clica nele porém nem todos os botões de fechar são iguais
