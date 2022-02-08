from flask import Flask, redirect, render_template, request, url_for, make_response #, session

app = Flask(__name__)
app.config["DEBUG"] = True
#app.config.from_object(__name__)

@app.route("/linkchecker", methods=["GET", "POST"])
def index():
    import re
    import urllib.request
    from urllib.request import Request, urlopen
    from bs4 import BeautifulSoup

    res_links = []
    clinks = []
    count = 0
    table = ""
    if request.method == "GET":
        return render_template("main_page.html")

    user_blink = request.form["contents"]
    #user_link = re.split(r"\n|[' ']", user_blink)
    user_link = user_blink.split("\n")
    #res_links[user_blink] = len(user_link)
    for user_links in user_link:
        carr = []
        if len(user_links) == 0 and count == 0:# or re.match(r'^[_\W]+$', user_links):
            link = "<center><div>Nothing to analyze. Please enter some links.</div></center>"
            #res_links.append(link)
            #res_links[link] = " "
            carr.append(link)
            carr.append(" ")
            carr.append(" ")
        elif len(user_links) == 0:
            pass
        else:
            try:
                count = 0
                req = Request(user_links , headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/90.0.4430.93 Safari/537.36",
                "referer": "https://dlnr.hawaii.gov/",}) #HTTP Error 403: Forbidden 'fixed'   #headers={'User-Agent': 'Mozilla/5.0'}
                page = urllib.request.urlopen(req)
                #page = urllib.request.urlopen(user_links) #'https://en.wikipedia.org/wiki/Main_Page'
                html = BeautifulSoup(page.read(),"html.parser")
                links = html.find_all('a', rel= "nofollow")
                ls = html.find_all('a')
                cls = len(ls)
                for link in links:
                    count += 1
                if count >= 0:
                    #res_links[user_links] = count
                    carr.append(user_links)
                    table = "<tr><th><center>URL</center></th><th><center>Nofollow </center></th><th><center>Dofollow </center></th></tr>"
                carr.append(count)
                carr.append(cls-count)
            except Exception as e:
                #res_links[e] = " "
                carr.append(e)
                carr.append(" ")
                carr.append(" ")

                #res_links.append(link)
                #print(res_links)
            #re.compile(r'crummy\.com/')
        res_links.append(carr)
    return render_template("main_page.html", res_links=res_links,table=table)

@app.route("/about")
def about_route():
    return render_template("about.html")