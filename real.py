sc=404
match sc:
	case 404:
		print("Bad request!")
	
	case 200:
		print("Good request!")

	case other:
		print("Invalid request1")