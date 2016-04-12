from flask import Flask, request, jsonify, Response
import sqlite3
import os
import sys
import httplib2
import xml.etree.ElementTree as ET
from datetime import date
from dateutil.parser import parse
from dateutil.parser import parse

app = Flask(__name__)
app.debug = True


@app.route('/')
def root():
    return app.send_static_file('mashup.html')

@app.route('/getWeather/<string:city>/<string:region>', methods = ['GET', 'POST'])
def getWeather(city, region):
    query = "weather" + "%20" +city + "%20" + region
    def request(query):
        wolfram_api = "http://api.wolframalpha.com/v2/query?appid=XXXX&input="+query+"&includepodid=InstantaneousWeather:WeatherData"
        resp, content = httplib2.Http().request(wolfram_api)
        return content

    def response(query):
        content = request(query)
        root = ET.fromstring(content)
        error = root.get('error')
        success = root.get('success')
        numpods = root.get('numpods')
        print(numpods, success)
        answer= ''
        if success and int(numpods) > 0 :
            for plaintext in root.iter('plaintext'):
                if isinstance(plaintext.text, str) :
                    answer = answer + plaintext.text
            return answer
        elif error:
            return "error"



    weather = response(query)

    print(weather)
    print(type(weather))

    return jsonify(weather)


    #res = wolframAlpha.query('Weather' + city + region)
    #print(res.content())
    #return Response(res.Content, mimetype = 'text/xml')
def getImage(city, region):
    pass


if __name__ == '__main__':
    app.run()
