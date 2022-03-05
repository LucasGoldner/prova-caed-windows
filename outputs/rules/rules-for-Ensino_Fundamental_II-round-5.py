def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0306, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Verbos", "instances": 1093, "metric_value": 0.0101, "depth": 2}
		if obj[0]>10.235201384613958:
			# {"feature": "Palavras_Frase", "instances": 908, "metric_value": 0.0035, "depth": 3}
			if obj[4]>8.297926395169196:
				return 0.05559325059557142
			elif obj[4]<=8.297926395169196:
				return -0.0778574055733801
			else: return -0.0778574055733801
		elif obj[0]<=10.235201384613958:
			# {"feature": "Canonicas", "instances": 185, "metric_value": 0.0091, "depth": 3}
			if obj[2]>18.857142857142858:
				return -0.14485168092600678
			elif obj[2]<=18.857142857142858:
				return 0.7834731042385101
			else: return 0.7834731042385101
		else: return -0.13983370911430668
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0196, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0322, "depth": 3}
			if obj[1]>50.15338176787905:
				return -0.1956382599059373
			elif obj[1]<=50.15338176787905:
				return -0.18173460515192996
			else: return -0.18173460515192996
		elif obj[0]>12.63497838546153:
			# {"feature": "Substantivos", "instances": 459, "metric_value": 0.0228, "depth": 3}
			if obj[1]>39.90239674817307:
				return -0.1222827667708224
			elif obj[1]<=39.90239674817307:
				return -0.20369520068985142
			else: return -0.20369520068985142
		else: return -0.1352307137775525
	else: return -0.16399466704922072
