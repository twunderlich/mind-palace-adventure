dic = {
	"ball": {"word": "ball", "type": "noun"},
	"red": {"word": "red", "type": "adjective"},
	"get": {"word": "get", "type": "verb"}
}

class Parser:
	def __init__(self, dictionary):
		self.dictionary = dictionary

	def parse(self, text):
		text = text.split(" ")
		parsed = []

		for word in text:
			word = self.dictionary.get(word, "unknown")
			if word != "unknown":
					parsed.append(word)

		return parsed

text = "I would like to pickup the red ball"

parser = Parser(dic)

print(parser.parse(text))