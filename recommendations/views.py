from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from pymongo import MongoClient
import json
from bson.json_util import dumps
import datetime
from django.views.decorators.csrf import csrf_exempt

# A minor database :)
database = {'building':'null','industry':'null','defense':'null','transportaion':'null'}
camera={'max_obj_dist':'null'}


def clear_database(request):
	database = {'building':'null','industry':'null','defense':'null','transportaion':'null'}
	return HttpResponse("Database Cleared")

@csrf_exempt
def test2(request):
	parsed_req = request.body.decode('utf-8')
	print (parsed_req)
	req=json.loads(parsed_req)
	res = req["result"]

	if 'premises' in res['parameters'].keys():
		database[res['parameters']['premises']]='set'
		dict2= {
		"speech": "Which type of Building: Public Building, Residential, Commercial-Mall/Retail or Hospital?",
                "source": "webserver",
                "displayText": "Which type of Building: Public Building, Residential, Commercial-Mall/Retail or Hospital?"
	       }		


	if 'obj_dist' in res['parameters'].keys():
		camera['max_obj_dist']=res['parameters']['obj_dist']
		dict2= {
		"speech": "What type of sensitivity camera you would like to choose? Low sensitivity camera or High Sensitivity Camera !",
                "source": "webserver",
                "displayText": "What type of sensitivity camera you would like to choose? Low sensitivity camera or High Sensitivity Camera"
	       }		




	if 'unit-length' in res['parameters'].keys():
		if database['building']=="set":
			if res["parameters"]['unit-length']['amount'] > 100:
				dict2= {
				"speech": "Whats illumination level ? Proper or improper ?",
		                "source": "webserver",
		                "displayText": "Whats illumination level ? Proper or improper ?"
			       }
			else:
				dict2= {
						"speech": "Checkout this PTZ camera having model no. VG5-7230-EPC5",
		                "source": "webserver",
		                "displayText": "Suggesting the Camera"
			       }
		elif database['industry']=='set':
			dict2= {
					"speech": "Do you want optical cameras or Do you  want explosion proof cameras?",
		    		"source": "webserver",
		            "displayText": "Do you want optical cameras or Do you  want explosion proof cameras?"
			       }
		elif database['defense']=='set':
			dict2= {
					"speech": "Do you want optical cameras or thermal cameras?",
		    		"source": "webserver",
		            "displayText": "Do you want optical cameras or thermal cameras?"
			       }


	return HttpResponse(json.dumps(dict2),content_type="application/json")
	


