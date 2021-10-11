TARGETS = \
	sudoku-rule-counter-size3.run \

all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm ${TARGETS}

mrproper: clean
	touch dummy~
	rm        *~


sudoku-rule-counter-size3.run: sudoku-rule-counter-size3
	./sudoku-rule-counter-size3

sudoku-rule-counter-size3: sudoku-rule-counter.c Makefile
	gcc sudoku-rule-counter.c -O3 -g -std=gnu11 -pedantic -DPROBLEM_SIZE=3 -o sudoku-rule-counter-size3

