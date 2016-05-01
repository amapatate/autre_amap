def entete():
    entete='''
    <!DOCTYPE HTML>
<html lang=“fr”>
          <head>
                    <title>AMAP'PATATE</title>
                    <meta charset="UTF-8" />
                    <link rel="stylesheet" type="text/css" href="/IENAC15/amapatate/css/font-awesome.min.css" />
                    <link rel="stylesheet" type="text/css" href="/IENAC15/amapatate/css/bootstrap.min.css" />
                    <link rel="stylesheet" type="text/css" href="/IENAC15/amapatate/css/style.css" />
                    <link rel="stylesheet" type="text/css" href="/IENAC15/amapatate/css/menu.css" />
                    <link rel="stylesheet" type="text/css" href="/IENAC15/amapatate/css/form.css" />
                    <link rel="stylesheet" type="text/css" href="/IENAC15/amapatate/css/button.css" />
                    <script type="text/javascript" src= " /IENAC15/amapatate/js/jquery-2.2.0.min.js" ></script>
					<script type="text/javascript" src= " /IENAC15/amapatate/js/bootstrap.min.js" ></script>
          </head>
         <body>

        '''
    return entete

def nav():
    nav='''
        <nav>
             <ul>
	           <li><a href="/IENAC15/amapatate/index.py">
	             	<span class="fa-stack fa-lg">
    	      			<i class="fa fa-circle fa-stack-2x"></i>
    	      			<i class="fa fa-home fa-stack-1x fa-inverse"></i>
    	      		</span>
	             	Accueil</a>
	            </li>
                <li><a href="/IENAC15/amapatate/index.py#ecole">
                    <span class="fa-stack fa-lg">
    	      			<i class="fa fa-circle fa-stack-2x"></i>
    	      			<i class="fa fa-plane fa-stack-1x fa-inverse"></i>
    	      		</span>
                    L'école</a>
                    	<ul>
                 			<li><a href="http://www.eag-tournament.com">
                 			    <i class="fa fa-soccer-ball-o fa-fw"></i>EAG</a>
                 			</li>
                 			<li><a href="index.html#contacter">
                 				<i class="fa fa-phone fa-fw"></i>Nous Contacter</a>
                 			</li>
             			</ul>
                 </li>
		       	<li><a href="/IENAC15/amapatate/python/clubs.py">
		       		<span class="fa-stack fa-lg">
    	      			<i class="fa fa-circle fa-stack-2x"></i>
    	      			<i class="fa fa-bicycle fa-stack-1x fa-inverse"></i>
    	      		</span>
		       		Les clubs</a>
		       	</li>
		       	<li><a href="/IENAC15/amapatate/python/connecter.py">
		       		<span class="fa-stack fa-lg">
    	      			<i class="fa fa-circle fa-stack-2x"></i>
    	      			<i class="fa fa-user fa-stack-1x fa-inverse"></i>
    	      		</span>
		       	Se connecter</a>
		       	</li>
		       	'''
    if "nom" in Session() and Session()["nom"]!='':
        nav+='''
            <li><a href="/IENAC15/amapatate/python/page_prive.py">
		       		<span class="fa-stack fa-lg">
    	      			<i class="fa fa-circle fa-stack-2x"></i>
    	      			<i class="fa fa-user fa-stack-1x fa-inverse"></i>
    	      		</span>
		       	Page privée</a>
		       	</li>
		       	'''
    nav+='''
 			</ul>
        </nav>
        '''
    return nav

def titre(intitule):
    titre='''
        <header>
                <h1>'''+intitule+'''</h1>
                <p>L'AMAP fruits et légumes qui vous donne la patate </p>
         </header>
        '''
    return titre

def footer():
    footer='''
            <footer>&copy All right reserved ENAC
            </footer>
        </body>
        </html>
        '''
    return footer
