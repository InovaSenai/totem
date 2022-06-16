import reconhecimento

if(reconhecimento.reconhecer_face() == 0) : 
    print('Retorna erro')
elif(reconhecimento.localizar() == 0) :
    print('retorna erro')
else :
    print(reconhecimento.identificar())