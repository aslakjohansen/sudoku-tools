TARGETS = \
	sudoku-rule-counter-size3-std.run \

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
	gcc sudoku-rule-counter.c -O3 -g -std=gnu11 -pedantic -DPROBLEM_SIZE=3 -DENABLE_ROW_RULE -DENABLE_COLUMN_RULE -DENABLE_BOX_RULE -o sudoku-rule-counter-size3-std

