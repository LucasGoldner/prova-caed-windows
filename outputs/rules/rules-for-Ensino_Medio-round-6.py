def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0078, "depth": 1}
	if obj[0]<=18.71755632751331:
		# {"feature": "Diferentes", "instances": 1745, "metric_value": 0.0041, "depth": 2}
		if obj[3]>70.64785271414716:
			# {"feature": "Palavras_Frase", "instances": 910, "metric_value": 0.0122, "depth": 3}
			if obj[4]>9.518886934360191:
				return 0.16028784381018746
			elif obj[4]<=9.518886934360191:
				return -0.11383568379310292
			else: return -0.11383568379310292
		elif obj[3]<=70.64785271414716:
			# {"feature": "Substantivos", "instances": 835, "metric_value": 0.0033, "depth": 3}
			if obj[1]<=55.701026807823716:
				return 0.027459597835938137
			elif obj[1]>55.701026807823716:
				return -0.0966821023951406
			else: return -0.0966821023951406
		else: return 0.0103622379238734
	elif obj[0]>18.71755632751331:
		# {"feature": "Diferentes", "instances": 331, "metric_value": 0.0511, "depth": 2}
		if obj[3]>77.69876829045978:
			# {"feature": "Palavras_Frase", "instances": 201, "metric_value": 0.0214, "depth": 3}
			if obj[4]<=11.864496538882769:
				return -0.19550488931074572
			elif obj[4]>11.864496538882769:
				return -0.10537704371887704
			else: return -0.10537704371887704
		elif obj[3]<=77.69876829045978:
			# {"feature": "Palavras_Frase", "instances": 130, "metric_value": 0.0167, "depth": 3}
			if obj[4]<=28.055256389679315:
				return 0.035031933764942354
			elif obj[4]>28.055256389679315:
				return -0.20174980908632278
			else: return -0.20174980908632278
		else: return 0.020460749589479885
	else: return -0.10442188778312544
