def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0505, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Palavras_Frase", "instances": 1093, "metric_value": 0.0276, "depth": 2}
		if obj[4]<=12.421757680118793:
			# {"feature": "Verbos", "instances": 600, "metric_value": 0.0111, "depth": 3}
			if obj[0]>17.029405380496936:
				return -0.18122022041996705
			elif obj[0]<=17.029405380496936:
				return -0.12677530811209858
			else: return -0.12677530811209858
		elif obj[4]>12.421757680118793:
			# {"feature": "Substantivos", "instances": 493, "metric_value": 0.0045, "depth": 3}
			if obj[1]>47.4620254013171:
				return 0.07499406947699966
			elif obj[1]<=47.4620254013171:
				return -0.03669718002616349
			else: return -0.03669718002616349
		else: return 0.021527264441002697
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.006, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0073, "depth": 3}
			if obj[1]>50.15338176787905:
				return 0.45613140991998313
			elif obj[1]<=50.15338176787905:
				return 0.32030576442985376
			else: return 0.32030576442985376
		elif obj[0]>12.63497838546153:
			# {"feature": "Palavras_Frase", "instances": 459, "metric_value": 0.015, "depth": 3}
			if obj[4]<=21.90501697864883:
				return 0.21997930287425196
			elif obj[4]>21.90501697864883:
				return 0.5112246222663344
			else: return 0.5112246222663344
		else: return 0.25614702227588315
	else: return 0.3291746797239065
