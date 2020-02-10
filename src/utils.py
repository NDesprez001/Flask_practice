from flask import jsonify, url_for

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def practice_1(app):
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])
    return """
        <div style="text-align: center;">
        <title>Nas's Flask Practice</title>
        <img src='https://image.myanimelist.net/ui/5pjpFizOF0WqHWXSGonzMSQ5rUJs3dN5-g9kjG6-NGc5DpxXlc2GRQpelVhG7rjXE6uve6ZFC4d0DHXg4IWhvlPbtt5yzvwmkMXkXWHQWMw'/>
        <h1>Sashiburi dana! Genki desu ka?</h1>
        Yokoso!: <ul style="text-align: left;">"""+links_html+"</ul></div>"""



def generate_sitemap(app):
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])
    return """
        <div style="text-align: center;">
        <title>Nas's Flask Practice</title>
        <img src='https://i.kym-cdn.com/photos/images/original/001/381/631/05e.gif' width = 800px />
        <h1>Konnichiwa, watashi no namae wa Komi desu!</h1>
        Watashi no u~ebusaito, yokoso!: <ul style="text-align: left;">"""+links_html+"</ul></div>"""

def home_content(app):
    links = []
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])

    print('Nice practice')

    return """<div style="text-align: center;"><title>Nas's Flask Practice</title>
                <img src='https://i.pinimg.com/originals/1b/ce/fe/1bcefe9201469c9fbbd932e4c5ab971d.gif' />
                <h1> There is english here</h1>
                <p>Im learning Japanese on my free time, so i thought it would be fun to put some in here.</p>
                <p>Douzo: <ul style="text-align: left;">"""+links_html+"</ul></p></div>"""
