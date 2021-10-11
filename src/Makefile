TARGETS = \
	sudoku-rule-counter-size3-std.run \

CLASSIC_RULESET = -DENABLE_ROW_RULE -DENABLE_COLUMN_RULE -DENABLE_BOX_RULE
CLASSIC = -DPROBLEM_SIZE=3 ${CLASSIC_RULESET}

all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm ${TARGETS}

mrproper: clean
	touch dummy~
	rm        *~


sudoku-rule-counter-size3-std.run: sudoku-rule-counter-size3-std
	./sudoku-rule-counter-size3-std

sudoku-rule-counter-size3-std: sudoku-rule-counter.c Makefile
	gcc sudoku-rule-counter.c -O3 -g -std=gnu11 -pedantic ${CLASSIC} -o sudoku-rule-counter-size3-std

