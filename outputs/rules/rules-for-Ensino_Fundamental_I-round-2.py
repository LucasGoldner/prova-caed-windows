def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0602, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.028, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 613, "metric_value": 0.0491, "depth": 3}
			if obj[4]>10.643470540623449:
				return -0.18497099941028916
			elif obj[4]<=10.643470540623449:
				return -0.00016627582636746492
			else: return -0.00016627582636746492
		elif obj[3]<=68.82111094763226:
			# {"feature": "Canonicas", "instances": 533, "metric_value": 0.0004, "depth": 3}
			if obj[2]<=29.310321711712607:
				return -0.18527985897931185
			elif obj[2]>29.310321711712607:
				return -0.18854896712672803
			else: return -0.18854896712672803
		else: return -0.1868622790581737
	elif obj[0]>13.987250505732058:
		# {"feature": "Palavras_Frase", "instances": 930, "metric_value": 0.065, "depth": 2}
		if obj[4]<=12.60829693515217:
			# {"feature": "Diferentes", "instances": 578, "metric_value": 0.0336, "depth": 3}
			if obj[3]>68.9582927109911:
				return 0.22925865989973357
			elif obj[3]<=68.9582927109911:
				return -0.16489335715770723
			else: return -0.16489335715770723
		elif obj[4]>12.60829693515217:
			# {"feature": "Diferentes", "instances": 352, "metric_value": 0.0485, "depth": 3}
			if obj[3]<=80.34048212640499:
				return -0.18947533149361204
			elif obj[3]>80.34048212640499:
				return -0.0908442394713224
			else: return -0.0908442394713224
		else: return -0.17294341550123962
	else: return 0.03464539941921029
