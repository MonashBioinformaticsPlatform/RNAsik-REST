# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas


class Runs(Resource):

    def get(self):

        return [{"name": "this is a test run name"}], 200, None

    def post(self):

        ## steve debug code
        import time
        now = time.strftime("%c")
        ## date and time representation
       
        # insert date and time into response json as a test
        # g.json comes from the request and is a dict, not json
        g.json['sampleNames'] = "Time of request " + time.strftime("%c")
        
        #import json
        #json_response = json.dumps(g.json)

        # return type is dict
        return g.json, 200, None