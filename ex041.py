from datetime import date
print('\033[36m=-=\033[m'*11)
print('\033[34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('\033[36m=-=\033[m'*11)
print()
ano = int(input('\033[36mDigite o ano de nascimento: \033[m'))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 0:
    print('\033[31mVocê inseriu o ano incorretamente!\033[m')
elif idade <= 9:
    print('\033[33mCategoria\033[m: \033[34mMIRIM\033[m')
elif idade <= 14:
    print('\033[33mCategoria\033[m: \033[34mINFANTIL\033[m')
elif idade <= 19:
    print('\033[33mCategoria\033[m: \033[34mJUNIOR\033[m')
elif idade == 20:
    print('\033[33mCategoria\033[m: \033[34mSÊNIOR\033[m')
elif idade >= 21:
    print('\033[33mCategoria\033[m: \033[34mMASTER\033[m')
