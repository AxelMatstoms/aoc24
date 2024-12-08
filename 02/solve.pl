okay_inc([_]).

okay_inc([H, H2 | T]) :-
    H < H2,
    Diff is H2 - H,
    Diff > 0,
    Diff =< 3,
    okay_inc([H2 | T]).

okay_dec([_]).

okay_dec([H, H2 | T]) :-
    H > H2,
    Diff is H - H2,
    Diff > 0,
    Diff =< 3,
    okay_dec([H2 | T]).

okay(Seq) :-
    okay_inc(Seq).

okay(Seq) :-
    okay_dec(Seq).

n_okay_helper(Reports, X) :-
    member(X, Reports),
    okay(X).

n_okay(Reports, N) :-
    findall(X, n_okay_helper(Reports, X), Bag),
    length(Bag, N).

input([[7, 6, 4, 2, 1],
       [1, 2, 7, 8, 9],
       [9, 7, 6, 2, 1],
       [1, 3, 2, 4, 5],
       [8, 6, 4, 4, 1],
       [1, 3, 6, 7, 9]]).

