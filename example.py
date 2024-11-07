import dhlab as dh

corpus = dh.Corpus(doctype="digibok", from_year=1980, to_year=2005)

print(corpus.count())