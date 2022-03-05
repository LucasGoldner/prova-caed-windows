def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0797, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.032, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 613, "metric_value": 0.0548, "depth": 3}
			if obj[4]>10.643470540623449:
				return 0.005376344086021506
			elif obj[4]<=10.643470540623449:
				return 0.23636363636363636
			else: return 0.23636363636363636
		elif obj[3]<=68.82111094763226:
			return 0
		else: return 0.0
	elif obj[0]>13.987250505732058:
		# {"feature": "Palavras_Frase", "instances": 930, "metric_value": 0.0892, "depth": 2}
		if obj[4]<=12.60829693515217:
			# {"feature": "Diferentes", "instances": 578, "metric_value": 0.0558, "depth": 3}
			if obj[3]>78.48607670054238:
				return 0.6607669616519174
			elif obj[3]<=78.48607670054238:
				return 0.200836820083682
			else: return 0.200836820083682
		elif obj[4]>12.60829693515217:
			# {"feature": "Diferentes", "instances": 352, "metric_value": 0.0519, "depth": 3}
			if obj[3]<=80.34048212640499:
				return 0.0034129692832764505
			elif obj[3]>80.34048212640499:
				return 0.13559322033898305
			else: return 0.13559322033898305
		else: return 0.02556818181818182
	else: return 0.3021505376344086
