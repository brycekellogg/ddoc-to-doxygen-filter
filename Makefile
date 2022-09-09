INPUTS = test/input-javadoc.h
OUTPUTS = test/output-javadoc.h

test: filter.py ${OUTPUTS}

output-%.h: input-%.h target-%.h
	@echo "Processing $<"
	@./filter.py $< > $@
	@echo "Diffing $^"
	@diff $^

doxygen:
	doxygen

ddoc:
	dmd -o- -D test/input.d

clean:
	rm -rf result.diff html input.html test/output-*.h
