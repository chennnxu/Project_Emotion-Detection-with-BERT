from transformers import pipeline

unmasker = pipeline('fill-mask', model='bert-base-uncased')
print(unmasker("Hello I'm a [MASK] model."))