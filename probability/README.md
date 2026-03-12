# Probability

My study notes on probability theory.

## Current Resources

- **Steve Brunton's YouTube Series** - Conditional probability, Bayes' theorem, Total probability
- **Introduction to Probability (Bertsekas & Tsitsiklis, 2nd Ed)** - MIT textbook, more rigorous

## Structure

```
probability/
├── probability-notes.ipynb          # Steve Brunton series notes
└── bertsekas-intro-probability/
    └── chapter-02-discrete-random-variables.ipynb
```

## Topics Covered

| Topic | Source | Status |
|-------|--------|--------|
| Conditional Probability | Brunton | Done |
| Law of Total Probability | Brunton | Done |
| Bayes' Theorem | Brunton | Done |
| Discrete Random Variables (2.1-2.4) | Bertsekas | Done |
| Joint PMFs, Conditioning, Independence (2.5-2.7) | Bertsekas | Not Started |

## My Approach

I like to think about probability from the **universe perspective** - start with the full sample space, find intersections, then "squeeze" down by dividing. This keeps everything grounded in actual probabilities rather than mixing counts with probabilities.

### Key Intuitions

**Conditional Probability:** "Zooming in" from the universe to a smaller world

**Expected Value:** Like a weighted average where probabilities replace $\frac{1}{n}$ - same normalization idea since probabilities sum to 1

**Variance:** How spread out values are from the mean
