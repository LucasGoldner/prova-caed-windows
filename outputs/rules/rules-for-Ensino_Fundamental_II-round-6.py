def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.03, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Verbos", "instances": 1093, "metric_value": 0.0099, "depth": 2}
		if obj[0]>10.235201384613958:
			# {"feature": "Palavras_Frase", "instances": 908, "metric_value": 0.0032, "depth": 3}
			if obj[4]>8.297926395169196:
				return 0.052875781996017474
			elif obj[4]<=8.297926395169196:
				return -0.07459270052549218
			else: return -0.07459270052549218
		elif obj[0]<=10.235201384613958:
			# {"feature": "Canonicas", "instances": 185, "metric_value": 0.009, "depth": 3}
			if obj[2]>26.274534141330836:
				return -0.12132210703875056
			elif obj[2]<=26.274534141330836:
				return -0.20056934742366567
			else: return -0.20056934742366567
		else: return -0.13588646473111332
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0193, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0322, "depth": 3}
			if obj[1]>50.15338176787905:
				return -0.19705589380764876
			elif obj[1]<=50.15338176787905:
				return -0.1746701845293673
			else: return -0.1746701845293673
		elif obj[0]>12.63497838546153:
			# {"feature": "Substantivos", "instances": 459, "metric_value": 0.0233, "depth": 3}
			if obj[1]>39.90239674817307:
				return -0.1204737225653594
			elif obj[1]<=39.90239674817307:
				return -0.20155578953762576
			else: return -0.20155578953762576
		else: return -0.133369127552234
	else: return -0.1617843240560132
