template = Import('python/template.py')

# test modif github

def index():
    result = template.entete()
    result += template.nav()
    result += template.titre("Bienvenue sur le site AMAP'PATATE")
    result += ecole()
    result += contacter()
    result += template.footer()
    return result

    return result


def ecole():
    ecole = '''
        <section id="ecole">
             <h2>AMAP'PATATE !</h2>
				<div class="row">
                    <article class="col-md-4  col-sm-6 col-xs-12">
                         <img src="/IENAC15/amapatate/images/patate.jpg" alt="formation" title="Les formations ENAC" />
                          <h3>Les formations</h3>
                           <p>Travaillez dans l'aviation civile. Devenez ingénieur,technicien , contrôleur ou pilote.</p>
                    </article>

                     <article class="col-md-4  col-sm-6 col-xs-12">
                           <img src="/IENAC15/amapatate/images/fruitlegume.jpg" alt= "campus" title="Le campus"  />
                           <h3>Le campus</h3>
                           <p>Plus d'excuse pour vous perdre dans les couloirs et  sécher les cours!! Consultez le plan de l'ENAC.</p>
                      </article>

                     <article class="col-md-4  col-sm-6 col-xs-12">
                           <img src="/IENAC15/amapatate/images/leg3.jpg" alt= "soiree"  title="Les soirées"  />
                           <h3>Les soirées</h3>
                            <p>Moments de détente et d'amitié </p>
                      </article>

                 </div>
        </section>
    '''
    return ecole


def contacter():
    contact = '''
        <section id="contacter">
              <h2>Des questions ou des commentaires?</h2>
    			    <div class="row">
        				<div class="col-md-10 col-sm-12 col-xs-12 col-md-offset-1 form-group" >
            				<form method="post" action="/IENAC15/amapatate/python/page2.py/fcontacter"  enctype="multipart/form-data">
            					<input name="name" placeholder="Nom Prénom" type="text" />
         						<input name="email" placeholder="Email" type="text" />
         						<textarea name="message" placeholder="Message"></textarea>
								<button class="button" type="submit">Send Message</button>
 	  						</form>
        				</div>
     				</div>
        </section>
        '''
    if "nom" in Session() and Session()["nom"] != '':
        contact += Session()["nom"] + " , votre message a bien été enregistré "

    return contact
