def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.067, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0283, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 613, "metric_value": 0.0494, "depth": 3}
			if obj[4]>10.643470540623449:
				return -0.20243404063272646
			elif obj[4]<=10.643470540623449:
				return -0.014758773283524946
			else: return -0.014758773283524946
		elif obj[3]<=68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 533, "metric_value": 0.0003, "depth": 3}
			if obj[4]<=17.437530934006695:
				return -0.20507847544274818
			elif obj[4]>17.437530934006695:
				return -0.20075491523104055
			else: return -0.20075491523104055
		else: return -0.20416995997612292
	elif obj[0]>13.987250505732058:
		# {"feature": "Palavras_Frase", "instances": 930, "metric_value": 0.071, "depth": 2}
		if obj[4]<=12.60829693515217:
			# {"feature": "Diferentes", "instances": 578, "metric_value": 0.0461, "depth": 3}
			if obj[3]>78.48607670054238:
				return 0.35083898005232345
			elif obj[3]<=78.48607670054238:
				return -0.05883718958459638
			else: return -0.05883718958459638
		elif obj[4]>12.60829693515217:
			# {"feature": "Diferentes", "instances": 352, "metric_value": 0.0494, "depth": 3}
			if obj[3]<=80.34048212640499:
				return -0.1989779891414447
			elif obj[3]>80.34048212640499:
				return -0.09009051979598352
			else: return -0.09009051979598352
		else: return -0.18072696445001799
	else: return 0.04436175746302451
