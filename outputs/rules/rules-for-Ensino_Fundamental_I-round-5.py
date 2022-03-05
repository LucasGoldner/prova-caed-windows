def findDecision(obj): #obj[0]: Verbos, obj[1]: Substantivos, obj[2]: Canonicas, obj[3]: Diferentes, obj[4]: Palavras_Frase
	# {"feature": "Verbos", "instances": 2076, "metric_value": 0.0661, "depth": 1}
	if obj[0]<=13.987250505732058:
		# {"feature": "Diferentes", "instances": 1146, "metric_value": 0.0284, "depth": 2}
		if obj[3]>68.82111094763226:
			# {"feature": "Palavras_Frase", "instances": 613, "metric_value": 0.0491, "depth": 3}
			if obj[4]>10.643470540623449:
				return -0.20011112921767765
			elif obj[4]<=10.643470540623449:
				return -0.014415595477277582
			else: return -0.014415595477277582
		elif obj[3]<=68.82111094763226:
			# {"feature": "Substantivos", "instances": 533, "metric_value": 0.001, "depth": 3}
			if obj[1]>49.80530248330753:
				return -0.19709824540012671
			elif obj[1]<=49.80530248330753:
				return -0.2027466225009116
			else: return -0.2027466225009116
		else: return -0.19976877265978485
	elif obj[0]>13.987250505732058:
		# {"feature": "Palavras_Frase", "instances": 930, "metric_value": 0.0702, "depth": 2}
		if obj[4]<=12.60829693515217:
			# {"feature": "Diferentes", "instances": 578, "metric_value": 0.046, "depth": 3}
			if obj[3]>78.48607670054238:
				return 0.34735725050830557
			elif obj[3]<=78.48607670054238:
				return -0.06125164019512831
			else: return -0.06125164019512831
		elif obj[4]>12.60829693515217:
			# {"feature": "Diferentes", "instances": 352, "metric_value": 0.0493, "depth": 3}
			if obj[3]<=80.34048212640499:
				return -0.19853759178122563
			elif obj[3]>80.34048212640499:
				return -0.08869469292083029
			else: return -0.08869469292083029
		else: return -0.18012642407451163
	else: return 0.042699424345647136
