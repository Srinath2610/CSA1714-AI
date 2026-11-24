
% Student marks

marks(kumar, mathematics, 85).
marks(kumar, programming, 90).
marks(kumar, english, 75).

% Eligibility rules

eligible(Student) :-
    marks(Student, mathematics, M),
    marks(Student, programming, P),
    marks(Student, english, E),
    M >= 60,
    P >= 60,
    E >= 50.

% Display result

check_eligibility(Student) :-
    eligible(Student),
    write(Student),
    write(' is eligible for the course.').

check_eligibility(Student) :-
    \+ eligible(Student),
    write(Student),
    write(' is not eligible for the course.').
