# let's install weasyprint!
!pip install weasyprint==52.5

# also we need markdown
import markdown

# import some specific parts of weasyprint
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
import random

novel = """


# growing up: a novel
### by Mia Buffington


"""
#Chapters 1,2
for chapter in range(1,3): 

  novel += f"""

## Chapter {chapter}

  """ 
  
  for w in range( random.randrange(10000) ): 
    novel += " MAMA "
    
    if (random.randrange(1,12) < 2): #punctuation 
      novel += random.choice([". ","; ","? ","! ",])

    if (random.randrange(1,100) < 2): #paragraph
      novel += ".\n\n"

#Chapter 3,4
for chapter in range(3,5):

  novel += f"""

## Chapter {chapter}

  """ 

  for w in range( random.randrange(10000) ): 
    novel += " MOMMY "
    
    if (random.randrange(1,12) < 2): #punctuation 
      novel += random.choice([". ","; ","? ","! ",])

    if (random.randrange(1,100) < 2): #paragraph
      novel += ".\n\n"

#Chapter 5,6
for chapter in range(5,7):

  novel += f"""

## Chapter {chapter}

  """ 
  for w in range( random.randrange(10000) ): 
    novel += " MOTHER "
    
    if (random.randrange(1,12) < 2): #punctuation 
      novel += random.choice([". ","; ","? ","! ",])

    if (random.randrange(1,100) < 2): #paragraph
      novel += ".\n\n"

#Chapter 7,8
for chapter in range(7,9):

  novel += f"""

## Chapter {chapter}

  """ 
  for w in range( random.randrange(10000) ): 
    novel += " MOM "
    
    if (random.randrange(1,12) < 2): #punctuation 
      novel += random.choice([". ","; ","? ","! ",])

    if (random.randrange(1,100) < 2): #paragraph
      novel += ".\n\n"

#Chapter 9,10
for chapter in range(9,11):

  novel += f"""

## Chapter {chapter}

  """ 
  for w in range( random.randrange(10000) ): 
    novel += " MA"
    
    if (random.randrange(1,12) < 2): #punctuation 
      novel += random.choice([". ","; ","? ","! ",])

    if (random.randrange(1,100) < 2): #paragraph
      novel += ".\n\n"

#print(novel)
# convert markdown formatted novel string into html
html = markdown.markdown(novel)


# prepare WeasyPrint
font_config = FontConfiguration()
rendered_html = HTML(string=html)



css = CSS(string='''
@import url('https://fonts.googleapis.com/css2?family=Festive&display=swap');

@import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300&display=swap');
body {
font-family: 'Merriweather', serif;
}

hr {
  break-after: recto; 
}

h1 {
  font-size: 50pt;
  text-align:center;
  margin-top: 3in;
  font-family: 'Festive',cursive;
}
h2{
  break-before: recto;
  font-family: 'Festive',cursive;
}

h3 {
  font-size: 20pt;
  text-align:center;
}

/* set the basic page geometry and start the incrementer */
@page {
  font-family: 'Merriweather', serif;
  margin: 1in;
  size: letter;
  counter-increment: page;
  @bottom-center {
    content: "growing up: a";
    text-align:center;
    font-style: italic;
    color: #666666;
  }
}

/* print the page number on the bottom-right of recto pages */
@page :right {
  @bottom-right{
    content: "[" counter(page) "]";
    text-align:right;
    color: #666666;
    visibility: invisible;
  }
}

/* print the page number on the bottom-left of verso pages */
@page :left {
  @bottom-left{
    content: "[" counter(page) "]";
    text-align:left;
    color: #666666;
  }
}

/* blank the footer on the first page */
@page:first{
  @bottom-left {content: ""}
  @bottom-right {content: ""}
  @bottom-center {content: ""}
}


''', font_config=font_config)

rendered_html.write_pdf('/content/sample.pdf', stylesheets=[css],font_config=font_config)
