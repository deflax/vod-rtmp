#!/usr/bin/env python3

# imports
import flask
import urllib
from zomstream import Zomstream

streamList = []
zomstream = Zomstream()

frontend = flask.Blueprint('frontend', __name__)

@frontend.route("/")
def start():
    mainTemplate = '%s/main.html.j2' % zomstream.configuration['template_folder']
    streamList = zomstream.getStreamNames()
    page = flask.render_template(
        mainTemplate,
        items=streamList,
        configuration=zomstream.configuration
    )
    return page

@frontend.route("/player/<appname>/<streamname>")
def show_player(appname, hlsindex):
    playerTemplate = '%s/player.html.j2' % zomstream.configuration['template_folder']
    hlsindex = streamname.split('_')[0]
    page = flask.render_template(
        playerTemplate, 
        appname=appname,
        hlsindex=hlsindex,
        configuration=zomstream.configuration
        )
    return page
