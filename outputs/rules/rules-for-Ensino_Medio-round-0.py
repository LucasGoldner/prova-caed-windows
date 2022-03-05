def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0107, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0174, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Canonicas", "instances": 613, "metric_value": 0.0038, "depth": 3}
			if obj[2]<=30.16098958147355:
				return 0.4383116883116883
			elif obj[2]>30.16098958147355:
				return 0.5606557377049181
			else: return 0.5606557377049181
		elif obj[3]<=68.82111094763226:
			# {"feature": "Canonicas", "instances": 533, "metric_value": 0.0061, "depth": 3}
			if obj[2]<=29.310321711712607:
				return 0.1890909090909091
			elif obj[2]>29.310321711712607:
				return 0.313953488372093
			else: return 0.313953488372093
		else: return 0.24953095684803
	elif obj[0]>13.987250505732058:
		# {"feature": "Diferentes", "instances": 930, "metric_value": 0.0241, "depth": 2}
		if obj[3]>75.40838940251871:
			# {"feature": "Palavras_Frase", "instances": 512, "metric_value": 0.0314, "depth": 3}
			if obj[4]<=10.536759696002553:
				return 0.03389830508474576
			elif obj[4]>10.536759696002553:
				return 0.19815668202764977
			else: return 0.19815668202764977
		elif obj[3]<=75.40838940251871:
			# {"feature": "Palavras_Frase", "instances": 418, "metric_value": 0.0221, "depth": 3}
			if obj[4]<=21.80223406221278:
				return 0.3651226158038147
			elif obj[4]>21.80223406221278:
				return 0.0392156862745098
			else: return 0.0392156862745098
		else: return 0.3253588516746411
	else: return 0.2032258064516129
