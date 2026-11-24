
% Facts

studies_ai(kumar).

% Rules

learns_intelligent_systems(X) :-
    studies_ai(X).

solves_ai_problems(X) :-
    learns_intelligent_systems(X).

% Display result

prove(X) :-
    solves_ai_problems(X),
    write(X),
    write(' can solve AI problems.').
