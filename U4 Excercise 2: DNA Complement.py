def comp(S):
  complementary_strand = ""
  for nucleotide in S:
    if nucleotide == 'A':
      complementary_strand += 'T'
    elif nucleotide == 'T':
      complementary_strand += 'A'
    elif nucleotide == 'C':
      complementary_strand += 'G'
    elif nucleotide == 'G':
      complementary_strand += 'C'
  return complementary_strand

print(comp("ATCAAGGCCTATTCCGGGAAAGG"))
