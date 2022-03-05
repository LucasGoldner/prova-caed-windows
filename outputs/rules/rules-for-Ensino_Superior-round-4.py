def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0499, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Palavras_Frase", "instances": 1093, "metric_value": 0.0275, "depth": 2}
		if obj[4]<=12.421757680118793:
			# {"feature": "Verbos", "instances": 600, "metric_value": 0.0111, "depth": 3}
			if obj[0]>17.029405380496936:
				return -0.18065713022904875
			elif obj[0]<=17.029405380496936:
				return -0.12641694942086013
			else: return -0.12641694942086013
		elif obj[4]>12.421757680118793:
			# {"feature": "Substantivos", "instances": 493, "metric_value": 0.0045, "depth": 3}
			if obj[1]>47.4620254013171:
				return 0.07494794342536407
			elif obj[1]<=47.4620254013171:
				return -0.03672138936186241
			else: return -0.03672138936186241
		else: return 0.02149162996129622
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0055, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0073, "depth": 3}
			if obj[1]>50.15338176787905:
				return 0.4508061679444703
			elif obj[1]<=50.15338176787905:
				return 0.31557676711200194
			else: return 0.31557676711200194
		elif obj[0]>12.63497838546153:
			# {"feature": "Palavras_Frase", "instances": 459, "metric_value": 0.0143, "depth": 3}
			if obj[4]<=21.90501697864883:
				return 0.22255088959760333
			elif obj[4]>21.90501697864883:
				return 0.5020517837582973
			else: return 0.5020517837582973
		else: return 0.25726015096396404
	else: return 0.32700315045073464
