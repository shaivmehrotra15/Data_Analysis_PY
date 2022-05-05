import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1= jp.QDiv(a=wp,text="Analysis of course reviews",classes="text-h1 text-center")
    p1 = jp.QDiv(a=wp,text="These graaphs represent course review analysis")
    return wp

jp.justpy(app)    