print('Hello world')
#special letters
'č, ŏ, ž, đ, ŷ, Č, Ŏ, Ž, Đ, Ŷ, ķ, Ķ'
###########  W O R D   L I S T  ###############
verbs = 'est est larre rioq rioq rioq rioq sate sate sate ferre ferre fob nelŏ nelŏ gein gein satesh> lare'.split()
Verbe = 'want desire like be am is are go goes travel do work understand start birth see know migrate die'.split()

prosA = 'mi de ei ei ei ei mu tai nis mus eis <noprefix>'.split()
ProeA = 'i you she he sing-they one royal we ones pl-they to'.split()

prosP = 'A Ku Su Ru Fe E Mun Ŏts <us Muns Fen'.split()
ProeP = 'me you-p her him sing-they-p one-p royal-p us ones-p pl-they-p'.split()

poss = 'Af Def Suf Ruf Fef Ef Munaf Ŏtsaf <usaf Munsaf Fenaf Af Def Suf Fef <usaf Fenaf'.split()
Pose = 'my your her-ps his sing-their its one"s royals our ones" pl-their mine yours hers sing-theirs ours pl-theirs'.split()

nouns = 'av nen bey ne nu bo ra ra ķetsŏ ķetsŏmun huav huavmun av nen tol tŏl mun inye giqi rie giqirie vainye pŏa Pŏa pŏa vahu juanyeqi vagan jugan vajuan satesh> nelo lari nelŏ nelŏ jura pŏra hura hura hua pŏjan inyeqi qi qi yor jua nune yorqi hujaqi avŏb'.split()
Noune = 'yes no and place time thing way reason noble nobleperson common commoner good bad name title person stone egg child newborn toy void deeps dark fish land animal air birds migration new death start birth up down middle average water nightsky sand little small big lightworld size freshwater knowledge'.split()

querys = 'q;omun q;en q;e q;o q;a q;ui q;ui munen nenen nunen bonen ranen ranen muni nei nui boi rai ne> nu> tsh> ne< nu< tsh< munis neis nuis bois'.split()
Querye = 'who where when what which why how no-one nowhere never thing noway noreason someone somewhere sometime something somehow there then that here now this everyone everywhere always everything'.split()

##################################################

def display(SEA, ENG):
    print(int(len(SEA)) + ', ' + int(len(ENG)))
    maxi = len(SEA) - 1
    if len(SEA) != len(ENG):
        print('WORD NUM ERROR')
        return ''
    i = 0
    c = 0
    text = ''
    while c != maxi:
            if i < 3:
                text = text + ENG[c] + ' - ' + SEA[c] + ',  '
                c += 1
                i += 1
            else:
                text = text + ENG[c] + ' - ' + SEA[c] + ',  '
                print(text)
                input()
                text = ''
                c += 1
                i = 0
    if i < 3:
        print(text)







################################################
################S T A R T#########
start = True
while start:
    go = True
    navi = ''
    phrase = ''
    place = 'start'

    print('''           Welcome to my English-SEA translator!
    To navigate enter the CAPITAL LETTERS.
    Would you like to view the translatable words list or translate a phrase?
    ''')

    while go:
        if place == 'start':
            print('View Words or Translate Phrase')
            navi = ''
            while navi not in 'vw tp q'.split():
                navi = input().lower()
                if navi == 'vw':
                    place = 'words'

                elif navi == 'tp':
                    place = 'tranl8'
                elif navi == 'q':
                    start = False
                    break

                else:
                    print('Invalid input')

        elif place == 'words':
            print('What word group would you like to view?')
            print('Verbs, PRonouns, POSSessives, Nouns and others, All or go Back')
            navi = ''
            while navi not in 'v pr poss n a b q'.split():
                navi = input().lower()
                if navi == 'v':
                    print()
                    print('Verbs')
                    display(verbs, Verbe)

                elif navi == 'pr':
                    nati = ''
                    print('Active or Passive pronouns? or Back')
                    while nati not in 'a p b'.split():
                        nati = input().lower()
                        if nati == 'a':
                            print()
                            print('Active Pronuns')
                            display(prosA, ProeA)
                        elif nati == 'p':
                            print()
                            print('Passive Pronouns')
                            display(prosP, ProeP)
                        elif nati == 'b':
                            place = 'words'
                        elif nati == 'q':
                            start = False
                            break
                        else:
                            print('Invalid input')

                elif navi == 'poss':
                    print()
                    print('Possessives')
                    display(poss, Pose)

                elif navi == 'n':
                    print()
                    print('Nouns, Adjectives and Others')
                    display(nouns, Noune)

                elif navi == 'a':
                    print()
                    print('Verbs')
                    display(verbs, Verbe)
                    print()
                    print('Active Pronuns')
                    display(prosA, ProeA)
                    print()
                    print('Passive Pronouns')
                    display(prosP, ProeP)
                    print()
                    print('Nouns, Adjectives and Others')
                    display(nouns, Noune)

                elif navi == 'b':
                    place = 'start'

                elif navi == 'q':
                    start = False

                    break
                else:
                    print('Invalid input')

        elif place == 'transl8':
            print('this will translate, but not now')
            input()
            place = 'start'

        else:
            print('Invalid input')
