def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0632, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0286, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 613, "metric_value": 0.0501, "depth": 3}
			if obj[4]>10.643470540623449:
				return -0.19423778088075713
			elif obj[4]<=10.643470540623449:
				return -0.001485420898957686
			else: return -0.001485420898957686
		elif obj[3]<=68.82111094763226:
			# {"feature": "Canonicas", "instances": 533, "metric_value": 0.0003, "depth": 3}
			if obj[2]<=29.310321711712607:
				return -0.19716791174628517
			elif obj[2]>29.310321711712607:
				return -0.19972490923580274
			else: return -0.19972490923580274
		else: return -0.19840563285753382
	elif obj[0]>13.987250505732058:
		# {"feature": "Palavras_Frase", "instances": 930, "metric_value": 0.0691, "depth": 2}
		if obj[4]<=12.60829693515217:
			# {"feature": "Diferentes", "instances": 578, "metric_value": 0.0355, "depth": 3}
			if obj[3]>68.9582927109911:
				return 0.24218024843407476
			elif obj[3]<=68.9582927109911:
				return -0.16695858538150787
			else: return -0.16695858538150787
		elif obj[4]>12.60829693515217:
			# {"feature": "Diferentes", "instances": 352, "metric_value": 0.049, "depth": 3}
			if obj[3]<=80.34048212640499:
				return -0.20008606211927563
			elif obj[3]>80.34048212640499:
				return -0.09651504507509329
			else: return -0.09651504507509329
		else: return -0.18272614733062006
	else: return 0.03736203908920288
