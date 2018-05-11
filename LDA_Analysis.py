# -*- coding: utf-8 -*-
"""
LDA Model: Copyright (C) 2010  Matthew D. Hoffman
URL: https://github.com/blei-lab/onlineldavb/blob/master/onlineldavb.py
"""

import numpy
import onlineldavb
import printtopics
import csv

def main():
    '''
    Read PApers
    '''
    papers_ = []
    
    with open('papers.csv', 'r') as csvfile:
      for line in csv.reader(csvfile, delimiter=',', quotechar='"'):
          papers_.append(line)
    
    D = len(papers_)
    
    # The number of topics
    K = 10

    # Our vocabulary
    vocab = open('./dictnostops.txt').readlines()

    # Initialize the algorithm with alpha=1/K, eta=1/K, tau_0=1024, kappa=0.7
    olda = onlineldavb.OnlineLDA(vocab, K, D, 1./K, 1./K, 1024., 0.7)
    
    docset = [row[3] for row in papers_]
    #articlenames = [row[0] for row in papers_]

    # Give them to online LDA
    (gamma, bound) = olda.update_lambda_docs(docset)
    # Compute an estimate of held-out perplexity
    (wordids, wordcts) = onlineldavb.parse_doc_list(docset, olda._vocab)
    perwordbound = bound * len(docset) / (D * sum(map(sum, wordcts)))
    print('%d:  rho_t = %f,  held-out perplexity estimate = %f' % \
        (1, olda._rhot, numpy.exp(-perwordbound)))

    # Save lambda, the parameters to the variational distributions
    # over topics, and gamma, the parameters to the variational
    # distributions over topic weights for the articles analyzed in
    # the last iteration.

    numpy.savetxt('lambda.dat', olda._lambda)
    numpy.savetxt('gamma.dat', gamma)
    
    #show topics
    printtopics.main(5)

if __name__ == '__main__':
    main()