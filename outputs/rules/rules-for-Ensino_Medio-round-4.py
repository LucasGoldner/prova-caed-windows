def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0078, "depth": 1}
	if obj[0]<=18.71755632751331:
		# {"feature": "Diferentes", "instances": 1745, "metric_value": 0.0041, "depth": 2}
		if obj[3]>70.64785271414716:
			# {"feature": "Palavras_Frase", "instances": 910, "metric_value": 0.0122, "depth": 3}
			if obj[4]>9.518886934360191:
				return 0.16000273732582432
			elif obj[4]<=9.518886934360191:
				return -0.11368894522343206
			else: return -0.11368894522343206
		elif obj[3]<=70.64785271414716:
			# {"feature": "Substantivos", "instances": 835, "metric_value": 0.0033, "depth": 3}
			if obj[1]<=55.701026807823716:
				return 0.02807487549467219
			elif obj[1]>55.701026807823716:
				return -0.09555175939331884
			else: return -0.09555175939331884
		else: return 0.01104845272566744
	elif obj[0]>18.71755632751331:
		# {"feature": "Diferentes", "instances": 331, "metric_value": 0.051, "depth": 2}
		if obj[3]>77.69876829045978:
			# {"feature": "Palavras_Frase", "instances": 201, "metric_value": 0.0214, "depth": 3}
			if obj[4]<=11.864496538882769:
				return -0.19525322050191043
			elif obj[4]>11.864496538882769:
				return -0.10554589395937712
			else: return -0.10554589395937712
		elif obj[3]<=77.69876829045978:
			# {"feature": "Palavras_Frase", "instances": 130, "metric_value": 0.0165, "depth": 3}
			if obj[4]<=28.055256389679315:
				return 0.03441157985906132
			elif obj[4]>28.055256389679315:
				return -0.1979051325470209
			else: return -0.1979051325470209
		else: return 0.020115166787917797
	else: return -0.10443400945007981
