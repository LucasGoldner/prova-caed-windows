def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0516, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Palavras_Frase", "instances": 1093, "metric_value": 0.0278, "depth": 2}
		if obj[4]<=12.421757680118793:
			# {"feature": "Verbos", "instances": 600, "metric_value": 0.0109, "depth": 3}
			if obj[0]>17.029405380496936:
				return -0.1835457667660173
			elif obj[0]<=17.029405380496936:
				return -0.12712710896103652
			else: return -0.12712710896103652
		elif obj[4]>12.421757680118793:
			# {"feature": "Canonicas", "instances": 493, "metric_value": 0.0064, "depth": 3}
			if obj[2]>30.35797925019979:
				return -0.04114268250190295
			elif obj[2]<=30.35797925019979:
				return 0.09316460097552369
			else: return 0.09316460097552369
		else: return 0.022333173583777392
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.008, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Canonicas", "instances": 524, "metric_value": 0.0088, "depth": 3}
			if obj[2]<=29.181658395150027:
				return 0.48187957452062297
			elif obj[2]>29.181658395150027:
				return 0.3321517530887846
			else: return 0.3321517530887846
		elif obj[0]>12.63497838546153:
			# {"feature": "Palavras_Frase", "instances": 459, "metric_value": 0.0203, "depth": 3}
			if obj[4]<=21.90501697864883:
				return 0.20243410491824743
			elif obj[4]>21.90501697864883:
				return 0.5674385543455157
			else: return 0.5674385543455157
		else: return 0.2477614548471239
	else: return 0.33417700287163077
