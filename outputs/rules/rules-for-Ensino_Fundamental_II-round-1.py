def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0362, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Verbos", "instances": 1093, "metric_value": 0.0119, "depth": 2}
		if obj[0]>10.235201384613958:
			# {"feature": "Palavras_Frase", "instances": 908, "metric_value": 0.0042, "depth": 3}
			if obj[4]>8.297926395169196:
				return 0.06305449936628643
			elif obj[4]<=8.297926395169196:
				return -0.09033613445378151
			else: return -0.09033613445378151
		elif obj[0]<=10.235201384613958:
			# {"feature": "Canonicas", "instances": 185, "metric_value": 0.0089, "depth": 3}
			if obj[2]>18.857142857142858:
				return -0.16847826086956522
			elif obj[2]<=18.857142857142858:
				return 0.75
			else: return 0.75
		else: return -0.1635135135135135
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0207, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0344, "depth": 3}
			if obj[1]>50.15338176787905:
				return -0.25
			elif obj[1]<=50.15338176787905:
				return -0.22530864197530864
			else: return -0.22530864197530864
		elif obj[0]>12.63497838546153:
			# {"feature": "Substantivos", "instances": 459, "metric_value": 0.0247, "depth": 3}
			if obj[1]>39.90239674817307:
				return -0.15414507772020725
			elif obj[1]<=39.90239674817307:
				return -0.25
			else: return -0.25
		else: return -0.16938997821350762
	else: return -0.2062563580874873
