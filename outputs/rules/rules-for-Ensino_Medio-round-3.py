def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0088, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0131, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Canonicas", "instances": 613, "metric_value": 0.0037, "depth": 3}
			if obj[2]<=30.16098958147355:
				return 0.15407184796867432
			elif obj[2]>30.16098958147355:
				return 0.27515184923273617
			else: return 0.27515184923273617
		elif obj[3]<=68.82111094763226:
			# {"feature": "Canonicas", "instances": 533, "metric_value": 0.0057, "depth": 3}
			if obj[2]<=29.310321711712607:
				return -0.05675165122205561
			elif obj[2]>29.310321711712607:
				return 0.0627923494623613
			else: return 0.0627923494623613
		else: return 0.001113925094228748
	elif obj[0]>13.987250505732058:
		# {"feature": "Diferentes", "instances": 930, "metric_value": 0.0229, "depth": 2}
		if obj[3]>75.40838940251871:
			# {"feature": "Palavras_Frase", "instances": 512, "metric_value": 0.0265, "depth": 3}
			if obj[4]<=10.536759696002553:
				return -0.18991583545329208
			elif obj[4]>10.536759696002553:
				return -0.06444234177813551
			else: return -0.06444234177813551
		elif obj[3]<=75.40838940251871:
			# {"feature": "Palavras_Frase", "instances": 418, "metric_value": 0.0211, "depth": 3}
			if obj[4]<=21.80223406221278:
				return 0.10797691008213106
			elif obj[4]>21.80223406221278:
				return -0.20426369268520206
			else: return -0.20426369268520206
		else: return 0.06988056859616458
	else: return -0.04386998059288148
