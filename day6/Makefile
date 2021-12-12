CC=gcc
CFLAGS=-ggdb -Wall

all:	day6

day6:	day6.c
	$(CC) $(CFLAGS) -o $@ $^

test: clean day6
	./day6

debug: clean day6
	gdb ./day6

clean:
	rm -f day6
	# Remove gdb debug symbol containing dirs specific to macOS
	rm -rf day6.dSYM
