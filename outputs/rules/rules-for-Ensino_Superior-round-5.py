def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0499, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Palavras_Frase", "instances": 1093, "metric_value": 0.0275, "depth": 2}
		if obj[4]<=12.421757680118793:
			# {"feature": "Verbos", "instances": 600, "metric_value": 0.0109, "depth": 3}
			if obj[0]>17.029405380496936:
				return -0.1812997186453983
			elif obj[0]<=17.029405380496936:
				return -0.12551987263345227
			else: return -0.12551987263345227
		elif obj[4]>12.421757680118793:
			# {"feature": "Canonicas", "instances": 493, "metric_value": 0.0064, "depth": 3}
			if obj[2]>30.35797925019979:
				return -0.04127142435083023
			elif obj[2]<=30.35797925019979:
				return 0.09304164650614169
			else: return 0.09304164650614169
		else: return 0.022207166946683888
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0061, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Canonicas", "instances": 524, "metric_value": 0.0091, "depth": 3}
			if obj[2]<=29.181658395150027:
				return 0.4648317866684759
			elif obj[2]>29.181658395150027:
				return 0.31331954955581637
			else: return 0.31331954955581637
		elif obj[0]>12.63497838546153:
			# {"feature": "Palavras_Frase", "instances": 459, "metric_value": 0.0168, "depth": 3}
			if obj[4]<=21.90501697864883:
				return 0.213749088532296
			elif obj[4]>21.90501697864883:
				return 0.5325060282882891
			else: return 0.5325060282882891
		else: return 0.25333328366539315
	else: return 0.32723372295453373
