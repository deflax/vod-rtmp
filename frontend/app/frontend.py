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
    itemList = zomstream.getStreamNames()

    applications = []
    appnames = []
    for item in itemList:
        if item[0] not in appnames:
            appnames.append(item[0])

    for appname in appnames:
        streamnames = []
        for item in itemList:
            streamitem=item[1].split('_')[0]
            if streamitem not in streamnames and item[0] == appname:
                streamnames.append(streamitem)

        streams = []
        for streamname in streamnames:
            substreams = []
            for item in itemList:
               if item[0] == appname:
                   if item[1].split('_')[0] == streamname:
                       substreams.append(item[1])
            stream = [streamname, substreams]
            streams.append(stream)

        app = [appname, streams]
        applications.append(app)

    page = flask.render_template(
        mainTemplate,
        applications=applications,
        configuration=zomstream.configuration
    )
    return page

@frontend.route("/player/<appname>/<stream>")
def show_player(appname, stream):
    playerTemplate = '%s/player.html.j2' % zomstream.configuration['template_folder']
    page = flask.render_template(
        playerTemplate, 
        appname=appname,
        stream=stream,
        configuration=zomstream.configuration
        )
    return page
