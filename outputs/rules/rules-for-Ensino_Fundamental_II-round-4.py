def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0299, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Verbos", "instances": 1093, "metric_value": 0.0099, "depth": 2}
		if obj[0]>10.235201384613958:
			# {"feature": "Palavras_Frase", "instances": 908, "metric_value": 0.0032, "depth": 3}
			if obj[4]>8.297926395169196:
				return 0.05295478810375634
			elif obj[4]<=8.297926395169196:
				return -0.07432038455951114
			else: return -0.07432038455951114
		elif obj[0]<=10.235201384613958:
			# {"feature": "Canonicas", "instances": 185, "metric_value": 0.009, "depth": 3}
			if obj[2]>26.274534141330836:
				return -0.12126079823402379
			elif obj[2]<=26.274534141330836:
				return -0.200521679047276
			else: return -0.200521679047276
		else: return -0.1358276628159188
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0191, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0321, "depth": 3}
			if obj[1]>50.15338176787905:
				return -0.19488155969097096
			elif obj[1]<=50.15338176787905:
				return -0.17292340835671366
			else: return -0.17292340835671366
		elif obj[0]>12.63497838546153:
			# {"feature": "Substantivos", "instances": 459, "metric_value": 0.0232, "depth": 3}
			if obj[1]>39.90239674817307:
				return -0.12100005620810653
			elif obj[1]<=39.90239674817307:
				return -0.2014799567118083
			else: return -0.2014799567118083
		else: return -0.13379969180019852
	else: return -0.16093200919647546
