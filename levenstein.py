# levenstein distance calculator
# Word Error Rate (WER) = Subsitutions + Deletions + Insertions / Num Words

#
#
def levenstein(reference,hypothesis):
    norm_ref = reference.split()
    norm_hyp = hypothesis.split()

    # if one of them is an empty string then the distance is simply the number of words
    # of the other
    if (len(norm_ref) == 0) or (len(norm_hyp) == 0):
        return abs(len(norm_ref) - len(norm_hyp))

    substitutions = 0
    deletions = 0
    insertions = 0
    print(f"Reference: '{reference}'; hypothesis: '{hypothesis}'")

    # reference index and hypothesis index. They're tracked separately
    # because there may be deletions or insertions
    hi= 0
    ri = 0
    num_hyp_words= len(norm_hyp)
    num_ref_words = len(norm_ref)
    while (ri < num_ref_words) and (hi < num_hyp_words):
        print(f" -- ri: {ri}; hi: {hi}, ")
        print(f"comparing '{norm_ref[ri]}' with hypothesis '{norm_hyp[hi]}'")

        # our words don't match
        if norm_ref[ri] != norm_hyp[hi]:

            # we're at the last hypothesis word
            if hi == num_hyp_words-1:
                # we're at the last reference word too so don't look ahead
                if ri == num_ref_words-1:
                    print("  -- subtitution case 1")
                    substitutions += 1

                elif norm_hyp[hi] == norm_ref[ri+1]:
                    print(f"  -- matches reference word at index {ri+1} so it's a deletion case 1")
                    deletions += 1
                    ri += 1

                else:
                    print("  -- subtitution case 2")
                    substitutions += 1

            # deletion: hypothesis matches our NEXT reference word (e.g. r:"one two three", h:"one three"
            elif norm_ref[ri+1] == norm_hyp[hi]:
                print( "  -- deletion case 2")
                deletions += 1
                ri += 1

            # substitution: NEXT hypothesis word matches NEXT reference word
            # e.g. "one two three" vs "one four three"
            else:
                print("  -- subtitution case 3")
                substitutions +=1
        ri += 1
        hi += 1

    # any extra words in the hypothesis are insertions
    hyp_insertions_at_end = num_hyp_words - hi
    print(f"  -- number of hypothesis words left over: {hyp_insertions_at_end}")
    insertions += hyp_insertions_at_end

    # any extra words in reference are deletions
    hyp_deletions_at_end = num_ref_words - ri
    print(f"  -- number of reference words left over: {hyp_deletions_at_end}")
    deletions += hyp_deletions_at_end

    score = substitutions + deletions + insertions
    print(f"Conclusion: for '{reference}' vs '{hypothesis}': score {score}\n")
    return score


