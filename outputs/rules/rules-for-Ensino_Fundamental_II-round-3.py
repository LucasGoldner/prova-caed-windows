def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Diferentes", "instances": 2076, "metric_value": 0.0309, "depth": 1}
	if obj[3]>71.7720593884051:
		# {"feature": "Verbos", "instances": 1093, "metric_value": 0.0102, "depth": 2}
		if obj[0]>10.235201384613958:
			# {"feature": "Palavras_Frase", "instances": 908, "metric_value": 0.0035, "depth": 3}
			if obj[4]>8.297926395169196:
				return 0.05552740334633487
			elif obj[4]<=8.297926395169196:
				return -0.07871445575181175
			else: return -0.07871445575181175
		elif obj[0]<=10.235201384613958:
			# {"feature": "Canonicas", "instances": 185, "metric_value": 0.0091, "depth": 3}
			if obj[2]>18.857142857142858:
				return -0.14550486741506535
			elif obj[2]<=18.857142857142858:
				return 0.7827456295490265
			else: return 0.7827456295490265
		else: return -0.1404872971612054
	elif obj[3]<=71.7720593884051:
		# {"feature": "Verbos", "instances": 983, "metric_value": 0.0201, "depth": 2}
		if obj[0]<=12.63497838546153:
			# {"feature": "Substantivos", "instances": 524, "metric_value": 0.0307, "depth": 3}
			if obj[1]>50.15338176787905:
				return -0.20374587326711607
			elif obj[1]<=50.15338176787905:
				return -0.1859702589335265
			else: return -0.1859702589335265
		elif obj[0]>12.63497838546153:
			# {"feature": "Substantivos", "instances": 459, "metric_value": 0.0232, "depth": 3}
			if obj[1]>39.90239674817307:
				return -0.12103788585551663
			elif obj[1]<=39.90239674817307:
				return -0.2043914884737093
			else: return -0.2043914884737093
		else: return -0.13429455903880216
	else: return -0.16692224405668032
