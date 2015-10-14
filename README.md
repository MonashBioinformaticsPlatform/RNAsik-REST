# RNAsik-pipe Restful API

This will be a restful web api on top of the https://github.com/MonashBioinformaticsPlatform/RNAsik-pipe application.

Currently, running this application requires a little knowledge of Flask and Swagger (during development).

The skeleton API (just 2 methods!) was generated using Swagger Editor http://editor.swagger.io/#/

I then used this app to generate Python Flask code based on the Swagger API Spec I created https://github.com/guokr/swagger-py-codegen

The intention is to generate / create an AngularJS app that controls this API (ie a web interface for users). Until then, the Swagger Editor can be used with the included yaml spec to generate requests to the API and get information back as this develops. I'm using tunnels in my tests so far (note the localhost port in the swagger yaml file).

Run the Flask app as one usually would, `python app/__init__.py`
