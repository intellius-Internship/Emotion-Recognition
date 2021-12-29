
from transformers import ElectraModel, ElectraTokenizer

def load_model(model_name):
    if 'bert' == model_name:
        raise NotImplementedError('Should implement this!')

    elif 'electra' == model_name:
        model = ElectraModel.from_pretrained("monologg/koelectra-base-discriminator")  # KoELECTRA-Base
        tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator")

        return model, tokenizer

    elif 'bigbird' == model_name:
        raise NotImplementedError('Should implement this!')


    raise NotImplementedError('Unknown model')