from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    if request.method == "POST":
        statename = request.POST.get('stateName')
        #print('statename:',statename)
        url ='http://covid19-india-adhikansh.herokuapp.com/state/'
        
        
        if statename is None or statename == '':
            all_states = {
                'name': '',
                'active':'',
                'cured': '',
                'death': '',
                'total': ''
            }
        else:
            try:
                stateData = requests.get(url+statename).json()
                #print('statedate:::',stateData)
                # {"data":[{"_id":"5ee654205268cc39fcc8a6bc","active":453,"cured":70,"death":0,"total":523,"name":"Goa"}]}
                all_states = {
                    'name': statename,
                    'active': stateData['data'][0]['active'],
                    'cured': stateData['data'][0]['cured'],
                    'death': stateData['data'][0]['death'],
                    'total': stateData['data'][0]['total'] 
                }
            except (IndexError, ValueError):
                print(f'dictionary does not conatin the data for : {statename}')
                all_states = {
                    'name': statename,
                    'active':'No Data found',
                    'cured': 'No Data found',
                    'death': 'No Data found',
                    'total': 'No Data found'
                }

        context = {
            'all_states': all_states
        }
        #print(all_states)   
        return render(request, 'index.html', context)
    return render(request, 'index.html')
