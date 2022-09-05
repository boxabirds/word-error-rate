import sys
import argparse

import jiwer as j
# uses https://github.com/jitsi/jiwer
# https://www.researchgate.net/publication/221478089_From_WER_and_RIL_to_MER_and_WIL_improved_evaluation_measures_for_connected_speech_recognition
# WER: Word Error Rate 
# WIL: Word Information Lost
# MER: Match Error Rate
# "The commonly used WER measure is ideally suited only to
#CSR applications where output errors can be corrected by
# typing. For almost any other type of speech recognition system 
# a measure based on the proportion of information communicated would be more useful."


# file io
from pathlib import Path

def test_jiwer():
    ground_truth = "hello world"
    hypothesis = "hello duck"


    wer_val = j.wer(ground_truth, hypothesis)
    print( f"wer =  {wer_val}")
    mer_val = j.mer(ground_truth, hypothesis)
    print( f"mer =  {mer_val}")
    wil_val = j.wil(ground_truth, hypothesis)
    print( f"wil =  {wil_val}")

    # faster, because `compute_measures` only needs to perform the heavy lifting once:
    measures = j.compute_measures(ground_truth, hypothesis)
    wer = measures['wer']
    mer = measures['mer']
    wil = measures['wil']



def import_and_compare_two_files(reference = "reference.txt", hypothesis = "hypothesis.txt"):
    # read files
    with open(reference, "r") as ref:
        reference = ref.read()
    with open(hypothesis, "r") as hyp:
        hypothesis = hyp.read()

    # we want to heavily normalise the text -- none of these things are significant
    # when it comes to comparing the text
    transformation = j.Compose([
        j.ToLowerCase(),
        j.RemoveWhiteSpace(replace_by_space=True),
        j.RemoveMultipleSpaces(),
        j.RemovePunctuation(),
        j.ReduceToListOfListOfWords(word_delimiter=" ")
    ]) 

    # compare
    measures = j.compute_measures(reference, hypothesis, transformation, transformation)
    wer = measures['wer']
    mer = measures['mer']
    wil = measures['wil']
    return(wer, mer, wil)

if __name__ == "__main__":
    print( "=== Word error rate / word information lost / match error rate test ===" )
    # extract reference and hypothesis files from command line arguments
    parser = argparse.ArgumentParser(description='Compare two text files.')
    parser.add_argument('--reference', type=str, help='reference file')
    parser.add_argument('--hypothesis', type=str, help='hypothesis file')
    args = parser.parse_args()
    reference = args.reference
    hypothesis = args.hypothesis
    (wer, mer, wil) = import_and_compare_two_files(reference, hypothesis)
    print( f"Word Error Rate =  {wer*100:.2f}%")
    print( f"Match Error Rate =  {mer*100:.2f}%")
    print( f"Word Information Loss =  {wil*100:.2f}%")

