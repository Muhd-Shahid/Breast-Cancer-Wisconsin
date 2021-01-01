import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'texture_mean':10.38, 'area_mean':1001, 'concavity_mean':0.3001, 'area_se':153.4, 'concavity_se':0.05373,'fractal_dimension_se':0.006193,'smoothness_worst':0.1622,'concavity_worst':0.7119, 'symmetry_worst':0.4601,'fractal_dimension_worst':0.1189})

print(r.json())