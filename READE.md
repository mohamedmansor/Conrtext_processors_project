#Conrtext_processors_project
#Task:
#Create a model containing site main info (site name, logo, address, etc) which can be used as template tags
#Created a Django Project and Django App that Contain Simple CBV to 
#View the first object in the DB
#Highlighted_Points:
#We Create a context_processors.py file that Contains a Function "website" that take a request and return a Dictionary contains
#'site':<Model_Name>.objects.first()
#Settings: 
#in Settings.py >> TEMPLATES we add  'website.context_processors.website' in the conext_processors
#'<context_processors.py_path>.context_processors.<Function_in_context_processors.py>'
#then in html file we just {{ site.<query_object> }}

