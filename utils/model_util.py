from transformers import ElectraForSequenceClassification, ElectraTokenizer, ElectraConfig

def load_model(model_name, num_labels, labels=None):
    if labels is None:
        labels = list(range(num_labels))

    if 'bert' == model_name:
        raise NotImplementedError('Should implement this!')

    elif 'electra' == model_name:
        config = ElectraConfig.from_pretrained(
            "monologg/koelectra-base-v3-discriminator",
            num_labels=num_labels,
            id2label={str(i): label for i, label in enumerate(labels)},
            label2id={label: i for i, label in enumerate(labels)}
        )
    
        model = ElectraForSequenceClassification.from_pretrained(
            "monologg/koelectra-base-v3-discriminator", 
            config=config
        )
        tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator")

        return model, tokenizer

    elif 'bigbird' == model_name:
        raise NotImplementedError('Should implement this!')


    raise NotImplementedError('Unknown model')