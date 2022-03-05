def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.009, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0126, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Canonicas", "instances": 613, "metric_value": 0.0037, "depth": 3}
			if obj[2]<=30.16098958147355:
				return 0.15301035209135574
			elif obj[2]>30.16098958147355:
				return 0.27414463992978705
			else: return 0.27414463992978705
		elif obj[3]<=68.82111094763226:
			# {"feature": "Canonicas", "instances": 533, "metric_value": 0.0058, "depth": 3}
			if obj[2]<=29.310321711712607:
				return -0.05376824276013808
			elif obj[2]>29.310321711712607:
				return 0.06639334409273873
			else: return 0.06639334409273873
		else: return 0.00439627770523193
	elif obj[0]>13.987250505732058:
		# {"feature": "Diferentes", "instances": 930, "metric_value": 0.0226, "depth": 2}
		if obj[3]>75.40838940251871:
			# {"feature": "Palavras_Frase", "instances": 512, "metric_value": 0.0263, "depth": 3}
			if obj[4]<=10.536759696002553:
				return -0.18892207120434712
			elif obj[4]>10.536759696002553:
				return -0.06520367321056154
			else: return -0.06520367321056154
		elif obj[3]<=75.40838940251871:
			# {"feature": "Palavras_Frase", "instances": 418, "metric_value": 0.0201, "depth": 3}
			if obj[4]<=21.80223406221278:
				return 0.10429829663574208
			elif obj[4]>21.80223406221278:
				return -0.19318934223231146
			else: return -0.19318934223231146
		else: return 0.06800195792217574
	else: return -0.044576763097316986
