# Better Explained Bridge Notes

## Connecting the BetterExplained Guide to Axler's Definitions

Source: [An Intuitive Guide to Linear Algebra](https://betterexplained.com/articles/linear-algebra-guide/)

---

The BetterExplained article is one of the clearest practical introductions to linear algebra.
It uses a "spreadsheet" metaphor that makes everything feel concrete and useful.

But it never stops to say what a vector actually is, or why operations work the way they do.
It uses the word "linear" without pinning down the definition.

These notes walk through every major idea in that article and attach the formal structure
from Axler underneath it. The goal is to have both:

- the practical intuition from BetterExplained;
- and the first-principles foundation from Axler that tells you why the intuition is correct.

---

## 1. What does "linear" actually mean?

### What the blog says

The blog opens with a rooftop analogy: move forward 3 feet, rise 1 foot. Move forward 6 feet,
rise 2 feet. Doubling the input doubles the output. Combining two moves gives you the combined rise.

It then states: an operation $F$ is linear if

$$
F(ax) = a \cdot F(x)
$$

and

$$
F(x + y) = F(x) + F(y).
$$

This is presented as "predictable" or "nice" behaviour.

### What Axler would say

BetterExplained describes precisely what Axler defines in Chapter 3 as a **linear map**.

Axler's definition:
A function $T : V \to W$ between two vector spaces is a **linear map** if

1. **Additivity:** $T(u + v) = T(u) + T(v)$ for all $u, v \in V$.
2. **Homogeneity:** $T(\lambda v) = \lambda T(v)$ for all $\lambda \in \mathbb{F}$, $v \in V$.

These two conditions are exactly the two conditions in the blog.

### Why these two conditions?

Think about what you lose if you drop either one.

**Drop homogeneity.** Suppose $T(2v) \neq 2 T(v)$. Then scaling your input before feeding it
in gives a different result from scaling the output. Your operation behaves differently depending
on units. That is useless for anything systematic.

**Drop additivity.** Suppose $T(v + w) \neq T(v) + T(w)$. Then you cannot decompose a complex
input into simple parts, process each part, and reassemble. The whole power of linear algebra — that
you can split a problem into pieces — would collapse.

So the two conditions are the minimum rules that allow linear algebra to be a useful tool.

### Why $F(x) = x + 3$ is not linear

The blog points out that $F(x) = x + 3$ is not linear, which surprises most people. Let's check:

$$
F(2x) = 2x + 3 \neq 2(x + 3) = 2F(x).
$$

The $+3$ shifts the output regardless of the input. It breaks homogeneity.

In Axler's language, this is because $F(x) = x + 3$ is an **affine map**, not a linear map.
Affine maps are linear maps plus a constant shift. They behave linearly only locally (slopes are
preserved) but not globally (the origin is moved).

### The geometric picture

Linear maps preserve the origin. If $T$ is linear, then $T(0) = 0$, because

$$
T(0) = T(0 \cdot v) = 0 \cdot T(v) = 0.
$$

This is a quick sanity check: if an operation moves the zero vector, it is not a linear map.

---

## 2. What is a vector?

### What the blog says

The blog treats vectors as lists like $(x, y, z)$ — inputs to be tracked. It says "inputs in
vertical columns".

### What Axler says

Axler's definition (1.21):

> Elements of a vector space are called **vectors** or **points**.

That is, a vector is simply a member of a set that satisfies the eight axioms of a vector space
(Definition 1.20 in the notes).

There is no requirement that a vector look like a list.

### Why this matters

The blog's "input" $(a, b, c)$ for a stock portfolio is a vector in $\mathbb{R}^3$ — the space
of all ordered triples of real numbers. That is a completely standard vector space.

But everything the blog does with it — adding inputs, scaling inputs — is valid because
$\mathbb{R}^3$ satisfies the vector space axioms, not because $(a, b, c)$ happens to look like a list.

If instead your inputs were functions — say, the historical price curves of three stocks over
time — the same operations would still work, because function spaces are also vector spaces
(as the notes show in Section 7.4, and as Axler proves in Example 1.25).

The abstract definition is what gives you permission to apply linear algebra far beyond lists
of numbers.

---

## 3. Scalar multiplication and the field $\mathbb{F}$

### What the blog says

The blog uses "multiply inputs by a constant" without naming what kinds of constants are allowed.

### What Axler says

In Axler's definition 1.19, scalar multiplication on a vector space $V$ is defined over a field
$\mathbb{F}$. In most practical contexts, $\mathbb{F} = \mathbb{R}$ (real numbers) or
$\mathbb{F} = \mathbb{C}$ (complex numbers).

The scalars in the blog — percentages like $1.2$ for a 20% gain, or $0.95$ for a 5% loss — are
real numbers. So the blog is silently working in a **real vector space** (Definition 1.22 in
the notes).

### Why the field matters

Axler notes that a vector space must specify its field. The same underlying set can behave as a
real vector space or a complex vector space, and these are different objects with different
properties.

For most of the blog's examples, $\mathbb{F} = \mathbb{R}$, and you do not need to think about
this. But it becomes essential once you encounter quantum mechanics, signal processing, or
anything that uses complex numbers naturally.

---

## 4. Operations (rows) and inputs (columns) — why the layout makes sense

### What the blog says

The blog argues that we should store inputs in columns and operations in rows. An operation like

$$
F(x, y, z) = 3x + 4y + 5z
$$

is abbreviated as the row $(3, 4, 5)$.

### First-principles connection

This choice is not arbitrary. It follows directly from how linear maps interact with coordinate
vectors.

In Axler's framework, once you fix a basis for $V$ and a basis for $W$, every linear map
$T : V \to W$ corresponds to a unique matrix $M$.

The rule is: to compute $T(v)$ using coordinates, you multiply the matrix $M$ by the coordinate
column of $v$.

The blog's "operation" row $(3, 4, 5)$ is one row of such a matrix. Each entry tells you how
much of the corresponding input coordinate contributes to this particular output.

### Why rows are operations and columns are inputs

Consider what a single column of the input matrix represents. If your inputs are

$$
v = (a, b, c) \quad \text{and} \quad w = (x, y, z),
$$

they are two separate vectors. Storing them as two columns keeps them independent but allows you
to apply the same operations matrix to both at once. This is matrix multiplication.

The row/column convention is not a memory trick. It is a direct consequence of how linear maps
compose with basis representations.

---

## 5. What is a matrix?

### What the blog says

"A matrix is a shorthand for our diagrams." It represents a collection of operations, stored
as rows, waiting to act on inputs, stored as columns.

### First-principles meaning

A matrix is the coordinate description of a linear map.

Specifically, if $T : V \to W$ is a linear map, and you choose a basis
$(e_1, \dots, e_n)$ of $V$ and a basis $(f_1, \dots, f_m)$ of $W$, then the matrix $M$ of $T$
is defined by: the $j$th column of $M$ contains the coordinates of $T(e_j)$ in the $f$-basis.

So each column tells you where one basis vector goes. The whole matrix tells you where the whole
space goes.

### The identity matrix

The blog introduces the identity matrix:

$$
I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}.
$$

In Axler's language, this is the matrix of the **identity map** $I_V : V \to V$ defined by
$I_V(v) = v$. Every basis vector maps to itself. The multiplicative identity axiom for vector
spaces (Definition 1.20) guarantees this operation makes sense: $1v = v$ for all $v$.

### The zero matrix

A matrix of all zeros represents the zero linear map $T(v) = 0$ for all $v$. The image of
every input is the zero vector. This connects directly to the additive identity axiom:
the zero vector exists and acts as the neutral element for addition.

### The reordering matrix

The blog shows:

$$
\begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{pmatrix}
$$

sends $(x, y, z)$ to $(x, z, y)$. This is a linear map: it is additive and homogeneous. Verify:

$$
T(v + w) = T(v) + T(w)
$$

because reordering the components of a sum is the same as summing the reordered components.
This follows from commutativity and associativity of addition in the underlying field.

---

## 6. Matrix multiplication as function composition

### What the blog says

"Applying one operations matrix to another gives a new operations matrix that applies both
transformations, in order." If $N$ adjusts for news and $T$ adjusts for taxes, then

$$
TN
$$

is the combined operation.

### What this is formally

Matrix multiplication is function composition of linear maps.

If $T : W \to X$ and $N : V \to W$ are linear maps, then the composition

$$
T \circ N : V \to X
$$

is defined by $(T \circ N)(v) = T(N(v))$.

Axler proves that the composition of two linear maps is itself a linear map. The matrix of
$T \circ N$ is the product of the matrices of $T$ and $N$:

$$
M(T \circ N) = M(T) \cdot M(N).
$$

### Why multiplication, not addition?

Matrix multiplication is not component-wise. It is the result of asking: "after applying $N$,
what does $T$ do to the output?"

This is why matrix multiplication does not commute in general. First adjusting for news
and then for taxes ($TN$) may give a different answer than first adjusting for taxes and then
for news ($NT$), because the operations interact.

### Why order matters

The blog notes we write $TN$, meaning $N$ is applied first. This is the standard convention for
function composition: the rightmost function acts first. Just as $f \circ g$ means "apply $g$
first, then $f$", the matrix on the right acts first.

---

## 7. What does the stock portfolio example actually show?

### What the blog says

Three inputs (Apple, Google, Microsoft dollar amounts) pass through an operations matrix to
produce four outputs (updated values plus profit).

### The linear algebra underneath

The portfolio is a vector $v \in \mathbb{R}^3$:

$$
v = (v_{\text{AAPL}}, v_{\text{GOOG}}, v_{\text{MSFT}}).
$$

The news event defines a linear map $T : \mathbb{R}^3 \to \mathbb{R}^4$. Its matrix is:

$$
M = \begin{pmatrix}
1.2 & 0    & 0 \\
0   & 0.95 & 0 \\
0   & 0    & 1 \\
0.2 & -0.05 & 0
\end{pmatrix}.
$$

The output $T(v) = Mv$ is a vector in $\mathbb{R}^4$: three updated stock values plus the
net profit.

Why is this a linear map? Because each output is a weighted sum of inputs — that is the
definition of homogeneity plus additivity. If Alice and Bob pool their portfolios, the
combined output equals the sum of their individual outputs. That is the additivity condition:
$T(v + w) = T(v) + T(w)$.

### Multiple portfolios at once

The blog feeds in both Alice's and Bob's portfolios simultaneously, treating them as two
columns in a single input matrix $A$:

$$
A = \begin{pmatrix}
1000 & 500 \\
1000 & 2000 \\
1000 & 500
\end{pmatrix}.
$$

The output is $MA$, which computes $T$ applied to each portfolio at once. This is just the
definition of matrix multiplication: every column of $A$ is processed independently by the
same operations matrix $M$.

In Axler's language, $A$ represents two vectors in $\mathbb{R}^3$, and $MA$ applies the same
linear map to both vectors.

---

## 8. Linear combinations and why the "mini arithmetic" is enough

### What the blog says

Linear algebra's "mini arithmetic" is: multiply each input by a constant, then add the results.
The blog argues this feels limiting but is surprisingly powerful.

### The formal name

What the blog calls "mini arithmetic" is a **linear combination**.

Given vectors $v_1, \dots, v_n \in V$ and scalars $a_1, \dots, a_n \in \mathbb{F}$, the
linear combination is

$$
a_1 v_1 + a_2 v_2 + \cdots + a_n v_n.
$$

This is the fundamental operation in linear algebra. It is the operation that the two
distributive axioms in Definition 1.20 govern.

### Why it is enough

Axler's approach shows that all the structure of a vector space is determined by which
sets of vectors can be combined, and how.

The blog's operations matrix $F(x, y, z) = 3x + 4y + 5z$ is a linear combination of the three
coordinate projections. Each row of any matrix is a linear combination of the input components.

This is why linear algebra is so broadly applicable: a linear combination is the simplest
non-trivial thing you can do with a set of objects that has addition and scalar multiplication.

---

## 9. The identity matrix and the multiplicative identity axiom

### What the blog says

The identity matrix copies inputs to outputs unchanged.

### The formal connection

The identity matrix corresponds to the scalar $1$ in the vector space axioms.

Axiom 5 of Definition 1.20 says: $1v = v$ for all $v \in V$. This guarantees that the scalar
$1$ leaves every vector unchanged.

When we represent the identity map as a matrix, every basis vector must map to itself. In
coordinates, the matrix must have $1$s on the diagonal and $0$s everywhere else. That is the
identity matrix.

The identity matrix is not merely a convenient example. It is the coordinate manifestation of
the most fundamental axiom connecting scalars to vectors.

---

## 10. The determinant as "what happens to volume"

### What the blog says

The determinant is the "size" of the output transformation. A determinant of 0 means the
transformation is destructive and cannot be reversed.

### First-principles intuition

When a linear map $T : V \to V$ acts on a region of space, it can:

- stretch it (determinant $> 1$);
- shrink it (determinant between $0$ and $1$);
- reflect it (negative determinant);
- collapse it to a lower-dimensional object (determinant $= 0$).

A determinant of $0$ means the map squashes the whole space into a lower-dimensional image.
You lose information. Two different inputs can map to the same output, so the map is not
invertible.

In Axler's treatment, this connects to the concept of **injectivity**. A linear map is
injective if and only if its null space contains only the zero vector. A matrix with
determinant $0$ has a non-trivial null space, meaning some non-zero vector maps to $0$.

### Why this matters for the blog's stock example

If the operations matrix has determinant $0$, you cannot recover the original portfolio from
the updated one. Information is lost. In the blog, all four outputs are recoverable from the
inputs precisely because the map is injective on the three-dimensional input space.

---

## 11. Eigenvectors and eigenvalues

### What the blog says

An eigenvector is an input that does not change direction when passed through a matrix.
The eigenvalue is how much it gets scaled.

### First-principles meaning

A vector $v \neq 0$ is an **eigenvector** of a linear map $T$ if

$$
T(v) = \lambda v
$$

for some scalar $\lambda \in \mathbb{F}$. The scalar $\lambda$ is the corresponding eigenvalue.

Why does this matter? Because the eigenvectors identify the "axes" along which the linear map
acts by pure scaling. If you decompose an arbitrary vector in terms of eigenvectors, each
component just gets multiplied by its eigenvalue. The complex interaction of the whole map
reduces to simple scalar multiplication in the eigenvector basis.

### Connecting to vector spaces

The set of all solutions to $T(v) = \lambda v$, including the zero vector, forms a subspace
of $V$ called the **eigenspace** for $\lambda$. This is a consequence of the vector space
axioms: sums and scalar multiples of solutions are also solutions, which is precisely what
the linearity of $T$ guarantees.

---

## 12. Gauss-Jordan elimination as solving a linear map equation

### What the blog says

Reducing a matrix to the identity matrix reveals the values of $x$, $y$, $z$ in a system
of equations.

### Axler's perspective

A system of linear equations

$$
Ax = b
$$

is asking: "which vector $x \in V$ does the linear map $T_A$ send to $b \in W$?"

This is the equation for a preimage of $b$ under $T_A$.

Gauss-Jordan elimination transforms $A$ step by step using a sequence of elementary row
operations. Each row operation is itself a linear map. So the whole elimination process is
applying a composition of linear maps to both sides of the equation.

When the left side becomes the identity matrix, you have composed the operations until they
cancel $T_A$, leaving $x$ exposed on the left and $A^{-1}b$ on the right.

This is possible exactly when $T_A$ is invertible — which, by Axler, means $T_A$ is both
injective and surjective.

---

## 13. Homogeneous coordinates: how to encode "add a constant"

### What the blog says

Appending a dummy input of $1$ to every vector — turning $(x, y, z)$ into $(x, y, z, 1)$ — 
allows you to encode additions like $x + 1$ as a matrix multiplication:

$$
\begin{pmatrix} 1 & 0 & 0 & 1 \end{pmatrix}
\begin{pmatrix} x \\ y \\ z \\ 1 \end{pmatrix}
= x + 1.
$$

### Why this works formally

Adding a constant to a function is an affine operation, not a linear one. It moves the zero
vector, which violates the requirement that linear maps fix the origin.

The trick is to embed $\mathbb{R}^3$ into $\mathbb{R}^4$ by appending a $1$. Inside the larger
space, the affine shift looks like a genuine linear operation on the extra coordinate.

Formally, you are replacing the affine map $T(x) = Mx + c$ with the linear map

$$
\tilde{T}\begin{pmatrix} x \\ 1 \end{pmatrix}
= \begin{pmatrix} M & c \\ 0 & 1 \end{pmatrix}
\begin{pmatrix} x \\ 1 \end{pmatrix}
= \begin{pmatrix} Mx + c \\ 1 \end{pmatrix}.
$$

The dummy $1$ at the bottom is preserved through every multiplication, so you can compose
multiple affine operations as if they were linear ones.

This construction — called the **homogeneous coordinate embedding** — appears everywhere:
computer graphics (3D transforms), robotics (rigid-body motion), and projective geometry.

### What this says about vector spaces

This shows that the vector space axioms are the right minimum structure. Affine maps live
just outside them. The moment you need a constant shift, you have left the linear world, and
you must either expand the space or give up some structure.

---

## 14. Why "spreadsheet" is the right intuition and also incomplete

### The blog's final message

The blog ends with: "Why are spreadsheets useful? They're not, unless you want a tool used to
attack nearly every real-world problem."

This is exactly right as a practical motivator. Linear algebra is a way of writing
spreadsheet-style computations compactly and generally.

### Where the formal layer adds value

But spreadsheets do not tell you:

- when a calculation is invertible (can you undo it?);
- which combinations of inputs produce zero output (null space);
- what structure is preserved across transformations (eigenspaces);
- how different vector spaces relate to each other (linear maps as structure-preserving functions);
- why a given set of functions, sequences, or signals obeys the same algebra as a list of numbers.

Those questions require the abstract definition. A vector space is the formal name for any
collection of objects that behaves like a spreadsheet column at the algebraic level, regardless
of what the objects physically are.

Once you know that something is a vector space, every theorem in Axler's book applies to it
automatically.

---

## 15. A translation table: blog language to Axler language

| BetterExplained term | Axler formal term |
|---|---|
| "input" | element of the domain vector space $V$ |
| "output" | element of the codomain vector space $W$ |
| "list $(x, y, z)$" | vector in $\mathbb{F}^n$ (a specific vector space) |
| "linear operation $F$" | linear map $T : V \to W$ (Definition 3.2) |
| "matrix" | matrix representation of a linear map (Chapter 3) |
| "mini arithmetic" | linear combination (Chapter 2) |
| "identity matrix" | matrix of the identity linear map; related to axiom $1v = v$ |
| "determinant = 0" | map is not injective; null space is non-trivial |
| "eigenvector" | vector satisfying $T(v) = \lambda v$ |
| "eigenvalue" | scalar $\lambda$ in the eigenvector equation |
| "multiply two matrices" | compose two linear maps |
| "append a dummy 1" | embed an affine map into a linear map in higher dimension |
| "operations on 2 inputs at once" | apply a linear map to multiple vectors simultaneously |

---

## 16. What to take away

The BetterExplained guide teaches you to see a matrix as a compact spreadsheet.
That intuition is correct and worth keeping.

These bridge notes add the formal layer underneath:

- A "vector" is any element of any set satisfying the eight vector space axioms.
- An "operation" is a function from one vector space to another that preserves linearity.
- A "matrix" is the coordinate description of such a function, once you fix bases.
- The "nice" behaviour of linear operations (predictability, decomposability) is exactly
  what the two conditions $T(u + v) = T(u) + T(v)$ and $T(\lambda v) = \lambda T(v)$ enforce.
- The vector space axioms are the minimum rules needed to make all of this work coherently.

The blog shows you what linear algebra does. Axler shows you why it has to work that way.
Both perspectives are necessary.
