def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0287, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Verbos", "instances": 1093, "metric_value": 0.0096, "depth": 2}
		if obj[0]>10.235201384613958:
			# {"feature": "Palavras_Frase", "instances": 908, "metric_value": 0.0031, "depth": 3}
			if obj[4]>8.297926395169196:
				return 0.05214672479943782
			elif obj[4]<=8.297926395169196:
				return -0.07100302281499911
			else: return -0.07100302281499911
		elif obj[0]<=10.235201384613958:
			# {"feature": "Canonicas", "instances": 185, "metric_value": 0.0089, "depth": 3}
			if obj[2]>26.274534141330836:
				return -0.11695803849902374
			elif obj[2]<=26.274534141330836:
				return -0.1964669968275463
			else: return -0.1964669968275463
		else: return -0.1315704957053468
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.019, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0318, "depth": 3}
			if obj[1]>50.15338176787905:
				return -0.18286687544020044
			elif obj[1]<=50.15338176787905:
				return -0.16184514503420136
			else: return -0.16184514503420136
		elif obj[0]>12.63497838546153:
			# {"feature": "Substantivos", "instances": 459, "metric_value": 0.0229, "depth": 3}
			if obj[1]>39.90239674817307:
				return -0.11125035610995762
			elif obj[1]<=39.90239674817307:
				return -0.19007501598090343
			else: return -0.19007501598090343
		else: return -0.12378673992385532
	else: return -0.15008349528693474
