def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0075, "depth": 1}
	if obj[0]<=18.71755632751331:
		# {"feature": "Diferentes", "instances": 1745, "metric_value": 0.0035, "depth": 2}
		if obj[3]>70.64785271414716:
			# {"feature": "Palavras_Frase", "instances": 910, "metric_value": 0.0116, "depth": 3}
			if obj[4]>9.518886934360191:
				return 0.1533428941587086
			elif obj[4]<=9.518886934360191:
				return -0.10996911408157524
			else: return -0.10996911408157524
		elif obj[3]<=70.64785271414716:
			# {"feature": "Substantivos", "instances": 835, "metric_value": 0.0033, "depth": 3}
			if obj[1]<=55.701026807823716:
				return 0.03061669119116333
			elif obj[1]>55.701026807823716:
				return -0.09220301845799321
			else: return -0.09220301845799321
		else: return 0.013701401838285481
	elif obj[0]>18.71755632751331:
		# {"feature": "Diferentes", "instances": 331, "metric_value": 0.0505, "depth": 2}
		if obj[3]>77.69876829045978:
			# {"feature": "Palavras_Frase", "instances": 201, "metric_value": 0.0208, "depth": 3}
			if obj[4]<=11.864496538882769:
				return -0.1894026275598601
			elif obj[4]>11.864496538882769:
				return -0.10784096303193466
			else: return -0.10784096303193466
		elif obj[3]<=77.69876829045978:
			# {"feature": "Palavras_Frase", "instances": 130, "metric_value": 0.0162, "depth": 3}
			if obj[4]<=28.055256389679315:
				return 0.03534855437083322
			elif obj[4]>28.055256389679315:
				return -0.19377434253692627
			else: return -0.19377434253692627
		else: return 0.02124868379189418
	else: return -0.10100205728834849
