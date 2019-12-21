"""
@author : Hyunwoong
@when : 2019-12-19
@homepage : https://github.com/gusdnd852
"""
import os

from data import *

from models.model.transformer import Transformer

model = Transformer(src_pad_idx=src_pad_idx,
                    trg_pad_idx=trg_pad_idx,
                    trg_sos_idx=trg_sos_idx,
                    d_model=d_model,
                    enc_voc_size=enc_voc_size,
                    dec_voc_size=dec_voc_size,
                    max_len=max_len,
                    ffn_hidden=ffn_hidden,
                    n_head=n_heads,
                    n_layers=n_layers,
                    drop_prob=0.00,
                    device=device).to(device)


def test_model(num_examples):
    iterator = train_iter
    model.load_state_dict(torch.load("./saved/model-saved.pt"))

    with torch.no_grad():
        for i, batch in enumerate(iterator):
            if i >= 1: break
            src = batch.src
            trg = batch.trg
            output = model(src, trg[:, :-1])

            for j in range(num_examples):
                src_words = idx_to_word(src[j], loader.source.vocab)
                trg_words = idx_to_word(trg[j], loader.target.vocab)
                output_words = output[j].max(dim=1)[1]
                output_words = idx_to_word(output_words, loader.target.vocab)

                print('source :', src_words)
                print('target :', trg_words)
                print('predicted :', output_words)
                print()


def idx_to_word(x, vocab):
    words = []
    for i in x:
        word = vocab.itos[i]
        if '<' not in word:
            words.append(word)
    words = " ".join(words)
    return words


if __name__ == '__main__':
    test_model(num_examples=20)
