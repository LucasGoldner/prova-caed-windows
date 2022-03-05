def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0749, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Palavras_Frase", "instances": 1093, "metric_value": 0.033, "depth": 2}
		if obj[4]<=12.421757680118793:
			# {"feature": "Verbos", "instances": 600, "metric_value": 0.0119, "depth": 3}
			if obj[0]>17.029405380496936:
				return 0.025889967637540454
			elif obj[0]<=17.029405380496936:
				return 0.09278350515463918
			else: return 0.09278350515463918
		elif obj[4]>12.421757680118793:
			# {"feature": "Canonicas", "instances": 493, "metric_value": 0.0065, "depth": 3}
			if obj[2]>30.35797925019979:
				return 0.21153846153846154
			elif obj[2]<=30.35797925019979:
				return 0.34763948497854075
			else: return 0.34763948497854075
		else: return 0.27586206896551724
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0091, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Canonicas", "instances": 524, "metric_value": 0.0095, "depth": 3}
			if obj[2]<=29.181658395150027:
				return 0.8235294117647058
			elif obj[2]>29.181658395150027:
				return 0.6666666666666666
			else: return 0.6666666666666666
		elif obj[0]>12.63497838546153:
			# {"feature": "Palavras_Frase", "instances": 459, "metric_value": 0.0221, "depth": 3}
			if obj[4]<=21.90501697864883:
				return 0.5248756218905473
			elif obj[4]>21.90501697864883:
				return 0.9122807017543859
			else: return 0.9122807017543859
		else: return 0.5729847494553377
	else: return 0.6663275686673449
