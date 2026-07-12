# Chapter 1 Notes

## Section 1B - Definition of a Vector Space

These notes are meant to make Axler's Section 1B feel natural before it feels formal.
The main goal is to understand why the definition of a vector space looks the way it does,
why the axioms are exactly the right ones, and how to solve the first exercises using only
those axioms.

## 1. The big idea

At the start of linear algebra, vectors usually look like arrows or coordinate lists such as
$$(2, -1, 3).$$

That picture is useful, but it is also too narrow.

Axler's big move is this:

- stop focusing on what vectors look like;
- focus instead on what you are allowed to do with them.

If a collection of objects can be added together and multiplied by scalars in a way that obeys
the same basic rules as ordinary coordinate vectors, then all the important linear algebra
arguments work there too.

That means the "vectors" in a vector space do not have to be arrows. They can be:

- lists of numbers;
- infinite sequences;
- functions;
- polynomials;
- matrices;
- signals;
- or other abstract objects.

So a vector space is not really about shape. It is about structure.

## 2. From $\mathbb{F}^n$ to abstraction

In $\mathbb{F}^n$, you already know how to do two things:

- add vectors;
- multiply vectors by numbers.

For example, in $\mathbb{R}^3$,
$$
(1, -2, 4) + (3, 5, -1) = (4, 3, 3),
$$
and
$$
2(1, -2, 4) = (2, -4, 8).
$$

These operations satisfy familiar rules:

- order does not matter in addition;
- grouping does not matter in addition;
- there is a zero vector;
- every vector has an opposite;
- multiplying by $1$ changes nothing;
- multiplying by scalars behaves the way ordinary multiplication behaves;
- scalar multiplication distributes over addition.

Axler asks: what if we keep only these rules and forget the coordinate picture?

That question leads to the definition of a vector space.

## 3. The two operations

A vector space needs two operations.

### Addition

Addition takes two vectors in $V$ and produces another vector in $V$.

So if $u, v \in V$, then $u + v$ must also lie in $V$.

This is a closure requirement. If adding two allowed objects produces a forbidden object,
then the set is not a vector space.

Example of failure:

- Let $V$ be the set of positive real numbers.
- Using ordinary scalar multiplication, $(-1) \cdot 2 = -2$.
- But $-2$ is not positive.

So the positive real numbers are not a vector space over $\mathbb{R}$.

### Scalar multiplication

Scalar multiplication takes:

- a scalar $\lambda \in \mathbb{F}$, and
- a vector $v \in V$,

and produces a new vector $\lambda v \in V$.

The word scalar means "the number doing the scaling". In this chapter, the field $\mathbb{F}$
is usually either $\mathbb{R}$ or $\mathbb{C}$.

## 4. What is the field $\mathbb{F}$?

The field tells you what kinds of scalars are allowed.

- If $\mathbb{F} = \mathbb{R}$, then the scalars are real numbers.
- If $\mathbb{F} = \mathbb{C}$, then the scalars are complex numbers.

This matters. The same underlying set can behave differently depending on which scalars you allow.

Example:

- $\mathbb{C}$ is a vector space over $\mathbb{C}$.
- $\mathbb{C}$ is also a vector space over $\mathbb{R}$.
- But these are not the same vector-space structure, because the allowed scalars are different.

When the field is $\mathbb{R}$, we say real vector space.
When the field is $\mathbb{C}$, we say complex vector space.

## 5. Why these axioms?

The vector space axioms are the minimum rules needed to make linear algebra stable.
Each axiom prevents a type of algebraic chaos.

### 5.1 Commutativity of addition

$$u + v = v + u$$

Intuition:

Adding two displacements should not depend on order. If one move means "go right 3" and another
means "go up 2", then doing them in either order lands you at the same place.

Why it matters:

Without this, addition would behave like a process with memory, not like a genuine combination
of two vectors.

### 5.2 Associativity of addition

$$
(u + v) + w = u + (v + w)
$$

Intuition:

When you add several vectors, the grouping should not matter.

Why it matters:

This lets us write sums like $u + v + w$ without ambiguity.

### 5.3 Additive identity

There exists a vector $0 \in V$ such that
$$
v + 0 = v
$$
for every $v \in V$.

Intuition:

There must be a "do nothing" vector.

Important distinction:

- the scalar $0$ is a number in $\mathbb{F}$;
- the vector $0$ is the additive identity in $V$.

They are related, but they are not the same kind of object.

Examples:

- in $\mathbb{R}^3$, the zero vector is $(0, 0, 0)$;
- in a function space, the zero vector is the zero function;
- in a matrix space, the zero vector is the zero matrix.

### 5.4 Additive inverse

For every $v \in V$, there exists $w \in V$ such that
$$
v + w = 0.
$$

We write that vector as $-v$.

Intuition:

Every vector must be undoable.

If $v$ moves you away from the origin, then $-v$ moves you back.

### 5.5 Multiplicative identity

$$1v = v$$

Intuition:

Scaling by $1$ should do nothing.

Without this, scalar multiplication would not actually agree with the ordinary meaning of
"multiply by 1".

### 5.6 Associativity of scalar multiplication

$$
(ab)v = a(bv)
$$

Intuition:

Scaling by $b$ and then by $a$ should be the same as scaling once by $ab$.

Example:

- stretch by $3$;
- then shrink by $1/2$;
- that should be the same as scaling once by $3/2$.

### 5.7 Distributive law over vector addition

$$
a(u + v) = au + av
$$

Intuition:

Scaling a combined motion should equal combining the individually scaled motions.

### 5.8 Distributive law over scalar addition

$$
(a + b)v = av + bv
$$

Intuition:

Applying two amounts of scaling and then adding the results should match scaling once by the
sum of those amounts.

## 6. A compact way to remember the definition

A vector space is a set of objects where:

- you can add any two objects and stay inside the set;
- you can multiply any object by any scalar and stay inside the set;
- zero exists;
- negatives exist;
- the operations behave the same way they do in ordinary coordinate spaces.

If those things hold, the objects deserve to be called vectors.

## 7. The simplest examples

### 7.1 The one-point vector space

The set $\{0\}$ is a vector space.

This is the smallest possible vector space. There is only one vector, and it has to act as the
zero vector.

This example is useful because it reminds you that a vector space does not need to contain many
objects. It only needs to satisfy the axioms.

### 7.2 Coordinate spaces $\mathbb{F}^n$

These are the standard examples:

$$
\mathbb{F}^n = \{(x_1, \dots, x_n) : x_k \in \mathbb{F}\}.
$$

Addition and scalar multiplication are done coordinate by coordinate.

Example in $\mathbb{R}^2$:

$$
(2, -1) + (5, 4) = (7, 3), \qquad -3(2, -1) = (-6, 3).
$$

Why the axioms hold:

Every coordinate is just an ordinary number, and the familiar rules of arithmetic hold for each
coordinate. So the whole vector inherits those rules component by component.

### 7.3 Infinite sequences $\mathbb{F}^{\infty}$

An element of $\mathbb{F}^{\infty}$ is an infinite sequence
$$
(x_1, x_2, x_3, \dots).
$$

Addition and scalar multiplication are still defined coordinate by coordinate:

$$
(x_1, x_2, \dots) + (y_1, y_2, \dots) = (x_1 + y_1, x_2 + y_2, \dots),
$$
$$
\lambda(x_1, x_2, \dots) = (\lambda x_1, \lambda x_2, \dots).
$$

Example:

$$
(1, 0, 1, 0, \dots) + (0, 1, 0, 1, \dots) = (1, 1, 1, 1, \dots).
$$

The zero vector is the infinite sequence of zeros.

This example is important because it shows that vectors do not have to be finite lists.

### 7.4 Function spaces $\mathbb{F}^S$

If $S$ is a set, then $\mathbb{F}^S$ means the set of all functions from $S$ to $\mathbb{F}$.

This is one of the biggest conceptual jumps in early linear algebra.

Here, a vector is a whole function.

If $f, g \in \mathbb{F}^S$, define:

$$
(f + g)(x) = f(x) + g(x),
$$
$$
(\lambda f)(x) = \lambda f(x)
$$

for every $x \in S$.

In words:

- to add functions, add their outputs pointwise;
- to scale a function, scale every output.

Example with $S = [0, 1]$ and $\mathbb{F} = \mathbb{R}$:

- let $f(x) = x$;
- let $g(x) = x^2$.

Then

$$
(f + g)(x) = x + x^2,
$$
and

$$
(2f - g)(x) = 2x - x^2.
$$

The zero vector in this space is the zero function:

$$
0(x) = 0 \quad \text{for all } x \in [0, 1].
$$

The additive inverse of $f$ is the function $-f$ defined by

$$
(-f)(x) = -f(x).
$$

## 8. Why function spaces feel strange at first

In $\mathbb{R}^n$, you can see a vector as a short list. In $\mathbb{F}^S$, a vector is an entire
rule.

That can feel too abstract until you notice that lists are also functions.

### Lists as functions

A vector in $\mathbb{F}^n$,
$$
(x_1, \dots, x_n),
$$
can be viewed as a function on the set $\{1, 2, \dots, n\}$ by defining
$$
x(k) = x_k.
$$

So

- $\mathbb{F}^n$ is really $\mathbb{F}^{\{1, 2, \dots, n\}}$;
- $\mathbb{F}^{\infty}$ is really $\mathbb{F}^{\{1, 2, 3, \dots\}}$.

This is a deep unifying idea:

- finite lists are functions on a finite index set;
- sequences are functions on a countable index set;
- ordinary functions are functions on whatever domain $S$ happens to be.

So the difference between these examples is not algebraic. The difference is only the indexing set.

## 9. How proofs in function spaces work

When vectors are functions, to prove two vectors are equal you must prove they give the same value
at every input.

For example, to prove
$$
a(f + g) = af + ag,
$$
you do not stare at the functions globally. You evaluate both sides at an arbitrary point $x$:

$$
(a(f + g))(x) = a(f + g)(x) = a(f(x) + g(x)) = af(x) + ag(x) = (af + ag)(x).
$$

Because both sides agree for every $x$, the functions are equal.

This "evaluate at an arbitrary point" method is standard and very important.

## 10. Common failure modes when checking vector spaces

Most candidate sets fail for simple reasons.

### 10.1 Not closed under scalar multiplication

Example:

- the set of positive functions on $[0, 1]$ is not a vector space over $\mathbb{R}$;
- multiplying by $-1$ produces a negative function.

### 10.2 Missing the zero vector

Example:

- a line in $\mathbb{R}^2$ not passing through the origin is not a vector space;
- it does not contain the zero vector.

### 10.3 Not closed under addition

Example:

- the unit circle in $\mathbb{R}^2$ is not a vector space;
- adding two unit vectors usually does not give another unit vector.

### 10.4 Confusing a set with the operations on it

Sometimes the same set can become different algebraic objects depending on how addition and scalar
multiplication are defined. The operations are part of the structure, not just decoration.

## 11. Useful facts that can be proved from the axioms

These facts are not extra axioms. They follow from the axioms.

### 11.1 The zero vector is unique

If $0$ and $0'$ both act as additive identities, then
$$
0 = 0 + 0' = 0'.
$$

So there is only one zero vector.

### 11.2 Additive inverses are unique

If $x$ and $y$ both satisfy $v + x = 0$ and $v + y = 0$, then
$$
x = x + 0 = x + (v + y) = (x + v) + y = 0 + y = y.
$$

So each vector has exactly one additive inverse.

### 11.3 For every scalar $a$, we have $a0 = 0$

Using $0 + 0 = 0$,
$$
a0 = a(0 + 0) = a0 + a0.
$$

Add the inverse of $a0$ to both sides, and you get $a0 = 0$.

### 11.4 For every vector $v$, we have $0v = 0$

Using $0 + 0 = 0$ in the scalar field,
$$
0v = (0 + 0)v = 0v + 0v.
$$

Add the inverse of $0v$ to both sides, and you get $0v = 0$.

### 11.5 For every vector $v$, we have $(-1)v = -v$

Because
$$
v + (-1)v = 1v + (-1)v = (1 + (-1))v = 0v = 0,
$$
the vector $(-1)v$ is the additive inverse of $v$, so it equals $-v$.

## 12. Section 1B exercises

Below are detailed solutions written in the style Axler wants: use the axioms, not coordinates.

### Exercise 1

Show that $-(-v) = v$ for every $v \in V$.

#### Intuition

Taking the negative means "reverse the direction". Reversing direction twice should bring you back
to the original vector.

#### Proof

By definition of additive inverse,
$$
v + (-v) = 0.
$$

By commutativity,
$$
(-v) + v = 0.
$$

Also, because $-v$ is itself a vector, it has an additive inverse, namely $-(-v)$, so
$$
(-v) + (-(-v)) = 0.
$$

Thus both $v$ and $-(-v)$ are additive inverses of $-v$.
Additive inverses are unique, so
$$
-(-v) = v.
$$

### Exercise 2

Suppose $a \in \mathbb{F}$ and $v \in V$ satisfy $av = 0$. Prove that $a = 0$ or $v = 0$.

#### Intuition

There are only two ways scaling can produce the zero vector:

- the scalar is zero, so everything is collapsed to zero;
- the vector was already zero.

No nonzero scalar can erase a nonzero vector.

#### Proof

Assume $av = 0$.

If $a = 0$, we are done.

Now assume $a \neq 0$. Because $\mathbb{F}$ is a field, $a$ has a multiplicative inverse $a^{-1}$.
Multiply both sides of $av = 0$ by $a^{-1}$:

$$
a^{-1}(av) = a^{-1}0.
$$

Using associativity of scalar multiplication,

$$
(a^{-1}a)v = a^{-1}0.
$$

Thus

$$
1v = a^{-1}0.
$$

By multiplicative identity, $1v = v$. Also, by the derived fact $a0 = 0$ for every scalar $a$,
we have $a^{-1}0 = 0$. Therefore

$$
v = 0.
$$

Hence $a = 0$ or $v = 0$.

### Exercise 3

Suppose $v, w \in V$. Explain why there exists a unique $x \in V$ such that
$$
v + 3x = w.
$$

#### Intuition

You want the vector $x$ that takes you from $v$ to $w$ in three equal pieces.

So first find the whole displacement from $v$ to $w$, then divide by $3$.

#### Existence

Rewrite the equation:

$$
3x = w - v,
$$

where $w - v$ means $w + (-v)$.

Because the field is $\mathbb{R}$ or $\mathbb{C}$, the scalar $3$ is nonzero, so $1/3$ exists.
Define

$$
x = \frac{1}{3}(w - v).
$$

Then

$$
3x = 3\left(\frac{1}{3}(w - v)\right) = (3 \cdot \tfrac{1}{3})(w - v) = 1(w - v) = w - v.
$$

Hence

$$
v + 3x = v + (w - v) = w.
$$

So a solution exists.

#### Uniqueness

Suppose both $x$ and $y$ satisfy the equation. Then

$$
v + 3x = w = v + 3y.
$$

Add $-v$ to both sides:

$$
3x = 3y.
$$

Multiply by $1/3$:

$$
x = y.
$$

So the solution is unique.

### Exercise 4

The empty set is not a vector space. Which requirement fails?

#### Answer

The empty set fails the additive identity requirement.

#### Why only that one?

Most of the axioms say something like "for all $u, v, w \in V$...". If $V$ is empty, statements of
that form are vacuously true because there are no counterexamples.

But the additive identity axiom says that there exists an element $0 \in V$ such that
$$
v + 0 = v
$$
for all $v \in V$.

That cannot happen in the empty set because there is no element to serve as $0$.

### Exercise 5

Show that the additive inverse axiom can be replaced by the condition
$$
0v = 0 \quad \text{for all } v \in V,
$$
where the $0$ on the left is the scalar $0$ and the $0$ on the right is the zero vector.

This means we must prove two directions.

#### Direction 1: the usual additive inverse axiom implies $0v = 0$

Take any $v \in V$. Then

$$
0v = (0 + 0)v.
$$

Using distributivity,

$$
0v = 0v + 0v.
$$

Add the additive inverse of $0v$ to both sides. This gives

$$
0 = 0v.
$$

So $0v = 0$ for every $v$.

#### Direction 2: assume $0v = 0$ for all $v$, and prove additive inverses exist

Take any $v \in V$. Consider the vector $(-1)v$.

Then

$$
v + (-1)v = 1v + (-1)v = (1 + (-1))v = 0v = 0.
$$

So $(-1)v$ is an additive inverse of $v$.

Because every vector has such an inverse, the additive inverse axiom follows.

Thus the two conditions are interchangeable in the definition.

### Exercise 6

Let $\mathbb{R} \cup \{\infty, -\infty\}$ have the operations described in the problem.
Is it a vector space over $\mathbb{R}$?

#### Intuition

This structure is trying to extend the real line by attaching two special endpoints. But those
endpoints do not behave linearly. The algebra looks plausible at first, but the rules do not stay
consistent under regrouping.

#### Counterexample to associativity of addition

Take

$$
u = 1, \qquad v = \infty, \qquad w = -\infty.
$$

Then

$$
(u + v) + w = (1 + \infty) + (-\infty) = \infty + (-\infty) = 0.
$$

But

$$
u + (v + w) = 1 + (\infty + (-\infty)) = 1 + 0 = 1.
$$

Thus

$$
(u + v) + w \neq u + (v + w).
$$

Associativity of addition fails, so this set is not a vector space over $\mathbb{R}$.

### Exercise 7

Suppose $S$ is nonempty. Let $V^S$ be the set of functions from $S$ to $V$.
Define a natural addition and scalar multiplication on $V^S$, and show that $V^S$ is a vector space.

#### Natural definitions

If $f, g \in V^S$ and $a \in \mathbb{F}$, define

$$
(f + g)(s) = f(s) + g(s)
$$

for all $s \in S$, and define

$$
(af)(s) = a(f(s))
$$

for all $s \in S$.

These are the natural definitions because each value $f(s)$ and $g(s)$ already lies in the vector
space $V$, so you simply use the operations of $V$ pointwise.

#### Why this forms a vector space

Every axiom is inherited from $V$ point by point.

For example, commutativity holds because for every $s \in S$,

$$
(f + g)(s) = f(s) + g(s) = g(s) + f(s) = (g + f)(s).
$$

So $f + g = g + f$.

Associativity of addition is similar:

$$
((f + g) + h)(s) = (f(s) + g(s)) + h(s) = f(s) + (g(s) + h(s)) = (f + (g + h))(s).
$$

The additive identity is the zero function $0_{V^S}$ defined by

$$
0_{V^S}(s) = 0_V
$$

for all $s \in S$, where $0_V$ is the zero vector of $V$.

The additive inverse of $f$ is the function $-f$ defined by

$$
(-f)(s) = -f(s).
$$

The distributive laws and scalar associativity also hold pointwise because they already hold in $V$.

Therefore $V^S$ is a vector space over $\mathbb{F}$.

#### Intuition

You can think of each function in $V^S$ as a whole family of vectors, one vector for each input
value $s$. Adding functions means adding the vectors at each slot.

### Exercise 8

Suppose $V$ is a real vector space. Define its complexification $V_{\mathbb{C}}$ by

$$
V_{\mathbb{C}} = V \times V,
$$

but write an ordered pair $(u, v)$ as
$$
u + iv.
$$

Addition is defined by

$$
(u_1 + iv_1) + (u_2 + iv_2) = (u_1 + u_2) + i(v_1 + v_2),
$$

and complex scalar multiplication is defined by

$$
(a + bi)(u + iv) = (au - bv) + i(av + bu),
$$

where $a, b \in \mathbb{R}$.

We want to prove that $V_{\mathbb{C}}$ is a complex vector space.

#### First intuition

An element $u + iv$ here is not literally a sum inside $V$, because $i$ is not a real scalar in the
original real vector space $V$. It is just a convenient way to label the ordered pair $(u, v)$.

This construction is analogous to building complex numbers from ordered pairs of real numbers.

#### Closure under addition

If $u_1, v_1, u_2, v_2 \in V$, then $u_1 + u_2 \in V$ and $v_1 + v_2 \in V$ because $V$ is a real
vector space. Hence

$$
(u_1 + iv_1) + (u_2 + iv_2) = (u_1 + u_2) + i(v_1 + v_2)
$$

is again in $V_{\mathbb{C}}$.

#### Closure under complex scalar multiplication

If $a + bi \in \mathbb{C}$ and $u + iv \in V_{\mathbb{C}}$, then

$$
(a + bi)(u + iv) = (au - bv) + i(av + bu).
$$

Because $a, b \in \mathbb{R}$ and $V$ is closed under real scalar multiplication and addition, both
$au - bv$ and $av + bu$ lie in $V$. So the result lies in $V_{\mathbb{C}}$.

#### Commutativity of addition

$$
(u_1 + iv_1) + (u_2 + iv_2) = (u_1 + u_2) + i(v_1 + v_2)
$$

and because addition in $V$ is commutative,

$$
(u_1 + u_2) + i(v_1 + v_2) = (u_2 + u_1) + i(v_2 + v_1) = (u_2 + iv_2) + (u_1 + iv_1).
$$

#### Associativity of addition

For $u_j, v_j \in V$,

$$
((u_1 + iv_1) + (u_2 + iv_2)) + (u_3 + iv_3)
$$
equals
$$
((u_1 + u_2) + u_3) + i((v_1 + v_2) + v_3),
$$

which equals
$$
(u_1 + (u_2 + u_3)) + i(v_1 + (v_2 + v_3))
$$

by associativity in $V$. That is exactly
$$
(u_1 + iv_1) + ((u_2 + iv_2) + (u_3 + iv_3)).
$$

#### Additive identity

The additive identity is
$$
0 + i0,
$$

where both zeros are the zero vector of $V$.

Indeed,

$$
(u + iv) + (0 + i0) = (u + 0) + i(v + 0) = u + iv.
$$

#### Additive inverse

The additive inverse of $u + iv$ is
$$
(-u) + i(-v),
$$

because

$$
(u + iv) + ((-u) + i(-v)) = (u - u) + i(v - v) = 0 + i0.
$$

#### Multiplicative identity

Using the scalar $1 + 0i$,

$$
(1 + 0i)(u + iv) = (1u - 0v) + i(1v + 0u) = u + iv.
$$

#### Associativity of scalar multiplication

Take complex scalars $a + bi$ and $c + di$.
First compute

$$
(c + di)(u + iv) = (cu - dv) + i(cv + du).
$$

Now multiply by $a + bi$:

$$
(a + bi)((c + di)(u + iv))
$$

equals

$$
(a + bi)((cu - dv) + i(cv + du))
$$

which equals

$$
(a(cu - dv) - b(cv + du)) + i(a(cv + du) + b(cu - dv)).
$$

Simplifying,

$$
((ac - bd)u - (ad + bc)v) + i((ad + bc)u + (ac - bd)v).
$$

But

$$
(a + bi)(c + di) = (ac - bd) + (ad + bc)i.
$$

So

$$
((a + bi)(c + di))(u + iv)
$$

is exactly

$$
((ac - bd)u - (ad + bc)v) + i((ad + bc)u + (ac - bd)v).
$$

Thus

$$
(a + bi)((c + di)(u + iv)) = ((a + bi)(c + di))(u + iv).
$$

#### Distributivity over vector addition

Let $\alpha = a + bi$. Then

$$
\alpha((u_1 + iv_1) + (u_2 + iv_2))
$$

equals

$$
\alpha((u_1 + u_2) + i(v_1 + v_2))
$$

which is

$$
(a(u_1 + u_2) - b(v_1 + v_2)) + i(a(v_1 + v_2) + b(u_1 + u_2)).
$$

Expanding inside $V$ gives

$$
(au_1 - bv_1) + (au_2 - bv_2) + i((av_1 + bu_1) + (av_2 + bu_2)).
$$

That is exactly

$$
\alpha(u_1 + iv_1) + \alpha(u_2 + iv_2).
$$

#### Distributivity over scalar addition

Let $\alpha = a + bi$ and $\beta = c + di$. Then

$$
(\alpha + \beta)(u + iv) = ((a + c) + (b + d)i)(u + iv).
$$

By definition this equals

$$
((a + c)u - (b + d)v) + i((a + c)v + (b + d)u).
$$

Regrouping,

$$
(au - bv) + i(av + bu) + (cu - dv) + i(cv + du).
$$

That is precisely

$$
\alpha(u + iv) + \beta(u + iv).
$$

#### Conclusion

All vector space axioms hold, so $V_{\mathbb{C}}$ is a complex vector space.

#### Intuition to keep

Complexification takes a real vector space and attaches an independent imaginary copy of it.
So every element has:

- a real part from $V$;
- an imaginary part from another copy of $V$.

This is why $\mathbb{C}^n$ can be viewed as the complexification of $\mathbb{R}^n$.

## 13. What to remember from Section 1B

If you want the shortest possible summary of the section, keep these points:

- A vector space is a set where addition and scalar multiplication behave like they do in familiar coordinate spaces.
- Vectors are defined by rules, not by appearance.
- The zero vector and additive inverses make vector addition reversible.
- The distributive laws tie scalar multiplication and vector addition together.
- Function spaces and sequence spaces are genuine vector spaces, not secondary examples.
- Most proofs in abstract linear algebra work by using only the axioms, not coordinates.

That is the real point of Section 1B: it gives you the language in which the rest of linear
algebra will be written.