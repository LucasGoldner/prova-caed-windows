def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0441, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Palavras_Frase", "instances": 1093, "metric_value": 0.0265, "depth": 2}
		if obj[4]<=12.421757680118793:
			# {"feature": "Verbos", "instances": 600, "metric_value": 0.011, "depth": 3}
			if obj[0]>17.029405380496936:
				return -0.1712498664855957
			elif obj[0]<=17.029405380496936:
				return -0.11947060604275707
			else: return -0.11947060604275707
		elif obj[4]>12.421757680118793:
			# {"feature": "Substantivos", "instances": 493, "metric_value": 0.0045, "depth": 3}
			if obj[1]>47.4620254013171:
				return 0.07431383517929552
			elif obj[1]<=47.4620254013171:
				return -0.037295100863202146
			else: return -0.037295100863202146
		else: return 0.020886433747187107
	elif obj[3]<=71.7720593884051:
		# {"feature": "Substantivos", "instances": 983, "metric_value": 0.0052, "depth": 2}
		if obj[1]<=55.09953458106427:
			# {"feature": "Palavras_Frase", "instances": 840, "metric_value": 0.0045, "depth": 3}
			if obj[4]<=15.022668656369083:
				return 0.23439235305430947
			elif obj[4]>15.022668656369083:
				return 0.358115417040614
			else: return 0.358115417040614
		elif obj[1]>55.09953458106427:
			# {"feature": "Verbos", "instances": 143, "metric_value": 0.0099, "depth": 3}
			if obj[0]>3.691236836589024:
				return 0.46279434924540314
			elif obj[0]<=3.691236836589024:
				return 0.014075177907943725
			else: return 0.014075177907943725
		else: return 0.4471048677301073
	else: return 0.3034726968859365
