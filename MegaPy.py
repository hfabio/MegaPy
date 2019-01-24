from itertools import permutations

dezenas = []
jogo = []
label= 1
resp = 's'
#---------------------------------------------- functions ------------------------------------------------------------------------------
def clearScreen():
    print('\n'*40)
#---------------------------------------------------------------------------------------------------------------------------------------
#fatorial
def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat
#---------------------------------------------------------------------------------------------------------------------------------------
def calculaCombinacoes():
    return fatorial(len(dezenas))/(fatorial(6)*fatorial(len(dezenas)-6))
    #return fatorial(len(dezenas))/fatorial(6)*(fatorial(len(dezenas)-6))
#---------------------------------------------------------------------------------------------------------------------------------------
def printFormattedResult(jogo):
    string = ''
    for i in range(len(jogo)):
        if(i<1000) and (i>=99):
            string += (str(i+1)+'  |')
        if(i<=98) and (i>=9):
            string += (str(i+1)+'   |')
        if(i<=8):
            string += ('0' +str(i+1)+'   |')
        if(i>1000):
            string += (str(i+1)+' |')
    
        for j in range(len(jogo[0])):
            if(jogo[i][j] <10):
                string += (' 0' + str(jogo[i][j]))
            else:
                string += (' ' + str(jogo[i][j]))
        string += ' | \n'
    return string
#------------------------------------------ end of functions ----------------------------------------------------------------------------
#------------------------------------------ init of program  ----------------------------------------------------------------------------
clearScreen()
#receiving the data
while((resp != 'n') and (resp != 'N')):
    d = int(input('Digite a dezena para inserir: '))
    if(((d>=1) and (d<=60)) and (d not in dezenas)):
        dezenas.insert(len(dezenas),d)
        dezenas.sort()
        clearScreen()
        print('\nDezenas inseridas: '+ str(dezenas) + '\n')
        if(len(dezenas)>=6):
            resp = input('Deseja inserir mais dezenas? (s/n)  ')
    elif d in dezenas:
        print('Esta dezena ja foi inserida')
    else:
        print('Por favor insira uma dezena valida')
print('Length: ', len(dezenas))
print('Length -6 :', (len(dezenas)-6))
#print('Combinacoes possiveis: ', (fatorial((len(dezenas)-6)*6)))
print('Combinacoes possiveis: ', calculaCombinacoes())
print(dezenas)
print('Pressione enter para continuar...')
input('')
print('Combinando os jogos, por favor aguarde!')
jogos = list(permutations(dezenas, 6))
for x in range(len(jogos)):
    a = list(jogos[x])
    a.sort()
    if a not in jogo:
        jogo.insert(len(jogo), a)
        
print('\nJogos combinados:\n')
print(printFormattedResult(jogo))