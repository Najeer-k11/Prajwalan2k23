from googletrans import Translator

tl = Translator()

out = tl.translate("how are you",dest="te")

print(out)