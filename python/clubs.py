template=Import('template.py')

def index():
    result=template.entete()
    result+=template.nav()
    result+=template.titre("Les clubs")
    result+=club()
    result+=template.footer()
    return result


def club():
    club='''
           <section id="clubs">
               <h2>Liste des clubs sportifs à l'ENAC</h2>

                   <table>
                       <thead>
                             <tr>
                             	 <th>Club</th>
                             	 <th>Responsable</th>
                             </tr>
                             		
                        </thead>
                        <tbody>
                              <tr>
                             		<td>Foot</td>
                             		<td>M. Potogoal - IENAC 12S</td>
                               </tr>
                               <tr>
                             		<td>Tennis</td>
                             		<td>Melle Baballe - IESSA 13</td>
                             	</tr>
                             		 <td>Rugby</td>
                             		 <td>M. Ovale - TSA 13B</td>
                             	</tr>
                             	<tr>
                             		<td>Ski</td>
                             		<td>Melle Piquet - EPL 15</td>
                             	</tr>
                             		
                         </tbody>
                             
                    </table>
             </section>
             '''
    return club


