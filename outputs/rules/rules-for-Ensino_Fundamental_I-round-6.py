def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0634, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0289, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 613, "metric_value": 0.0501, "depth": 3}
			if obj[4]>10.643470540623449:
				return -0.19478865483221613
			elif obj[4]<=10.643470540623449:
				return -0.0015676230192184447
			else: return -0.0015676230192184447
		elif obj[3]<=68.82111094763226:
			# {"feature": "Canonicas", "instances": 533, "metric_value": 0.0003, "depth": 3}
			if obj[2]<=29.310321711712607:
				return -0.19850207762284713
			elif obj[2]>29.310321711712607:
				return -0.200906952048919
			else: return -0.200906952048919
		else: return -0.19966616317993258
	elif obj[0]>13.987250505732058:
		# {"feature": "Palavras_Frase", "instances": 930, "metric_value": 0.0693, "depth": 2}
		if obj[4]<=12.60829693515217:
			# {"feature": "Diferentes", "instances": 578, "metric_value": 0.0355, "depth": 3}
			if obj[3]>68.9582927109911:
				return 0.24304984961967588
			elif obj[3]<=68.9582927109911:
				return -0.16604261130094528
			else: return -0.16604261130094528
		elif obj[4]>12.60829693515217:
			# {"feature": "Diferentes", "instances": 352, "metric_value": 0.049, "depth": 3}
			if obj[3]<=80.34048212640499:
				return -0.20035909624840212
			elif obj[3]>80.34048212640499:
				return -0.096809530662278
			else: return -0.096809530662278
		else: return -0.183002777016637
	else: return 0.037802784385219695
