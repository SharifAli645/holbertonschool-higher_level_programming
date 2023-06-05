#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    if sentence:
        return (le, sentence[0])
    return (le, None)
