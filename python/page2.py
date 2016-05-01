bdd=Import('bdd.py')
template=Import('template.py')

def  fcontacter(name='', email='', message=''):
    result=template.entete()
    result+=template.nav()
    result+=template.titre("Nous contacter")
    result+="<section>"
    result+=afficheContact()
    bdd.insertComment(name,email,message)
    result+=afficheComment()
    result+="</section>"
    result+=afficheContact(name,email,message)

    result+=template.footer()
    return result
    return result

def afficheContact(name='', email='', message=''):
    result=''
    result+="les données envoyées sont:<br />nom:"+name
    result+=" <br /> email:"+email
    result+=" <br /> message:"+message
    Session()["nom"]=name
    return result


def afficheComment():
    result=''
    liste=bdd.affichComment()

    for (id, nom, comment, email) in liste:
        result+='<div>'
        result+=str(id)+' '
        result+=str(nom)+' '
        result+=str(comment)+' '
        result+=str(email)+' '
        result+='</div>'

    return result